import copy
import json
import tempfile
import unittest
import wave
from unittest.mock import patch
from pathlib import Path
from videos.motor3.alignment import associate, human_plan, srt, tokens, validate_transcript
from videos.motor3.media import ROOT, checked_sources, read_json, reserve, validate_plan, write_json, extract_audio


PLAN = read_json(ROOT / 'editorial/montagens/04-004_Montagem.json')
POLICY = read_json(ROOT / 'videos/motor3/politica_v04.json')


def transcript(texts):
    words, t = [], .1
    for i, text in enumerate(texts):
        for word in text.split():
            words.append({'word': word, 'start': t, 'end': t + .2})
            t += .3
        t += i * .5
    return words


class TemporalTests(unittest.TestCase):
    def test_real_plan_and_sources(self):
        self.assertEqual(validate_plan(PLAN), 1577)
        self.assertEqual(len(checked_sources(PLAN)), 5)

    def test_reject_gap_overlap_negative_nan_duplicate_and_inconsistent_frames(self):
        for key, val in [('inicio_s', 1), ('duracao_s', -1), ('duracao_s', float('nan')),
                         ('id', 'S02'), ('quadros', 1)]:
            plan = copy.deepcopy(PLAN)
            plan['segmentos'][0][key] = val
            with self.assertRaises(ValueError):
                validate_plan(plan)

    def test_reject_wrong_region_or_geometry(self):
        for key, val in [('regiao_id', 'inexistente'), ('bbox_px', [0, 0, 1, 1])]:
            plan = copy.deepcopy(PLAN)
            plan['segmentos'][0][key] = val
            with self.assertRaises(ValueError):
                checked_sources(plan)

    def test_different_durations_explicit(self):
        plan = copy.deepcopy(PLAN)
        cursor = 0
        for seg in plan['segmentos']:
            frames = seg['quadros'] + 30
            seg.update(inicio_s=cursor/30, duracao_s=frames/30,
                       frame_inicial=cursor, quadros=frames)
            cursor += frames
        plan['duracao_s'] = cursor/30
        self.assertEqual(validate_plan(plan), 1727)

    def test_exclusive_json_write(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / 'record.json'
            write_json(path, {'a': 1})
            with self.assertRaises(FileExistsError):
                write_json(path, {'a': 2})
            self.assertEqual(read_json(path), {'a': 1})


class InputTests(unittest.TestCase):
    def test_execution_directory_is_exclusive(self):
        with tempfile.TemporaryDirectory() as tmp, patch('videos.motor3.media.ARTIFACTS', Path(tmp)):
            dest = reserve('V04-004', 'teste')
            marker = dest / 'preservar.txt'
            marker.write_text('original')
            with self.assertRaises(FileExistsError):
                reserve('V04-004', 'teste')
            self.assertEqual(marker.read_text(), 'original')
            with self.assertRaises(ValueError):
                reserve('V04-004', '../escape')

    def test_silent_input_and_wrong_track_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / 'silencio.wav'
            with wave.open(str(source), 'wb') as wav:
                wav.setnchannels(1)
                wav.setsampwidth(2)
                wav.setframerate(48000)
                wav.writeframes(b'\0\0' * 48000)
            with self.assertRaises(ValueError):
                extract_audio(source, root, 1, 0)
            with self.assertRaises(ValueError):
                extract_audio(source, root, 0, 0)

    def test_critical_short_subtitle_cannot_have_zero_duration(self):
        with self.assertRaises(ValueError):
            srt([{'word': 'Não.', 'start': .0001, 'end': .0002}])


class AlignmentTests(unittest.TestCase):
    def setUp(self):
        self.texts = [s['texto'] for s in PLAN['segmentos']]
        self.words = transcript(self.texts)

    def test_exact_with_different_pauses_associates_without_markers(self):
        result = associate(PLAN, self.words, POLICY)
        self.assertEqual(result['estado'], 'ASSOCIADO_CONSERVADORAMENTE')
        final = human_plan(PLAN, result, self.words[-1]['end'] + 1, 'hash')
        validate_plan(final)
        self.assertNotEqual(final['segmentos'][1]['inicio_s'], PLAN['segmentos'][1]['inicio_s'])
        self.assertEqual([x['regiao_id'] for x in final['segmentos']], [x['regiao_id'] for x in PLAN['segmentos']])
        self.assertLessEqual(self.words[-1]['end'], final['duracao_s'])

    def test_critical_negation_missing_never_accepted(self):
        self.texts[3] = self.texts[3].replace('Não é', 'É')
        result = associate(PLAN, transcript(self.texts), POLICY)
        self.assertEqual(result['estado'], 'PENDENTE_REVISAO')
        self.assertIn('RESSALVA_ESSENCIAL_NAO_CONFIRMADA', [x['tipo'] for x in result['ocorrencias']])
        with self.assertRaises(ValueError):
            human_plan(PLAN, result, 70, 'hash')

    def test_entire_essential_take_missing(self):
        result = associate(PLAN, transcript(self.texts[:3] + self.texts[4:]), POLICY)
        self.assertEqual(result['estado'], 'PENDENTE_REVISAO')

    def test_omission_repetition_reordering_and_unknown_reformulation_block(self):
        variants = [self.texts[:2] + self.texts[3:], self.texts[:1] + self.texts,
                    list(reversed(self.texts)), [self.texts[0].replace('configuração', 'banana')] + self.texts[1:]]
        for texts in variants:
            self.assertEqual(associate(PLAN, transcript(texts), POLICY)['estado'], 'PENDENTE_REVISAO')

    def test_documented_lexical_reformulation_preserves_spoken_words(self):
        policy = copy.deepcopy(POLICY)
        policy['equivalencias'] = [{'de': 'Um programa', 'para': 'Uma aplicação'}]
        self.texts[0] = self.texts[0].replace('Uma aplicação', 'Um programa', 1)
        words = transcript(self.texts)
        result = associate(PLAN, words, policy)
        self.assertEqual(result['estado'], 'ASSOCIADO_CONSERVADORAMENTE')
        self.assertTrue(result['takes'][0]['texto_observado'].startswith('Um programa'))
        self.assertIn('Um programa', srt(words))
        self.assertNotIn('Uma aplicação', srt(words))

    def test_bad_timestamps_wrong_audio_and_missing_provenance(self):
        doc = {'words': self.words, 'audio_sha256': 'hash', 'provenance': {'teste': True}}
        validate_transcript(doc, 1000, 'hash')
        with self.assertRaises(ValueError):
            validate_transcript(doc, 1000, 'outro')
        for data in [{**doc, 'provenance': {}}, {**doc, 'words': []},
                     {**doc, 'words': [{'word': 'erro', 'start': 5, 'end': 2}]}]:
            with self.assertRaises(ValueError):
                validate_transcript(data, 1000, 'hash')


if __name__ == '__main__':
    unittest.main()
