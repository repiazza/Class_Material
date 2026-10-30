# Protocolo de consolidação editorial

> **Identificador:** `curadoria/consolidacao_editorial`\
> **Versão:** `0.1.0` — contrato inicial de decisões e referências\
> **Estado:** PROPOSTO — sujeito à revisão e homologação humana\
> **Escopo:** comparação de candidatos entre dossiês e registro de identidades, alternativas e deliberações\
> **Registro previsto:** `editorial/consolidacoes/NN_Consolidacao_Editorial.md`

## 1. Finalidade e fronteiras

**Consolidar não é reescrever. É reconhecer identidades narrativas, organizar alternativas e registrar decisões sem modificar as propostas de origem.**

A consolidação é uma camada de governança entre a descoberta de oportunidades e a seleção para roteiros individuais. Compara candidatos de diferentes dossiês ou versões, reconhece equivalências e oportunidades independentes, registra sobreposições e ambiguidades e encaminha a seleção de uma fonte editorial específica. Mantém rastreabilidade das fontes e das decisões humanas.

O catálogo de consolidação **não é uma nova fonte de conteúdo narrativo**. Não cria falas, hooks, storyboards, exemplos técnicos ou combinações inéditas; não reproduz integralmente narrativas ou storyboards existentes. Pergunta e promessa são identificações concisas, atribuídas às fontes, sem ampliar seu sentido. As abordagens disponíveis são referenciadas nos dossiês.

A descoberta e o desenvolvimento das propostas seguem o [protocolo de roteirização](protocolo_roteirizacao.md). O desenvolvimento de um candidato selecionado segue o [protocolo de roteiro individual](protocolo_roteiro_individual.md). A consolidação não modifica as fontes, o caminho independente do mapeamento espacial ou os contratos de montagem e produção.

## 2. Identidade, candidato e abordagem

| Termo | Significado operacional |
|---|---|
| Candidato | Proposta narrativa documentada em um dossiê, com ID e conteúdo próprios. |
| Identidade editorial | Reconhecimento de uma oportunidade de vídeo, que pode ter uma ou mais abordagens documentadas. Não é um novo candidato nem uma aprovação. |
| Alternativa | Abordagem diferente para a mesma pergunta e promessa pedagógica, sem justificar automaticamente outro vídeo. |
| Oportunidade independente | Proposta cuja pergunta, demonstração ou recompensa pedagógica justifica uma identidade própria, com fundamento na trajetória narrativa completa. |
| Sobreposição parcial | Interseção relevante entre propostas sem equivalência integral demonstrada. |
| Fonte editorial selecionada | Referência exata ao candidato e ao dossiê autorizados pelo responsável humano para um roteiro individual. |

**Identidade editorial, aprovação e produção são dimensões distintas.** Reconhecer uma identidade não aprova seus candidatos; um roteiro ou vídeo experimental existente não comprova homologação editorial. O estado dos candidatos continua regido exclusivamente pelo protocolo de roteirização, sem migração automática pela consolidação.

## 3. Relações entre propostas

Para cada relação, comparar **pergunta central, promessa pedagógica, demonstração e conclusão narrativa**, localizando as evidências nas fichas de origem. Registrar diferenças e limites, não somente etiquetas comuns.

| Classificação proposta | Critério |
|---|---|
| `ALTERNATIVA` | As propostas são abordagens da mesma oportunidade; as diferenças de execução não justificam, por si, outro vídeo. |
| `INDEPENDENTE` | As oportunidades têm distinção narrativa substantiva, sustentada pela pergunta, demonstração ou recompensa e pela coerência do conjunto. |
| `SOBREPOSICAO_PARCIAL` | Há interseção relevante, mas a equivalência integral não está demonstrada; explicitar a parcela comum e a diferença. |
| `INCONCLUSIVA` | As fontes disponíveis não permitem classificar com confiança; indicar a evidência ou deliberação faltante. |

Repetição de assunto, conceito, palavra-chave ou material visual não demonstra equivalência. Mudança superficial de título ou hook não demonstra independência. Não usar pontuações artificiais, quotas ou limiares quantitativos obrigatórios.

As classificações são propostas do agente até decisão humana expressa. Uma relação `INCONCLUSIVA` pode ter sua inconclusão homologada: isso reconhece o limite documental, não resolve a identidade. Classificação da relação e estado de sua deliberação devem permanecer separados.

