# Regras operacionais de curadoria

## Inventário e catálogos semânticos

- Consulte `inventario.csv` para identificar os arquivos presentes em cada módulo. Preserve o separador `;` e as colunas `modulo` e `arquivo`; não acrescente campos, substitua identificadores estáveis ou descarte metadados existentes sem autorização para mudar o contrato.
- Consulte `NN_Catalogo_Semantico.docx` no módulo correspondente antes de interpretar semanticamente seus materiais. Os 12 catálogos são a fonte documental de referência para conteúdos, representações, exemplos, conceitos, palavras-chave e transições relevantes de GIFs.
- Consulte `curadoria/vocabulario_controlado.md` para a etiqueta canônica, definição consolidada, capítulos e materiais associados antes de classificar ou atualizar registros. Preserve os significados locais dos homônimos e as pendências ali documentadas; revisões do vocabulário e dos catálogos continuam restritas ao escopo autorizado.
- Relacione os registros documentais aos materiais físicos pelos nomes exatos dos arquivos e pelo módulo. Não confunda o catálogo com imagem, GIF, exercício, gabarito ou código: ele é um documento de referência e também possui entrada própria no inventário.
- Leia os DOCX com uma ferramenta que extraia o texto do corpo e das tabelas; se a leitura for parcial ou impossível, registre a limitação. Não alegue consulta apenas pela existência do arquivo.
- Respeite o vocabulário controlado cumulativo. Reutilize o termo estabelecido para o mesmo conceito, por exemplo `ponteiro`, sem criar etiquetas alternativas `pointer` ou `apontador`. Mantenha conceitos distintos separados e não normalize, unifique ou renomeie termos automaticamente.
- Não infira conteúdo visual ausente das descrições. Distinga conhecimento documentado, verificação física/integridade e inspeção visual; nenhum desses estados implica automaticamente os demais.
- Os catálogos não substituem os arquivos originais nem comprovam sua correção. Quando a tarefa exigir confirmação visual ou houver dúvida sobre uma descrição, examine o original e os quadros relevantes dos GIFs; informe o que foi efetivamente verificado.
- Não modifique os catálogos automaticamente. Relate separadamente divergências semânticas, referências quebradas, inconsistências documentais e propostas pedagógicas para avaliação humana, sem alterar materiais para fazê-los corresponder ao catálogo.

## Relacionamentos conceituais entre capítulos

- Quando a tarefa envolver relações entre conceitos ou materiais de capítulos diferentes, consulte `curadoria/relacionamentos_conceituais.md`, incluindo o laudo e as ressalvas de cada RC.
- O mapa é uma fonte documental auxiliar de 26 relações homologadas pedagogicamente por decisão humana: 23 APROVADAS e RC-014, RC-023 e RC-024 APROVADAS COM RESSALVAS, cujos limites de interpretação devem ser respeitados integralmente. Os catálogos e o vocabulário mestre continuam sendo as fontes primárias para conteúdos e conceitos. A homologação pedagógica não modifica a fundamentação documental: 23 relações continuam sustentadas e RC-014, RC-023 e RC-024 continuam plausíveis. Não deduza aprovação pedagógica de uma classificação documental em futuras relações.
- Preserve os cinco tipos e seus significados, os IDs RC, as direções e as justificativas. A direção não define necessariamente ordem de estudo; etiquetas coincidentes não comprovam dependência pedagógica.
- Distinga relações sustentadas, plausíveis dependentes de interpretação e insuficientemente fundamentadas. Não infira conteúdo visual que não esteja documentado nas fontes.
- A homologação destas relações não autoriza alterações automáticas nos materiais nem a criação de novas relações e não substitui autorizações humanas específicas. Não reclassifique, inverta, acrescente, exclua ou homologue relações sem autorização específica; relate divergências para avaliação.

## Inspeção e evidências

- Inspecione o conteúdo real dos materiais. A existência de um arquivo não prova sua correção.
- Em auditorias visuais ou tarefas que exijam confirmação direta, examine PNGs e quadros suficientes dos GIFs para compreender sua evolução; registre limites de inspeção. A consulta ao catálogo, por si só, não constitui validação visual.
- Distinga erros objetivos de escolhas pedagógicas, hipóteses e sugestões. Fundamente recomendações em evidências verificáveis.
- Não recomende remoções apenas por semelhança ou repetição de assunto; avalie a contribuição pedagógica.
- Preserve o propósito didático dos exercícios. Não presuma que a numeração de arquivos ou módulos estabelece uma sequência pedagógica obrigatória.

