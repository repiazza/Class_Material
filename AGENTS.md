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
- Não modifique os catálogos silenciosamente. Divergências documentais objetivas seguem `curadoria/protocolo_retroalimentacao.md`: inspeção do original, proposta verificável e, **somente com autorização explícita de implementação**, correção documental delimitada em PR, sem merge automático. Nunca altere materiais originais para fazê-los corresponder ao catálogo.

### Integridade das referências visuais nos catálogos

- Na criação ou revisão dos catálogos semânticos, confronte as descrições com os arquivos originais, verificando a correspondência entre os elementos didáticos mencionados e aqueles efetivamente presentes nas imagens e GIFs.
- Preserve a estrutura e os campos existentes dos catálogos. Acrescente `Referências visuais verificadas` somente quando necessário para documentar elementos relevantes, sequências de animação ou limitações que possam comprometer a interpretação do material.
- Diferencie conceitos explicados de elementos efetivamente exibidos. Não afirme a presença de tabelas, expressões, diagramas, destaques ou outros recursos visuais sem confirmação no arquivo original.
- Para GIFs, documente a sequência de estados ou acontecimentos relevantes à compreensão pedagógica, quando a descrição existente não for suficiente. Não é necessária uma descrição exaustiva de todos os quadros.
- Priorize descrições concisas, sem repetir informações já registradas. O objetivo é permitir a seleção e a referência às mídias durante a roteirização sem exigir nova inspeção visual.
- Registre divergências e lacunas para deliberação humana, aplicando `curadoria/protocolo_retroalimentacao.md` quando couber. Não altere os materiais originais nem corrija silenciosamente inconsistências pedagógicas.

### Geração autônoma de dossiês editoriais

Quando solicitado a criar um dossiê editorial para determinado capítulo, execute a geração autonomamente, seguindo `curadoria/protocolo_roteirizacao.md` e as regras deste arquivo.

**Localização das fontes**

1. Identifique o diretório do capítulo pelo prefixo numérico `NN_`.
2. Consulte `inventario.csv` e o catálogo `NN_Catalogo_Semantico.docx` localizado no diretório correspondente.
3. Consulte `curadoria/vocabulario_controlado.md` e `curadoria/relacionamentos_conceituais.md` para fundamentar conceitos e identificar oportunidades de conexão entre capítulos.
4. Quando uma proposta depender de elementos específicos de outro capítulo, consulte também seu catálogo semântico.
5. Utilize exclusivamente fontes documentais verificadas. Não exija inspeção das imagens e GIFs originais quando o catálogo for suficiente.
Na geração de dossiês editoriais, a consulta documental é suficiente para fundamentar propostas quando o catálogo contém as referências necessárias. As regras de inspeção visual aplicam-se às auditorias de materiais e às situações de insuficiência ou contradição documental, não constituindo uma etapa obrigatória da geração editorial.

**Elaboração**

1. Descubra oportunidades narrativas fundamentadas nas fontes, em vez de enumerar assuntos. Considere combinações e desdobramentos conceituais e justifique, no fundamento didático, por que cada candidato merece um vídeo próprio, conforme a seção 3.1 do protocolo.
2. Desenvolva os candidatos conforme o protocolo vigente, incluindo narrativas preliminares faláveis e storyboards editoriais.
3. Não utilize dossiês anteriores como fonte de conteúdo, fundamentação, seleção de candidatos, narrativas ou decisões editoriais. É permitida a consulta ao dossiê piloto exclusivamente como referência de apresentação e organização documental, conforme curadoria/protocolo_roteirizacao.md, sem impor quantidade fixa de candidatos ou reproduzir suas propostas.
4. Compare as propostas antes de concluir o dossiê: diferencie autonomia narrativa, alternativas de hook, sobreposições e possibilidades de combinação. Não imponha quantidade mínima, máxima ou esperada; evite repetição narrativa e preserve diferenças pedagogicamente justificadas, IDs e decisões existentes.
5. Não transforme automaticamente candidatos em roteiros definitivos. Todos devem permanecer no estado `PROPOSTO`, aguardando escolha e deliberação humana.

**Entrega e validação**