## 4. Registro de consolidação

Convenção: `editorial/consolidacoes/NN_Consolidacao_Editorial.md`. O caminho define um artefato futuro; este contrato não cria catálogos consolidados de capítulos nem autoriza sua geração por iniciativa do agente.

No cabeçalho do registro, indicar capítulo, versão, dossiês e versões consultadas e escopo autorizado. Organizar por identidade existente ou referência local provisória, sem instituir outro sistema global de IDs. Manter somente os campos necessários:

| Informação | Conteúdo mínimo |
|---|---|
| Identidade | ID existente pertinente ou referência provisória claramente marcada; não inventar um ID oficial para preencher o campo. |
| Pergunta e promessa | Identificação concisa e atribuída ao candidato-fonte; se houver divergência relevante, registrar separadamente em vez de sintetizar uma promessa nova. |
| Candidatos e dossiês | Caminho exato relativo à raiz, versão do dossiê, ID original e título/seção que permita localizar cada ficha. Usar links relativos válidos a partir do registro. Commit ou hash pode distinguir revisões quando necessário. |
| Relações e justificativas | Candidatos comparados, classificação proposta, evidências de pergunta/promessa/demonstração/conclusão e limites. Vínculos parcialmente sobrepostos podem referenciar outras entradas sem duplicar as fichas. |
| Abordagens disponíveis | Referências às propostas nas fontes, sem copiar suas narrativas ou criar uma combinação. |
| Fonte preferencial sugerida | Quando fundamentada, indicar um único candidato e dossiê com motivo da recomendação; sugestão não é seleção autorizada. Caso contrário, deixar pendente. |
| Deliberação humana | Decisões efetivamente manifestadas sobre relação e oportunidade, com justificativa e referência à manifestação; ausência de decisão permanece pendente. |
| Encaminhamento para roteiro | Somente se autorizado: candidato-fonte, caminho e versão do dossiê selecionado, ID oficial de destino quando aplicável e referência à autorização. Sem autorização, registrar apenas que não há encaminhamento autorizado. |
| Pendências e ressalvas | Apenas dúvidas, conflitos, limites e dependências efetivos. |

Evitar repetir o cadastro completo de candidatos ou criar campos paralelos para a mesma decisão. Uma relação já registrada pode ser referenciada em outra entrada. A consolidação deve permitir encontrar o conteúdo de origem sem substituí-lo.

## 5. IDs, fontes e preservação

Preservar IDs históricos `VNN-XXX` e experimentais existentes, como `EXP03-XXX`, com seus caminhos e versões. Não renumerar, reciclar, excluir ou promover IDs automaticamente. A referência de fonte é o conjunto **dossiê/versão + ID do candidato**: a presença do mesmo ID em revisões preservadas não é, por si, uma duplicação indevida.

Um experimental pode ser proposto como oportunidade independente e continuar com ID provisório. A atribuição oficial depende de decisão humana e das convenções vigentes. Não deduzir o ID definitivo retirando o prefixo experimental ou copiando sua sequência numérica. Se houver atribuição posterior, registrar a correspondência com a origem sem renomear a fonte preservada.

Reconhecer alternativas não exclui candidatos. A consolidação não altera dossiês, roteiros, materiais, mapas ou produtos existentes, mesmo quando houver equivalência homologada. Se surgir a necessidade de combinar conteúdo de candidatos, registrar a dependência de **revisão editorial autorizada de um dossiê**, com escopo próprio; não executar a combinação no registro ou no roteiro.

## 6. Deliberação e histórico

Há três decisões independentes:

1. **Homologação de relacionamento:** aprovação humana da classificação e do vínculo entre candidatos.
2. **Aprovação de oportunidade:** decisão humana sobre a pertinência da identidade editorial para o projeto.
3. **Autorização para roteirização:** escolha explícita do candidato e do dossiê que alimentarão o roteiro individual.

A homologação de equivalência não aprova um vídeo; a aprovação de uma oportunidade não autoriza gerar roteiro. O agente pode analisar, classificar, recomendar, elaborar e validar registros no escopo solicitado, mas não presume nenhuma dessas decisões. Presença de registro, fonte preferida ou artefato produzido não é autorização.

