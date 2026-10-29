# Protocolo de revisão audiovisual

**Destino no repositório:** `curadoria/protocolo_revisao_audiovisual.md`  
**Estado:** proposta de protocolo operacional, sujeita à homologação humana.  
**Responsabilidade:** inspecionar uma execução audiovisual, classificar ocorrências, orientar correções dirigidas e apresentar evidências para decisão humana.

## 1. Objetivo e limites

Este protocolo responde **como verificar o vídeo produzido, como corrigir defeitos e quando submetê-lo à homologação humana**.

Ele complementa, sem substituir:

- `AGENTS.md`: governança, autorização, commits, PRs e aprovação humana.
- `curadoria/protocolo_montagem_audiovisual.md`: decisões editoriais, seleção de regiões e plano temporal.
- `curadoria/contrato_entrega_video.md`: perfil técnico, MP4, áudio, SRT, manifesto e entrega.
- `curadoria/protocolo_mapeamento_espacial.md`: geometria e integridade das regiões.
- `curadoria/protocolo_retroalimentacao.md`: divergências de catálogo, original, ressalvas visuais e geometria.

**Revisar não significa reescrever o roteiro, refazer a curadoria ou reconstruir o capítulo.** O objeto principal da revisão é a execução audiovisual concreta, comparada às fontes e ao plano.

## 2. Unidade de revisão e rastreabilidade

A unidade mínima é o **segmento identificado no plano de montagem**, com seus intervalos efetivos de áudio e vídeo.

Para cada ocorrência, registrar:

- ID do vídeo e ID do segmento.
- Instante ou intervalo (`HH:MM:SS.mmm`) onde o problema aparece.
- Arquivo de saída e fonte pertinente.
- Evidência verificável: quadro, trecho, medição, log ou comparação.
- Classificação, gravidade, responsável pela camada e encaminhamento.
- Estado da ocorrência e resultado de eventual reinspeção.

Usar identificadores estáveis, por exemplo `V02-003-REV-001`. Não reutilizar IDs nem apagar registros anteriores; correções devem atualizar o estado e preservar o histórico.

## 3. Pré-condições e modalidades

Antes da revisão, confirmar:

1. Qual modalidade foi produzida: `PREVIA_SEM_AUDIO`, `REFERENCIA` ou `FINAL_TECNICO`.
2. Qual plano, roteiro, mapa, originais e revisões foram efetivamente usados.
3. Se MP4, SRT, áudio, manifesto e relatório esperados existem e podem ser abertos.
4. Quais pendências conhecidas incidem sobre os segmentos realmente utilizados.
5. Quais verificações já foram executadas e quais dependem de inspeção humana.

Não exigir SRT final nem áudio definitivo de uma prévia sem áudio. Não homologar como voz humana definitiva um protótipo com narração sintética.

Se não houver acesso real aos binários, a revisão pode ser **documental e parcial**, mas não pode declarar inspeção audiovisual concluída.

## 4. Duas camadas de revisão

### 4.1 Validação técnica automatizável

Conferir:

- Integridade e abertura do MP4.
- Resolução, proporção, orientação, codec, formato de pixels, fps e duração real.
- Presença e propriedades da trilha de áudio quando exigida.
- Ausência de falhas evidentes de decodificação, interrupções e arquivos vazios.
- Conformidade do SRT: codificação, numeração, intervalos válidos, ordem e duração.
- Correspondência entre plano, segmentos, manifesto, arquivos e hashes calculados.
- Registro de ferramentas, versões e parâmetros efetivamente empregados.

Uma checagem automatizada aprovada **não prova**, isoladamente, qualidade narrativa, legibilidade ou sincronismo perceptivo.

### 4.2 Inspeção audiovisual

Examinar a execução concreta quanto a:

- Correspondência entre fala e visual mostrado.
- Preservação de títulos, fórmulas, diagramas, bordas e relações didáticas.
- Legibilidade no quadro vertical e duração suficiente para compreensão.
- Continuidade entre segmentos, ausência de cortes indevidos ou congelamentos inesperados.
- Fidelidade dos estados de GIFs à intenção editorial.
- Clareza, integridade, ritmo e volume perceptivo da narração.
- Alinhamento temporal e fidelidade textual das legendas ao áudio.
- Coerência pedagógica da sequência e preservação das ressalvas do roteiro.