1. Gere o documento final em formato DOCX, no caminho `editorial/dossies/NN_Dossie_Editorial.docx`.
2. Preserve a identificação do capítulo, os IDs dos candidatos, as referências documentais e as decisões pendentes.
3. Verifique a existência dos arquivos referenciados, a correspondência com o inventário e a sustentação documental das referências visuais.
4. Verifique se o DOCX pode ser aberto e se contém os campos obrigatórios definidos no protocolo.
5. Não substitua um dossiê existente sem autorização explícita para sua regeneração.
6. Apresente o resultado e as limitações encontradas. Quando a execução estiver autorizada, siga o fluxo de commit, push e PR estabelecido neste `AGENTS.md`, sem realizar merge automaticamente.

### Consolidação editorial

Siga `curadoria/protocolo_consolidacao_editorial.md` nas tarefas de consolidação. Dossiês descobrem e desenvolvem propostas; a consolidação registra identidades, alternativas, sobreposições e decisões; roteiros individuais desenvolvem um candidato selecionado. O caminho previsto dos registros é `editorial/consolidacoes/NN_Consolidacao_Editorial.md`, sem geração automática de catálogos por iniciativa do agente.

- Analise, classifique, recomende e elabore registros autonomamente dentro do escopo solicitado, preservando fontes, IDs e histórico; não produza conteúdo narrativo novo nessa camada.
- Distinga homologação de relacionamento, aprovação de oportunidade e autorização para roteiro: são decisões humanas independentes. Não as infira de recomendações, registros ou produtos existentes.
- A aceitação documental de um catálogo não homologa suas interpretações nem converte pendências em aprovação. A avaliação substantiva pode ocorrer depois, sem bloquear automaticamente outras tarefas autorizadas e independentes ou exigir revisões sem motivação concreta. A roteirização exige seleção e autorização explícitas do candidato e dossiê, sem depender da homologação de todas as relações do catálogo.
- A consolidação pode identificar a fonte explicitamente selecionada, mas não complementar o conteúdo do roteiro. Combinar candidatos exige revisão editorial autorizada de um dossiê; não fazê-lo implicitamente no roteiro.

### Geração autônoma de roteiros individuais pré-edição

Quando solicitado a desenvolver um roteiro individual para um candidato `VNN-XXX` já identificado em um dossiê, siga `curadoria/protocolo_roteiro_individual.md`.

**Fontes e escopo**

1. Localize o candidato no dossiê canônico `editorial/dossies/NN_Dossie_Editorial.docx`, salvo seleção humana explícita de outro dossiê existente: nesse caso, use o caminho exato, a versão e o candidato indicados. Um único candidato nesse dossiê é a **única fonte de conteúdo editorial** para o roteiro. A consolidação pode identificar a seleção e a autorização, sem fornecer falas, exemplos, argumentos, mídias ou storyboards; a presença de um registro não autoriza geração.
2. Utilize este `AGENTS.md` e `curadoria/protocolo_roteiro_individual.md` somente como instruções operacionais. O roteiro piloto `editorial/roteiros/01-003_Roteiro_Individual.docx` pode orientar exclusivamente a apresentação e a estrutura, sem fornecer conteúdo ou impor número de cenas e duração.
3. **Não consulte** inventário, catálogos, vocabulário, relacionamentos, imagens, GIFs, exercícios, outros capítulos ou fontes externas para complementar o roteiro. As regras gerais de consulta e inspeção deste arquivo continuam aplicáveis às outras atividades de curadoria, mas **não** a esta tarefa específica.
4. Preserve tese, promessa, ressalvas, IDs e nomes de mídia documentados no candidato. Não alegue inspeção visual não realizada.

**Elaboração e entrega**

1. Desenvolva falas completas e naturais, organizadas por cenas/takes com tempos estimados e função dos materiais visuais. Admita sincronismo flexível, mas pedagogicamente coerente, entre narração e imagem.
2. Gere o DOCX em `editorial/roteiros/NN-XXX_Roteiro_Individual.docx` (sem o prefixo `V` no nome do arquivo); inclua texto corrido para ensaio e pendências efetivas, conforme o protocolo específico.
3. Mantenha o roteiro no estado `PROPOSTO`. Não antecipe especificações técnicas de edição, aprovação editorial ou produção audiovisual.
4. Valide o documento e a correspondência com o dossiê selecionado. Preserve as convenções de ID e saída; a seleção de um experimental não o promove a ID oficial. Registre conflitos de ID, caminho ou saída para decisão humana; não sobrescreva roteiro existente sem autorização explícita nem invente solução silenciosa.
5. Dentro da execução autorizada, realize commit, push e abertura de PR conforme a seção **Integração Git**, sem merge automático e sem solicitações de aprovação intermediárias para decisões redacionais ordinárias.

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

