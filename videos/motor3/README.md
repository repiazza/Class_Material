# Motor 3 — primeiro núcleo experimental

Implementa **execução de plano temporal independente de síntese** e um fluxo conservador de finalização com áudio externo. Referência: V04-004. Não altera o Motor 1, os materiais, o roteiro, o mapa ou os contratos. Não incorpora apresentador, legendas permanentes, efeitos, publicação ou Motor 4.

## Estado demonstrado

| Capacidade | Resultado |
| --- | --- |
| Marco A: executar plano explícito | Demonstrado com dois MP4: 1.577 e 1.727 quadros; 52,566667 e 57,566667 s. Mesmas cinco regiões, um segundo adicional por take. |
| Áudio externo exclusivo | Demonstrado com o WAV **sintético anterior**, sem chamar TTS. Não é prova de gravação humana. |
| Associação e nova montagem | Fluxo completo demonstrado com dez enunciados e tempos fornecidos do SRT sintético, sem IDs de takes na transcrição. É teste controlado, não reconhecimento autônomo. |
| ASR local real | Executado com faster-whisper base; texto incorreto e uma palavra com duração zero. Finalização interrompida; transcrição preservada, sem MP4/SRT falsamente validados. |
| Gravação humana | Não fornecida; ausência confirmada pelo responsável. Marco B humano/autônomo **não concluído**. |
| Reformulação narrativa geral | Não implementada como classificador semântico geral. Equivalências documentadas são suportadas; desconhecidas ficam pendentes. |

Comparação no mesmo instante: [quadro 460 nas duas montagens](evidencias/A-comparacao-mesmo-instante.jpg). Dados de validação: [JSON](evidencias/validacao-renderizacoes.json). Laudo: [RELATORIO.md](RELATORIO.md).

## Preparação

Python 3.12, FFmpeg/ffprobe no PATH; instalar `requirements.txt`. Somente a transcrição local exige `requirements-asr.txt`. Foi fixado `av==15.1.0`: PyAV 19.0.2, instalado inicialmente, não aceitou o argumento `metadata_errors` usado pelo faster-whisper 1.2.1. Não há dependência de TTS no executor.

O backend recebe um **diretório local** de modelo convertido para CTranslate2. Downloads são uma preparação explícita, não uma operação oculta do comando. Nesta execução, o modelo foi `Systran/faster-whisper-base`, revisão `ebe41f70d5b6dfa9166e2c581c45c9c0cfc57b66`. Os hashes dos arquivos e os parâmetros efetivamente usados estão na transcrição preservada em `../V04-004/execucoes/M3-B-asr-sintetico/transcricao.json`. Pesos e dependências instaladas ficam fora do Git.

## Marco A

Da raiz do repositório:

```bash
python -B -m videos.motor3 render \
  --plan videos/motor3/evidencias/A-original.json \
  --execution minha-previa-01 --nature TESTE_SINTETICO

python -B -m videos.motor3 render \
  --plan videos/motor3/evidencias/A-mais-um-segundo.json \
  --execution minha-previa-02 --nature TESTE_SINTETICO
```

Sem `--recording`, gera `PREVIA_SEM_AUDIO`, sem SRT. Com gravação, `--recording`, `--track` (índice absoluto da trilha) e `--start` (segundos do início conhecido) permitem testar a execução de um plano já temporizado. A duração do áudio deve corresponder ao plano, com diferença máxima de um quadro para arredondamento; o executor não estica nem trunca a fala para adaptar a um plano inadequado.

O plano é lido **antes** de renderizar e contém todas as escolhas visuais. O executor não codifica a lista de regiões do V04-004. O primeiro perfil suporta 1080 × 1920, 30 fps, fundo neutro, imagens estáticas e corte seco. Outros modos são rejeitados, não simulados. Valida continuidade temporal, grade de quadros, IDs, geometria e hashes das fontes.

## Marco B

```bash
python -B -m videos.motor3 finalize \
  --plan editorial/montagens/04-004_Montagem.json \
  --recording /caminho/gravacao-humana.wav --track 0 --start 0 \
  --execution humana-01 --nature HUMANA \
  --policy videos/motor3/politica_v04.json \
  --model /caminho/modelo-local
```

`HUMANA` é a natureza **declarada da entrada**, não detecção automática de autoria vocal. Nunca identificar o WAV sintético anterior como humano.

É possível reexecutar a associação usando `--transcript /caminho/transcricao.json` em vez de `--model`, preservando os resultados intermediários. Isso não comprova que a transcrição importada foi obtida autonomamente. Para o teste controlado disponível, usar `--nature TESTE_SINTETICO`, o WAV sintético original e `--transcript videos/motor3/evidencias/transcricao-controle.json`.

