# V03-003 — NOT precisa de uma largura

**Modalidade: REFERENCIA experimental. Estado: PENDENTE_REVISAO.**

[Abrir MP4 no workspace](/workspace/artifacts/V03-003/V03-003.mp4). No visualizador, use **Salvar vídeo como...** para obter o arquivo. O arquivo real existe e foi validado; não se afirma que o usuário o abriu ou baixou. Não é necessária confirmação de download para a entrega técnica.

[WAV de referência para reprodução](/workspace/artifacts/V03-003/V03-003_Audio_Referencia.wav) · [SRT provisório da referência](V03-003.srt) · [Manifesto](V03-003_Manifesto.json) · [Plano](../../editorial/montagens/03-003_Montagem.json)

## Produção e escolhas

Base sincronizada com main em e203083cfaf267d17489720da86de01de8684a25. Roteiro lido integralmente, incluindo tabela; cinco takes e todas as falas preservados literalmente. Mapa/autoauditoria, ocorrências e original foram confrontados somente para os elementos usados. Não se repetiu auditoria dos outros capítulos nem se alterou fonte.

A duração estimada de 68 s foi adaptada à referência sintetizada: WAV de 91,848 s e MP4 de 91,833333 s. A narração não foi acelerada, resumida ou reescrita. Diferença final de vídeo/AAC/PCM fica abaixo de um quadro: os 30 ms finais ausentes da trilha AAC são silêncio digital confirmado, depois do último bloco falado/SRT em 91,648 s. O plano conserva as estimativas e registra separadamente os tempos medidos.

| Take | Intervalo medido da montagem (s) | Regiões reais do PNG | Função |
|---|---|---|---|
| T01 | 0.000–14.296 | caracteristicas, exemplo_8_bits | Hipótese de largura e inversão |
| T02 | 14.296–32.488 | exemplo_8_bits | Inversão de cada uma das oito posições |
| T03 | 32.488–49.040 | exemplo_8_bits | Leitura sem sinal e resultado 245 |
| T04 | 49.040–70.904 | caracteristicas, logico_vs_bitwise | Tipo efetivo em C e distinção de negação lógica |
| T05 | 70.904–91.848 | caracteristicas, exemplo_8_bits | Síntese e retorno ao modelo de oito bits |

O último limite do plano refere-se ao PCM antes da quantização da exportação. Todos os recortes vêm exclusivamente de bitwise_not.png e das caixas já mapeadas. A mesma região permanece entre frases quando sustenta a explicação; isso é uma escolha de imagem estática, não congelamento acidental. As barras neutras preservam a proporção e o painel completo. Não há GIFs, efeitos, trilha musical ou legendas queimadas.

M03-P-001 não é exibida: integral, interpretacao e complemento_dois não participam. As demais pendências do capítulo referem-se a fontes ausentes desta montagem. Não se escolheu promocao_inteiros, que detalha um ambiente de 32 bits e um resultado signed desnecessário à fala. Caracteristicas sustenta o limite de tipo sem fixar tamanho de int; logico_vs_bitwise sustenta ~ versus !; exemplo_8_bits apresenta o modelo unsigned e 245. Nenhuma correção pedagógica pendente foi implementada ou disfarçada.

O cartão binário novo tornou-se desnecessário porque exemplo_8_bits contém o par correto. Os textos exercicio.md/gabarito.md continuam referências documentais do roteiro; o pedido atual autoriza selecionar regiões válidas do PNG para acompanhar essas falas. Não se projetaram documentos completos, nem se acrescentou conteúdo editorial. Não houve edição do original ou das coordenadas.

## Voz, legendas e reprodução

Voz de referência pt-BR realmente sintetizada pelo endpoint Google Translate TTS, client=tw-ob. Doze requisições de frases literais produziram MP3s decodificados para PCM16 mono 48 kHz; o serviço não informa modelo/versão de voz. Preservados WAV final e trechos no diretório de artefatos. Não é voz humana definitiva nem locução homologada.