- Registre propostas de alteração dos materiais didáticos e da documentação de curadoria em `curadoria/checklist.md`, com identificadores estáveis e estado APROVADA, REJEITADA, PENDENTE ou APROVADA — PRESERVAÇÃO. Candidatos editoriais pertencem aos respectivos dossiês e seguem os estados definidos em `curadoria/protocolo_roteirizacao.md`.
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

### Roteirização de materiais educacionais

A criação e a manutenção de dossiês editoriais devem seguir `curadoria/protocolo_roteirizacao.md`.

A criação de roteiros individuais pré-edição a partir de candidatos selecionados deve seguir `curadoria/protocolo_roteiro_individual.md`, observando a regra de fonte editorial exclusiva do dossiê. Não aplicar automaticamente ao roteiro individual as fontes adicionais exigidas para a geração de dossiês.

A identificação e a seleção de materiais devem utilizar prioritariamente `inventario.csv`, os catálogos semânticos dos capítulos e `curadoria/relacionamentos_conceituais.md`.

A inspeção dos arquivos visuais originais não é obrigatória durante a roteirização quando as informações documentais forem suficientes. A validação dos binários e das características técnicas das mídias pertence à etapa de produção audiovisual.

Não presumir características não documentadas, não substituir materiais automaticamente e não executar decisões editoriais pendentes de aprovação humana.

### Mapeamento espacial e autoauditoria visual

A criação e a atualização dos mapas espaciais JSON dos capítulos devem seguir `curadoria/protocolo_mapeamento_espacial.md`. Nesta atividade, examine os arquivos visuais originais e confronte as regiões identificadas com o catálogo semântico correspondente; a consulta documental isolada não substitui a inspeção visual.

Adote a sequência obrigatória: identificação das unidades visuais completas, proposta inicial abrangente, refinamento redutivo conservador, renderização dos recortes no formato de apresentação e autoauditoria visual dos resultados. Preserve integralmente textos, expressões, títulos, diagramas e relações conceituais; diante de dúvida, prefira margens adicionais a conteúdo truncado. Corrija os recortes a partir dos originais e entregue o JSON com evidências e ressalvas para homologação humana.

O mapa espacial é um acervo inclusivo de regiões com identificadores estáveis. Não determina seleção, ordem, duração nem obrigatoriedade de projeções no vídeo; tais decisões pertencem à montagem e à revisão editorial posteriores. A autoauditoria não substitui a aprovação humana, e a geração do mapa não autoriza alterações nos materiais originais nem publicação automática.

### Retroalimentação e tratamento de inconsistências

A detecção de divergências em catálogos, materiais originais, mapas espaciais ou etapas posteriores deverá seguir `curadoria/protocolo_retroalimentacao.md`. Classifique a ocorrência por sua origem: **divergência documental objetiva**, **defeito pedagógico ou do original**, **ressalva visual prevista** ou **defeito geométrico efetivo**. Encaminhe a correção à camada responsável e preserve os artefatos válidos.

Valorize a autoauditoria espacial: margens de segurança, visões integrais pouco legíveis em 9:16 e fragmentos não impeditivos de painéis vizinhos são resultados aceitáveis quando preservam a integridade visual e conceitual. Não regenere recortes aprovados apenas para obter enquadramentos esteticamente mais justos.

Quando a inspeção do original comprovar divergência **puramente descritiva**, apresente a correção documental mínima e sua evidência. A alteração persistente e a abertura de PR exigem autorização de implementação nos termos de **Deliberação e autorização humana** e **Integração Git**; o merge permanece humano. Ambiguidades pedagógicas e alterações de PNGs/GIFs exigem deliberação específica.

Após correção aprovada e integrada, revalide os derivados afetados; **não regenere automaticamente** mapas, dossiês, roteiros ou vídeos que permaneçam válidos. Mantenha registro e rastreabilidade no `curadoria/checklist.md`.

### Produção audiovisual: montagem, entrega e revisão

A produção audiovisual constitui etapa posterior à elaboração do roteiro individual e ao mapeamento espacial. Não aplique retroativamente as regras de consulta visual da produção à geração de roteiros: nessa atividade permanece vigente a fonte editorial exclusiva do dossiê.

