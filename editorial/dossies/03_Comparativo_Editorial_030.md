# Capítulo 03 — Comparativo editorial do experimento 0.3.0

Estado: parecer do agente para avaliação humana. Todos os candidatos experimentais permanecem `PROPOSTO`; seleção, promoção e produção estão `A_DEFINIR`.

Documentos comparados:

- [Dossiê experimental 030](03_Dossie_Editorial_Experimental_030.docx), versão 1.0, cinco candidatos `EXP03-001` a `EXP03-005`, protocolo 0.3.0.
- [Dossiê anterior](03_Dossie_Editorial.docx), versão 1.0, oito candidatos `V03-001` a `V03-008`, protocolo 0.2.4. As referências abaixo apontam para os IDs e títulos das respectivas fichas, não para números de página dependentes do visualizador.

## Método, fontes e limites da comparação

A base foi sincronizada com `main`, commit `6456b993ac2d58f91a50880c0770b95cd4047c6c`, após a integração da PR #22. Na fase de descoberta foram consultados `AGENTS.md`, o protocolo 0.3.0, o inventário, o catálogo do capítulo 03, o vocabulário controlado e os relacionamentos conceituais. O checklist foi consultado como instrução operacional de preservação das pendências, sem usar seus comentários sobre candidatos anteriores como fonte de ideias. Não foram abertos o dossiê anterior, os roteiros ou o vídeo nessa fase. Não houve consulta a dossiês de outros capítulos para conteúdo ou quantidade.

O catálogo foi lido no corpo e teve a ausência de tabelas confirmada. Foram considerados seus 20 registros; as mídias candidatas tiveram existência e registro no inventário conferidos. Não houve inspeção visual dos originais nesta tarefa. As referências ao conteúdo das imagens e às transições dos GIFs são documentais. Cartões novos, exemplos calculados e sua organização são `PROPOSTA_EDITORIAL`; não são elementos existentes alegadamente observados.

O experimental foi concluído e salvo em **2026-10-30, 02:39:38 UTC**, antes da primeira abertura do anterior nesta execução, registrada em **02:39:46 UTC**. Seu SHA-256 foi fixado em `b4d01eeefba7a771febcf77595c57920368ed090afc08ac18eee6afcf1dd67c3` e conferido novamente após a comparação; não houve ajuste de conteúdo para aumentar diferenças retrospectivamente. O anterior foi então extraído integralmente, incluindo suas dez tabelas, para esta segunda fase.

**Limite metodológico:** o histórico da conversa já continha informações de trabalhos anteriores. Portanto, a separação das leituras demonstra a ordem operacional desta execução, mas não um experimento cego ou ausência de influência residual. A avaliação é um estudo de caso documental, não prova causal de superioridade do protocolo. O SHA-256 do catálogo usado pelo anterior e pelo experimental é o mesmo: `d3611c7308f2e10329a6036ffaaa152f61b37e1bd7bd6672358e358db992f6e9`. O contexto de governança, entretanto, já inclui pendências posteriores ao primeiro dossiê; o detalhamento desses riscos não deve ser atribuído apenas à versão 0.3.0.

## Correspondência entre candidatos

Cada referência `EXP03-...` corresponde à ficha de mesmo ID no experimental. Cada `V03-...` corresponde à ficha de mesmo ID no anterior.