Usar controle simples para as **relações**: `PENDENTE`, `HOMOLOGADA` ou `REJEITADA`, registrando a manifestação e a justificativa. A classificação proposta permanece identificável mesmo se rejeitada. Para oportunidade e autorização, registrar a decisão expressa ou sua ausência, sem criar outro ciclo de estados para candidatos. Não converter esses registros automaticamente em `APROVADO`, `RESERVADO` ou `PRODUZIDO`.

Uma mesma manifestação humana pode conter as três decisões, desde que cada uma seja explícita e rastreável; não exigir ritos adicionais para decisões já fornecidas. A aprovação de uma PR não deve ser interpretada como homologação pedagógica de cada proposta nela contida sem manifestação nesse sentido.

Revisões posteriores preservam decisões anteriores, justificativas e referências em um histórico conciso no próprio registro. Registrar a revisão da classificação e a nova deliberação quando aplicáveis; não apagar silenciosamente o vínculo anterior nem tratar rejeição como pedido de alternativa. Decisões de consolidação ficam nesse registro; ocorrências nas fontes seguem os registros e autorizações do [protocolo de retroalimentação](protocolo_retroalimentacao.md), sem duplicar seu checklist.

## 7. Encaminhamento e fonte exclusiva do roteiro

**O catálogo de consolidação identifica e encaminha a fonte editorial, mas não fornece conteúdo narrativo ao roteirizador.**

A consulta do registro pode localizar a seleção humana e sua autorização. Depois disso, falas, exemplos, argumentos, mídias e storyboard devem provir exclusivamente de **um candidato-fonte no dossiê selecionado**, conforme o protocolo de roteiro individual. Nenhuma justificativa, comparação ou abordagem de outro candidato na consolidação pode complementar o conteúdo.

Sem caminho específico autorizado, permanece a entrada canônica `editorial/dossies/NN_Dossie_Editorial.docx`. Com escolha humana explícita de outro dossiê existente, usar o caminho e o candidato indicados, preservando a rastreabilidade da versão e as regras de identificação e saída. A recomendação do agente não substitui essa escolha.

Antes de encaminhar, verificar a presença do candidato na fonte exata e os possíveis conflitos de ID, caminho e arquivo de saída. Um ID experimental não é promovido pela seleção: se faltar a atribuição oficial necessária à convenção do roteiro, registrar o impedimento para decisão humana. Não sobrescrever, atribuir IDs ou inventar variantes de saída silenciosamente. Interromper somente a operação afetada, preservando os demais registros válidos.

## 8. Validação e publicação

Antes de entregar uma consolidação, verificar:

- Existência e legibilidade dos dossiês citados, com leitura do corpo e das tabelas pertinentes, e correspondência de cada candidato à versão e à seção indicadas.
- Ausência de IDs reciclados, fontes equivocadas, entradas duplicadas para a mesma identidade sem justificativa ou classificações contraditórias não registradas como pendências. A mesma fonte em comparações parciais pode ser referenciada sem criar novo candidato.
- Fundamentação da relação nas quatro dimensões narrativas, sem presumir equivalência por assunto ou independência por título.
- Distinção entre proposta do agente, homologação do vínculo, aprovação da oportunidade e autorização para roteiro.
- Preservação dos IDs, fontes, decisões e histórico; nenhuma exclusão ou promoção automática.
- Ausência de conteúdo narrativo novo ou de conteúdo de um candidato atribuído a outro; referências suficientes para localizar as abordagens.
- Encaminhamento somente quando autorizado, com um único candidato-fonte, dossiê exato e ausência de conflito de saída.
- Caminhos e links relativos válidos; diff restrito ao escopo autorizado e verificações Git conforme [AGENTS.md](../AGENTS.md).

A validação documental não equivale à homologação editorial. Divergências não resolvidas são pendências delimitadas, sem correção pedagógica automática ou ampliação de escopo. Commit, push e PR seguem a autorização da tarefa e o fluxo Git vigente; **não realizar merge automático**.

## 9. Critério de conclusão

O registro deve permitir reconhecer quais propostas estão relacionadas, onde suas abordagens estão documentadas, o que o agente recomenda, o que o responsável humano decidiu e qual fonte, se alguma, está autorizada para o próximo roteiro. As propostas originais continuam preservadas e acessíveis. Este contrato não produz a consolidação do capítulo 03.
