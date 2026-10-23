# Regras operacionais de curadoria

## Inspeção e evidências

- Inspecione o conteúdo real dos materiais. A existência de um arquivo não prova sua correção.
- Examine visualmente PNGs e quadros suficientes dos GIFs para compreender sua evolução; registre limites de inspeção.
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