A transcrição contém `audio_sha256` do WAV de trabalho, `provenance` e `words` com `start`, `end`, `word`. O backend produz palavras; o teste controlado fornece enunciados, explicitamente identificado como tal. Não há marcação obrigatória de takes na entrada. Tempos precisam ser finitos, crescentes, não sobrepostos e internos ao áudio; duração zero não é reparada por adivinhação.

O áudio original é copiado byte a byte, com hash e metadados. O trabalho usa PCM mono 48 kHz; o backend pode reamostrar internamente para ASR. Não há remoção de silêncios, aceleração, mistura sintética ou edição da interpretação. Somente a trilha externa selecionada entra no MP4. O deslocamento inicial conhecido é registrado; o restante da gravação é preservado, incluindo pausas e silêncio final.

### Associação e limites

O alinhamento global monotônico registra as edições e os trechos associados aos takes. Para este núcleo, só avança se houver correspondência completa após normalização ortográfica e equivalências explicitamente documentadas na política. **Distância de edição é evidência diagnóstica, não um limiar de aprovação.** Não há porcentagem arbitrária de confiança.

A política está vinculada ao hash do plano e às revisões editoriais. A ressalva de S04 (`Não é uma prioridade imposta pela linguagem C a todos os programas`) tem verificação própria. Omissão, acréscimo, repetição, ordem incompatível, reformulação desconhecida, ressalva não confirmada ou timestamps inválidos levam a `PENDENTE_REVISAO`. Não se distingue automaticamente um erro ASR de uma divergência real somente pela distância textual. Nenhuma fala é eliminada ou corrigida para forçar encaixe.

As equivalências aceitas devem ser fundamentadas; não são aprendidas automaticamente dos erros do teste para obter aprovação. O teste de uma reformulação conhecida está na suíte. A política V04 entregue não contém equivalências novas. Formulações humanas equivalentes podem gerar falsos bloqueios; isso é uma limitação explícita, não autonomia semântica plena.

Quando a associação passa, cada composição começa no quadro imediatamente anterior ou igual ao início da fala correspondente. A cena anterior permanece durante a pausa. Não se permite cortar antes de terminar a fala anterior. A última composição acompanha o restante do áudio, com arredondamento total inferior a um quadro. Isso não substitui o alinhamento interno dos takes.

O SRT usa o texto e os tempos observados na transcrição; não copia o roteiro como fala humana. ASR não é prova de transcrição correta: os resultados continuam sujeitos à revisão perceptiva. As probabilidades são registradas, sem aprovação por limiares não calibrados. Não há legendas queimadas.

## Saídas e preservação

Cada `--execution` reserva um novo diretório exclusivo:

- `/workspace/artifacts/V04-004/<execucao>/`: original recebido, WAV de trabalho, intermediários e MP4 real, além dos registros.
- `videos/V04-004/execucoes/<execucao>/`: cópias leves de plano, transcrição, associação, SRT, manifesto, metadados e relatório, conforme a execução.

Essa separação por execução atende à autorização de não sobrescrever a referência em `/workspace/artifacts/V04-004/V04-004.mp4`. Nenhum ID editorial novo foi criado. Diretórios existentes são rejeitados; uma falha mantém seus registros e exige outro identificador para uma nova execução. Não se deve executar novamente o script antigo para finalizar áudio humano, pois ele é preservado como Motor 1 e escreve os produtos sintéticos anteriores.

Os manifestos atuais registram hashes da implementação; registros capturados antes dessa adição permanecem preservados sem inventar hashes retroativos. Erros e resultados parciais não são apagados. Não há upload, commit, push ou merge dentro do programa. MP4/WAV/MP3 não devem entrar no Git.

## Verificação e reprodução

```bash
python -B -m unittest discover -s videos/motor3/tests -v
```

São 14 testes sobre tempos, fontes, exclusividade, silêncio digital, trilha errada, reformulação cadastrada, omissão, repetição, reordenação, negacão essencial, associação com pausas diferentes e SRT. Os MP4 de demonstração também passaram por decodificação integral, conferência de quadros, áudio e inspeção visual documentada no laudo.

Para reconstruir uma execução, preservar gravação, transcrição, política, plano, hashes, versões e parâmetros. Reusar a transcrição preservada evita variação de ASR. Reproduzibilidade funcional não promete MP4 binariamente idêntico entre plataformas. Não há escuta perceptiva ou revisão audiovisual integral automática implementada; isso não foi transferido silenciosamente ao futuro Motor 4.
