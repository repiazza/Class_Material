# Checklist de curadoria

## Escopo e origem

Registro inicial consolidado na Etapa 07 a partir das Etapas 03–06C e da deliberação humana da Etapa 05. Módulo auditado: `01_Logica_e_Raciocinio`. Os IDs originais 01–14 são preservados; a chave estável usa `M01-XX` para evitar colisões futuras.

A auditoria examinou oito PNGs, quatro GIFs (todos os 14 quadros) e dois Markdown. Classificação relatada: A para a inspeção de conteúdo. A qualidade de uma edição gráfica posterior exige validação própria e aprovação humana.

P1: erro demonstrado; P2: ambiguidade relevante; P3: melhoria opcional ou investigação. Aprovação conceitual não autoriza execução. Ausência de manifestação significa PENDENTE. Nenhuma proposta foi rejeitada na deliberação registrada.

## Limites de execução e integração

- Proposta 08: execução autorizada na Etapa 06A e commit exclusivo autorizado na Etapa 07. A deliberação atual da Etapa 08 autoriza publicar esse commit e abrir PR; merge permanece sob decisão humana.
- Propostas 01/02: apenas protótipo temporário autorizado na Etapa 06C; nenhuma substituição do original foi autorizada.
- Propostas 04/05/07: aprovadas conceitualmente, sem autorização de implementação.
- Propostas 03/06/09/10/11: pendentes; não executar.
- Propostas 12/13/14: preservação aprovada; não constituem autorização de edição.
- Na Etapa 07, este checklist e `AGENTS.md` foram autorizados apenas para criação. A deliberação atual da Etapa 08 autoriza atualizá-los, criar um commit específico e publicá-lo em PR junto à proposta 08. A restrição anterior de não comitar governança foi superada por essa autorização.

O protótipo 01/02 foi criado em `/tmp/modulo01-candidata/`, fora do checkout. Preservação técnica relatada: PNG RGB 1312 × 1199, 9.856 pixels alterados, zero fora das máscaras [240,611,413,630) e [634,1098,934,1121). Classificação B: diferenças de tipografia e espaçamento requerem ajustes. O original contém bloco caBX com marcador C2PA; a candidata não o transfere e não possui proveniência C2PA válida demonstrada. O usuário não conseguiu visualizar as imagens na interface; entrega visual e aprovação humana continuam pendentes. Arquivos temporários não são registros duráveis nem devem ser incluídos no Git.

## M01-01 — observação original 01

- **Módulo:** `01_Logica_e_Raciocinio`.
- **Arquivo(s):** problemas_condicoes4.png (relativos ao módulo).
- **Classificação:** Erro.
- **Evidência:** No segundo exemplo NOT, a frase diz “é falso” enquanto apresenta p = F e ¬p = V.
- **Correção ou ação proposta:** Trocar “é falso” por “é verdadeiro”, mantendo os resultados simbólicos.
- **Prioridade:** P1.
- **Estado da deliberação:** APROVADA.
- **Justificativa humana:** Corrigir contradição textual na operação NOT.
- **Autorização de execução:** Somente protótipo temporário autorizado; substituição do PNG NÃO autorizada.
- **Estado da implementação:** Protótipo produzido fora do checkout; original não modificado.
- **Estado da validação:** Comparação técnica demonstrada; qualidade visual classificada B pelo agente. Inspeção e aprovação visual humanas pendentes por falha de disponibilização.
- **Estado da integração Git:** Não integrado; nenhuma alteração gráfica commitada. Não incluir o protótipo.

## M01-02 — observação original 02

- **Módulo:** `01_Logica_e_Raciocinio`.
- **Arquivo(s):** problemas_condicoes4.png (relativos ao módulo).
- **Classificação:** Erro.
- **Evidência:** O resumo informa “Quando inverte o valor da proposição” na coluna “Quando é verdadeiro” de NOT.
- **Correção ou ação proposta:** Usar “Quando a proposição de entrada é falsa”.
- **Prioridade:** P1.
- **Estado da deliberação:** APROVADA.
- **Justificativa humana:** Corrigir a definição da condição de verdade de NOT.
- **Autorização de execução:** Somente protótipo temporário autorizado; substituição do PNG NÃO autorizada.
- **Estado da implementação:** Protótipo produzido fora do checkout; original não modificado.
- **Estado da validação:** Comparação técnica demonstrada; qualidade visual classificada B pelo agente. Inspeção e aprovação visual humanas pendentes por falha de disponibilização.
- **Estado da integração Git:** Não integrado; nenhuma alteração gráfica commitada. Não incluir o protótipo.

## M01-03 — observação original 03

