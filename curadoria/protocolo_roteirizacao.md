# Protocolo de roteirização e leitura de dossiês

> **Identificador:** `curadoria/roteirizacao`  
> **Versão:** `0.2.3` — revisão operacional da versão editorial 0.2.2 homologada  
> **Escopo:** dossiês editoriais de tópicos, seleção de candidatos e passagem para especificações de produção  
> **Estado:** HOMOLOGADO — protocolo vigente  
> **Documento piloto de referência:** `editorial/dossies/01_Dossie_Editorial.docx`

## 1. Finalidade

Este protocolo centraliza as regras comuns para **ler, criar, revisar e aprovar** dossiês editoriais. Cada dossiê registra **N candidatos independentes de vídeos** originados de um tópico; não há correspondência obrigatória de um capítulo para um vídeo. O dossiê permite propostas e alternativas, mas **não é um contrato executável**.

O objetivo é preservar uma fronteira clara: **curadoria e roteirização propõem; responsável humano decide; renderizador executa apenas instruções fechadas**. Não inferir decisões ausentes.

## 2. Artefatos e responsabilidades

| Artefato | Responsabilidade | Pode conter alternativas? | Pode ser renderizado? |
|---|---|---|---|
| `curadoria/protocolo_roteirizacao.md` | Regras compartilhadas, estados e campos | Não, na versão homologada | Não |
| `editorial/dossies/NN_Dossie_Editorial.docx` | Dossiê com N candidatos, fontes, hipóteses, alternativas e decisões | Sim | Não |
| `editorial/roteiros/<video_id>_producao.md` (proposto) | Especificação fechada de **um** vídeo aprovado | Não | Sim, após validação |
| `<video_id>_cenas.json` | Plano de execução derivado da especificação | Não | Entrada técnica |
| `<video_id>_guia.mp4` | Vídeo-guia sem legendas e com áudio provisório | Não | Produto |
| `<video_id>_roteiro.md` | Texto/guia para gravação humana derivado do contrato | Não | Produto auxiliar |

O caminho dos dossiês é a **convenção vigente** do repositório. Os caminhos dos artefatos posteriores à seleção editorial são **provisórios** e dependem da definição do contrato técnico de produção. A autorização explícita da tarefa de geração abrange a criação do dossiê no caminho previsto; operações Git seguem o `AGENTS.md`.

## 3. Unidade editorial e identificação

- **Tópico:** recorte de origem, normalmente um capítulo, mas não necessariamente restrito a ele.
- **Candidato:** pergunta/gancho central e promessa pedagógica que possam sustentar um vídeo curto. ID estável `V<capitulo>-<sequencial>`, por exemplo `V01-003`.
- **Alternativa:** outro gancho, exemplo, abordagem ou sequência de mídias para o **mesmo** candidato; não vira novo vídeo automaticamente.
- **Seleção editorial:** escolha humana explícita de uma versão, incluindo suas dependências e restrições.
- **Contrato de produção:** instruções completas para um único vídeo; não pode depender de julgamento criativo do executor.

Novos candidatos recebem novos IDs. Não renumerar IDs existentes; não reaproveitar ID rejeitado.

## 4. Estados e transições

Estados do candidato: `PROPOSTO`, `EM_REVISAO`, `APROVADO`, `RESERVADO`, `REJEITADO`, `PRODUZIDO`.

- `PROPOSTO`: hipótese editorial registrada, sem autorização de produção.
- `EM_REVISAO`: apuração de fontes, imagens, roteiro e escolhas em andamento.
- `APROVADO`: conteúdo, versão e decisões editoriais aprovados pelo responsável humano.
- `RESERVADO`: candidato aprovado mantido para execução futura.
- `REJEITADO`: proposta recusada, preservando o motivo e o histórico.
- `PRODUZIDO`: produto concluído e aceito; não presumir esse estado apenas porque houve renderização.

**Regra:** o estado `APROVADO` não dispensa a validação técnica do contrato. Mudanças de conteúdo após aprovação exigem nova revisão/aceite. A escolha de um candidato não aprova automaticamente os demais.

## 5. Fontes documentais e política de confiança

### 5.1 Fontes e precedência operacional

A roteirização é **documental por padrão**. Consultar efetivamente, conforme o escopo:

1. `inventario.csv`: existência registrada, módulo, nome exato e metadados disponíveis; não prova acesso ao binário.
2. `NN_Catalogo_Semantico.docx` do capítulo de origem e dos capítulos referenciados: descrição de conteúdo, finalidade didática, representações e transições de GIFs **quando efetivamente documentadas**.
3. `curadoria/vocabulario_controlado.md`: terminologia canônica, distinções conceituais e homônimos.
4. `curadoria/relacionamentos_conceituais.md`: vínculos entre capítulos homologados, justificativas e limites, inclusive ressalvas.

O inventário responde **qual arquivo e onde**; o catálogo responde **o que está documentado sobre ele**; o vocabulário auxilia na precisão dos conceitos; as RCs fundamentam **por que associar** materiais de capítulos distintos. Nenhuma dessas fontes substitui automaticamente as demais. Consultar a fonte real; não alegar leitura com base apenas no nome ou na existência do arquivo.

### 5.2 Regra de confiança

O roteirista pode utilizar a descrição do catálogo como **evidência documental suficiente para propor e desenvolver narrativas e storyboards editoriais**, sem exigir a inspeção recorrente de PNG/JPEG/GIF. Não apresentar essa confiança como verificação visual independente nem como garantia de que o catálogo esteja correto.

**Não solicitar mídias originais por padrão durante a roteirização.** Solicitar prioritariamente o catálogo, inventário ou registro documental faltante, com escopo preciso. Só solicitar a mídia nesta fase se uma decisão editorial essencial depender de característica não descrita, e não houver maneira de reformular a cena sem ela. Para a produção, os binários selecionados são obrigatórios.

### 5.3 Classificação das afirmações e cenas

- `DOCUMENTADO`: afirmação diretamente sustentada pelo catálogo, inventário ou outra fonte consultada, com identificação do registro.
- `PROPOSTA_EDITORIAL`: criação narrativa, exemplo, associação ou aplicação sugerida a partir das evidências, sem atribuí-la falsamente ao material original.
- `VALIDAR_NA_PRODUCAO`: característica técnica ou visual não documentada que precisa ser confirmada com o binário (dimensão, legibilidade, quadro, timing, crop, loop, enquadramento etc.).
- `DECISAO_HUMANA_PENDENTE`: escolha de abordagem, inclusão, prioridade ou autorização ainda não manifestada; usar `A_DEFINIR` no dossiê, nunca no contrato final.

Registrar essa classificação de modo proporcional ao risco, preferencialmente na ficha ou cena, sem burocracia repetitiva. Uma cena pode ter conteúdo `DOCUMENTADO` e ainda exigir `VALIDAR_NA_PRODUCAO` para o enquadramento.

### 5.4 Divergências, limites e solicitações

Se catálogo e inventário divergirem, ou se o catálogo for ambíguo, incompleto ou ilegível, **não completar silenciosamente**. Identificar a divergência, sua consequência e a fonte/decisão específica necessária. Não modificar catálogos, inventário ou mídias sem autorização.

Uma relação `RC-###` homologada demonstra pertinência pedagógica documental da associação, **não** prova qualidade visual, legibilidade ou disponibilidade do binário. Preservar seu tipo, direção, justificativa e ressalvas. Conexões novas são hipóteses editoriais, não novas RCs homologadas.

A ausência de um arquivo opcional não paralisa outros candidatos. Caminhos de mídia são relativos à raiz `Class_Material/`, com grafia exata; anexos da conversa não significam inclusão no Git.

### 5.5 Fronteira com a produção

Na fase editorial podem permanecer riscos `VALIDAR_NA_PRODUCAO` identificados. **Antes da emissão de um contrato executável**, o responsável pela preparação técnica deve resolver os requisitos de mídia e parâmetros de cena necessários à execução, sem escolher novas soluções editoriais por conta própria. Se a validação exigir mudar o conteúdo, a seleção ou o sentido, devolver a decisão ao responsável humano. O renderizador recebe apenas instruções fechadas e rejeita dependências não resolvidas.

## 6. Estrutura de um dossiê por tópico

O cabeçalho de cada dossiê deve conter **somente**: título/tópico, versão do dossiê, estado, fontes consultadas, protocolo de referência e síntese do objetivo. **Não copiar este protocolo para dentro do dossiê.**

Seções recomendadas:

1. **Escopo e evidências:** fontes, materiais disponíveis, limites da inspeção e relações pertinentes.
2. **Inventário de oportunidades:** tabela de IDs, perguntas, promessa pedagógica, relações, prioridade exploratória e estado.
3. **Fichas de candidatos:** uma seção por ID, sem depender da ordem de aprovação.
4. **Decisões e pendências:** deliberações, pedidos de insumos e próximos passos.

A seção de instruções de leitura que apareceu no piloto do capítulo 01 pertence **a este protocolo** e deve ser retirada de futuras versões do dossiê. A lista de parâmetros comuns também deve ser centralizada aqui; o dossiê mantém apenas exceções específicas do tópico.

O piloto `editorial/dossies/01_Dossie_Editorial.docx` pode orientar **apresentação, legibilidade e organização** da entrega, mas **não** deve ser usado como fonte de conteúdo, seleção de assuntos, fundamentação, número de candidatos ou reprodução de narrativas. A geração de cada novo dossiê deve ser independente e baseada nas fontes documentais do capítulo.

## 7. Estrutura mínima da ficha de candidato

Cada seção `## VXX-### — <título>` deve identificar:

| Campo | Significado |
|---|---|
| `Estado` | Estado do ciclo de vida |
| `Tese/pergunta` | Problema central do vídeo |
| `Promessa` | O que o espectador compreenderá ao final |
| `Público` | Conhecimento pressuposto, quando relevante |
| `Alternativas de hook` | Aberturas candidatas, sem seleção implícita |
| `Fundamento didático` | Conceitos e evidências documentais |
| `Relações RC` | IDs, finalidade e limites de uso, ou `NENHUMA` |
| `Mídias candidatas` | Caminho exato, papel proposto e situação de inspeção |
| `Narrativa proposta` | Texto provisório, não locução obrigatória |
| `Storyboard indicativo` | Ordem e intenção das cenas, ainda sem comando executável |
| `Propósito final` | Aprendizado ou distinção a ser demonstrado |
| `Dependências e riscos` | Arquivos ausentes, legibilidade, ambiguidade, restrições |
| `Decisão editorial` | Escolha expressa, justificativa, data/versão quando aprovada |

Campos podem ser estendidos por versão do protocolo, sem renumerar candidatos nem apagar decisões anteriores.

### 7.1 Desenvolvimento editorial mínimo do candidato

A ficha deve permitir **avaliar o vídeo como proposta narrativa**, e não apenas reconhecer o tema ou delegar a escrita a uma etapa posterior. As exigências abaixo são editoriais e **não transformam o dossiê em contrato de produção**:

1. **Narrativa preliminar falável.** Redigir uma proposta contínua de fala, com abertura, desenvolvimento e conclusão, que possa ser lida em voz alta para avaliar clareza, ritmo e promessa pedagógica. Não substituir a narrativa por instruções como “explicar a regra”, “mostrar os casos” ou “narrar a conclusão”. O texto é provisório: não é locução aprovada, transcrição obrigatória nem comando ao renderizador. Quando houver alternativas de abordagem, indicar qual narrativa exemplifica a proposta, sem presumir escolha humana.
2. **Storyboard editorial desenvolvido.** Descrever os momentos da explicação em ordem, associando cada momento à mídia candidata ou a um elemento **explicitamente proposto para criação**. Indicar o que o espectador deve observar e como isso sustenta a fala. Incluir estimativa de duração total e, quando útil, faixas aproximadas por momento para avaliar a viabilidade no formato curto. Não inventar tempos de GIF, recortes, destaques ou elementos existentes na mídia; separar o que é `DOCUMENTADO` do que é `PROPOSTA_EDITORIAL` ou `VALIDAR_NA_PRODUCAO`. Tempos editoriais são indicativos, não marcações executáveis.
3. **Variedade de abordagem.** Apresentar hooks e possibilidades narrativas que representem diferenças reais de pergunta, exemplo, contraste, surpresa ou progressão didática, quando houver fundamento para isso. Evitar alternativas meramente parafraseadas e fichas mecanicamente idênticas. Não criar quantidade artificial de candidatos nem comprometer a precisão conceitual para obter variedade.

**Critério de suficiência:** ao ler a ficha, o responsável humano deve conseguir imaginar a explicação, avaliar seu interesse e julgar se as mídias documentadas sustentam a demonstração, sem precisar escrever o roteiro por conta própria. Se faltarem evidências para uma referência visual específica, registrar a lacuna ou reformular a proposta; não preencher o vazio com uma afirmação não documentada.


