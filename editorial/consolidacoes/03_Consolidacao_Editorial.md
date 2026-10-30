# Capítulo 03 — Consolidação editorial

**Versão:** 1.0 — primeira aplicação experimental do contrato 0.1.0.\
**Estado:** propostas do agente; todas as relações `PENDENTE` de homologação humana.\
**Base:** `main`, commit `364b88dc9cd1ee62afc84eb1cff2f8eddc27a431`, com a PR #24 integrada.\
**Escopo autorizado:** analisar e registrar relações entre os dois dossiês; publicar exclusivamente este catálogo. Sem seleção definitiva, promoção de IDs ou autorização de roteiro/produção.

## 1. Fontes e método

| Referência local | Documento e versão consultados | Leitura efetiva |
|---|---|---|
| **O** | [Dossiê original](../dossies/03_Dossie_Editorial.docx), versão 1.0, protocolo de origem 0.2.4 | Corpo completo: 184 parágrafos e 10 tabelas, incluindo as oito narrativas e os respectivos storyboards. |
| **E** | [Dossiê experimental 030](../dossies/03_Dossie_Editorial_Experimental_030.docx), versão 1.0 — experimento paralelo 030, protocolo de origem 0.3.0 | Corpo completo: 159 parágrafos e 2 tabelas, incluindo as cinco narrativas e os respectivos storyboards. |
| Auxiliar | [Comparativo editorial 030](../dossies/03_Comparativo_Editorial_030.md) | Leitura integral para confrontar conclusões; não determina equivalência, aprovação ou preferência. |

Integridade das fontes primárias, SHA-256:

- **O:** `93c507abbee1d08f4e21015cdadd8ea61ac02e77b438af73dede4b84970e4033`.
- **E:** `b4d01eeefba7a771febcf77595c57920368ed090afc08ac18eee6afcf1dd67c3`.

Regras consultadas: [AGENTS.md](../../AGENTS.md), [protocolo de consolidação editorial](../../curadoria/protocolo_consolidacao_editorial.md) 0.1.0 e [protocolo de roteirização](../../curadoria/protocolo_roteirizacao.md) 0.3.0. O checklist foi consultado para os limites operacionais e riscos de mídia preexistentes, sem nova investigação ou retroalimentação corretiva.

A comparação própria partiu das fichas completas: pergunta, promessa, demonstração nos momentos do storyboard e conclusão da narrativa/propósito final. As classificações abaixo indicam relações editoriais, não correção dos originais ou viabilidade audiovisual já comprovada. A leitura do comparativo foi usada para testar se suas conclusões também se sustentam nessas quatro dimensões. Os pareceres anteriores não foram importados como decisões.

Para localizar uma proposta, usar **O/E + ID + título da ficha** na seção 3 de seu dossiê, “Fichas dos candidatos” em O e “Fichas de candidatos” em E. Os links levam aos DOCX completos; não se inventam âncoras internas ou páginas fixas para eles. As quatro dimensões são resumidas para identificação e análise, sem copiar falas ou storyboards.

## 2. Visão geral e cobertura

Foram analisados **13 candidatos: 8 de O e 5 de E**. A proposta de organização resulta em **10 identidades**: oito referências históricas e duas referências locais provisórias. Três experimentais são tratados como alternativas de identidades históricas; dois conservam oportunidade própria proposta. Isso não reduz ou renumera os candidatos de origem.

Há **13 relações relevantes registradas**: **3 `ALTERNATIVA`, 8 `INDEPENDENTE` e 2 `SOBREPOSICAO_PARCIAL`**. Dez relações confrontam O com E; três complementam a análise entre candidatos da mesma origem. Nenhuma relação foi classificada `INCONCLUSIVA`: as fontes permitem as classificações propostas, embora a homologação continue pendente. Pares não listados não receberam classificação implícita nem constituem evidência de exclusão.