Inspecionar **todos os segmentos** e as transições entre eles, com atenção especial ao início e fim de cada fala e aos estados temporais relevantes. Capturas de quadros representativos ajudam a documentar, mas **não substituem** reprodução temporal quando o defeito depende de movimento ou som.

## 5. Critérios editoriais

A revisão não deve confundir preferência estética com defeito objetivo.

| Dimensão | Aceitável | Ocorrência que exige análise |
| --- | --- | --- |
| Enquadramento | Região completa com margens ou pequenos fragmentos adjacentes previstos | Informação essencial cortada ou deformada |
| Visão integral | Slide completo reduzido quando cumpre função de contexto | Detalhe ilegível que deveria sustentar a explicação |
| Ritmo | Pausa ou permanência prolongada com função didática | Corte antes de concluir uma explicação visual |
| Narração | Cadência natural, incluindo pausas | Palavra truncada, frase ausente ou áudio dessincronizado |
| Legenda | Segmentação natural e fiel à fala | Termo técnico incorreto, sobreposição ou descompasso relevante |
| GIF | Quadro estático ou animação escolhidos explicitamente | Ordem falsa, alteração de valor sugerida ou estado importante omitido |
| Continuidade | Cortes secos previstos | Flash, tela inesperada ou transição não planejada |

Não introduzir efeitos, movimentos de câmera, zooms ou alterações de texto apenas por gosto estético.

## 6. Classificação das ocorrências

A revisão audiovisual usa as categorias operacionais abaixo **sem substituir** as classes D/P/V/G do protocolo de retroalimentação.

| Código | Camada responsável | Exemplo |
| --- | --- | --- |
| `AV-T` | Produção técnica | Codec, exportação, resolução, tela preta, quadro perdido |
| `AV-S` | Sincronismo/legendas | SRT adiantado, texto diferente do áudio, fala truncada |
| `AV-M` | Montagem editorial | Região correta no momento errado, duração insuficiente, sequência inadequada |
| `AV-F` | Fonte preexistente | Erro pedagógico do PNG, texto encoberto no GIF, descrição documental incorreta |

Para `AV-F`, abrir ou referenciar ocorrência conforme `curadoria/protocolo_retroalimentacao.md`, identificando sua classe D/P/V/G. Não duplicar a investigação já concluída.

**Uma ressalva visual aceita (`V`) não deve reaparecer como falha técnica apenas porque a montagem preservou margens.**

## 7. Gravidade e bloqueio

- **BLOQUEANTE:** erro pedagógico efetivamente exibido; conteúdo essencial ausente; MP4 inválido; narração exigida ausente; SRT final incompatível com áudio; distorção ou corte que comprometa a compreensão; impossibilidade de verificar requisito obrigatório.
- **CORRIGÍVEL:** falha localizada de montagem, exportação ou sincronismo cuja solução está dentro do escopo técnico autorizado e não altera o sentido editorial.
- **RESSALVA:** limitação conhecida, documentada e compatível com a modalidade de entrega, sem prejuízo demonstrado ao conteúdo utilizado.

A gravidade depende do **uso real no vídeo**, não apenas da existência do problema no acervo.

Uma ocorrência pode ser `AV-M` e bloqueante; outra `AV-T` e corrigível. Classificação de origem e gravidade são dimensões independentes.

## 8. Correção dirigida e preservação

Para cada defeito confirmado:

1. Identificar a camada responsável e a menor unidade afetada.
2. Verificar se há solução autorizada sem mudar roteiro, fonte ou mapa.
3. Corrigir apenas os segmentos ou artefatos dependentes.
4. Atualizar plano, manifesto, SRT e hashes **somente quando impactados**.
5. Renderizar novamente o trecho ou saída necessária.
6. Reinspecionar o trecho corrigido **e suas fronteiras com os segmentos vizinhos**.
7. Executar uma checagem final de integridade do MP4 completo, áudio e SRT, pois uma nova exportação pode introduzir defeitos fora do trecho alterado.

Correções técnicas próprias da execução podem ser realizadas autonomamente dentro do escopo autorizado.

Alterações pedagógicas no original, reescrita de falas, modificação de geometria do mapa e mudança substancial da narrativa exigem autorização conforme a governança vigente.

**Preservar trabalho válido não significa dispensar a checagem final do arquivo renderizado.** Significa não refazer análises e recortes independentes sem causa demonstrada.

