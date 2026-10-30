"""Associação monotônica conservadora. Similaridade não equivale a aprovação semântica."""
import copy
import math
import re
import unicodedata


def tokens(text):
    plain = ''.join(c for c in unicodedata.normalize('NFD', text.lower())
                    if unicodedata.category(c) != 'Mn')
    return re.findall(r'[a-z0-9]+', plain)


def canonical(units, aliases):
    """Units retain the original word range, even after a documented paraphrase."""
    for alias in aliases:
        original, replacement = tokens(alias['de']), tokens(alias['para'])
        if not original or not replacement:
            raise ValueError('Equivalência vazia')
        result, i = [], 0
        while i < len(units):
            part = units[i:i + len(original)]
            if [x[0] for x in part] == original:
                result.extend((t, part[0][1], part[-1][2]) for t in replacement)
                i += len(original)
            else:
                result.append(units[i])
                i += 1
        units = result
    return units


def validate_transcript(transcript, duration, audio_hash):
    if transcript.get('audio_sha256') != audio_hash:
        raise ValueError('Transcrição não corresponde ao áudio de trabalho')
    words = transcript.get('words', [])
    if not words:
        raise ValueError('Transcrição sem palavras temporizadas')
    previous = 0
    for word in words:
        a, b = word['start'], word['end']
        if not all(math.isfinite(t) for t in [a, b]) or not (previous <= a < b <= duration + .001):
            raise ValueError('Palavras sem tempos válidos, sobrepostas ou fora do áudio')
        if not tokens(word['word']):
            raise ValueError('Palavra vazia')
        previous = b
    if not transcript.get('provenance'):
        raise ValueError('Procedência da transcrição ausente')
    return words


