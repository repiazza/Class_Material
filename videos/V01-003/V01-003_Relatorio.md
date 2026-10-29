# Piloto V01-003 — pré-voo e preparação preservada

**Estado: PENDENTE_REVISAO. Nenhum vídeo foi renderizado.** Modalidade solicitada: REFERENCIA; modalidade produzida: nenhuma. Esta entrega não é PREVIA_SEM_AUDIO nem GERADO_OK.

## Resultado concreto

O roteiro individual foi lido integralmente, incluindo suas duas tabelas e cinco takes. Preparou-se `editorial/montagens/01-003_Montagem.json`, com cinco falas literais, ordem original, referências visuais e janelas estimadas totalizando 70 segundos. A concatenação das falas coincide exatamente com o texto corrido de ensaio. O dossiê 01 foi consultado somente no candidato de origem V01-003 para rastreabilidade; não serviu para regenerar a narrativa.

Não foram inventados IDs, coordenadas, duração medida, voz ou sincronismo. Os campos `regiao_id` são nulos e `renderizavel` é falso. O roteiro mantém seu estado documental PROPOSTO; a solicitação humana autoriza este piloto experimental, sem homologação editorial implícita.

## Impedimento demonstrado — V01-003-REV-001

Falta o mapa espacial vigente do capítulo 01. Em main cdb7036, o único `NN_Mapa_Espacial.json` é o do capítulo 02. A consulta da árvore remota após fetch confirmou o mesmo resultado; a pesquisa no histórico local para mapa do capítulo 01 não retornou registro. A busca por arquivos de mapas em /workspace e /tmp também não o localizou; um diretório interno do daemon em /tmp não permitiu leitura, limitação sem efeito sobre a constatação da árvore Git. Não se presume ausência em sistemas externos não acessados.

Camada: dependência de entrada da produção (AV-T, bloqueante no pré-voo), não defeito D/P/V/G de fonte existente. Afeta S01–S05: sem mapa não há como selecionar/verificar IDs e coordenadas. Registro de deliberação: M01-AV-001 no checklist. Não se criou mapa substituto, nem se reutilizou o mapa 02 ou coordenadas temporárias antigas.

Os §§2 e 6 do contrato_entrega_video.md e o §2 do protocolo_montagem_audiovisual.md exigem mapa compatível e IDs reais antes da renderização. A prévia sem áudio permitida pelo pedido resolve ausência de voz, mas não esta dependência espacial. Inventar um recorte integral ou novo ID não satisfaria esse contrato.

## Fontes e ferramentas verificadas

Base: main cdb7036. AGENTS.md e os protocolos vigentes de montagem, entrega, revisão audiovisual, retroalimentação e mapeamento espacial; checklist consultado. As fontes existentes têm hashes no manifesto/plano. Os quatro PNGs indicados pelo roteiro existem e abrem tecnicamente. Não se realizou nova auditoria pedagógica ou inspeção visual das imagens: a compatibilidade espacial permanece não demonstrada.

FFmpeg e ffprobe 7.1.5-0+deb13u1 disponíveis; encoders libx264 e AAC listados. Python, python-docx e Pillow disponíveis para leitura e pré-voo. Não se executou teste de encode ou renderização, pois a entrada obrigatória está ausente.

Não foram localizados comandos espeak, espeak-ng, piper, say ou festival, nem módulos edge_tts, gtts, pyttsx3, piper, TTS, soundfile ou moviepy. Isso documenta a busca local, não prova impossibilidade de instalar ou obter um serviço. Não se adicionaram dependências, pois não resolveriam o bloqueio espacial. A descoberta das ferramentas habilitadas não retornou mecanismo de síntese de voz ou upload de arquivos.

## Artefatos e acesso

Produzidos: plano JSON incompleto de preparação, manifesto de pré-voo e este relatório; registro no checklist. Nenhum MP4, WAV, SRT, captura de vídeo ou binário fictício foi criado. Não há tamanho/hash de MP4 a informar.

Não houve tentativa de upload de vídeo, pois não existe MP4 para transmitir. Não se testaram destinos externos nem se publicou em plataforma audiovisual. Não se declara impedimento de entrega externa testado: a execução foi bloqueada antes dessa etapa. A entrega do vídeo acessível permanece não realizada.

## Validação e retomada

Verificados cinco takes, falas literais, ordem, quatro referências físicas, hashes e estimativas contíguas sem sobreposição, total de 70 segundos. Verificados JSONs e integridade/reabertura do roteiro. Não executados: inspeção de recortes, áudio, sincronismo SRT, MP4, transições e reprodução temporal; zero segmentos renderizados/revisados audiovisualmente.

Retomada delimitada: disponibilizar a revisão identificável do mapa 01; validar regiões e hashes contra os quatro PNGs; completar os cinco vínculos, resolver a ferramenta de voz ou usar a prévia sem áudio autorizada, produzir e medir os artefatos, revisar segmentos/transições e disponibilizar o MP4 por mecanismo efetivamente acessível. Não reescrever roteiro, criar protocolos ou repetir auditorias gerais.

O plano, manifesto e relatório são propostos em PR de preparação pendente, não de vídeo concluído. Hashes e link de publicação serão informados na conversa e na PR; não se presume publicação ou integração pelo conteúdo deste relatório. Nenhum merge é autorizado.
