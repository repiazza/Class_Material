# Contrato técnico de entrega de vídeo

**Destino no repositório:** `curadoria/contrato_entrega_video.md`  
**Estado:** proposta sujeita à homologação humana.  
**Responsabilidade:** transformar um plano de montagem em artefatos audiovisuais verificáveis, reproduzíveis e rastreáveis.

## 1. Escopo e precedência

Este contrato especifica **como executar, validar e entregar** a montagem. Não decide o conteúdo pedagógico nem substitui:

- `AGENTS.md`: autorização, limites de autonomia, Git e aprovação humana.
- `curadoria/protocolo_montagem_audiovisual.md`: escolha de regiões, sequência, função visual e tempo.
- `curadoria/protocolo_mapeamento_espacial.md`: integridade e geometria das regiões.
- `curadoria/protocolo_retroalimentacao.md`: classificação e encaminhamento de defeitos.
- `curadoria/protocolo_revisao_audiovisual.md` (a definir): inspeção e homologação da renderização.

**Preparar montagem** produz um plano. **Gerar vídeo** executa o plano autorizado e produz artefatos técnicos. **Publicar** é uma operação distinta e não está autorizada por este contrato.

Não inferir que a existência de um roteiro, mapa, plano ou PR equivale à sua homologação. Registrar o estado efetivo de cada fonte e a autorização que fundamenta a execução.

## 2. Identidade, entradas e pré-voo

O vídeo usa ID `VNN-XXX`; o roteiro e o plano usam nomes `NN-XXX_Roteiro_Individual.docx` e `NN-XXX_Montagem.json`, respectivamente.

Antes de executar, confirmar:

1. Roteiro completo, plano de montagem e mapa espacial legíveis e compatíveis.
2. Arquivos originais acessíveis; regiões e IDs efetivamente existentes.
3. Commit, hash ou outra identificação verificável das entradas.
4. Situação das pendências incidentes sobre **os segmentos usados**.
5. Ferramentas locais disponíveis para renderização, inspeção e validação.
6. Modalidade de narração e existência ou não de áudio definitivo.

Não inventar versão de fonte, duração, resolução, quadro de GIF, estado de aprovação ou capacidade de ferramenta. Se o plano estiver apenas `PROPOSTO`, a geração experimental pode ocorrer **somente quando explicitamente autorizada**, mantendo a entrega identificada como experimental e não homologada.

## 3. Perfil audiovisual inicial

O perfil padrão é:

| Atributo | Contrato |
| --- | --- |
| Orientação | Vertical 9:16 |
| Quadro | 1080 × 1920 pixels |
| Contêiner | MP4 |
| Vídeo | H.264, `yuv420p`, progressivo |
| Áudio no MP4 | AAC, quando houver narração |
| Transições | Corte seco, salvo decisão expressa no plano |
| Proporção das fontes | Preservada; sem esticar ou deformar |
| Fundo | Neutro quando necessário ao enquadramento |
| Legendas | SRT externo; não queimar no vídeo por padrão |
| Taxa de quadros | Definida e registrada por execução, com padrão sugerido de 30 fps |
| Áudio de trabalho | WAV PCM quando necessário para sincronização ou auditoria |

Não fixar bitrate, taxa de amostragem, loudness ou tolerâncias de sincronismo sem validação experimental e homologação do perfil. Registrar os valores realmente utilizados. Não adicionar efeitos, zoom, movimentos ou trilha musical automaticamente.

A escolha de H.264/AAC é um **perfil técnico proposto**, não um requisito herdado dos protocolos anteriores.

## 4. Modos de produção e narração

### A. Montagem com áudio definitivo

Usar a gravação autorizada. Medir sua duração real, alinhar cenas e produzir SRT sincronizado com o áudio renderizado.

### B. Protótipo com voz de referência

Somente quando houver ferramenta disponível e autorização para voz sintética. Identificar claramente o áudio e o vídeo como **referência**, não como gravação definitiva. Não substituir silenciosamente uma narração humana esperada.

### C. Prévia sem narração

Permitida para verificar enquadramento, ordem e ritmo visual. Não produzir SRT **final** nem declarar sincronismo validado. Tempos e eventuais legendas permanecem provisórios.

A ausência de um serviço de voz não deve bloquear uma prévia visual autorizada; deve impedir apenas alegações de entrega com áudio definitivo.

## 5. Contrato de sincronismo e SRT

O SRT final deve refletir **as palavras efetivamente audíveis no áudio do MP4**.

- Usar sequência numérica crescente, timestamps `HH:MM:SS,mmm --> HH:MM:SS,mmm` e texto UTF-8.
- Exigir início menor que fim, ordem cronológica e ausência de sobreposição não intencional.
- Preservar palavras técnicas, operadores, valores e sinais de modo fiel à fala.
- Segmentar em unidades de leitura coerentes, evitando quebrar expressões ou relações semânticas importantes.
- Confirmar o alinhamento por escuta e/ou inspeção temporal do áudio, sem presumir precisão a partir do roteiro escrito.
- Registrar o método de alinhamento utilizado e suas limitações.
- Se o áudio mudar, regenerar ou revisar os intervalos afetados e revalidar.
- Se não houver áudio definitivo, rotular o SRT como `PROVISORIO` e não entregá-lo como versão final.