## Deliberação e autorização humana

- Registre as propostas em `curadoria/checklist.md`, com identificadores estáveis e estado APROVADA, REJEITADA, PENDENTE ou APROVADA — PRESERVAÇÃO.
- Ausência de manifestação significa PENDENTE. Preserve as justificativas humanas e não interprete rejeição como pedido de alternativa.
- Aprovação conceitual não autoriza modificação de arquivos. A implementação exige autorização textual explícita, identificando propostas e escopo permitido. Após essa autorização, execute autonomamente as operações técnicas e de publicação necessárias, sem pedir aprovação para cada comando.
- Não execute propostas pendentes ou rejeitadas nem amplie o escopo autorizado.

## Edição e validação

- Preserve os originais até que sua substituição seja autorizada. Protótipos não aprovados devem ficar fora do checkout.
- Não modifique materiais fora do escopo e não amplie exercícios sem aprovação.
- Verifique a correspondência entre exercício e gabarito e preserve os critérios de correção autorizados.
- Para imagens, distinga validação técnica de validação visual. Não integre imagens cuja qualidade visual não tenha aprovação humana.
- Arquivo disponível na máquina não significa arquivo acessível ao usuário. Não considere concluída a avaliação visual quando a entrega não permitir inspeção.
- Confira alterações preexistentes antes de editar, preserve-as e diferencie-as do trabalho atual. Apresente mudanças e verificações realizadas.

## Integração Git

Distinga e registre: (1) proposta aprovada; (2) execução autorizada; (3) alteração implementada; (4) alteração validada; (5) commit criado; (6) push realizado; (7) PR aberto; (8) PR integrado.

- Dentro de um conjunto autorizado para implementação, crie commits coerentes, organize branches, realize push e abra PRs autonomamente. A autorização de implementação abrange essas operações, salvo restrição explícita do usuário.
- A abertura de PR não autoriza merge. A revisão, aprovação, rejeição e decisão de integração pertencem ao responsável humano; não realize merge automaticamente.
- Sinalize explicitamente alterações validadas ainda sem commit, commits locais sem push e PRs ainda não integrados.
- Prefira commits coerentes e PRs com escopo delimitado. Confira o diff, os arquivos preparados e `git diff --check` antes do commit.
- Não inclua protótipos, arquivos temporários ou materiais fora do escopo aprovado nos commits. Documentos de governança podem ser publicados quando abrangidos pelo escopo autorizado.
- Mudanças esperadas no histórico remoto e operações Git rotineiras não exigem nova deliberação se preservarem o escopo. Não realize rebase, force-push ou reescrita de histórico sem necessidade técnica demonstrada; o avanço da main, isoladamente, não é motivo.
- Use o checkout existente: tarefas de nuvem já são isoladas. Não crie worktrees sem solicitação explícita.

## Autonomia e limites

- Investigue materiais e apresente laudos fundamentados dentro do escopo solicitado, sem solicitar autorização por arquivo ou comando técnico.
- Após autorização de implementação, modifique os arquivos abrangidos, execute verificações e testes, corrija problemas técnicos introduzidos pela própria implementação e publique resultados e evidências em PRs delimitados.
- Solicite nova deliberação somente diante de conteúdo não aprovado, extrapolação do escopo, ambiguidade técnica ou pedagógica relevante, impossibilidade de execução ou validação, risco significativo de perda de conteúdo ou integridade, ou decisão editorial não contemplada.
- Concentre a supervisão humana nos laudos, decisões sobre propostas, prioridades pedagógicas e revisão dos PRs. Evite verificações redundantes e pedidos de autorização para operações rotineiras.

## Continuidade

Consulte `curadoria/checklist.md` antes de agir. O registro não substitui autorização. A auditoria deve ocorrer por módulo, dentro do escopo solicitado, com resultados apresentados para deliberação humana. Não inicie alterações pedagógicas ou auditorias adicionais fora desse escopo.