| Experimental | Correspondência anterior | Natureza da diferença |
|---|---|---|
| EXP03-001 — Dois comandos iguais na primeira vez — e na segunda? | Equivalência central com V03-007 — XOR alterna; OR fixa. Apoio parcialmente semelhante a V03-002 — OR ou XOR: o caso que separa os dois. | Reformulação da demonstração de V03-007, incorporando o contraste por coluna. Não é uma oportunidade inteiramente nova. |
| EXP03-002 — Três respostas certas podem formar uma sequência errada | Semelhante parcialmente a V03-006 — Ligar e desligar sem afetar os vizinhos, com apoio de V03-007. Não há ficha anterior cuja promessa central seja comparar entradas independentes e encadeadas. | Nova pergunta central a partir de uma condição já explicitada no anterior; combina objetivos conhecidos e muda o problema avaliado. |
| EXP03-003 — A mesma inversão pode dar cinco ou duzentos e quarenta e cinco? | Equivalência central com V03-003 — NOT precisa de uma largura. | Reformulação com contraste entre larguras, reduzindo a discussão de C e de sinal. Não é descoberta de outro conceito ou outra oportunidade fundamental. |
| EXP03-004 — Deslocar de volta desfaz o caminho? | Semelhança parcial com V03-004 — Deslocar não é multiplicar sem limites. | Novo foco narrativo em reversibilidade, derivado do descarte já explicado no anterior. Não é assunto técnico inédito. |
| EXP03-005 — Já desloquei o campo. Por que a resposta ainda está errada? | Equivalência central com V03-008 — Extrair um campo: deslocar e depois selecionar. | Reformulação com exemplo numérico e erro intermediário explícito; a pergunta e a conclusão essenciais já existiam. |

### EXP03-001 — Primeira coincidência, segunda aplicação

**Pergunta e promessa:** se OR e XOR levam ao mesmo resultado inicialmente, como decidir qual usar? Distinguir garantir um bit ligado de alterná-lo.

**Conceitos e materiais:** OR bitwise, XOR bitwise, máscara de bits, ativação e inversão de bit. Registros de `03_Operacoes_Bitwise/mascara_bitwise2.png`, `mascara_bitwise3.png`, `xor.png` e `bitwise_mascaras.gif`, com caminhos completos na ficha. O teste 10/4 é criação editorial calculada, não transcrição dessas mídias.

**Diferença efetiva:** o anterior V03-007 já explica a dupla aplicação de XOR e a contrapõe a OR, usando 10 XOR 8 → 2 → 10. O novo começa com um bit desligado: 10 OR 4 e 10 XOR 4 coincidem em 14; só na segunda aplicação as trajetórias se separam. A tabela do caso 1/1, que era centro de V03-002, passa a explicar a surpresa.

**Parecer:** há ganho potencial de encenação, pois a coincidência inicial prepara uma previsão testável. A autonomia, porém, já existia em V03-007. Seria inadequado promover os dois como vídeos independentes apenas por trocarem os números ou a abertura. Se houver interesse, avaliar esta abordagem como alternativa editorial, sem consolidar ou renumerar IDs automaticamente. A correção do exemplo foi conferida; a adequação dos painéis permanece pendente, especialmente diante de M03-P-002.

### EXP03-002 — A entrada faz parte da pergunta

**Pergunta e promessa:** por que as mesmas operações podem terminar em 2 ou 4? Identificar a entrada de cada transformação antes de comparar respostas.

**Conceitos e materiais:** ativação, limpeza e inversão de bit, máscaras e estados sucessivos. Registros de `03_Operacoes_Bitwise/exercicio.md`, `gabarito.md`, `mascara_bitwise4.png` e `bitwise_mascaras.gif`. As duas estruturas de setas são elementos novos propostos.

**Diferença efetiva:** V03-006 já exige operações independentes e conclui explicitamente que 14 e 8 não são passos da mesma atualização. Ali, isso protege o exemplo cuja promessa é preservar os bits vizinhos. EXP03-002 transforma a condição em pergunta central: as saídas independentes de 10 são 14, 8 e 2; uma cadeia que armazena cada resultado percorre 10 → 14 → 12 → 4. O contraste não denuncia um erro no gabarito: compara problemas distintos. A cadeia é uma hipótese editorial, sem acrescentar questões ao exercício.

**Parecer:** é uma oportunidade narrativa nova em relação às promessas das fichas anteriores, embora derivada de uma ressalva já presente, combinando operações em vez de propor uma por vídeo. Seu teste de autonomia é manter o foco nas entradas; se for necessário reensinar cada operador, a duração estimada de 75 s e a clareza ficam ameaçadas. O anterior é mais direto para aprender a construir máscaras; não seria substituído por esta proposta. M03-P-003 impede usar sem ressalva a linha incorreta de limpeza da fonte.

### EXP03-003 — Larguras diferentes, regra igual