O SRT é um artefato independente. Não embutir legendas na imagem sem autorização específica.

## 6. Renderização visual

Para cada segmento:

1. Resolver o arquivo original e a região pelo ID exato do mapa.
2. Verificar coordenadas e dimensões no sistema real do arquivo; não adivinhar transformações.
3. Gerar o quadro vertical preservando integralmente a região e sua proporção, com preenchimento neutro quando necessário.
4. Respeitar o modo de GIF previsto no plano: quadro estático, sequência de estados ou animação fiel ao original.
5. Aplicar início, duração e transições conforme o plano sincronizado.
6. Manter consistência de resolução, formato de pixels e taxa de quadros.
7. Produzir o MP4 e registrar parâmetros e ferramentas efetivamente empregados.

**A montagem não redefine a geometria do mapa.** Se a região não funcionar, escolher outra região válida ou abrir ocorrência espacial; não criar um recorte agressivo invisível ao acervo.

Não declarar fidelidade temporal do GIF se apenas alguns quadros foram usados. Identificar explicitamente o modo editorial de apresentação.

## 7. Estrutura de entrega

Os arquivos de projeto permanecem versionados no repositório:

```text
editorial/montagens/NN-XXX_Montagem.json
videos/VNN-XXX/
  VNN-XXX.srt
  VNN-XXX_Manifesto.json
  VNN-XXX_Relatorio.md
  renderizar.py                  # quando aplicável
```

Os binários devem ser gerados e preservados fora do checkout:

```text
/workspace/artifacts/<ID_VIDEO>/
  <ID_VIDEO>.mp4
  <ID_VIDEO>_Audio_Referencia.wav  # somente quando aplicável
```

É proibido incluir MP4 ou WAV em commits, Git LFS, GitHub Releases ou anexos hospedados no repositório. Não criar ZIPs para distribuição audiovisual nem realizar uploads externos para entrega. Planos, scripts, legendas, manifestos, relatórios e evidências leves continuam versionados normalmente.

### Procedimento padrão de disponibilização

1. Gerar e preservar o MP4 real em `/workspace/artifacts/<ID_VIDEO>/<ID_VIDEO>.mp4`.
2. Executar as validações técnicas e inspeções previstas neste contrato, registrando resultados e limitações.
3. Conferir a existência e o tamanho não nulo do MP4, calcular seu SHA-256 e registrar o caminho real no manifesto e no relatório.
4. Apresentar obrigatoriamente na resposta final um link Markdown direto para esse arquivo no workspace, permitindo sua abertura pelo visualizador da interface. Exemplo de sintaxe para V01-003: `[Abrir MP4 V01-003](/workspace/artifacts/V01-003/V01-003.mp4)`. Usar somente o ID e o caminho do arquivo efetivamente produzido, sem inventar URLs.
5. Orientar o responsável editorial a abrir o vídeo no visualizador e utilizar **Salvar vídeo como...** no navegador para obter o arquivo.

O acesso pelo visualizador e o download com **Salvar vídeo como...** foram validados manualmente pelo responsável editorial no piloto V01-003. Esse é o procedimento padrão; não depende de um conector de upload ou de exportação. Não exigir confirmação de download para concluir a produção técnica quando a disponibilização no workspace estiver comprovada e os demais critérios técnicos da modalidade estiverem atendidos. Não afirmar que o usuário abriu ou baixou o arquivo sem evidência.

O link e o arquivo disponível não substituem as inspeções técnicas exigidas nem a aprovação editorial humana. Se o arquivo ou o acesso pelo visualizador estiver indisponível na execução, registrar a limitação e preservar os binários enquanto o ambiente permitir, sem refazer renderização ou síntese desnecessariamente. Não prometer persistência após o encerramento do ambiente nem publicar em outro serviço como alternativa automática.

Se um artefato obrigatório não puder ser gerado, registrar a ausência e a causa. Não criar arquivos vazios apenas para completar a estrutura.

## 8. Manifesto de produção

`VNN-XXX_Manifesto.json` deve conter, no mínimo:

- `schema_version`, `video_id`, `tipo_entrega` (`REFERENCIA`, `PREVIA_SEM_AUDIO` ou `FINAL_TECNICO`).
- `estado` (`GERADO_OK` ou `PENDENTE_REVISAO`) e justificativa quando houver impedimento.
- Data/hora UTC da execução, identificação da ferramenta e versões efetivamente verificadas.
- Fontes: caminho, commit/hash de roteiro, plano, mapa e originais usados.
- Perfil real de saída: dimensões, fps, codecs, parâmetros de áudio, duração e modalidade de narração.
- Lista dos segmentos executados, IDs de regiões e intervalos temporais efetivos.
- Artefatos produzidos: caminhos, tamanhos e SHA-256 quando disponíveis.
- Resultado das validações, limitações, ocorrências e decisões humanas pertinentes.