- **Módulo:** `01_Logica_e_Raciocinio`.
- **Arquivo(s):** problemas_condicoes4.png (relativos ao módulo).
- **Classificação:** Ambiguidade.
- **Evidência:** p significa “Está chovendo” em NOT/AND e “Não está chovendo” na coluna OR.
- **Correção ou ação proposta:** Revisar conjuntamente os símbolos, expressões e cabeçalhos para manter a consistência; nenhuma alteração autorizada.
- **Prioridade:** P2.
- **Estado da deliberação:** PENDENTE.
- **Justificativa humana:** A alteração dos símbolos exige revisão conjunta da imagem para preservar a consistência das expressões e tabelas.
- **Autorização de execução:** Execução não autorizada.
- **Estado da implementação:** NÃO IMPLEMENTADA.
- **Estado da validação:** Evidência da auditoria registrada; nenhuma versão corrigida implementada ou validada.
- **Estado da integração Git:** Sem alteração a integrar.

## M01-04 — observação original 04

- **Módulo:** `01_Logica_e_Raciocinio`.
- **Arquivo(s):** problemas_condicoes2.png; logica_booleana3.png (relativos ao módulo).
- **Classificação:** Ambiguidade.
- **Evidência:** O exemplo da chuva apresenta quatro linhas com p, q e r, enquanto a contagem com três entradas livres apresenta oito.
- **Correção ou ação proposta:** Explicitar que r é resultado determinado no exemplo da chuva e variável livre no exemplo de contagem.
- **Prioridade:** P2.
- **Estado da deliberação:** APROVADA.
- **Justificativa humana:** Diferenciar entradas independentes de resultados derivados.
- **Autorização de execução:** Execução não autorizada.
- **Estado da implementação:** NÃO IMPLEMENTADA.
- **Estado da validação:** Evidência da auditoria registrada; nenhuma versão corrigida implementada ou validada.
- **Estado da integração Git:** Sem alteração a integrar.

## M01-05 — observação original 05

- **Módulo:** `01_Logica_e_Raciocinio`.
- **Arquivo(s):** logica_booleana3.png (relativos ao módulo).
- **Classificação:** Ambiguidade.
- **Evidência:** O texto diz que duas variáveis assumem “4 valores” e três “8 valores”; as tabelas representam combinações.
- **Correção ou ação proposta:** Substituir por quatro e oito combinações, mantendo cada variável com dois valores.
- **Prioridade:** P2.
- **Estado da deliberação:** APROVADA.
- **Justificativa humana:** Corrigir a terminologia referente às combinações de valores.
- **Autorização de execução:** Execução não autorizada.
- **Estado da implementação:** NÃO IMPLEMENTADA.
- **Estado da validação:** Evidência da auditoria registrada; nenhuma versão corrigida implementada ou validada.
- **Estado da integração Git:** Sem alteração a integrar.

## M01-06 — observação original 06

- **Módulo:** `01_Logica_e_Raciocinio`.
- **Arquivo(s):** problema_condicoes.png; problemas_condicoes2.png; problemas_condicoes5.png; logica_booleana.png (relativos ao módulo).
- **Classificação:** Ambiguidade.
- **Evidência:** No modelo da chuva, possuir guarda-chuva basta para sair sem se molhar; uso e eficácia estão implícitos.
- **Correção ou ação proposta:** Avaliar a inclusão de uma premissa curta na apresentação inicial, sem alterar tabelas.
- **Prioridade:** P2.
- **Estado da deliberação:** PENDENTE.
- **Justificativa humana:** Avaliar se a explicitação das hipóteses acrescenta clareza suficiente para justificar a alteração.
- **Autorização de execução:** Execução não autorizada.
- **Estado da implementação:** NÃO IMPLEMENTADA.
- **Estado da validação:** Evidência da auditoria registrada; nenhuma versão corrigida implementada ou validada.
- **Estado da integração Git:** Sem alteração a integrar.

## M01-07 — observação original 07

- **Módulo:** `01_Logica_e_Raciocinio`.
- **Arquivo(s):** logica_booleana.png (relativos ao módulo).
- **Classificação:** Ambiguidade.
- **Evidência:** A introdução associa a representação 1/0 à definição de lógica booleana; a implementação é resumida como estados elétricos ligado/desligado.
- **Correção ou ação proposta:** Distinguir valores lógicos, representação 1/0 e níveis físicos de sinais, preservando a ponte didática para computação.
- **Prioridade:** P2.
- **Estado da deliberação:** APROVADA.
- **Justificativa humana:** Distinguir lógica booleana, representação binária e implementação física.
- **Autorização de execução:** Execução não autorizada.
- **Estado da implementação:** NÃO IMPLEMENTADA.
- **Estado da validação:** Evidência da auditoria registrada; nenhuma versão corrigida implementada ou validada.
- **Estado da integração Git:** Sem alteração a integrar.

## M01-08 — observação original 08