**Pergunta e promessa:** como inverter dez pode resultar em 5 e em 245? Mostrar que zeros adicionais participam da inversão quando integram a largura escolhida.

**Conceitos e materiais:** NOT bitwise, largura em bits e interpretação sem sinal. Registros de `03_Operacoes_Bitwise/bitwise_not.png`, `exercicio.md` e `gabarito.md`. O modelo de quatro bits é um exemplo proposto; somente o resultado de oito bits é diretamente registrado no catálogo.

**Diferença efetiva:** V03-003 já pergunta pela largura e distingue o resultado de oito bits de `~10` em C. EXP03-003 explicita dois modelos sem sinal, 1010 → 0101 e 00001010 → 11110101, deixando a discussão de tipos C como ressalva final. Não promete explicar sinal nem complemento de dois.

**Parecer:** o contraste visual pode facilitar a percepção dos zeros à esquerda, mas não cria uma oportunidade independente do V03-003. O anterior é melhor quando o objetivo é evitar uma extrapolação para C; o novo limita melhor o esforço inicial para quem ainda não conhece inteiros com sinal. Não há motivo demonstrado para refazer o piloto existente. A redução de escopo é uma escolha editorial, não evidência automática de qualidade superior. M03-P-001 continua restrição de uso dos painéis problemáticos.

### EXP03-004 — A volta não recupera o descarte

**Pergunta e promessa:** mover à direita e depois à esquerda desfaz o caminho? Identificar a informação perdida, em vez de pressupor uma operação de desfazer.

**Conceitos e materiais:** deslocamentos, valor posicional, largura, inteiro sem sinal e descarte. Registros de `03_Operacoes_Bitwise/bitwise_shift.png`, `bitwise_shift3.png`, `bitwise_deslocamento.gif` e `exercicio.md` (valor inicial 10). A sequência 10 → 2 → 8 é exemplo editorial novo, não sequência afirmada do GIF. RC-004 é usada só para o pré-requisito conceitual de posições, sem impor ordem ou importar imagens de outro capítulo.

**Diferença efetiva:** V03-004 parte da relação entre deslocamento e multiplicação/divisão, incluindo descarte e limites. EXP03-004 usa o descarte como prova contra uma previsão específica: após `10 >> 2`, voltar duas posições à esquerda dá 8. Os zeros de preenchimento não guardam os bits que saíram. A conclusão é sobre reversibilidade, não uma revisão das identidades aritméticas.

**Parecer:** a diferença de trajetória e de pergunta é substantiva, embora ancorada no mesmo fundamento técnico. A demonstração tem um resultado verificável e cabe, em estimativa, em 65 s. Isso torna o candidato promissor para testar a descoberta por surpresa. O anterior segue melhor para introduzir a relação com potências de dois; o novo pressupõe ou precisa retomar movimentos e posições. Compartilhar fontes não implica redundância, mas publicar os dois exigiria objetivos explícitos para não repetir a mesma explicação de descarte.

### EXP03-005 — Um resultado intermediário ainda contém vizinhos

**Pergunta e promessa:** por que o deslocamento chegou a 6 quando o campo desejado vale 2? Mostrar o papel complementar de alinhamento e seleção.

**Conceitos e materiais:** extração de bits, campo de bits, deslocamento à direita e AND com máscara. Registros de `03_Operacoes_Bitwise/get_bits.png`, `get_bits2.png`, `getbits.gif` e `exercicio.md` (B=12). O campo nas posições 2..1 e a máscara 3 são escolhas editoriais calculadas; não se inventa uma assinatura de getbits.

**Diferença efetiva:** V03-008 já pergunta se mover até a ponta basta, explica vizinhos remanescentes e combina deslocamento com máscara. O novo torna o caso concreto: 00001100 >> 1 = 00000110; AND 00000011 = 00000010. Não é uma pergunta nova; é uma demonstração mais definida da pergunta existente.

**Parecer:** o exemplo permite antecipar um erro e ver sua correção, com menos dependência de uma fórmula genérica. O anterior é melhor como porta para ler parâmetros e agrupamento de uma expressão getbits; o novo atende um objetivo mais estreito e evita apresentar código pendente como validado. Isso pode melhorar a clareza, mas aumenta a necessidade de cartões novos. M03-P-004 a M03-P-007 continuam limitações de reutilização. A ordem didática apresentada não é ordem de avaliação imposta pelo C.