O esquema JSON deverá ser estabilizado e testado em piloto antes de ser declarado definitivo. Não inventar hashes ou afirmar integridade sem calcular.

## 9. Validação automática e inspeção

### Verificações de arquivo

- Arquivos produzidos existem, são não vazios e podem ser abertos pelas ferramentas disponíveis.
- MP4 apresenta dimensões, codecs, fps e duração coerentes com o perfil registrado.
- Áudio esperado está presente; não há trilha silenciosa ou ausente apresentada como narração válida.
- SRT possui sintaxe correta, timestamps válidos e intervalos dentro da duração do vídeo.
- Plano, manifesto e referências cruzadas são consistentes.
- Hashes dos artefatos e fontes são calculados, não presumidos.

### Verificações visuais e auditivas

- Inspecionar quadros representativos de **todos os segmentos**, incluindo pontos de corte e estados relevantes de GIFs.
- Conferir títulos, fórmulas, bordas, ausência de distorção e correspondência visual com a fala.
- Reproduzir/inspecionar o vídeo e o áudio resultantes para detectar cortes, congelamentos indevidos, transições inesperadas e dessincronização.
- Conferir o SRT contra o áudio real, sobretudo termos técnicos e passagens com pausas.
- Documentar o que foi efetivamente reproduzido e inspecionado. Testes automatizados não substituem revisão audiovisual humana.

Se o ambiente não permitir assistir ou ouvir o resultado, registrar a limitação; não declarar inspeção integral.

## 10. Falhas, continuidade e retroalimentação

Aplicar `curadoria/protocolo_retroalimentacao.md` quando a causa estiver no catálogo, original ou geometria. Erros de exportação, codec, legenda ou sincronismo pertencem à produção técnica.

- Corrigir autonomamente falhas técnicas introduzidas pela própria execução, dentro do escopo autorizado.
- Preservar segmentos e artefatos válidos; refazer apenas o necessário.
- Não corrigir silenciosamente um erro pedagógico do original nem reescrever roteiro.
- Identificar o segmento bloqueado, a causa, a dependência e a ação necessária.
- Diferenciar falha impeditiva de ressalva aceita ou pendência que não participa do vídeo.

**`GERADO_OK` significa entrega técnica concluída e validada dentro da modalidade declarada; não significa homologação editorial, merge, publicação ou liberação pedagógica automática.**

**`PENDENTE_REVISAO` significa impedimento ou decisão humana necessária, com evidências e trabalho válido preservado.**

Não utilizar `GERADO_OK` para um vídeo que exibe erro pedagógico impeditivo conhecido no conteúdo efetivamente utilizado.

## 11. Relatório e evidências

`VNN-XXX_Relatorio.md` deve apresentar objetivamente:

1. Escopo, modalidade e fontes efetivamente utilizadas.
2. Plano executado e eventuais diferenças justificadas.
3. Artefatos gerados, local de acesso e respectivos hashes.
4. Testes realizados, ferramentas usadas e resultados.
5. Amostras de inspeção visual e auditiva, com indicação dos segmentos.
6. Pendências impeditivas, ressalvas aceitas e dependências futuras.
7. Situação Git e necessidade de homologação humana.

Não gerar relatórios extensos que apenas repitam o manifesto. O relatório explica decisões e evidências; o manifesto fornece dados estruturados.

## 12. Autonomia, Git e aprovação

Dentro de uma execução explicitamente autorizada, o Codex pode criar o plano técnico complementar, renderizar, validar, corrigir defeitos técnicos próprios, calcular hashes e preparar commits/PRs **dos arquivos permitidos**.

Não realizar merge, publicar em plataformas externas ou divulgar o vídeo automaticamente.

Preservar o escopo das fontes e as alterações preexistentes. Não fazer rebase ou force-push por conveniência. Para binários audiovisuais, aplicar exclusivamente o procedimento de workspace da seção 7; o link local de entrega não implica armazenamento persistente.

A aprovação de uma PR de artefatos técnicos não equivale à homologação pedagógica do vídeo.

## 13. Critérios de aceite do contrato

Uma entrega `FINAL_TECNICO` requer MP4 reproduzível, áudio definitivo esperado, SRT sincronizado, manifesto íntegro, relatório e inspeções documentadas, sem impedimentos conhecidos nos segmentos usados.

Uma entrega `REFERENCIA` pode conter narração sintética e SRT sincronizado à referência, mas **não** deve ser confundida com a versão final de voz humana.

Uma entrega `PREVIA_SEM_AUDIO` pode validar apenas a montagem visual e **não** satisfaz os requisitos de áudio/SRT final.

Em todos os casos, registrar com precisão a modalidade, o que foi produzido, o que foi verificado e o que depende de decisão humana.

**Síntese:** o plano estabelece as escolhas; o renderizador as executa; o manifesto comprova proveniência; o SRT acompanha o áudio real; o relatório registra evidências; a revisão humana decide a homologação.