- **Módulo:** `01_Logica_e_Raciocinio`.
- **Arquivo(s):** exercicio.md; gabarito.md (relativos ao módulo).
- **Classificação:** Ambiguidade.
- **Evidência:** “Acesso livre” ainda exige uma condição; o solicitante e o caráter alternativo das políticas não estavam suficientemente delimitados.
- **Correção ou ação proposta:** Apresentar políticas alternativas A/B para um aluno solicitante e harmonizar os nomes no exercício e gabarito, sem ampliar o escopo.
- **Prioridade:** P2.
- **Estado da deliberação:** APROVADA.
- **Justificativa humana:** Esclarecer o contexto do exercício, preservando seu objetivo e suas respostas.
- **Autorização de execução:** Execução autorizada na Etapa 06A; commit exclusivo autorizado na Etapa 07.
- **Estado da implementação:** IMPLEMENTADA nos dois Markdown autorizados; contexto de aluno solicitante e políticas A/B harmonizado.
- **Estado da validação:** VALIDADA na Etapa 06A e novamente antes do commit: questões correspondentes, respostas e critérios preservados; expressões e tabelas idênticas; git diff --check passou.
- **Estado da integração Git:** Commit local criado: `def2abf391bb985847b4fd08edb1e77102a0d610` — `docs(modulo-01): esclarece politicas de acesso no exercicio`. Somente exercicio.md e gabarito.md; 18 inserções e 18 exclusões. Publicação em branch e abertura de PR autorizadas na Etapa 08; merge não autorizado. O registro de operações abaixo distingue autorização de realização.

## M01-09 — observação original 09

- **Módulo:** `01_Logica_e_Raciocinio`.
- **Arquivo(s):** exercicio.md (relativos ao módulo).
- **Classificação:** Lacuna de cobertura avaliativa, não defeito do objetivo atual.
- **Evidência:** O exercício avalia AND/OR; não avalia diretamente NOT, XOR ou expressões compostas presentes no módulo.
- **Correção ou ação proposta:** Manter o escopo atual. Não ampliar somente para abranger todo o módulo; eventual revisão exige deliberação específica.
- **Prioridade:** P3.
- **Estado da deliberação:** PENDENTE.
- **Justificativa humana:** Não ampliar o exercício apenas para abranger todo o módulo. Preservar seu escopo atual.
- **Autorização de execução:** Execução não autorizada.
- **Estado da implementação:** NÃO IMPLEMENTADA.
- **Estado da validação:** Evidência da auditoria registrada; nenhuma versão corrigida implementada ou validada.
- **Estado da integração Git:** Sem alteração a integrar.

## M01-10 — observação original 10

- **Módulo:** `01_Logica_e_Raciocinio`.
- **Arquivo(s):** p_xor_q.gif; logica_booleana2.png (relativos ao módulo).
- **Classificação:** Lacuna de articulação pedagógica.
- **Evidência:** O GIF XOR é correto, mas a síntese estática não compara explicitamente OR e XOR no caso de duas entradas verdadeiras.
- **Correção ou ação proposta:** Considerar futuramente comparação breve OR/XOR; não ampliar o exercício nem modificar o GIF.
- **Prioridade:** P3.
- **Estado da deliberação:** PENDENTE.
- **Justificativa humana:** Comparação OR/XOR é opcional e não constitui correção necessária.
- **Autorização de execução:** Execução não autorizada.
- **Estado da implementação:** NÃO IMPLEMENTADA.
- **Estado da validação:** Evidência da auditoria registrada; nenhuma versão corrigida implementada ou validada.
- **Estado da integração Git:** Sem alteração a integrar.

## M01-11 — observação original 11

- **Módulo:** `01_Logica_e_Raciocinio`.
- **Arquivo(s):** Todos os PNGs e GIFs do módulo 01 (relativos ao módulo).
- **Classificação:** Melhoria.
- **Evidência:** PNGs têm vários painéis e GIFs avançam a cada três segundos; não houve teste com estudantes ou dispositivos específicos.
- **Correção ou ação proposta:** Investigar legibilidade e ritmo com o público antes de alterar diagramação ou duração.
- **Prioridade:** P3.
- **Estado da deliberação:** PENDENTE.
- **Justificativa humana:** Alterações de legibilidade e ritmo dependem de evidências adicionais.
- **Autorização de execução:** Execução não autorizada.
- **Estado da implementação:** NÃO IMPLEMENTADA.
- **Estado da validação:** Evidência da auditoria registrada; nenhuma versão corrigida implementada ou validada.
- **Estado da integração Git:** Sem alteração a integrar.

## M01-12 — observação original 12