Doze blocos SRT derivam dos intervalos medidos dos trechos WAV realmente usados, sem incluir as pausas de montagem de 200 ms no fim do bloco. Estado PROVISORIO_REFERENCIA: não há alinhamento palavra a palavra nem confirmação perceptiva fina. Texto UTF-8, numeração, literalidade, ordem, não sobreposição e limites de duração conferidos. Não se declara o SRT como versão final de uma gravação humana.

Reproduzir com o WAV preservado: `python videos/V03-003/renderizar.py --audio /workspace/artifacts/V03-003/V03-003_Audio_Referencia.wav --saida /workspace/artifacts/V03-003/V03-003_reproducao.mp4`. Esse script foi usado na renderização entregue; confere hashes das fontes e do áudio, resolve IDs no mapa e aplica as caixas sem alteração. Recusa sobrescrever saída existente. Não houve segunda renderização redundante; não se promete ressíntese idêntica pelo serviço. Os binários permanecem fora do Git e sujeitos à retenção do workspace.

## Verificações e evidências

- MP4 real: 1080×1920, H.264 yuv420p, 30 fps; AAC mono 48 kHz; decodificação completa sem erros.
- Doze projeções comparadas pixel a pixel com as evidências do mapa: idênticas antes da compressão; doze quadros extraídos do MP4 inspecionados visualmente, cobrindo todos os takes e as três regiões.
- Comparação numérica em 22 amostras antes/depois das fronteiras dos blocos, mais início/fim; imagens esperadas presentes. Isso não equivale a playback temporal humano.
- Doze trechos de áudio com sinal ativo, sem saturação PCM. Correlação da trilha AAC decodificada com PCM: 0.9999004497813906. Métricas de sinal não comprovam pronúncia ou clareza perceptiva.
- Cinco falas recompostas literalmente; 12 blocos SRT dentro da duração do vídeo; fontes com hashes verificados. Nenhuma afirmação de escuta foi feita.

[Painel 1: T01 e início de T02](evidencias/inspecao-01.jpg) · [Painel 2: T02/T03/início de T04](evidencias/inspecao-02.jpg) · [Painel 3: T04/T05](evidencias/inspecao-03.jpg) · [Métricas completas](evidencias/validacao.json)

## Pendência delimitada

**V03-003-REV-001:** não há ferramenta de escuta perceptiva/playback audiovisual disponível ao agente nesta sessão. A referência foi produzida e está disponível; revisão humana deve confirmar pronúncia de NOT, sequência de dígitos, operadores, ritmo e sincronismo fino das legendas. Por esse limite de inspeção obrigatória, a execução permanece PENDENTE_REVISAO, sem declarar GERADO_OK ou homologação. Não há dependência espacial impeditiva nem bloqueio de disponibilização do MP4. Não se solicita nova autorização para operações técnicas já abrangidas.

## Arquivos e integridade

- `/workspace/artifacts/V03-003/V03-003.mp4`: 3705469 bytes; SHA-256 `a1f4adaae9b34194d8580c9c4c2c67bc24b3212f67d727213198683a4be351be`.
- `/workspace/artifacts/V03-003/V03-003_Audio_Referencia.wav`: 8817452 bytes; SHA-256 `8a76046381f99b8138df7a1bdc3a37d0954ddb229ff3019652dd6272331e7c06`.

Versionados: plano JSON, SRT provisório, script de reprodução, manifesto, relatório e três painéis leves com métricas; checklist recebe somente um novo registro de revisão, preservando histórico e decisões anteriores. Originais, catálogo, dossiê, roteiro, mapa e protocolos permanecem inalterados. Nenhum MP4/WAV/MP3 ou ZIP será incluído no Git; nenhum upload externo de entrega, publicação audiovisual ou merge automático foi realizado. Síntese de voz utilizou apenas o texto autorizado; não foi canal de distribuição do vídeo.
