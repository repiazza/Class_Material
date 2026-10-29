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


## Retroalimentação — capítulo 02 / reavaliação da PR #13

Base de governança consultada: `origin/main` no commit `e89cc0b`; `AGENTS.md` (blob `fbfd71129bd4f4cf869d0b8d2abc839dff4509e8`) e `curadoria/protocolo_retroalimentacao.md` (blob `3b07e05e4420a971c56acf2b949a0f775e9151dc`, estado declarado: protocolo operacional sujeito à homologação humana). Não se atribui número de versão inexistente. Aplicação expressamente solicitada pelo responsável humano nesta tarefa. Classificações D/P/V/G conforme o protocolo; o registro anterior permanece histórico.

Escopo autorizado: correções documentais objetivas mínimas no catálogo 02, registro neste checklist e publicação em PR independente. Nenhuma edição dos originais, mapas, dossiês, vocabulário, inventário ou governança normativa foi autorizada. A PR #13 permanece uma entrega espacial válida em avaliação, não automaticamente homologada.

As evidências abaixo remetem ao [relatório da PR #13](https://github.com/repiazza/Class_Material/blob/8bba787/02_Sistemas_de_Numeracao/evidencias_mapa_espacial/autoauditoria.md). Os 12 hashes dos originais foram reconferidos com o JSON dessa PR e permanecem iguais. Houve nova abertura dos originais questionados e dos seis quadros do GIF signed_unsigned; a inspeção anterior dos demais originais permanece aplicável a esses mesmos binários. Não se realizou nova auditoria geral do acervo.

### M02-RF-001 — PNG confundido documentalmente com exemplo do GIF

- **Classe:** D — divergência documental objetiva.
- **Capítulo / artefato:** `02_Sistemas_de_Numeracao/02_Catalogo_Semantico.docx`.
- **Responsável pela origem:** curadoria documental do catálogo.
- **Evidência:** Registro 10, `signed_unsigned.png`: o painel central mostra 1010, 10/−6, quatro bits; painel inferior direito contém declarações C e ressalva do modelo. Não há terminal nem exemplo 11111111 nesse PNG. O exemplo 255/−1 e o terminal aparecem em `signed_unsigned.gif`. A correspondência com o GIF é demonstrada; a causa histórica da troca é hipótese.
- **Antes:** Conteúdo apresentado: Contrasta tipos inteiros com e sem sinal em C e demonstra que a mesma sequência de bits pode representar números diferentes. Ilustra a leitura de 11111111 como 255 em unsigned e −1 em signed de 8 bits.
- **Depois:** Conteúdo apresentado: Contrasta interpretações com e sem sinal e demonstra que a mesma sequência de bits pode representar números diferentes. Ilustra a leitura de 1010 como 10 em unsigned e −6 em signed, em complemento de dois, no modelo didático de quatro bits; relaciona a interpretação aos tipos inteiros em C.
- **Antes:** Representação e exemplos: Trechos de código, representação visual de oito bits e saída de terminal.
- **Depois:** Representação e exemplos: Diagramas de quatro bits com setas, cálculo com peso negativo do MSB, tabelas comparativas de valores e faixas, e declarações signed char e unsigned char acompanhadas da ressalva do modelo didático de quatro bits.
- **Impacto / dependências:** As sete regiões desse PNG na PR #13 já descrevem o original correto; preservá-las. Palavras-chave byte/tipos C continuam sustentadas pelas notas sobre char e contexto real de oito bits; glossário e índice reverso não mudam. V02-005 do dossiê 02 atribui ao PNG o exemplo 11111111 e duas saídas; precisa de revisão documental delimitada antes de usar essa atribuição em roteiro/produção, sem alteração automática nesta tarefa.
- **Estado da deliberação:** APROVADA, no conjunto de correções documentais objetivas expressamente autorizado nesta solicitação; aprovação da integração permanece humana.
- **Autorização de implementação:** autorizada exclusivamente para descrição fiel do original, sem alteração pedagógica.
- **Implementação e validação:** correção aplicada; DOCX íntegro e reaberto, demais parágrafos e componentes preservados. Coordenadas e originais sem alteração.
- **Integração Git:** mudança preparada para commit e PR documental próprios; hashes/links de publicação serão informados na conversa e na descrição da PR. Este registro não presume publicação ou merge.

### M02-RF-002 — Comparação não exibida sobre quantidade e máximo

- **Classe:** D — divergência documental objetiva.
- **Capítulo / artefato:** `02_Sistemas_de_Numeracao/02_Catalogo_Semantico.docx`.
- **Responsável pela origem:** curadoria documental do catálogo.
- **Evidência:** Registro 05, `combinacao_bits.png`: fórmulas 2¹, 2², 2³, 2ⁿ, tabelas e conclusão de duplicação. Não há comparação explícita entre quantidade 2ⁿ e máximo 2ⁿ−1. Retirada somente a atribuição visual não sustentada; a distinção matemática continua válida em outros contextos.
- **Antes:** Conteúdo apresentado: Apresenta o crescimento do número de combinações de n bits pela expressão 2ⁿ. Exemplifica os casos de 1, 2 e 3 bits, chegando à fórmula geral e distinguindo quantidade de combinações de valor máximo.
- **Depois:** Conteúdo apresentado: Apresenta o crescimento do número de combinações de n bits pela expressão 2ⁿ. Exemplifica os casos de 1, 2 e 3 bits, chegando à fórmula geral e mostrando que cada bit adicional duplica o número de combinações.
- **Impacto / dependências:** As seis regiões desse arquivo descrevem contagem e duplicação corretamente e são preservadas. O dossiê V02-002 atribui essa distinção ao registro 05; exige revisão dessa atribuição, sem descartar a narrativa ou o candidato. Glossário/índice reverso não afetados.
- **Estado da deliberação:** APROVADA, no conjunto de correções documentais objetivas expressamente autorizado nesta solicitação; aprovação da integração permanece humana.
- **Autorização de implementação:** autorizada exclusivamente para descrição fiel do original, sem alteração pedagógica.
- **Implementação e validação:** correção aplicada; DOCX íntegro e reaberto, demais parágrafos e componentes preservados. Coordenadas e originais sem alteração.
- **Integração Git:** mudança preparada para commit e PR documental próprios; hashes/links de publicação serão informados na conversa e na descrição da PR. Este registro não presume publicação ou merge.

### M02-RF-003 — Progressão do GIF não altera os valores dos objetos

- **Classe:** D — divergência documental objetiva.
- **Capítulo / artefato:** `02_Sistemas_de_Numeracao/02_Catalogo_Semantico.docx`.
- **Responsável pela origem:** curadoria documental do catálogo.
- **Evidência:** Registro 11, `signed_unsigned.gif`, quadros 0–5: no quadro 0 a linha signed ainda não mostra os bits; no quadro 1 surge −1; quadro 2 compara os padrões; quadros 3 e 4 acrescentam 255 e −1 ao terminal; quadro 5 sintetiza. Os valores não mudam: há apresentação progressiva.
- **Antes:** Conteúdo apresentado: Compara a interpretação dos mesmos oito bits como unsigned e signed. Ao longo da animação, a representação binária permanece igual, mas o resultado numérico com sinal muda conforme a interpretação em complemento de dois.
- **Depois:** Conteúdo apresentado: Compara dois objetos de oito bits: unsigned char com valor 255 e signed char com valor −1, no modelo de complemento de dois. A animação apresenta progressivamente as representações, iguais a 11111111 quando ambas estão exibidas, destaca as linhas de código e acrescenta as saídas unsigned: 255 e signed: -1 ao terminal; os valores dos objetos não mudam.
- **Impacto / dependências:** As três regiões desse GIF mantêm vínculos semânticos corretos; caixas e evidências permanecem válidas. A descrição corrigida não remove o defeito de texto do quadro 2 (M02-RF-005). Glossário e índice reverso não afetados.
- **Estado da deliberação:** APROVADA, no conjunto de correções documentais objetivas expressamente autorizado nesta solicitação; aprovação da integração permanece humana.
- **Autorização de implementação:** autorizada exclusivamente para descrição fiel do original, sem alteração pedagógica.
- **Implementação e validação:** correção aplicada; DOCX íntegro e reaberto, demais parágrafos e componentes preservados. Coordenadas e originais sem alteração.
- **Integração Git:** mudança preparada para commit e PR documental próprios; hashes/links de publicação serão informados na conversa e na descrição da PR. Este registro não presume publicação ou merge.

### M02-RF-004 — Peso da posição 3 em msb_lsb.png

- **Classe:** P — inconsistência pedagógica do original; prioridade P1.
- **Capítulo / arquivo:** `02_Sistemas_de_Numeracao/msb_lsb.png`, linha Peso, coluna posição 3, aproximadamente x=575–670, y=400–505.
- **Evidência:** rótulo `2⁴` e valor `16` repetem a posição 4. Pela regra posicional já declarada no material, posição 3 tem `2³ = 8`. Conferência direta do original; evidência na PR #13, região `byte_extremos` e painel 19.
- **Responsável pela origem:** curadoria pedagógica e edição do PNG.
- **Proposta mínima:** substituir exclusivamente `2⁴` por `2³` e `16` por `8` na célula da posição 3; preservar tabela, demais valores, posições e setas. Não editar agora.
- **Impacto / dependências:** regiões `integral` e `byte_extremos`; demais regiões não são defeituosas por consequência automática. Defeito é P, não G: o recorte preserva exatamente o conteúdo errado da fonte.
- **Estado da deliberação:** PENDENTE. Autorização de implementação: NÃO concedida para o PNG. Implementação: não realizada.
- **Após eventual aprovação e edição:** conferir célula e preservação das demais áreas, atualizar SHA-256/dimensões no mapa, verificar caixas afetadas e renderizar/reinspecionar suas projeções. Rever descrição do catálogo apenas se a alteração exigir; não regenerar todo o mapa.

### M02-RF-005 — Texto encoberto no original signed_unsigned.gif

- **Classe:** P — defeito do original; prioridade P2.
- **Capítulo / arquivo:** `02_Sistemas_de_Numeracao/signed_unsigned.gif`, quadro de índice 2 (passo 3 de 6), faixa explicativa inferior esquerda, aproximadamente y=645–680; encobrimento à direita pelo painel do terminal em x≈815.
- **Evidência:** frase legível até “Os dois objetos apresentam o mesmo padrão de 8 bits neste mo…”; o restante já está encoberto no original completo. Os quadros 0–5 foram reabertos. [Quadro original registrado na PR #13](https://github.com/repiazza/Class_Material/blob/8bba787/02_Sistemas_de_Numeracao/evidencias_mapa_espacial/original_signed_unsigned_quadro02.png).
- **Responsável pela origem:** geração/edição da animação original.
- **Encaminhamento:** submeter à aprovação a redisposição da frase dentro do painel (por exemplo, quebra de linha), preservando os demais elementos e estados. Não completar o texto oculto por conjectura: recuperar o texto integral na fonte editável ou deliberar a redação antes da edição.
- **Impacto / dependências:** regiões `integral` e `codigo_contexto`; `bits_terminal` não recebe automaticamente o defeito do painel esquerdo. Classificação P, não falha do enquadramento.
- **Estado da deliberação:** PENDENTE. Autorização de implementação: NÃO concedida para o GIF. Implementação: não realizada.
- **Após eventual aprovação e edição:** verificar todos os estados alterados, duração/ordem/loop, integridade da frase e painéis, hash e dimensões; atualizar metadados do mapa e renderizar/reinspecionar apenas regiões afetadas, recalculando caixas somente se o leiaute mudar.

### M02-RF-006 — Ressalvas visuais previstas, sem bloqueio espacial

- **Classe:** V — observações aceitas pela política de preservação.
- **Arquivos / ocorrências:** visões `integral` dos 12 materiais; `tabela_nibble` de sistemas_representacao_numerica2.png; `ideia_principal` de combinacao_bits.png; `definicao`/`explicacao_resumo` de msb_lsb.png; `reta_nibble` e fragmento lateral em `linguagem_c` de signed_unsigned2.png; pequenas margens dos painéis contíguos. IDs e evidências estão no relatório da PR #13.
- **Evidência e justificativa:** unidades horizontais e quadros inteiros preservam contexto; margens e resíduo de painel vizinho evitam perda de títulos, texto ou relações. Visão geral reduzida não promete leitura detalhada de cada painel. O fragmento lateral de linguagem C decorre de contorno irregular; um corte mais justo removeria conteúdo principal.
- **Responsável:** curadoria espacial; nenhuma intervenção corretiva necessária nestes casos.
- **Estado da deliberação:** APROVADA — PRESERVAÇÃO, conforme instrução expressa de preservar os acertos e não refazer recortes por estética. Não equivale à homologação integral da PR #13.
- **Ação / impacto:** manter coordenadas e projeções; não classificar V como pendência impeditiva. A amostragem temporal dos GIFs continua sendo limite de cobertura declarado, não defeito geométrico demonstrado. As ocorrências P dos mesmos arquivos continuam independentes.

### M02-RF-007 — Defeitos de exportação/recorte já corrigidos na PR #13

- **Classe:** G para as duas bordas cortadas; a colisão de nomes das evidências foi falha técnica de rastreabilidade, não defeito dos originais.
- **Arquivos / regiões:** contagem_0_a_15.gif / `contagem_e_calculo`; contagem_0_a_15_hexa.gif / `tres_representacoes`; evidência `integral` de signed_unsigned.png colidia com a do GIF.
- **Evidência / correção existente:** caixas ampliadas de [32,225,1325,826] para [30,220,1370,835], reexportadas e reinspecionadas na PR #13; nomes finais incluem extensão png/gif. Comparações antes/depois e validação pixel a pixel estão no relatório dessa PR. Não se reintroduziu nem repetiu a correção.
- **Responsável:** curadoria espacial / exportação de evidências.
- **Estado da deliberação:** APROVADA — PRESERVAÇÃO do trabalho corrigido, conforme solicitação atual; integração/homologação global da PR #13 continuam humanas.
- **Implementação / revalidação:** correção técnica concluída na PR #13, commit `8bba787`. Nenhum defeito G remanescente demonstrado nesta reavaliação. Coordenadas e evidências não alteradas nesta PR documental.

### M02-RF-008 — Glifos sobrepostos na lista hexadecimal

- **Classe:** P — possível defeito de acabamento do original, sem decisão pedagógica automática; prioridade P3.
- **Arquivo / evidência:** sistemas_representacao_numericas.png, painel “Outros sistemas numéricos”, linha hexadecimal: glifos próximos de 5/6 aparecem sobrepostos/duplicados no próprio original, conforme laudo da PR #13. Não é corte causado pelo mapa.
- **Responsável / encaminhamento:** curadoria geradora do PNG; investigar a fonte gráfica para confirmar a redação e necessidade de ajuste. Não escolher correção por suposição.
- **Impacto:** regiões `integral` e `outros_sistemas`; preservar caixas. Não bloqueia a integração do mapa; exige atenção se essa lista for usada para ensino dos símbolos.
- **Estado da deliberação:** PENDENTE; edição do original não autorizada e não executada.

### Conclusão da reavaliação da PR #13

As 67 regiões e seus vínculos foram confrontados com as descrições atuais/corrigidas e os mesmos binários originais. Mudaram quatro parágrafos de três registros do catálogo, sem alteração de nomes, etiquetas, glossário ou índice reverso. Os sete IDs de signed_unsigned.png, seis de combinacao_bits.png e três de signed_unsigned.gif continuam descrevendo as unidades efetivamente presentes; as coordenadas não dependem dos exemplos incorretamente atribuídos pelo catálogo. A PR #13 e seus 113 arquivos permanecem byte a byte intocados nesta execução.

As quatro pendências anteriormente contadas no relatório espacial são duas ocorrências P em quatro regiões (M02-RF-004 e 005), não quatro defeitos geométricos. O relatório e o campo de confiança do JSON da PR #13 são registros históricos dessa autoauditoria; este checklist fornece a classificação por origem sem apagar evidências ou afirmar que os originais foram corrigidos. As observações V não impedem integração. Recomenda-se que a revisão humana possa aprovar/integrar a entrega espacial independentemente das correções P e da PR documental, mantendo tais limites explícitos. Isso não libera o uso pedagógico de uma célula incorreta ou de texto encoberto nem declara GERADO_OK de produção audiovisual.

Revalidação atual: pré-integração da correção documental, limitada à semântica e integridade. Após aprovação/integração desta PR, conferir que o catálogo publicado contém estes quatro parágrafos e retomar os derivados realmente afetados; não reconstruir mapas/dossiês por padrão. V02-002 e V02-005 permanecem sinalizados para revisão das atribuições documentais, sem edição nesta execução. Não foi identificado roteiro individual existente do capítulo 02 a atualizar.