- **Módulo:** `01_Logica_e_Raciocinio`.
- **Arquivo(s):** problemas_condicoes5.png; logica_booleana.png; logica_booleana2.png (relativos ao módulo).
- **Classificação:** Ponto positivo.
- **Evidência:** Colunas intermediárias e representações V/F e 1/0 permitem acompanhar e conferir o cálculo.
- **Correção ou ação proposta:** Manter as explicações intermediárias e a correspondência V/F–1/0.
- **Prioridade:** Preservação.
- **Estado da deliberação:** APROVADA — PRESERVAÇÃO.
- **Justificativa humana:** Manter as explicações intermediárias e a correspondência V/F–1/0.
- **Autorização de execução:** Preservação aprovada; sem autorização de alteração própria.
- **Estado da implementação:** Preservação mantida; nenhuma edição própria necessária.
- **Estado da validação:** Característica examinada na auditoria inicial; preservada nas alterações da proposta 08.
- **Estado da integração Git:** Sem alteração própria a integrar; não confundir preservação com execução de correção.

## M01-13 — observação original 13

- **Módulo:** `01_Logica_e_Raciocinio`.
- **Arquivo(s):** not_p.gif; p_and_q.gif; p_or_q.gif; p_xor_q.gif (relativos ao módulo).
- **Classificação:** Ponto positivo.
- **Evidência:** Todos os 14 quadros foram inspecionados: NOT 2, AND 4, OR 4 e XOR 4; os resultados estão corretos.
- **Correção ou ação proposta:** Manter os GIFs e suas demonstrações.
- **Prioridade:** Preservação.
- **Estado da deliberação:** APROVADA — PRESERVAÇÃO.
- **Justificativa humana:** Manter os GIFs e suas demonstrações.
- **Autorização de execução:** Preservação aprovada; sem autorização de alteração própria.
- **Estado da implementação:** Preservação mantida; nenhuma edição própria necessária.
- **Estado da validação:** Característica examinada na auditoria inicial; preservada nas alterações da proposta 08.
- **Estado da integração Git:** Sem alteração própria a integrar; não confundir preservação com execução de correção.

## M01-14 — observação original 14

- **Módulo:** `01_Logica_e_Raciocinio`.
- **Arquivo(s):** gabarito.md (relativos ao módulo).
- **Classificação:** Ponto positivo.
- **Evidência:** Aceita identificadores alternativos, diferentes ordens das linhas e tabela conjunta; apresenta justificativas e erros frequentes.
- **Correção ou ação proposta:** Manter a flexibilidade dos critérios de correção.
- **Prioridade:** Preservação.
- **Estado da deliberação:** APROVADA — PRESERVAÇÃO.
- **Justificativa humana:** Manter a flexibilidade dos critérios de correção do gabarito.
- **Autorização de execução:** Preservação aprovada; sem autorização de alteração própria.
- **Estado da implementação:** Preservação mantida; nenhuma edição própria necessária.
- **Estado da validação:** Característica examinada na auditoria inicial; preservada nas alterações da proposta 08.
- **Estado da integração Git:** Sem alteração própria a integrar; não confundir preservação com execução de correção.

## Próxima auditoria

Módulos 02–10: não auditados integralmente nesta etapa. Leituras pontuais anteriores para estabelecer relações não equivalem a auditoria. Iniciar apenas após autorização, um módulo por vez, com inspeção real de cada material, evidências localizadas, avaliação de exercícios/gabaritos e recomendações submetidas à deliberação humana. Nenhuma sequência pedagógica obrigatória é inferida da numeração.

## Etapa 08 — autonomia operacional e publicação

- **Deliberação vigente:** a implementação de um conjunto aprovado abrange verificações, correção de problemas técnicos introduzidos, commits, organização de branches, push e abertura de PR, salvo restrição explícita. Aprovação conceitual isolada continua sem autorizar edição. Merge não é automático.
- **Estado remoto verificado:** PR #1 integrado à main no commit `85186373c1059a923efdbcf2dd9a2778a379b7aa`, incluindo inventário e README. Esse avanço é conhecido e não impede a publicação atual.
- **Histórico preservado:** commit da proposta 08 `def2abf391bb985847b4fd08edb1e77102a0d610`; sem rebase, force-push ou reescrita.
- **Escopo de publicação:** proposta 08 nos dois Markdown e commit separado de `AGENTS.md` e deste checklist. Nenhum PNG, GIF ou protótipo será incluído.
- **Estado operacional ao preparar o commit:** governança atualizada e validada; commit, push e abertura de PR autorizados e ainda não concluídos nesse ponto. Os resultados posteriores serão informados na conversa e no PR; esta autorização não é evidência de execução.
- **Pendências preservadas:** 01/02 sem aprovação visual humana ou substituição do original; 04/05/07 aprovadas conceitualmente sem implementação autorizada; 03/06/09/10/11 pendentes; 12/13/14 preservação.
- **Próximo controle humano:** revisão do PR e decisão sobre integração. Não iniciar novas alterações pedagógicas nesta etapa.
