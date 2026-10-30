"""CLI: render (Marco A) e finalize (Marco B). Sem upload, síntese ou merge."""
import argparse
import datetime
import shutil
import sys
from pathlib import Path
from .alignment import associate, human_plan, srt, validate_transcript
from .media import (ROOT, checked_sources, digest, extract_audio, probe, read_json,
                    render, reserve, run, validate_plan, write_json)
from .transcription import transcribe


def manifest(destination, video_id, kind, nature, inputs, status, reason):
    artifacts = [{'path': str(p), 'bytes': p.stat().st_size, 'sha256': digest(p)}
                 for p in sorted(destination.iterdir()) if p.is_file()]
    result = {'schema_version': 'motor3-1', 'video_id': video_id, 'tipo_entrega': kind,
              'natureza_gravacao': nature, 'estado': status, 'motivo': reason,
              'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
              'homologacao_humana': False, 'inputs': inputs, 'artefatos': artifacts,
              'implementacao_sha256': {p.name: digest(p) for p in Path(__file__).parent.glob('*.py')},
              'ferramentas': {'python': sys.version.split()[0],
                              'ffmpeg': run(['ffmpeg', '-version']).stdout.decode().splitlines()[0]},
              'limites': ['Sem escuta perceptiva ou revisão audiovisual integral automática.',
                          'Aceitação textual conservadora não equivale a homologação semântica.']}
    (destination / 'relatorio.md').write_text(
        f'# Motor 3 — {video_id}\n\nEstado: {status}. Natureza: {nature}. Modalidade: {kind}.\n\n'
        + reason + '\n\nFontes e hashes no manifesto; associação e transcrição preservadas quando executadas. '
        + 'Sem homologação humana, upload ou alteração dos originais.\n', encoding='utf-8')
    result['artefatos'] = [
        {'path': str(p), 'bytes': p.stat().st_size, 'sha256': digest(p)}
        for p in sorted(destination.iterdir()) if p.is_file()]
    write_json(destination / 'manifesto.json', result)
    # Only lightweight execution records enter the checkout; binary inputs/outputs stay external.
    records = ROOT / 'videos' / video_id / 'execucoes' / destination.name
    records.mkdir(parents=True, exist_ok=False)
    for artifact in destination.iterdir():
        if artifact.suffix in {'.json', '.md', '.srt'}:
            shutil.copyfile(artifact, records / artifact.name)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['render', 'finalize'])
    parser.add_argument('--plan', required=True, type=Path)
    parser.add_argument('--execution', required=True)
    parser.add_argument('--recording', type=Path)
    parser.add_argument('--track', type=int, default=0, help='Índice absoluto da trilha no arquivo')
    parser.add_argument('--start', type=float, default=0, help='Início conhecido em segundos na gravação')
    parser.add_argument('--nature', choices=['HUMANA', 'TESTE_SINTETICO'], default='HUMANA')
    parser.add_argument('--policy', type=Path)
    parser.add_argument('--transcript', type=Path, help='ASR preservado, não marcação manual de takes')
    parser.add_argument('--model', type=Path, help='Modelo ASR local')
    args = parser.parse_args(argv)
    plan = read_json(args.plan)
    validate_plan(plan)
    checked_sources(plan)
    if args.command == 'finalize' and (not args.recording or not args.policy):
        parser.error('finalize exige --recording e --policy')
    if args.command == 'finalize' and not (args.transcript or args.model):
        parser.error('finalize exige --model ou --transcript preservado')
    if args.recording and (not args.recording.is_file() or args.recording.stat().st_size == 0):
        parser.error('Gravação inexistente/vazia')
    inputs = {'plano': {'path': str(args.plan.resolve()), 'sha256': digest(args.plan)},
              'fontes_sha256': plan['fontes_sha256']}
    if args.recording:
        inputs['gravacao'] = {'path': str(args.recording.resolve()), 'sha256': digest(args.recording),
                             'track': args.track, 'start_s': args.start}
    if args.policy:
        inputs['politica'] = {'path': str(args.policy.resolve()), 'sha256': digest(args.policy)}
    records = ROOT / 'videos' / plan['video_id'] / 'execucoes' / args.execution
    if records.exists():
        parser.error('Registros dessa execução já existem; use outro identificador')
    destination = reserve(plan['video_id'], args.execution)
    kind = 'REFERENCIA' if args.nature == 'TESTE_SINTETICO' else 'FINAL_TECNICO'
    try:
        audio, duration = None, None
        if args.recording:
            # Preserve a byte-identical input copy; process only the derived WAV.
            preserved = destination / ('gravacao_original' + args.recording.suffix.lower())
            shutil.copyfile(args.recording, preserved)
            audio, duration, metadata = extract_audio(preserved, destination, args.track, args.start)
            write_json(destination / 'gravacao_ffprobe.json', metadata)
        if args.command == 'finalize':
            policy = read_json(args.policy)
            if (policy.get('plano_origem_sha256') != digest(args.plan) or
                    policy.get('video_id') != plan['video_id'] or
                    policy['fontes_sha256'] != plan['fontes_sha256']):
                raise ValueError('Política não corresponde à revisão editorial')
            transcript = read_json(args.transcript) if args.transcript else transcribe(audio, args.model)
            write_json(destination / 'transcricao.json', transcript)
            try:
                words = validate_transcript(transcript, duration, digest(audio))
            except ValueError as exc:
                write_json(destination / 'associacao.json', {
                    'estado': 'PENDENTE_REVISAO', 'ocorrencias': [
                        {'tipo': 'TRANSCRICAO_TEMPORAL_INVALIDA', 'evidencia': str(exc)}],
                    'limite': 'Nenhuma associação temporal validada; transcrição bruta preservada.'})
                raise
            association = associate(plan, words, policy)
            write_json(destination / 'associacao.json', association)
            if association['estado'] != 'ASSOCIADO_CONSERVADORAMENTE':
                manifest(destination, plan['video_id'], kind, args.nature, inputs, 'PENDENTE_REVISAO',
                         'Associação não confirmada; ocorrências em associacao.json. Nenhum vídeo produzido e nenhuma fala eliminada/corrigida.')
                print(destination)
                return 2
            plan = human_plan(plan, association, duration, digest(args.recording))
            plan['tipo_entrega'] = kind
            plan['execucao'] = args.execution
            plan['audio_sha256'] = digest(audio)
            with (destination / (plan['video_id'] + '.srt')).open('x', encoding='utf-8') as stream:
                stream.write(srt(words))
        elif not audio:
            kind = 'PREVIA_SEM_AUDIO'
        write_json(destination / 'plano.json', plan)
        output = render(plan, destination, audio)
        manifest(destination, plan['video_id'], kind, args.nature, inputs, 'PENDENTE_REVISAO',
                 'MP4 renderizado e decodificado integralmente. Conferir áudio, legendas, takes e cortes na revisão audiovisual; não se presume escuta ou homologação. SRT baseado em ASR requer confirmação perceptiva.')
        print(output)
        return 0
    except Exception as exc:
        if not (destination / 'manifesto.json').exists():
            manifest(destination, plan['video_id'], kind, args.nature, inputs, 'PENDENTE_REVISAO',
                     f'Execução interrompida; resultados anteriores preservados: {type(exc).__name__}: {exc}')
        print(f'{destination}: {exc}', file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