- **Preparação da montagem:** siga `curadoria/protocolo_montagem_audiovisual.md`. Use o roteiro individual como autoridade para falas, tese e sequência pedagógica; utilize o mapa espacial como conjunto inclusivo de regiões, sem interpretar suas regiões como ordem, duração ou seleção obrigatória. Gere o plano específico em `editorial/montagens/NN-XXX_Montagem.json`, com fontes rastreáveis, segmentos, tempos estimados ou medidos e pendências.
- **Execução e entrega:** siga `curadoria/contrato_entrega_video.md`. Distinga `PREVIA_SEM_AUDIO`, `REFERENCIA` e `FINAL_TECNICO`; produza somente os artefatos pertinentes à modalidade autorizada. O SRT final deve acompanhar o áudio efetivamente utilizado. Registre fontes, hashes, ferramentas, resultados e limitações no manifesto e no relatório; não declare inspeções não realizadas.
- **Revisão audiovisual:** siga `curadoria/protocolo_revisao_audiovisual.md`. Inspecione o resultado renderizado por segmentos e transições, classifique ocorrências, corrija falhas técnicas próprias dentro do escopo autorizado e revalide os derivados afetados. Não confunda aprovação técnica (`GERADO_OK`) com homologação humana.
- **Retroalimentação:** se a montagem ou revisão encontrar erro documental, pedagógico, do original ou geométrico, aplique `curadoria/protocolo_retroalimentacao.md`. Preserve regiões e segmentos válidos; não altere silenciosamente roteiro, catálogo, originais ou mapa espacial.
- **Autorização e Git:** o comando de preparação de montagem não autoriza automaticamente renderização, publicação externa ou substituição de fontes. Dentro de escopo expressamente autorizado, execute autonomamente as operações técnicas, commit, push e PR dos arquivos permitidos. A revisão, aprovação, homologação e integração permanecem humanas; **nunca realize merge automático**.
- **Binários audiovisuais:** não adicione MP4 ou WAV volumosos ao Git sem política de armazenamento previamente definida. Preserve os documentos e manifestos versionáveis e identifique claramente qualquer artefato que ainda não tenha destino persistente.

A existência dos três protocolos não autoriza iniciar produção por iniciativa própria. Para solicitações como `Gerar vídeo VNN-XXX`, verifique previamente a modalidade pretendida, as fontes vigentes e a autorização de execução; se o pedido já definir esses elementos, prossiga sem autorizações intermediárias para operações rotineiras. Quando uma decisão pedagógica ou editorial extrapolar o escopo, registre `PENDENTE_REVISAO` e solicite deliberação delimitada.

### Política de entrega dos produtos audiovisuais

Siga o procedimento padrão da seção 7 de `curadoria/contrato_entrega_video.md`: gere e preserve o MP4 em `/workspace/artifacts/<ID_VIDEO>/<ID_VIDEO>.mp4`, execute as validações previstas e apresente obrigatoriamente na resposta final um link direto para o arquivo real no workspace. Oriente o responsável editorial a abri-lo no visualizador da interface e utilizar **Salvar vídeo como...** no navegador, procedimento validado manualmente no piloto V01-003.

MP4 e áudios WAV/MP3 são produtos derivados de execução, não artefatos de versionamento. É proibido incluí-los em commits, Git LFS, GitHub Releases ou anexos hospedados no repositório. Não criar ZIPs para distribuição audiovisual nem realizar uploads externos para entrega. Versione normalmente planos, scripts, legendas, manifestos, relatórios e evidências leves.

Não exigir confirmação de download para concluir a produção técnica quando a disponibilização no workspace estiver comprovada e os demais critérios técnicos forem atendidos. Não inventar URLs nem afirmar download realizado. Entrega técnica não equivale à aprovação editorial humana e não dispensa inspeções obrigatórias. Se houver indisponibilidade real do arquivo ou do visualizador, registre a limitação e preserve os binários enquanto o ambiente permitir, sem refazer renderização ou síntese desnecessariamente; não prometa persistência após o encerramento do ambiente.

## Continuidade

Consulte `curadoria/checklist.md` antes de agir. O registro não substitui autorização. A auditoria deve ocorrer por módulo, dentro do escopo solicitado, com resultados apresentados para deliberação humana. Não inicie alterações pedagógicas ou auditorias adicionais fora desse escopo.