## 9. Ciclo de revisão

O ciclo operacional é:

`RENDERIZADO → VALIDACAO_TECNICA → INSPECAO_AUDIOVISUAL → (CORRECAO_DIRIGIDA → REINSPECAO) → PRONTO_PARA_HOMOLOGACAO`

Se houver impedimento fora do escopo autorizado:

`INSPECAO_AUDIOVISUAL → PENDENTE_REVISAO`

Estados de revisão sugeridos:

- `NAO_INICIADA`: artefato ainda não inspecionado.
- `EM_REVISAO`: validações em andamento.
- `PENDENTE_CORRECAO`: defeito demonstrado e solução técnica autorizada.
- `PENDENTE_REVISAO`: decisão humana ou dependência externa necessária.
- `PRONTO_PARA_HOMOLOGACAO`: verificações exigíveis concluídas e sem bloqueios conhecidos.
- `HOMOLOGADO`: **somente após decisão humana explícita**.

Esses estados pertencem à revisão. Não substituir automaticamente o campo `estado` do manifesto (`GERADO_OK` ou `PENDENTE_REVISAO`) sem respeitar o contrato de entrega.

## 10. Evidências mínimas

O relatório de revisão deve conter:

- Identificação do vídeo, modalidade, plano, revisão das fontes e artefatos avaliados.
- Ferramentas e métodos efetivamente usados.
- Resultado das validações técnicas.
- Registro da inspeção por segmento e transições.
- Ocorrências com IDs, gravidade, evidência, correção e reinspeção.
- Limitações de inspeção (por exemplo, áudio não reproduzido ou ausência de fonte).
- Conclusão: pronto para homologação ou pendente, com justificativa.

Preferir evidências **dirigidas**: capturas antes/depois, timestamps, hashes e trechos representativos. Não gerar centenas de imagens redundantes quando poucas comprovam a correção.

Nenhum relatório deve afirmar que o vídeo foi ouvido ou assistido integralmente se apenas foram examinados metadados ou quadros estáticos.

## 11. Homologação humana e Git

O Codex pode, quando autorizado:

- Executar testes e inspeções possíveis no ambiente.
- Registrar ocorrências e classificá-las.
- Corrigir defeitos técnicos próprios.
- Regerar derivados afetados, revalidar e preparar relatório.
- Fazer commit, push e abrir PR dos artefatos permitidos pelo `AGENTS.md`.

O Codex **não pode**:

- Declarar homologação humana por conta própria.
- Integrar PRs automaticamente.
- Publicar vídeo ou materiais em plataformas externas sem autorização específica.
- Reescrever roteiro ou corrigir originais fora do escopo autorizado.
- Reabrir indefinidamente verificações já resolvidas sem nova evidência.

**Aprovação de PR e homologação audiovisual são decisões distintas.** Uma PR pode integrar artefatos técnicos ainda não homologados editorialmente, desde que o estado esteja explícito.

## 12. Resultado e comunicação

Ao concluir a revisão, informar de forma sucinta:

1. O que foi produzido e efetivamente inspecionado.
2. Quantos segmentos foram revisados e quais verificações ocorreram.
3. Quais problemas foram corrigidos e quais permanecem.
4. Quais arquivos foram modificados, seus destinos e a situação Git.
5. Se a execução está `PRONTO_PARA_HOMOLOGACAO` ou `PENDENTE_REVISAO`.

`GERADO_OK` no manifesto significa **entrega técnica validada na modalidade declarada**; não é sinônimo de `HOMOLOGADO`. Se houver impedimento conhecido nos segmentos utilizados, o manifesto deve indicar `PENDENTE_REVISAO`.

Não solicitar nova rodada de aprovação para cada operação técnica já autorizada. Solicitar decisão humana apenas quando a escolha altera conteúdo, fontes, geometria, governança ou publicação.

## 13. Critério de sucesso

A revisão está concluída quando o vídeo foi confrontado com seu plano e suas fontes, os testes exigíveis foram executados, a inspeção audiovisual foi documentada com honestidade, as correções autorizadas foram revalidadas e as pendências remanescentes foram delimitadas.

**Síntese:** validar o resultado real; corrigir a menor unidade responsável; preservar os artefatos válidos; comprovar a reinspeção; reservar a homologação ao responsável humano.