def associate(plan, words, policy):
    aliases = policy.get('equivalencias', [])
    expected, owner = [], []
    for scene, segment in enumerate(plan['segmentos']):
        ts = tokens(segment['texto'])
        unit = canonical([(t, i, i) for i, t in enumerate(ts)], aliases)
        expected.extend(x[0] for x in unit)
        owner.extend([scene] * len(unit))
    actual = []
    for index, word in enumerate(words):
        actual.extend((t, index, index) for t in tokens(word['word']))
    actual = canonical(actual, aliases)
    n, m = len(expected), len(actual)
    cost = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        cost[i][0] = i
    for j in range(m + 1):
        cost[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cost[i][j] = min(cost[i-1][j] + 1, cost[i][j-1] + 1,
                             cost[i-1][j-1] + (expected[i-1] != actual[j-1][0]))
    i, j, steps = n, m, []
    while i or j:
        if i and j and cost[i][j] == cost[i-1][j-1] + (expected[i-1] != actual[j-1][0]):
            steps.append((i-1, j-1, 'IGUAL' if expected[i-1] == actual[j-1][0] else 'SUBSTITUICAO'))
            i, j = i-1, j-1
        elif i and cost[i][j] == cost[i-1][j] + 1:
            steps.append((i-1, None, 'OMISSAO_OU_ASR'))
            i -= 1
        else:
            steps.append((max(0, i-1), j-1, 'ACRESCIMO_OU_REPETICAO'))
            j -= 1
    grouped = [set() for _ in plan['segmentos']]
    occurrences, edits = [], []
    for ei, aj, operation in reversed(steps):
        scene = owner[ei]
        if aj is not None:
            grouped[scene].update(range(actual[aj][1], actual[aj][2] + 1))
        if operation != 'IGUAL':
            edits.append({'take': plan['segmentos'][scene]['id'], 'operacao': operation,
                          'esperado': expected[ei] if operation != 'ACRESCIMO_OU_REPETICAO' else None,
                          'observado': actual[aj][0] if aj is not None else None,
                          'palavra_indice': actual[aj][1] if aj is not None else None})
    if edits:
        occurrences.append({'tipo': 'CORRESPONDENCIA_NAO_VERIFICADA', 'edicoes': edits,
                            'limite': 'Pode ser ASR, reformulação não cadastrada, omissão, repetição ou ordem divergente. Não corrigir a fala nem inferir equivalência.'})
    assignments = []
    previous = -1
    for segment, group in zip(plan['segmentos'], grouped):
        indices = sorted(group)
        if not indices or indices[0] <= previous or indices != list(range(indices[0], indices[-1] + 1)):
            occurrences.append({'tipo': 'ASSOCIACAO_AMBIGUA', 'take': segment['id']})
        if indices:
            previous = indices[-1]
        text = ' '.join(words[k]['word'].strip() for k in indices)
        normalized = ' '.join(tokens(text))
        for guard in policy.get('ressalvas_essenciais', []):
            if guard['take'] == segment['id'] and not any(re.search(p, normalized) for p in guard['padroes_aceitos']):
                occurrences.append({'tipo': 'RESSALVA_ESSENCIAL_NAO_CONFIRMADA',
                                    'take': segment['id'], 'id': guard['id'], 'texto_observado': text})
        assignments.append({'take': segment['id'], 'indices_palavras': indices, 'texto_observado': text,
                            'inicio_fala_s': words[indices[0]]['start'] if indices else None,
                            'fim_fala_s': words[indices[-1]]['end'] if indices else None,
                            'correspondencia': 'TEXTUAL' if not edits and not aliases else 'CANONICA_OU_NAO_VERIFICADA'})
    if set().union(*grouped) != set(range(len(words))):
        occurrences.append({'tipo': 'PALAVRAS_NAO_ASSOCIADAS'})
    return {'estado': 'ASSOCIADO_CONSERVADORAMENTE' if not occurrences else 'PENDENTE_REVISAO',
            'metodo': 'Alinhamento global monotônico por distância de edição; aceitação somente sem edições após equivalências documentadas. Sem limiar de similaridade/confiança arbitrário.',
            'equivalencias_consideradas': aliases, 'distancia_edicao': cost[n][m],
            'takes': assignments, 'ocorrencias': occurrences,
            'limite': 'Correspondência textual não certifica transcrição nem significado. Reformulações não cadastradas permanecem pendentes.'}


def human_plan(source, association, duration, recording_hash):
    if association['estado'] != 'ASSOCIADO_CONSERVADORAMENTE':
        raise ValueError('Associação pendente não autoriza remontagem')
    plan = copy.deepcopy(source)
    fps = plan['perfil']['fps']
    total = math.ceil(duration * fps)
    starts = [0] + [math.floor(s['inicio_fala_s'] * fps) for s in association['takes'][1:]]
    for i, (segment, found) in enumerate(zip(plan['segmentos'], association['takes'])):
        end = starts[i+1] if i+1 < len(starts) else total
        if end <= starts[i]:
            raise ValueError('Não há quadros suficientes para os takes')
        if found['fim_fala_s'] > end / fps + 1e-6:
            raise ValueError('Corte antes de terminar a fala do take')
        segment.update(inicio_s=starts[i]/fps, duracao_s=(end-starts[i])/fps,
                       frame_inicial=starts[i], quadros=end-starts[i],
                       texto_pronunciado=found['texto_observado'])
    plan.update(duracao_s=total/fps, estado='PROPOSTO', tipo_entrega='FINAL_TECNICO',
                audio='Gravação externa integral, sem alteração de velocidade',
                gravacao_sha256=recording_hash)
    return plan


def srt(words):
    def timestamp(t):
        ms = round(t * 1000)
        return f'{ms//3600000:02d}:{ms//60000%60:02d}:{ms//1000%60:02d},{ms%1000:03d}'
    chunks, current = [], []
    for word in words:
        current.append(word)
        # Readability segmentation, not a confidence threshold or editing of speech.
        if word['word'].rstrip().endswith(('.', '?', '!', ';', ':')) or len(current) >= 12:
            chunks.append(current)
            current = []
    if current:
        chunks.append(current)
    for chunk in chunks:
        if round(chunk[0]['start'] * 1000) >= round(chunk[-1]['end'] * 1000):
            raise ValueError('Cue não representável com precisão de milissegundos')
    return '\n\n'.join(f"{i}\n{timestamp(c[0]['start'])} --> {timestamp(c[-1]['end'])}\n" +
                        ' '.join(w['word'].strip() for w in c)
                        for i, c in enumerate(chunks, 1)) + '\n'
