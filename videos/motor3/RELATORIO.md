# Primeiro núcleo do Motor 3 — laudo de implementação

Base: `d065ffc`, PR #27 integrada. Branch: `audiovisual/motor3-nucleo`. Autorização: primeiro núcleo funcional, Marco A e Marco B; sem merge. Nenhuma gravação humana foi fornecida; o responsável confirmou sua ausência durante a execução.

## Resultado por capacidade

| Capacidade | Implementada | Demonstrada |
| --- | --- | --- |
| Execução de plano temporal antes da renderização, sem TTS | Sim | Sim: mesmos cinco takes, 52,566667 e 57,566667 s; 1.577 e 1.727 quadros |
| Seleção, preservação e extração de áudio externo | Sim | Sim, com WAV sintético preexistente, explicitamente identificado como teste |
| Transcrição temporal local | Sim, backend opcional | Executada; resultado inadequado sobre a voz eSpeak de referência, preservado e bloqueado |
| Associação monotônica sem marcação de takes | Sim, conservadora | Testes com pausas, correspondência literal e equivalência cadastrada; fluxo completo com enunciados e tempos sintéticos fornecidos |
| Detecção de divergências e ressalva essencial | Sim, lexical conservadora | Testes de omissão, repetição, reordenação, reformulação desconhecida e retirada do “Não” de S04 |
| Nova montagem e SRT a partir da representação temporal | Sim | MP4/SRT do teste controlado; não é comprovação de ASR correto nem de áudio humano |
| Finalização autônoma com gravação humana real | Fluxo implementado, sujeito aos limites abaixo | **Não demonstrada e não concluída**: insumo ausente; ASR sintético não foi aprovado |
| Equivalência narrativa geral e análise semântica abrangente | Não | Não; reformulações não cadastradas geram pendência |

Os resultados não homologam voz, roteiro ou vídeo. Não foi implementado Motor 4, composição do apresentador ou legenda permanente.

## Evidência do Marco A

Os planos [original](evidencias/A-original.json) e [com um segundo adicional por take](evidencias/A-mais-um-segundo.json) preservam fontes, IDs e escolhas visuais. O executor leu os tempos antes de produzir o vídeo, sem importar ou chamar TTS.

No **mesmo quadro 460**, a montagem original já apresenta S02 e a estendida ainda apresenta S01: [comparação visual](evidencias/A-comparacao-mesmo-instante.jpg). A diferença total foi de cinco segundos/150 quadros. Não houve regeneração de dossiê, roteiro, mapa ou imagens originais.

MP4 de teste, fora do checkout:

- [Marco A, tempos originais](/workspace/artifacts/V04-004/M3-A-original/V04-004.mp4), sem áudio.
- [Marco A, tempos alterados](/workspace/artifacts/V04-004/M3-A-mais-um-segundo/V04-004.mp4), sem áudio.
- [Marco A, áudio externo de teste](/workspace/artifacts/V04-004/M3-A-audio-externo/V04-004.mp4), voz sintética anterior como arquivo recebido; nenhuma síntese nova.

## Evidência e limites do Marco B

Foi instalado e executado faster-whisper 1.2.1 com o modelo multilíngue base, CPU int8. A incompatibilidade inicial com PyAV 19.0.2 foi resolvida pela versão 15.1.0, fixada no arquivo de dependências. Não foi adotado serviço externo de transcrição; áudio e vídeo não foram enviados para upload.

A transcrição real está em [M3-B-asr-sintetico](../V04-004/execucoes/M3-B-asr-sintetico/transcricao.json), com hashes do modelo e parâmetros. Apresenta trocas textuais relevantes e uma palavra `o` com início e fim em **50,74 s**. O fluxo recusou a temporização e não gerou vídeo nem SRT a partir desse resultado. A repetição determinística com a transcrição preservada confirma o bloqueio em [M3-B-bloqueio-final](../V04-004/execucoes/M3-B-bloqueio-final/associacao.json), sem executar ASR novamente.

Não foram cadastradas equivalências para “corrigir” os erros ASR do teste. Também não se tomou similaridade geral como evidência de preservação da ressalva de S04. A evidência disponível não permite inferir o desempenho do mesmo modelo sobre uma gravação humana clara.