## 8. Diretrizes editoriais compartilhadas — valores iniciais, não imposições

- Destino pretendido: vídeo curto vertical 9:16, referência técnica de 1080 × 1920 e 30 fps.
- Duração exploratória: 40 a 80 segundos, com ~60 segundos como ponto de partida; exceções exigem decisão explícita.
- Abertura preferencialmente interrogativa; demonstração visual e conclusão que responda ao gancho.
- Não transformar o Short em leitura literal de slides; o material deve apoiar a explicação.
- Vídeo-guia com voz provisória e **sem legendas incorporadas**. A gravação humana é a referência para legendas finais.
- Manter cenas/segmentos editáveis para ajuste de duração após gravação humana, sem alteração silenciosa do sentido.
- Preservar arquivos originais; recortes e ampliações não podem ocultar elementos essenciais sem aprovação.

Esses valores não devem ser copiados em cada dossiê. O contrato aprovado fixa os valores reais de cada vídeo.

## 9. Passagem do candidato para o contrato de produção

A ficha aprovada deve originar **uma especificação independente por vídeo** com: ID, versão, fontes, aprovação, formato e duração, narração final do vídeo-guia, segmentos, mídias existentes/derivadas, sequência de cenas, tempos em frames, enquadramento, animações, transições, áudio e política de legendas.

**A especificação não admite:** hooks alternativos, `A_DEFINIR`, instruções vagas como “melhorar visual”, mídias não verificadas ou operações não definidas no vocabulário do renderizador.

Fluxo previsto: `Markdown aprovado → validador → plano JSON → renderizador → vídeo-guia`. O JSON e o MP4 são **derivados**, não fontes concorrentes de verdade. A gramática exata do contrato e o vocabulário fechado do renderizador serão definidos em protocolo técnico próprio; **não estão homologados nesta versão**.

A validação deve rejeitar, com diagnóstico: ausência de aprovação, arquivo inexistente/ilegível, campos obrigatórios vazios, tempos inválidos ou descontínuos, operações desconhecidas e duração fora do intervalo aprovado. **Nunca escolher silenciosamente** mídia, transição, voz ou conteúdo.

## 10. Narração humana e remontagem

A locução sintética do vídeo-guia é **referência de ritmo**, não texto a ser lido obrigatoriamente. A gravação humana pode ser feita em trechos. A montagem final pode adaptar a duração de cada cena à fala real, preservando sequência e propósito; alterações substantivas exigem aceite editorial. Gerar legendas **após** receber o áudio humano definitivo.

## 11. Versionamento e evolução do protocolo

- Alterações apenas de esclarecimento: incrementar versão de correção.
- Novos campos opcionais ou novas etapas compatíveis: incrementar versão menor.
- Mudanças incompatíveis de campos, estados ou significado: incrementar versão maior e documentar migração.
- Cada dossiê declara a versão do protocolo que utiliza. Dossiês anteriores não são reescritos automaticamente.
- A autorização explícita para executar a tarefa de geração ou implementação abrange commit, push e abertura de PR, salvo restrição expressa, conforme `AGENTS.md`. Não solicitar aprovações adicionais para operações Git rotineiras dentro do escopo autorizado. A aprovação editorial isolada não autoriza implementar mudanças fora do escopo; a abertura do PR não autoriza merge.

## 12. Histórico de evolução

- `0.1.0`: estrutura dos dossiês, estados, separação entre editorial e contrato de produção.
- `0.2.0` (proposta): roteirização documental por padrão; fontes e política de confiança; classificação das afirmações; solicitação excepcional de mídias; validação física deslocada à produção; bloqueio de contrato executável com pendências.
- `0.2.1` (proposta): remoção de conteúdo específico do candidato V01-003; o protocolo permanece universal, com referências particulares mantidas exclusivamente nos dossiês.

- `0.2.2` (homologada por decisão humana): exigência de narrativa preliminar falável, storyboard editorial suficientemente desenvolvido e variedade substantiva de abordagens, sem alterar a política de confiança documental ou antecipar decisões do contrato de produção.
- `0.2.3` (homologada, revisão operacional): atualização dos caminhos dos artefatos, alinhamento com a autorização Git do `AGENTS.md` e delimitação do uso do dossiê piloto como referência de apresentação; sem alteração das exigências editoriais da 0.2.2.
