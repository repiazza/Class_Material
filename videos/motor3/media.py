"""Execução de plano explícito, sem dependência de TTS ou escolha narrativa."""
from pathlib import Path
from fractions import Fraction
from array import array
import hashlib
import json
import math
import subprocess
import wave
from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
ARTIFACTS = Path('/workspace/artifacts')


def digest(path):
    with Path(path).open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def read_json(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def write_json(path, value):
    # Exclusive creation is intentional: an execution is never silently replaced.
    with Path(path).open('x', encoding='utf-8') as stream:
        json.dump(value, stream, ensure_ascii=False, indent=2, allow_nan=False)
        stream.write('\n')


def run(args):
    return subprocess.run([str(x) for x in args], check=True, capture_output=True)


def probe(path):
    return json.loads(run(['ffprobe', '-v', 'error', '-show_streams',
                           '-show_format', '-of', 'json', path]).stdout)


def source_path(relative):
    path = (ROOT / relative).resolve()
    if not path.is_relative_to(ROOT) or not path.is_file():
        raise ValueError(f'Fonte inválida: {relative}')
    return path


def checked_sources(plan):
    sources = plan.get('fontes_sha256', {})
    if not sources:
        raise ValueError('Revisões das fontes ausentes')
    for path, expected in sources.items():
        if digest(source_path(path)) != expected:
            raise ValueError(f'Fonte alterada: {path}')
    maps = [p for p in sources if p.endswith('_Mapa_Espacial.json')]
    if len(maps) != 1:
        raise ValueError('Exigir um mapa espacial identificado por hash')
    map_path = source_path(maps[0])
    mapping = read_json(map_path)
    resolved = []
    for segment in plan['segmentos']:
        path = source_path(segment['arquivo'])
        if path.parent != map_path.parent:
            raise ValueError('Material fora do capítulo do mapa')
        material = next((m for m in mapping['materiais'] if m['arquivo'] == path.name), None)
        if material is None or digest(path) != material['sha256']:
            raise ValueError(f'Material ausente/alterado: {path.name}')
        region = next((r for r in material['regioes'] if r['id'] == segment['regiao_id']), None)
        if region is None:
            raise ValueError('Região inexistente')
        if segment.get('bbox_px', region['bbox_px']) != region['bbox_px']:
            raise ValueError('Geometria divergente do mapa')
        with Image.open(path) as image:
            if image.format == 'GIF':
                raise ValueError('Primeiro núcleo suporta somente as imagens estáticas do piloto')
            w, h = image.size
        x0, y0, x1, y1 = region['bbox_px']
        if not (0 <= x0 < x1 <= w and 0 <= y0 < y1 <= h):
            raise ValueError('Geometria fora do original')
        resolved.append((path, region['bbox_px']))
    return resolved


def validate_plan(plan):
    profile = plan['perfil']
    if (profile['largura'], profile['altura'], profile['fps']) != (1080, 1920, 30):
        raise ValueError('Perfil inicial: 1080x1920 a 30 fps')
    if profile.get('fundo_rgb') != [15, 20, 30]:
        raise ValueError('Fundo não suportado neste perfil')
    if profile.get('escala') != 'conter, proporção preservada':
        raise ValueError('Escala não suportada')
    fps = profile['fps']
    cursor = 0
    seen = set()
    segments = plan.get('segmentos', [])
    if not segments:
        raise ValueError('Plano sem segmentos')
    for segment in segments:
        if segment['id'] in seen:
            raise ValueError('ID de segmento duplicado')
        seen.add(segment['id'])
        start, duration = segment['inicio_s'], segment['duracao_s']
        if not all(math.isfinite(x) for x in [start, duration]) or start < 0 or duration <= 0:
            raise ValueError('Tempo inválido')
        first, count = round(start * fps), round(duration * fps)
        if count < 1 or abs(start * fps - first) > 1e-6 or abs(duration * fps - count) > 1e-6:
            raise ValueError('Tempos devem estar na grade de quadros')
        if first != cursor:
            raise ValueError('Lacuna ou sobreposição temporal')
        if segment.get('frame_inicial', first) != first or segment.get('quadros', count) != count:
            raise ValueError('Tempos e contagem de quadros contraditórios')
        if segment.get('transicao') != 'CORTE_SECO' or segment.get('modo_visual') != 'IMAGEM_ESTATICA':
            raise ValueError('Modo visual/transição não suportado')
        cursor += count
    if abs(plan['duracao_s'] * fps - cursor) > 1e-6:
        raise ValueError('Duração total inconsistente')
    return cursor


def reserve(video_id, execution):
    import re
    if not re.fullmatch(r'V\d{2}-\d{3}', video_id) or not re.fullmatch(r'[A-Za-z0-9_-]+', execution):
        raise ValueError('Identificador inválido')
    destination = ARTIFACTS / video_id / execution
    destination.mkdir(parents=True, exist_ok=False)
    return destination


def extract_audio(recording, destination, stream_index, start_s):
    if not math.isfinite(start_s) or start_s < 0:
        raise ValueError('Início inválido')
    metadata = probe(recording)
    stream = next((s for s in metadata['streams'] if s['index'] == stream_index), None)
    if stream is None or stream['codec_type'] != 'audio':
        raise ValueError('A trilha selecionada não é áudio')
    # No speed change, denoising, silence removal or synthetic audio mixing.
    target = destination / 'audio_trabalho.wav'
    run(['ffmpeg', '-n', '-v', 'error', '-i', recording, '-map', f'0:{stream_index}',
         '-ss', str(start_s), '-vn', '-c:a', 'pcm_s16le', '-ar', '48000', '-ac', '1', target])
    with wave.open(str(target), 'rb') as w:
        duration = w.getnframes() / w.getframerate()
        samples = array('h', w.readframes(w.getnframes()))
        if not any(samples):
            raise ValueError('Trilha digitalmente silenciosa; não apresentar como narração')
        write_json(destination / 'audio_metricas.json', {
            'duracao_s': duration, 'sample_rate': w.getframerate(),
            'pico_pcm16': max(abs(x) for x in samples),
            'limite': 'Ausência de silêncio digital não certifica voz ou inteligibilidade.'})
        if duration <= 0:
            raise ValueError('Gravação vazia após início informado')
    return target, duration, metadata


def project(path, box):
    with Image.open(path) as source:
        crop = source.crop(box).convert('RGB')
    scale = min(1080 / crop.width, 1920 / crop.height)
    size = round(crop.width * scale), round(crop.height * scale)
    result = Image.new('RGB', (1080, 1920), (15, 20, 30))
    result.paste(crop.resize(size, Image.Resampling.LANCZOS),
                 ((1080 - size[0]) // 2, (1920 - size[1]) // 2))
    return result


def render(plan, destination, audio=None):
    frames = validate_plan(plan)
    sources = checked_sources(plan)
    if audio:
        audio_duration = float(probe(audio)['streams'][0]['duration'])
        if abs(audio_duration - plan['duracao_s']) > 1 / 30 + 1e-6:
            raise ValueError('Duração do áudio diverge do plano; não truncar/esticar a gravação')
    clips = []
    for i, (segment, (path, box)) in enumerate(zip(plan['segmentos'], sources)):
        image_path = destination / f'quadro-{i:02d}.png'
        project(path, box).save(image_path)
        clip = destination / f'clipe-{i:02d}.mp4'
        run(['ffmpeg', '-n', '-v', 'error', '-loop', '1', '-framerate', '30', '-i', image_path,
             '-frames:v', str(round(segment['duracao_s'] * 30)), '-c:v', 'libx264',
             '-preset', 'fast', '-crf', '18', '-pix_fmt', 'yuv420p', '-threads', '2', clip])
        clips.append(clip)
    listing = destination / 'clips.txt'
    # Relative generated filenames avoid shell expansion and concat quoting ambiguity.
    listing.write_text(''.join(f"file '{p.name}'\n" for p in clips))
    output = destination / (plan['video_id'] + '.mp4')
    command = ['ffmpeg', '-n', '-v', 'error', '-f', 'concat', '-safe', '1', '-i', listing]
    if audio:
        command += ['-i', audio, '-map', '0:v:0', '-map', '1:a:0', '-c:a', 'aac', '-b:a', '128k']
    else:
        command += ['-map', '0:v:0', '-an']
    run(command + ['-c:v', 'copy', '-movflags', '+faststart', output])
    metadata = probe(output)
    v = next(s for s in metadata['streams'] if s['codec_type'] == 'video')
    if (v['width'], v['height'], v['codec_name'], v['pix_fmt'], Fraction(v['avg_frame_rate'])) != (1080, 1920, 'h264', 'yuv420p', 30):
        raise ValueError('Perfil de saída inválido')
    if int(v['nb_frames']) != frames:
        raise ValueError('Número de quadros divergente')
    run(['ffmpeg', '-v', 'error', '-i', output, '-f', 'null', '-'])
    write_json(destination / 'ffprobe.json', metadata)
    return output