## Avaliação dos conjuntos

| Aspecto | Dossiê anterior | Experimental e limite do ganho |
|---|---|---|
| Diversidade de perguntas | Distingue domínios lógico/bitwise, OR/XOR, largura, deslocamento, consulta, preservação, alternância e extração. Já tem perguntas próprias, não é mera lista de operadores. | Concentra-se em intenções, entradas e informação: coincidência, encadeamento, largura, reversibilidade e etapa insuficiente. Perde a pergunta autônoma de teste zero/não zero e o contraste lógico/bitwise; não equivale a cobrir melhor o capítulo. |
| Independência real | V03-002 e V03-007 se apoiam em OR/XOR, mas têm conclusões diferentes; V03-005/006/007 separam consulta, preservação e alternância. Há agrupamentos justificados. | As fichas justificam explicitamente a autonomia. EXP03-002 e EXP03-004 trazem focos diferentes; EXP03-001/003/005 não deveriam coexistir com seus equivalentes só por serem experimentais. A justificativa escrita facilita revisão, mas não prova independência por si. |
| Combinação de conceitos | Já combina ativação/limpeza em V03-006 e deslocamento/máscara em V03-008. Não há oposição simples entre versão antiga fragmentada e nova integradora. | EXP03-002 organiza várias operações em torno da entrada; EXP03-005 mantém a combinação anterior. OR/XOR vira apoio à escolha de comando. O ganho está em selecionar o problema, não em somar mais termos numa ficha. |
| Curiosidade e demonstração | Hooks como “oito ou um”, “um ou oito” e “a mesma operação desfaz a si própria?” já criam contraste. | Coincidência inicial, duas soluções válidas para problemas diferentes e ida/volta falha dão previsões verificáveis. Interesse real depende de leitura humana; não houve teste de público ou evidência de engajamento. |
| Recompensa pedagógica | Conclusões explícitas ligadas à distinção de operadores e interpretação de resultados. | Conclusões formuladas como decisões ou diagnósticos. O caso 10→2→8 tem recompensa clara; o caso 5/245 estreita o escopo e não é superior para ensinar semântica de C. |
| Sobreposições | Fontes compartilhadas não tornam as fichas redundantes automaticamente. | O confronto entre as novas fichas foi registrado. O compartilhamento de máscaras entre EXP03-001/002 requer disciplina; uma repetição longa das regras enfraqueceria o segundo. A redução de oito para cinco não mede qualidade. |
| Viabilidade de vídeo curto | Estimativas de 58–68 s, com falas e storyboards, sem tempo medido. V03-004 e V03-008 ficam mais genéricos nos exemplos. | Estimativas de 65–75 s. Há exemplos mais definidos, mas EXP03-002/005 demandam atenção a várias linhas binárias. Precisam de ensaio e demonstração legível; não há prova de duração real ou maior facilidade de produção. |
| Fundamentação e precisão | Mesmo catálogo principal; distingue confiança documental de validação visual, registra limites de largura e precedência. Apoios externos têm catálogos citados. | Mantém as distinções e acrescenta restrições preexistentes do checklist, sem corrigi-las. Não usa fontes visuais nem catálogos externos para sustentar afirmações novas. Cartões calculados não validam as imagens originais. Maior detalhe de risco decorre também do contexto posterior. |

Não foi identificada uma ficha experimental sem qualquer antecedente conceitual no acervo — nem isso seria desejável num trabalho fundamentado. A novidade relativa de EXP03-002/004 está no problema que passa a comandar a narrativa. EXP03-001 combina a encenação de OR/XOR com uma promessa já central em V03-007; EXP03-003/005 reformulam promessas existentes. Essas relações são constatações comparativas, não propostas de excluir, consolidar ou alterar candidatos históricos.

## Validação e preservação

