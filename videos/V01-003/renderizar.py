"""Reproduz o piloto a partir do plano, mapa e WAV de referência já sintetizado.
Uso: python videos/V01-003/renderizar.py --audio /caminho/Audio_Referencia.wav --saida /tmp/V01-003.mp4
Dependências existentes: Python, Pillow e FFmpeg. O script não instala serviços nem sintetiza nova voz.
"""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile
from PIL import Image


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--audio', type=Path, required=True)
    parser.add_argument('--saida', type=Path, required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    plan = json.loads((root / 'editorial/montagens/01-003_Montagem.json').read_text())
    manifest = json.loads((root / 'videos/V01-003/V01-003_Manifesto.json').read_text())
    expected_audio = next(a['sha256'] for a in manifest['artefatos'] if a['nome'] == 'V01-003_Audio_Referencia.wav')
    if sha(args.audio) != expected_audio:
        raise ValueError('WAV diferente do áudio de referência registrado; sincronização não é reutilizável.')
    map_source = plan['fontes']['mapa']
    map_path = root / map_source['caminho']
    if sha(map_path) != map_source['sha256']:
        raise ValueError('Mapa alterado: revalidar antes da reprodução.')
    spatial = json.loads(map_path.read_text())
    with tempfile.TemporaryDirectory(prefix='v01003-render-') as temp:
        work = Path(temp)
        concat = []
        last_image = None
        for take in plan['segmentos']:
            source = root / take['arquivo']
            material = next(m for m in spatial['materiais'] if m['arquivo'] == source.name)
            if sha(source) != material['sha256']:
                raise ValueError('Original alterado: ' + str(source))
            for shot in take['projecoes']:
                region = next(r for r in material['regioes'] if r['id'] == shot['regiao_id'])
                image = Image.open(source).convert('RGB')
                width, height = image.size
                box = tuple(round(v * d) for v, d in zip(region['bbox_normalizada'], [width, height, width, height]))
                crop = image.crop(box)
                scale = min(1080 / crop.width, 1920 / crop.height)
                size = (round(crop.width * scale), round(crop.height * scale))
                frame = Image.new('RGB', (1080, 1920), '#161616')
                frame.paste(crop.resize(size, Image.Resampling.LANCZOS), ((1080-size[0])//2, (1920-size[1])//2))
                last_image = work / (shot['id'] + '.png')
                frame.save(last_image, compress_level=1)
                concat.extend(["file '" + str(last_image) + "'", 'duration ' + str(shot['duracao_audio_ms']/1000)])
        if last_image is None:
            raise ValueError('Plano sem projeções.')
        concat.append("file '" + str(last_image) + "'")
        concat_path = work / 'quadros.ffconcat'
        concat_path.write_text('\n'.join(concat) + '\n')
        subprocess.run(['ffmpeg', '-hide_banner', '-y', '-f', 'concat', '-safe', '0', '-i', str(concat_path),
                        '-i', str(args.audio), '-vf', 'fps=30,format=yuv420p', '-c:v', 'libx264', '-preset', 'fast',
                        '-tune', 'stillimage', '-crf', '20', '-threads', '2', '-c:a', 'aac', '-b:a', '128k',
                        '-t', str(plan['duracao_total_ms_medida']/1000), '-shortest', '-movflags', '+faststart',
                        str(args.saida)], check=True)


if __name__ == '__main__':
    main()
