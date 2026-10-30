# V04-004 — referência audiovisual experimental

Estado: **PENDENTE_REVISAO**. Circuito dossiê → roteiro → mapa → montagem → MP4 executado; escuta perceptiva e homologação editorial humanas pendentes. Não é voz definitiva nem publicação.

## Fontes e ordem de execução

Main atualizada por pull seguro para `71853fc`; catálogo 04 revisado, SHA-256 `1611af1d4fe6d057daed3b74a5e41c7db6d4dae3ec0f0512afa2f3f307f34d9b`. Leitura integral do corpo e glossário; não há tabelas no catálogo. Dossiê 1.0 salvo integralmente com oito candidatos PROPOSTO antes da escolha excepcional de V04-004. `descoberta_concluida.json` e `selecao.json` registram ordem, horários e hash congelado. Não houve escolha prévia, uso de dossiês anteriores como conteúdo ou troca de candidato.

O roteiro 1.0 preserva exatamente a narrativa do candidato selecionado, única fonte editorial. Continua PROPOSTO. As fontes conceituais, catálogo, originais, inventário e protocolos não foram modificados. Apenas foram acrescentadas ocorrências ao checklist, preservando seu conteúdo anterior.

## Plano executado

Cinco segmentos, imagens estáticas proporcionais, fundo neutro e cortes secos. Sem GIF no vídeo. Regiões reais: `argopt3.png/tres_fontes`; `env4.png/fluxo_precedencia`; `env4.png/exemplos_fontes`; `resumo2.png/estrutura`; repetição de `env4.png/fluxo_precedencia`.

C05 usa uma região já pertencente às mídias do candidato, em lugar do painel de resumo2 que representa atribuição incremental em ordem inversa à consulta. Essa seleção ordinária preserva a fala, a política e a sequência. O roteiro não foi reescrito. A geometria do mapa permaneceu congelada durante a montagem.

A estimativa editorial de 70 s foi ajustada ao áudio real: **52,566984 s**, 1.577 quadros a 30 fps. Voz sintética local eSpeak NG `pt-br`, 155 palavras/minuto; ferramenta efetivamente disponível via espeakng-loader 0.2.4. O teste de serviço remoto falhou; a produção final não depende dele. Sem música, efeitos, novo conteúdo ou upload externo.

## Artefatos

- [Dossiê](../../editorial/dossies/04_Dossie_Editorial.docx), versão 1.0, oito candidatos PROPOSTO.
- [Roteiro](../../editorial/roteiros/04-004_Roteiro_Individual.docx), versão 1.0, PROPOSTO.
- [Mapa inclusivo](../../04_Argumentos_CommandLine/04_Mapa_Espacial.json), versão 1.0; [autoauditoria e 32 painéis](../../04_Argumentos_CommandLine/04_Autoauditoria_Mapa.md).
- [Plano medido](../../editorial/montagens/04-004_Montagem.json).
- [Manifesto](V04-004_Manifesto.json), [verificações](validacao.json), [legendas provisórias](V04-004.srt).
- [Quadros e cortes 01](evidencias/inspecao-01.jpg), [02](evidencias/inspecao-02.jpg), [03](evidencias/inspecao-03.jpg).
- MP4 real: `/workspace/artifacts/V04-004/V04-004.mp4`; 2138336 bytes; SHA-256 `5b7a7cc739515f8ccf88bd42f81a8699977463d3b82a3f0516c8cb8f31d2b6cb`.
- WAV: `/workspace/artifacts/V04-004/V04-004_Audio_Referencia.wav`; SHA-256 `4d6ab45cfbd63419be34f4428b30f028b378e217fb5b14f56627580cc4b03b9a`.

[Abrir MP4 V04-004](/workspace/artifacts/V04-004/V04-004.mp4). No visualizador, usar **Salvar vídeo como...** no navegador. Não foi presumido download. Binários permanecem fora do Git; sua persistência depende do ambiente.

## Verificações realizadas

- Dois DOCX íntegros, abertos por python-docx e exportados por LibreOffice; páginas inspecionadas. Referências do dossiê existem e correspondem ao inventário. O texto de todos os cinco takes e do SRT coincide com a narrativa congelada, sem acréscimo de outros candidatos.
- Mapa cobre os 31 originais visuais: 28 estáticos e três GIFs; 253 regiões com IDs únicos por arquivo, coordenadas válidas e hashes reais. Inspeção direta dos estáticos e 42 quadros de GIF. Todas as projeções representativas foram examinadas; 32 caixas corrigidas, duas delas em segundo ajuste. Limites temporais dos GIFs estão no laudo.
- MP4 decodificado integralmente por FFmpeg sem erro; 1080 × 1920, H.264 yuv420p progressivo, 30 fps, AAC mono 22.050 Hz. Duração coerente com o plano; diferença de contêiner inferior a um quadro.
- Áudio AAC efetivamente decodificado: RMS 0.091809, pico 0.814860; não silencioso, sem saturação numérica detectada. Isso não certifica inteligibilidade ou qualidade perceptiva.
- Dez cues SRT UTF-8, sequência e tempos válidos, sem sobreposição e dentro do vídeo. Cada intervalo deriva da contagem real de amostras PCM do enunciado sintetizado, com pausas medidas. Não há alinhamento palavra a palavra presumido. SRT **PROVISORIO**, correspondente à voz de referência.
- Quinze quadros do MP4 examinados: início/fim, todos os segmentos e ambos os lados dos quatro cortes. Títulos, diagramas, caixas e proporções preservados. Comparações ao quadro esperado resultaram em erro RGB médio de 1,36–1,55/255, compatível com a compressão, sem troca de segmento detectada.

## Limitações e pendências

Não houve reprodução temporal contínua nem escuta perceptiva pelo agente: a interface disponível permite inspeção de imagens e análise técnica, mas não ouvir o MP4. Pronúncia, naturalidade, ritmo e sincronismo fino precisam de avaliação humana no arquivo entregue. Não declarar revisão audiovisual integral, SRT final ou homologação editorial.

As visões integrais do mapa e painéis densos têm ressalvas de legibilidade e margens. Não foram usados como substitutos dos recortes legíveis selecionados. P04-001 registra a antecipação das alterações de delimitadores no GIF de strtok; não participa deste vídeo, não foi corrigida e não invalida as demais regiões. O estado de homologação de todas as fontes experimentais permanece distinto da autorização excepcional de execução.

## Reprodução e Git

Na raiz, com Python 3, Pillow, `espeakng-loader==0.2.4` e FFmpeg/ffprobe disponíveis: `python videos/V04-004/renderizar.py`. O script verifica os hashes das fontes congeladas e gera binários exclusivamente fora do checkout. A mesma voz/versão é necessária para reproduzir os tempos; o hash do MP4 original identifica esta execução, sem promessa de identidade binária entre plataformas.

Commit, push e PR da branch `audiovisual/experimento-integrado-capitulo-04` autorizados; hashes e URL informados na entrega da tarefa. Sem merge automático. A abertura da PR não homologa conteúdo, voz ou vídeo.