- O DOCX experimental abriu em `python-docx`, teve seu pacote ZIP/XML validado e foi convertido pelo LibreOffice para PDF temporário, com 13 páginas. O painel de páginas foi inspecionado para conferir apresentação e ausência de cortes evidentes; isso não é auditoria dos originais nem teste no visualizador do usuário. O LibreOffice emitiu avisos de cache de fontes, sem impedir a conversão. O PDF e os auxiliares ficaram fora do checkout.
- As cinco fichas têm os 13 campos obrigatórios, duas alternativas de hook cada, narrativa contínua e quatro momentos de storyboard desenvolvidos. Estado `PROPOSTO`; decisões `A_DEFINIR`. A prioridade exploratória permanece `A_DEFINIR`, sem ranking numérico.
- Os 14 materiais distintos referenciados nas fichas existem, estão inventariados e têm registro individual no catálogo. O DOCX contém os caminhos completos; os exemplos novos estão classificados como propostas, com os limites de inspeção e produção explícitos.
- Foram conferidos os cálculos de OR/XOR repetidos, as operações independentes e encadeadas, as inversões de 4/8 bits, a ida/volta de deslocamento e a extração do campo 2..1 de 12. Não se executou ou homologou código C dos originais.
- Foram verificadas as referências relativas deste Markdown, os IDs experimentais e históricos citados e a preservação do SHA-256 do experimental após a leitura comparativa.
- A comparação dos hashes dos arquivos previamente versionados não identificou alteração. Dossiê anterior, piloto e seus artefatos versionados, materiais, catálogos, inventário, protocolos, governança e checklist permaneceram intactos. Nenhum MP4 ou áudio foi aberto, renderizado ou regravado por esta tarefa.
- O escopo de publicação contém exclusivamente os dois arquivos novos solicitados. Não foram produzidos roteiros individuais, mapas, vídeos ou documentos adicionais de governança.

## Parecer final para deliberação

1. **O protocolo produziu oportunidades substancialmente diferentes?** Parcialmente. EXP03-002 desloca o centro da explicação para a entrada de cada operação; EXP03-004 testa a reversibilidade. Ambos exploram limites já documentados com perguntas próprias. As outras três propostas têm equivalentes fortes no anterior. Não houve renovação completa nem evidência de que fosse necessária.
2. **Há maior autonomia narrativa?** A autonomia ficou mais explícita e avaliável, sobretudo nos dois focos acima. O anterior já tinha candidatos autônomos e combinações pertinentes. Não há fundamento para afirmar superioridade geral, e os equivalentes de NOT, alternância e extração não devem ganhar vida independente apenas por outra apresentação.
3. **Houve ganho editorial ou só de apresentação?** Há ganho localizado nas previsões testáveis e nos exemplos desenvolvidos de perda e entradas. A extração recebeu uma demonstração concreta útil, embora de uma promessa já existente. O contraste de larguras é uma alternativa de abordagem. O detalhamento formal e a quantidade menor, isoladamente, não demonstram qualidade maior.
4. **Quais merecem atenção para outro piloto?** Recomendo avaliar **EXP03-004**, por sua pergunta curta e resultado inesperado demonstrável, e **EXP03-002**, por integrar operadores num problema de leitura de estado. São recomendações sem aprovação, ordem de produção ou promoção de IDs. EXP03-002 precisa de ensaio mais cuidadoso pela densidade. EXP03-005 pode interessar se a intenção for testar clareza de um exemplo de extração; sua disponibilidade visual tem restrições maiores. Não recomendo refazer o piloto de NOT só para testar outra abertura.
5. **O que ainda precisa ser discutido?** Se o público domina o suficiente de binário para acompanhar duas trajetórias; se a distinção entre independência e cadeia sustenta um vídeo sem virar recapitulação; quanto de criação gráfica nova é aceitável; como preservar a precisão de C sem carregar o formato curto; e se a preferência editorial por suspense melhora a aprendizagem nesse público. Não há ensaio narrado, teste de compreensão ou avaliação de público para resolver essas questões.

Os IDs experimentais permanecem provisórios e não substituem os históricos. A promoção de qualquer candidato exige deliberação humana e atribuição de ID definitivo conforme as regras vigentes. Este parecer encerra o experimento documental; não autoriza produção ou mudanças nos artefatos existentes.