Para testar o encadeamento restante, foram fornecidos dez enunciados com os tempos medidos dos blocos PCM da produção sintética anterior: [entrada controlada](evidencias/transcricao-controle.json). Esses enunciados não contêm IDs ou marcações de takes. A associação produziu os cinco vínculos, um novo plano e SRT, preservando o áudio externo integral:

- [MP4 de integração controlada, **sintético**](/workspace/artifacts/V04-004/M3-B-controle-enunciados/V04-004.mp4).
- [Associação](../V04-004/execucoes/M3-B-controle-enunciados/associacao.json), [plano](../V04-004/execucoes/M3-B-controle-enunciados/plano.json) e [SRT de teste](../V04-004/execucoes/M3-B-controle-enunciados/V04-004.srt).

Isso demonstra execução técnica com representação temporal fornecida. **Não demonstra transcrição autônoma bem-sucedida nem produção humana.** Os tempos do SRT antigo foram usados somente neste teste identificado; não são um procedimento para legendas humanas.

## Validações executadas

- **14 testes passaram**: planos com tempos diferentes; lacuna, sobreposição, duração negativa/NaN, IDs duplicados, contagem contraditória de quadros, região inexistente, geometria divergente, exclusividade de arquivo/diretório, trilha errada, silêncio digital, associação com pausas diferentes, equivalência lexical documentada, omissão, repetição, ordem divergente, ressalva ausente e cue de duração não representável em milissegundos.
- Quatro MP4 reais, todos H.264/yuv420p, 1080 × 1920, 30 fps e decodificados integralmente sem erro. Prévias A sem áudio; dois testes com áudio AAC externo.
- Para cada MP4, 15 quadros decodificados comparados às projeções esperadas: começo/fim, pontos médios dos cinco takes e ambos os lados dos quatro cortes. Erro médio RGB inferior a 5/255. Os cinco takes de cada saída foram examinados visualmente nos painéis.
- Nos dois testes com áudio, AAC decodificado não silencioso e correlação de aproximadamente **0,999416** com o WAV externo de trabalho, sem fonte sintética adicional misturada. O arquivo recebido foi preservado e a narração não foi acelerada.
- SRT controlado com texto/intervalos da representação recebida, dentro do vídeo. Correspondência ao texto de entrada não é certificação perceptiva de uma transcrição humana.
- Fontes editoriais e produção sintética anteriores preservadas por SHA-256. O script antigo de referência não foi alterado e continua independente do novo executor.

Resultados numéricos, hashes e quadros: [validacao-renderizacoes.json](evidencias/validacao-renderizacoes.json). Painéis: [original](evidencias/M3-A-original.jpg), [alterado](evidencias/M3-A-mais-um-segundo.jpg), [áudio externo](evidencias/M3-A-audio-externo.jpg), [integração controlada](evidencias/M3-B-controle-enunciados.jpg).

Não houve escuta perceptiva ou reprodução audiovisual contínua pelo agente. Não se declara sincronismo perceptivo integral ou homologação. O teste sintético controlado permanece REFERENCIA; o piloto humano só poderá ser avaliado após receber a gravação.

## Preservação, reprodução e pendências

Binários permanecem em `/workspace/artifacts/V04-004/<execucao>/`; registros leves são versionados por execução em `videos/V04-004/execucoes/`. Nenhuma saída anterior foi sobrescrita. Para obter um vídeo, abrir o link real no visualizador e utilizar **Salvar vídeo como...**. Não foi presumido download, nem persistência após encerramento do ambiente.

O caso `M3-B-bloqueio-final` foi executado após as adições finais de métricas e hashes da implementação; seus registros contêm essa revisão do núcleo. Os primeiros registros foram preservados como produzidos, sem inventar procedência retroativa.

Pendências concretas: gravação humana; avaliação do backend de transcrição sobre esse insumo; calibração baseada em evidências e cobertura fundamentada de reformulações; revisão perceptiva de legendas e áudio. O núcleo prefere bloquear uma associação não comprovada a produzir silenciosamente uma composição incorreta. Essa estratégia pode gerar falsos bloqueios; não equivale à autonomia semântica plena.

Instruções de instalação, execução e limites: [README.md](README.md). Commit, push e PR autorizados nesta etapa; sem merge automático. A aprovação da PR não equivale à conclusão do Marco B humano ou à homologação audiovisual.
