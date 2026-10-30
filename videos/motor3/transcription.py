"""Backend opcional local; nunca usa o roteiro como prompt para completar a fala."""
from importlib.metadata import version
from pathlib import Path
from .media import digest


def transcribe(audio, model_path):
    try:
        from faster_whisper import WhisperModel
    except ImportError as exc:
        raise RuntimeError('Backend indisponível: instalar requirements-asr.txt ou fornecer transcrição temporizada com procedência') from exc
    model_path = Path(model_path).resolve()
    if not model_path.is_dir():
        raise ValueError('Forneça diretório local de modelo; downloads são preparação explícita')
    model_files = {str(p.relative_to(model_path)): digest(p) for p in sorted(model_path.rglob('*')) if p.is_file()}
    model = WhisperModel(str(model_path), device='cpu', compute_type='int8', cpu_threads=4)
    segments, info = model.transcribe(str(audio), language='pt', word_timestamps=True,
                                       beam_size=5, vad_filter=False, condition_on_previous_text=False)
    records = list(segments)
    words = [{'start': w.start, 'end': w.end, 'word': w.word, 'probability': w.probability}
             for s in records for w in (s.words or [])]
    return {'audio_sha256': digest(audio), 'words': words,
            'segments': [{'start': s.start, 'end': s.end, 'text': s.text} for s in records],
            'provenance': {'backend': 'faster-whisper', 'version': version('faster-whisper'),
                           'ctranslate2': version('ctranslate2'), 'model_files_sha256': model_files,
                           'language': info.language, 'compute_type': 'int8', 'cpu_threads': 4,
                           'beam_size': 5, 'word_timestamps': True, 'vad_filter': False,
                           'condition_on_previous_text': False, 'prompt_roteiro': False},
            'limite': 'Tempos e palavras são estimativas ASR, não transcrição humana homologada. Probabilidades registradas, sem limiar não calibrado.'}