| Identidade proposta | Candidatos pertencentes ao agrupamento | Leitura recomendada |
|---|---|---|
| [V03-001](#v03-001) | O: V03-001 | Domínio lógico versus cálculo por coluna. |
| [V03-002](#v03-002) | O: V03-002 | Combinação de entradas que distingue OR/XOR. |
| [V03-003](#v03-003) | O: V03-003; E: EXP03-003 | Alternativas centradas na largura da inversão. |
| [V03-004](#v03-004) | O: V03-004 | Deslocamentos e relação aritmética com limites. |
| [V03-005](#v03-005) | O: V03-005 | Consulta de bit, valor mascarado e zero/não zero. |
| [V03-006](#v03-006) | O: V03-006 | Construção de máscaras que preservam vizinhos. |
| [V03-007](#v03-007) | O: V03-007; E: EXP03-001 | Alternativas de alternância versus ativação. |
| [V03-008](#v03-008) | O: V03-008; E: EXP03-005 | Alternativas para alinhar e selecionar um campo. |
| [Provisória: entradas e encadeamento](#provisoria-entradas) | E: EXP03-002 | Pergunta própria sobre a entrada de cada transformação. |
| [Provisória: reversibilidade dos deslocamentos](#provisoria-reversibilidade) | E: EXP03-004 | Pergunta própria sobre recuperação da informação descartada. |

Cada candidato aparece uma única vez como membro de identidade nesta tabela. Reaparecer nas comparações transversais não cria outro candidato ou agrupamento. Os rótulos “provisória” e os localizadores internos deste Markdown não são IDs oficiais novos.

**Regra comum de deliberação, aplicável a todas as entradas:** homologação das relações `PENDENTE`; reconhecimento das identidades propostas ainda sem decisão humana nesta consolidação; fonte preferencial é apenas recomendação. **Não há novo encaminhamento autorizado para roteiro.** Os estados escritos nos dossiês permanecem intactos. Este catálogo não revoga decisões históricas nem presume sua extensão a alternativas experimentais.

## 3. Catálogo de identidades

<a id="v03-001"></a>
### V03-001 — Domínio da operação

**Fonte e abordagem disponível:** O, seção 3, **V03-001 — Um & muda a pergunta**.

**Pergunta e promessa da fonte:** por que AND lógico e AND bitwise podem dar resultados diferentes com os mesmos números? Distinguir avaliação de condições de cálculo por posição, sem confundir `&` com `&&`.

**Fundamento:** a narrativa de O contrapõe os resultados 8 e 1 para 10/12. O storyboard passa da dúvida inicial à distinção de símbolos, ao cálculo por coluna e à conclusão sobre o domínio da operação. A recompensa é escolher a pergunta correta — condição ou bits —, e não apenas reconhecer o número produzido. Nenhum experimental repete esse percurso completo. A comparação com a consulta de bit está explicitada em R09, sem agrupá-las por compartilharem AND ou o resultado 8.

**Classificação e recomendação:** preservar a identidade histórica; R09 propõe `INDEPENDENTE` em relação a V03-005. **Fonte preferencial sugerida:** O/V03-001, única abordagem documentada neste conjunto para esse objetivo. Não há seleção humana decorrente desta recomendação.

**Pendências efetivas:** homologação de R09 e reconhecimento da oportunidade. As condições de uso visual permanecem nas dependências de O; não foram revalidadas nem ampliadas.

<a id="v03-002"></a>
### V03-002 — O caso que separa OR e XOR

**Fonte e abordagem disponível:** O, seção 3, **V03-002 — OR ou XOR: o caso que separa os dois**.

**Pergunta e promessa da fonte:** qual combinação revela que OR e XOR não são intercambiáveis? Identificar a combinação 1/1 e explicar a diferença entre os resultados 14 e 6 para 10/12.

**Fundamento:** O parte das duas entradas iguais a 1, aplica a distinção a operandos binários e encerra localizando o peso 8 que permanece no OR e desaparece no XOR. A demonstração é uma comparação de operações, não de atualizações sucessivas. A relação R07 com EXP03-001 é `SOBREPOSICAO_PARCIAL`: há explicação compartilhada da divergência 1/1, mas o experimental organiza uma escolha de comando pela repetição. Essa interseção não demonstra equivalência integral nem exige apagar a pergunta histórica.

**Classificação e recomendação:** manter como identidade histórica distinta, com a sobreposição delimitada em R07. **Fonte preferencial sugerida:** O/V03-002 para o objetivo de identificar a combinação divergente; não importar o desenvolvimento temporal de E para completar esta ficha.

**Pendências efetivas:** homologação de R07. A parcela comum precisa ser considerada caso se planejem ambos os vídeos; não há lacuna documental que obrigue adiar a classificação proposta.

<a id="v03-003"></a>
### V03-003 — Largura da inversão

**Fontes e abordagens disponíveis:** O, seção 3, **V03-003 — NOT precisa de uma largura**; E, seção 3, **EXP03-003 — A mesma inversão pode dar cinco ou duzentos e quarenta e cinco?**.

| Dimensão | Comparação própria das fontes |
|---|---|
| Pergunta | O pede a condição para interpretar NOT de 10 e limitar a extrapolação para C; E pede a condição que explica duas respostas à inversão do mesmo valor. Ambas fazem a largura deixar de ser uma informação implícita. |
| Promessa | O separa inversão, largura e leitura do padrão; E concentra-se nos zeros adicionais e na leitura sem sinal. O escopo de C é mais explícito em O; não se declara igualdade integral de todas as promessas. |
| Demonstração | O desenvolve o modelo de oito bits e o confronta com o tipo efetivo em C; E contrasta modelos de quatro e oito posições. Os exemplos específicos estão em suas fontes; não se cria um terceiro exemplo aqui. |
| Conclusão | Ambas encerram exigindo fixar a largura e interpretar o resultado, sem apresentar 245 como valor universal de `~10`. A diferença de demonstração e público não exige, nas fichas atuais, outro vídeo para a mesma descoberta central. |

**Classificação e recomendação:** R02, `ALTERNATIVA`, agrupamento proposto sob a referência histórica V03-003. E oferece uma entrada mais restrita para quem ainda não domina sinal; O atende melhor o cuidado com a leitura de C. **Fonte preferencial sugerida:** O/V03-003 para continuidade da linha histórica já desenvolvida, sem alegar superioridade geral; E fica preservada como alternativa, não como substituição do piloto.

**Contexto e pendências:** existe roteiro e piloto técnico V03-003, conforme o histórico da tarefa; o [roteiro preservado](../roteiros/03-003_Roteiro_Individual.docx) está disponível. Sua existência não homologa automaticamente a narrativa nem E. Não houve nova inspeção do roteiro ou vídeo. Homologação de R02 permanece pendente. Uma futura escolha de E exigirá seleção explícita de candidato/dossiê e resolução do ID e de eventual revisão do arquivo de roteiro existente, sem sobrescrita automática. A restrição gráfica M03-P-001 citada em E é preservada, não investigada novamente.

<a id="v03-004"></a>
### V03-004 — Deslocamento e aritmética com limites

**Fonte e abordagem disponível:** O, seção 3, **V03-004 — Deslocar não é multiplicar sem limites**.

**Pergunta e promessa da fonte:** quando deslocar equivale a multiplicar/dividir por potências de dois e onde essa relação falha? Associar pesos e posições, respeitando largura, descarte e domínio sem sinal.

**Fundamento:** O percorre peso posicional, movimento, descarte pela borda e conclusão condicionada sobre a analogia aritmética. Não apresenta uma volta ao estado inicial como problema central. R05 confronta essa trajetória com EXP03-004 e propõe `INDEPENDENTE`; R13 diferencia este objetivo da extração de campo em EXP03-005. O uso de shifts nos três não basta para reuni-los.

**Classificação e recomendação:** preservar a identidade histórica. **Fonte preferencial sugerida:** O/V03-004 para a introdução da relação aritmética, sem acrescentar a ida/volta do experimental à sua narrativa.

**Pendências efetivas:** homologação de R05/R13 e reconhecimento da distinção. O compartilhamento da explicação de descarte com a oportunidade provisória deve ser conhecido, mas não implica combinação automática ou ordem obrigatória.

<a id="v03-005"></a>
### V03-005 — Consultar e interpretar um bit

**Fonte e abordagem disponível:** O, seção 3, **V03-005 — Consultar um bit não precisa mudar o valor**.

**Pergunta e promessa da fonte:** como descobrir se uma posição está ligada sem confundir consulta e alteração? Ler o resultado mascarado como zero/não zero, não necessariamente 1.

**Fundamento:** o exemplo de O consulta o bit 3 de 10, obtém 8 e separa o valor da máscara de sua interpretação lógica. O storyboard distingue operando e resultado e termina contrastando consultar e alterar. R09 diferencia esta pergunta do domínio de AND em V03-001. R08 registra interseção com EXP03-005 na seleção por AND, mas sem equiparar teste de uma posição à leitura numérica de um campo.

**Classificação e recomendação:** preservar a identidade histórica, com R09 `INDEPENDENTE` e R08 `SOBREPOSICAO_PARCIAL`. **Fonte preferencial sugerida:** O/V03-005, única abordagem do conjunto centrada no teste zero/não zero sem alteração por mero cálculo.

**Pendências efetivas:** homologação de R08/R09. O uso de `mascara_bitwise.png` é apenas o papel descrito em O, não validado nesta consolidação. O checklist registra M03-D-001 para essa referência visual; a ocorrência permanece contexto de risco, sem conferir novamente o PNG ou corrigir a ficha.

<a id="v03-006"></a>
### V03-006 — Preservar os bits vizinhos

**Fonte e abordagem disponível:** O, seção 3, **V03-006 — Ligar e desligar sem afetar os vizinhos**.

**Pergunta e promessa da fonte:** por que ativar usa OR e limpar usa AND com máscara invertida? Explicar os zeros/uns que preservam as demais posições.

**Fundamento:** O compara as construções de máscara e calcula ativação e limpeza partindo separadamente do original. O encerramento ressalta a independência dos cálculos, mas a demonstração principal explica por que cada vizinho é preservado. E/EXP03-002 muda o centro para a entrada de cada operação, como detalha R04; V03-007 trata de alternância e repetição, como detalha R10.

**Classificação e recomendação:** preservar a identidade histórica; R04/R10 propõem `INDEPENDENTE`. **Fonte preferencial sugerida:** O/V03-006 para aprender a construir máscaras de ativação/limpeza, não E/EXP03-002 como substituta desse ensino.

**Pendências efetivas:** homologação dos vínculos. M03-P-003, já citada em E para a mídia compartilhada, limita eventual reutilização visual; a classificação narrativa não homologa o painel nem depende de corrigi-lo nesta etapa.

<a id="v03-007"></a>
### V03-007 — Alternar ou garantir ligado

**Fontes e abordagens disponíveis:** O, seção 3, **V03-007 — XOR alterna; OR fixa**; E, seção 3, **EXP03-001 — Dois comandos iguais na primeira vez — e na segunda?**.

| Dimensão | Comparação própria das fontes |
|---|---|
| Pergunta | O pergunta como a mesma operação pode desfazer a si própria; E pergunta por que a primeira saída igual não torna OR e XOR intercambiáveis. A segunda aplicação decide a diferença nas duas propostas. |
| Promessa | Ambas permitem escolher alternar ou garantir ligado, compreendendo o efeito de repetir a operação. |
| Demonstração | O aplica XOR duas vezes e contrapõe OR; E acompanha dois caminhos inicialmente coincidentes, que divergem na repetição. O storyboard de E muda a encenação, não cria uma regra ou recompensa final distinta. |
| Conclusão | O termina em alternar versus ativar; E termina em escolher a intenção, além de olhar o resultado inicial. A autonomia de um segundo vídeo não é demonstrada só pela nova previsão inicial. |

**Classificação e recomendação:** R01, `ALTERNATIVA`, agrupamento proposto sob V03-007. **Fonte preferencial sugerida:** E/EXP03-001 para uma avaliação futura focada em previsão e comparação de trajetórias, porque o primeiro resultado não entrega a resposta. O/V03-007 permanece disponível quando a explicação direta da reversibilidade do XOR for preferível. Esta sugestão não seleciona uma fonte autorizada nem transfere o ID histórico ao experimental.

**Pendências efetivas:** homologação de R01; avaliar R07 antes de oferecer também V03-002, cujo núcleo 1/1 aparece como apoio em E. R06/R10/R11/R12 delimitam perguntas próximas que não foram agrupadas. M03-P-002 e a ausência de confirmação da repetição no GIF, já descritas em E, permanecem restrições da abordagem sugerida. Não há combinação de conteúdos das duas fichas.

<a id="v03-008"></a>
### V03-008 — Alinhar e selecionar um campo

**Fontes e abordagens disponíveis:** O, seção 3, **V03-008 — Extrair um campo: deslocar e depois selecionar**; E, seção 3, **EXP03-005 — Já desloquei o campo. Por que a resposta ainda está errada?**.

| Dimensão | Comparação própria das fontes |
|---|---|
| Pergunta | O já pergunta se mover o campo à ponta basta; E manifesta a mesma insuficiência como erro de resultado intermediário. |
| Promessa | Ambas distinguem reposicionar o campo de eliminar vizinhos, justificando deslocamento mais máscara. O também orienta a leitura de parâmetros e agrupamento, sem inventar a assinatura. |
| Demonstração | O acompanha as etapas de getbits sem fixar um exemplo não descrito; E desenvolve o campo 2..1 de 12, mostrando o resultado intermediário e a seleção final. É uma concretização já escrita em E, não um novo exemplo deste catálogo. |
| Conclusão | Alinhar não seleciona tudo o que interessa: é preciso mascarar. Ambas preservam a distinção entre sequência didática e ordem de avaliação em C. |

**Classificação e recomendação:** R03, `ALTERNATIVA`, agrupamento proposto sob V03-008. **Fonte preferencial sugerida:** E/EXP03-005 para avaliar a explicação concreta das duas etapas sem apresentar uma função C genérica; O fica disponível para o foco em leitura da expressão e parâmetros. A preferência não autoriza importar os parâmetros de O para E ou reunir as fichas.

**Pendências efetivas:** homologação de R03; R08 delimita a sobreposição com consulta de bit, e R13 diferencia a extração da analogia aritmética de shifts. Os riscos M03-P-004 a M03-P-007 já registrados em E permanecem, inclusive a adequação das mídias e os limites do código/precedência. A preferência por E não certifica maior prontidão de produção.

<a id="provisoria-entradas"></a>
### Referência local provisória — Entradas e encadeamento

**Fonte e abordagem disponível:** E, seção 3, **EXP03-002 — Três respostas certas podem formar uma sequência errada**. Sem ID oficial novo.

**Pergunta e promessa da fonte:** por que os resultados mudam quando as operações recomeçam do original? Identificar a entrada de cada transformação e distinguir operações independentes de uma cadeia que guarda resultados.

**Fundamento:** E contrapõe um diagrama ramificado e uma sequência acumulada; as operações e os valores já estão escritos na narrativa e no storyboard. O encerramento julga a correspondência entre entrada e pergunta, não qual operador deve ser usado para ativar/limpar. R04/R12 sustentam independência frente a V03-006/V03-007; R11 a distingue da previsão de intenção em EXP03-001. O fato de os cálculos independentes já serem uma ressalva em O não faz dessa nova pergunta uma descoberta técnica inédita; torna possível um foco narrativo próprio.

**Classificação e recomendação:** propor identidade independente, mantendo EXP03-002 como referência de origem. **Fonte preferencial sugerida:** E/EXP03-002, única abordagem documentada do conjunto centrada no contraste ramificação/cadeia. Reconhecer essa oportunidade não atribui um número oficial nem seleciona roteiro.

**Pendências efetivas:** homologação de R04/R11/R12 e reconhecimento da identidade provisória. A densidade de operadores e diagramas é risco já apontado em E: uma futura avaliação deve verificar se o foco continua nas entradas. Não há necessidade de criar nova narrativa ou de acrescentar questões ao exercício para justificar a classificação atual.

<a id="provisoria-reversibilidade"></a>
### Referência local provisória — Reversibilidade dos deslocamentos

**Fonte e abordagem disponível:** E, seção 3, **EXP03-004 — Deslocar de volta desfaz o caminho?**. Sem ID oficial novo.

**Pergunta e promessa da fonte:** direita e depois esquerda recuperam o número inicial? Identificar a informação descartada e distinguir recompor posições de restaurar bits perdidos.

**Fundamento:** a ida/volta já documentada em E confronta a previsão de recuperação com o resultado final diferente. O storyboard destaca o que sai e os zeros que entram. A conclusão exige analisar a informação perdida, e não somente relacionar deslocamento a divisão/multiplicação. R05 sustenta a distinção frente a V03-004; R06 a distingue do desfazer por repetição do XOR de V03-007.

**Classificação e recomendação:** propor identidade independente, mantendo EXP03-004 como origem. **Fonte preferencial sugerida:** E/EXP03-004, única abordagem do conjunto que faz da recuperação do estado a pergunta central. Não lhe atribuir o ID histórico V03-004 por coincidência numérica ou assunto.

**Pendências efetivas:** homologação de R05/R06 e reconhecimento da identidade provisória. A descrição de preenchimento/descarte continua restrita ao modelo sem sinal apresentado em E; não se amplia para negativos ou código C irrestrito. A disponibilidade da demonstração visual e os cartões propostos permanecem limites de produção, sem impedir a classificação narrativa.

## 4. Fundamentação das relações transversais

As três relações de alternativa R01/R02/R03 têm as quatro dimensões comparadas nas entradas [V03-007](#v03-007), [V03-003](#v03-003) e [V03-008](#v03-008). A tabela abaixo completa as relações relevantes sem repetir suas fichas. Evidências são localizáveis nas mesmas seções 3 dos dossiês O/E.

| Relação | Pergunta central | Promessa pedagógica | Demonstração das fontes | Conclusão e fundamento da classificação |
|---|---|---|---|---|
| R04 — O/V03-006 × E/EXP03-002 | Preservar vizinhos ao ligar/limpar versus saber de onde cada cálculo começa. | Construção da máscara versus leitura da dependência de entradas. | O calcula duas operações separadas e explica zeros/uns; E compara ramificação e corrente de resultados. | Escolher a máscara não responde se usar o original ou a saída anterior. `INDEPENDENTE`, apesar de E se apoiar em operações que O ensina. |
| R05 — O/V03-004 × E/EXP03-004 | Relação com potências de dois e limites versus recuperação por ida/volta. | Entender pesos e analogia aritmética versus diagnosticar perda de informação. | O passa por movimento e descarte; E usa esse descarte numa composição de operadores opostos. | O limita uma regra de cálculo; E refuta uma garantia de desfazer. `INDEPENDENTE`: não basta trocar o hook de O, pois o teste e a conclusão-alvo mudam. |
| R06 — O/V03-007 × E/EXP03-004 | Desfazer com a mesma máscara XOR versus tentar desfazer com deslocamentos opostos. | Alternância versus recuperação impossível da informação descartada. | O volta ao original pela repetição de XOR; E acompanha uma volta que não restaura o estado. | São mecanismos e recompensas distintos; não se fundem por ambas tratarem de “voltar”. `INDEPENDENTE`, sem gerar uma terceira narrativa que os combine. |
| R07 — O/V03-002 × E/EXP03-001 | Distinguir OR/XOR por uma combinação de entradas versus distinguir comandos inicialmente coincidentes pela repetição. | Localizar a divergência 1/1 versus escolher garantir ligado ou alternar. | A regra 1/1 é explicação central em O e apoio à segunda aplicação em E; os arcos completos não coincidem. | Há uma explicação relevante reapresentada, mas não equivalência integral. `SOBREPOSICAO_PARCIAL`: preservar ambas as identidades enquanto se homologa esse limite. |
| R08 — O/V03-005 × E/EXP03-005 | Testar uma posição versus extrair o valor de uma faixa. | Interpretar zero/não zero sem alteração versus separar alinhamento de seleção. | Ambas leem um resultado mascarado; O enfatiza 8 como resposta do teste, E destaca o intermediário que ainda contém vizinhos. | A seleção por AND é parcela narrativa comum, mas uma leitura lógica de teste não substitui a leitura do campo. `SOBREPOSICAO_PARCIAL`, sem agrupar oportunidades só porque usam máscara. |
| R09 — O/V03-001 × O/V03-005 | Domínio lógico/bitwise versus consulta de bit e possível alteração. | Distinguir operadores versus interpretar a saída mascarada. | O/V03-001 contrapõe 8 e 1 entre operações; O/V03-005 explica por que o teste pode produzir 8, e não exatamente 1. | O mesmo número participa de perguntas diferentes: escolha de domínio e interpretação de consulta. `INDEPENDENTE`; não são abordagens intercambiáveis. |
| R10 — O/V03-006 × O/V03-007 | Preservação de vizinhos ao ativar/limpar versus efeito de repetir uma alternância. | Construção de máscaras versus escolha entre fixar e alternar. | Comparação de posições preservadas versus dupla aplicação e contraste de objetivos. | A explicação de OR reaparece como apoio, mas o encerramento e a prova diferem. `INDEPENDENTE`, preservando o agrupamento ativação/limpeza já presente em O. |
| R11 — E/EXP03-001 × E/EXP03-002 | Intenção de comandos com primeira saída igual versus entrada de cada transformação. | Prever o comportamento da repetição versus distinguir tarefas independentes de cadeia. | E/EXP03-001 mantém caminhos separados de cada comando; E/EXP03-002 confronta dois modelos de entrada para operações diferentes. | Acertar a intenção do operador não resolve de qual estado partir. `INDEPENDENTE`, sem transformar a recapitulação de máscaras em um segundo arco idêntico. |
| R12 — O/V03-007 × E/EXP03-002 | Dupla aplicação da mesma operação versus operações diferentes com ou sem atualização da entrada. | Alternância reversível versus adequação do encadeamento à instrução. | XOR repetido em O; ramificação/corrente com objetivos distintos em E. | A presença de XOR e de estados sucessivos não produz a mesma resposta pedagógica. `INDEPENDENTE`. |
| R13 — O/V03-004 × E/EXP03-005 | Relação aritmética e descarte versus insuficiência de alinhar o campo. | Interpretar pesos/limites versus compreender por que ainda é preciso mascarar. | Movimento e borda em O; campo identificado, deslocamento e seleção em E. | Deslocar é objeto da explicação em O e ferramenta para outra finalidade em E. `INDEPENDENTE`, sem tornar O pré-requisito curricular obrigatório. |

R07 e R08 são classificações positivas de interseção parcial, não falta de leitura ou convite para apagar candidatos. Não são relações transitivas: uma alternativa de V03-007 não torna automaticamente V03-002 alternativa da mesma identidade. Reconhecer R05 não apaga a explicação de descarte compartilhada. As justificativas precisam permanecer junto dos vínculos caso o catálogo seja revisto.

## 5. Matriz sintética dos relacionamentos

Todos os estados abaixo são **PENDENTE de homologação**. “O” e “E” remetem aos documentos e versões da seção 1. Os localizadores R são apenas linhas deste catálogo, não IDs de candidatos, novas RCs conceituais ou deliberações homologadas.

| Localizador | Candidato A | Candidato B | Classificação proposta | Fundamento |
|---|---|---|---|---|
| R01 | O/V03-007 | E/EXP03-001 | ALTERNATIVA | [V03-007](#v03-007), quadro das quatro dimensões. |
| R02 | O/V03-003 | E/EXP03-003 | ALTERNATIVA | [V03-003](#v03-003), quadro das quatro dimensões. |
| R03 | O/V03-008 | E/EXP03-005 | ALTERNATIVA | [V03-008](#v03-008), quadro das quatro dimensões. |
| R04 | O/V03-006 | E/EXP03-002 | INDEPENDENTE | Seção 4, R04. |
| R05 | O/V03-004 | E/EXP03-004 | INDEPENDENTE | Seção 4, R05. |
| R06 | O/V03-007 | E/EXP03-004 | INDEPENDENTE | Seção 4, R06. |
| R07 | O/V03-002 | E/EXP03-001 | SOBREPOSICAO_PARCIAL | Seção 4, R07. |
| R08 | O/V03-005 | E/EXP03-005 | SOBREPOSICAO_PARCIAL | Seção 4, R08. |
| R09 | O/V03-001 | O/V03-005 | INDEPENDENTE | Seção 4, R09. |
| R10 | O/V03-006 | O/V03-007 | INDEPENDENTE | Seção 4, R10. |
| R11 | E/EXP03-001 | E/EXP03-002 | INDEPENDENTE | Seção 4, R11. |
| R12 | O/V03-007 | E/EXP03-002 | INDEPENDENTE | Seção 4, R12. |
| R13 | O/V03-004 | E/EXP03-005 | INDEPENDENTE | Seção 4, R13. |

## 6. Confronto com o comparativo auxiliar e limites

A leitura das fichas sustenta os equivalentes centrais já sugeridos no comparativo: alternância, largura de NOT e extração. A presente análise acrescenta a separação explícita das quatro dimensões e dos estados de deliberação; não toma a palavra “equivalência” do parecer como homologação. Nas alternativas de NOT e extração, a diferença de escopo entre as fichas foi preservada, sem sintetizar uma promessa nova.

A independência de EXP03-002 e EXP03-004 é sustentada por suas próprias demonstrações e conclusões, não apenas por constarem da recomendação anterior de piloto. A interpretação aqui proposta é mais explícita que uma semelhança por assunto: R04/R05 recomendam oportunidades distintas, enquanto R07/R08 registram interseções narrativas sem equivalência integral. O comparativo não foi usado para selecionar automaticamente o próximo vídeo ou para presumir que o protocolo mais recente produz as melhores fontes.

As limitações são documentais e editoriais: não houve nova inspeção de imagens/GIFs, ensaio, teste de compreensão ou avaliação da audiência. Os riscos de mídia e as estimativas de duração permanecem nas fontes; sua transcrição contextual não constitui nova auditoria. O histórico conhecido da conversa e a autoria anterior dos documentos impedem alegar análise cega. Nenhuma fonte primária ficou indisponível ou ilegível nesta execução.

Não se identificou incompatibilidade arquitetural impeditiva. Uma possível combinação futura de conteúdos de duas fichas exigiria revisão editorial autorizada de um dossiê; este catálogo não cria tal combinação nem permite ao roteirizador realizá-la implicitamente. O catálogo de consolidação identifica fontes e decisões, **não fornece conteúdo narrativo** ao roteiro.

## 7. Deliberações humanas efetivamente necessárias

1. **Homologação dos vínculos:** apreciar as três alternativas R01–R03, as oito independências e as duas sobreposições parciais da matriz. Recomendo as classificações apresentadas, sem pendência artificial de nova pesquisa para classificá-las. Aceite, rejeição e justificativas deverão ser registrados sem apagar a proposta inicial.
2. **Reconhecimento das oportunidades:** apreciar a manutenção das oito referências históricas e o reconhecimento das duas provisórias. As provisórias merecem atenção por diagnosticarem, respectivamente, a entrada de cada operação e a perda de informação na ida/volta. Elas continuam sem ID oficial novo. Reconhecer uma oportunidade não aprova automaticamente uma abordagem ou roteiro.
3. **Seleção futura, em etapa própria:** se o responsável posteriormente desejar roteirização, deverá indicar explicitamente o candidato e o caminho do dossiê-fonte. As preferências das entradas são sugestões para essa decisão, não uma fila aprovada ou autorização solicitada agora. A seleção de experimental não atribui ID oficial; conflitos de destino precisam ser resolvidos sem sobrescrever o roteiro existente. O piloto técnico V03-003 permanece preservado e não é proposto para substituição automática.

Não há encaminhamento autorizado para novo roteiro ou produção nesta etapa. O roteiro futuro só pode desenvolver um candidato-fonte no dossiê selecionado, sem complementar falas, exemplos ou mídias a partir deste catálogo ou de outra ficha.

## 8. Validação e histórico do registro

- Pacotes dos dois DOCX íntegros e legíveis; corpo e tabelas extraídos integralmente. As fichas contêm as dimensões utilizadas, inclusive narrativas e storyboards, não somente títulos e inventários.
- Cobertura dos 8 candidatos O e 5 E, com IDs distintos nas respectivas fontes e uma única associação principal por candidato nas 10 identidades. Comparações adicionais não duplicam identidades; nenhum ID foi promovido, excluído ou reciclado.
- As 13 relações têm fundamentação nas quatro dimensões, referência às fichas e classificação proposta separada da homologação. R01/R02/R03 são propostas de agrupamento sob IDs históricos, não atos de aprovação.
- Caminhos e links relativos conferidos, inclusive destinos e localizadores deste Markdown. As perguntas e promessas são identificações atribuídas; exemplos citados já pertencem às fontes. Não há novas falas, hooks, storyboards ou exemplos técnicos apresentados como conteúdo dos dossiês.
- Hashes das fontes e de todos os arquivos previamente versionados preservados; somente `editorial/consolidacoes/03_Consolidacao_Editorial.md` é novo no escopo de publicação. Dossiês, comparativo, piloto, contratos, governança, inventário e originais não foram alterados.
- `git diff --check` sem erros. Validação documental não equivale a homologação editorial, aprovação de oportunidade ou autorização de roteiro.

**Histórico 1.0:** primeira proposta de consolidação, autorizada pelo pedido “Etapa 2: Consolidação Editorial do Capítulo 03”, com publicação para revisão. Não há deliberações humanas sobre os vínculos produzidos nesta etapa. A aprovação das PRs anteriores não foi convertida em aprovação dos candidatos ou destas relações. Revisões futuras deverão preservar este registro e as justificativas, indicando o que mudou e a manifestação correspondente.
