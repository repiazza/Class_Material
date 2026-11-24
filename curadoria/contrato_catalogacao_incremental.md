# Contrato — manutenção incremental dos catálogos semânticos

**Estado:** Implementado para candidatos DOCX. O agente publica alterações canônicas em PR no escopo de manutenção definido em AGENTS.md.
**Referências:** `AGENTS.md`, `inventario.csv`, `curadoria/protocolo_catalogacao_semantica.md`, `curadoria/protocolo_retroalimentacao.md`, `ferramentas/reconciliar_documentacao.py`.

## 1. Responsabilidades

- **Reconciliador físico:** descobre arquivos e atualiza `inventario.csv` e regiões geradas do `README.md`. Continua independente da catalogação.
- **Catalogador incremental:** confronta a identidade operacional `modulo/arquivo` e os hashes dos originais com a evidência de última catalogação; inspeciona semanticamente somente os arquivos novos ou cujo conteúdo mudou; preserva fichas válidas.
- **Histórico avaliativo:** avaliações de execuções e pilotos ficam em `curadoria/avaliacoes/`. Não são normas nem fontes semânticas substitutas. Regras gerais permanecem em `curadoria/protocolo_*.md`; decisões persistentes continuam no checklist e nos contratos responsáveis.

## 2. Detecção e identidade

1. Antes de qualquer leitura visual ou textual dos originais, executar ou conferir a reconciliação documental e obter a relação física do capítulo.
2. Comparar cada caminho `modulo/arquivo` com a evidência de hashes SHA-256 correspondente à versão catalogada. O `inventario.csv` **não contém hashes**; portanto, não afirmar que o CSV sozinho detecta alteração de conteúdo. Definir um manifesto de evidências mínimo, associado à revisão do catálogo, sem criar cadastro semântico concorrente.
3. Classificar `inalterado`, `novo`, `conteúdo alterado`, `ausente` e `renomeação comprovada`. Identidade por caminho e integridade por hash são dimensões diferentes; hash igual não prova identidade semântica de dois arquivos distintos.
4. Se não houver evidência confiável de baseline ou não for possível ler a estrutura do catálogo, buscar uma linha de base controlada no histórico. Se não for verificável, bloquear a operação semântica dependente naquele capítulo. Não reinterpretar tudo silenciosamente.
5. Excluir catálogos, mapas, relatórios e derivados técnicos da lista de originais, conforme a reconciliação física.

## 3. Atualização mínima

- **Inalterado:** não reabrir original para interpretação semântica e não reescrever sua ficha. Reutilizar descrição, etiquetas, ressalvas e referências.
- **Novo:** abrir e interpretar somente o novo material, adicionar uma ficha no DOCX do capítulo e atualizar as estruturas dependentes.
- **Conteúdo alterado:** reler somente o arquivo alterado (e quadros relevantes quando GIF); substituir ou revisar sua ficha com confronto explícito entre versão anterior e atual.
- **Ausente:** não eliminar silenciosamente a ficha; sinalizar remoção e suas referências, preservando rastreabilidade e exigindo decisão para a alteração semântica destrutiva.
- **Renomeação:** quando comprovada pelo Git ou por evidência inequívoca, atualizar identidade e referências sem reinterpretar o conteúdo se o hash for igual; caso contrário, tratar como remoção/adição sem inventar continuidade.
- **Vocabulário, glossário e índice reverso:** recalcular coerência das atribuições do capítulo inteiro a partir das fichas preservadas e modificadas, **sem reabrir todos os originais**. Não homologar automaticamente etiquetas novas, relações conceituais ou decisões pedagógicas.
- **Formato DOCX:** preservar fichas e campos existentes, legibilidade, tabelas e contrato do Motor 1; evitar alterações colaterais de texto, ordem ou apresentação. Não confundir reserialização necessária do DOCX com reinterpretação semântica das fichas.

## 4. Fronteiras de autonomia

A autorização permanente e seus limites estão em `AGENTS.md`. A operação da ferramenta produz um candidato externo; o agente valida o resultado e publica a alteração canônica quando ela estiver no escopo. Registre adiamentos com justificativa e prossiga com materiais independentes, mantendo os hashes e fichas anteriores das identidades adiadas.

## 5. Prova de funcionamento antes de adoção

A implementação em `ferramentas/catalogacao_incremental.py` deve manter os seguintes critérios verificáveis:
1. Inclusão de PNG em capítulo catalogado: uma ficha adicionada, nenhuma releitura dos demais originais.
2. Modificação de PNG ou GIF existente: somente ficha correspondente revista; demais fichas preservadas.
3. Nenhuma mudança: zero interpretação e nenhuma alteração dos bytes dos documentos.
4. Renomeação com hash idêntico: identidade corrigida sem nova inspeção; sem prova, não inventar renomeação.
5. Exclusão: pendência explícita, sem apagamento silencioso.
6. Mudança em vocabulário ou relações: avaliar impacto documental separadamente; não tratar como alteração física do capítulo.
7. DOCX: fichas únicas, referências existentes, glossário e índice reverso exatos; compatibilidade com consumo do Motor 1.
8. Baseline inexistente ou inválido: bloqueio localizado, sem reconstrução total automática.

Os testes devem instrumentar quais arquivos originais foram efetivamente abertos, para comprovar a **ausência de releitura integral**. Relatar limitações e não declarar autonomia sem piloto real.

## 6. Organização das avaliações

`curadoria/avaliacoes/` armazena laudos históricos identificados por execução/capítulos, incluindo a avaliação dos pilotos 04/13. Documentos históricos podem mencionar estados e caminhos válidos à época: preservar esse caráter temporal. Novos laudos só devem ser versionados quando acrescentarem rastreabilidade relevante; evidências temporárias volumosas continuam fora do Git. Não criar um laudo por material nem um protocolo paralelo por capítulo.

## 7. Mecanismo e referência implementados

Instruções: [ferramentas/README.md](../ferramentas/README.md#catalogação-incremental). As operações são `validar`, `baseline`, `planejar`, `aplicar` e `revisar`. O planejamento reutiliza a elegibilidade do reconciliador físico; não cria outro inventário. A aplicação recebe fichas elaboradas pelo agente após inspeção efetiva e produz somente candidato externo ao acervo. O mecanismo não possui visão computacional ou geração semântica autônoma embutida; a autonomia resulta da execução coordenada pelo agente.

A baseline reside em `customXml/catalogacao_baseline.xml` no próprio pacote DOCX, relacionada pelo OPC. Contém identidades, SHA-256 dos materiais, hashes das partes do catálogo e das fontes normativas, além da procedência da referência inicial. Não duplica descrições ou etiquetas. É evidência de versão, não um cadastro semântico externo, assinatura digital ou homologação pedagógica.

Para estabelecer a primeira baseline, exige-se referência Git explícita: o DOCX de entrada deve coincidir byte a byte com o catálogo naquela revisão, e todos os materiais descritos devem existir no mesmo snapshot. Os hashes são obtidos desse snapshot, não adotados da árvore atual por conveniência. Essa associação controlada documenta a referência utilizada; não comprova que o catálogo antigo era semanticamente correto. Se o histórico não estiver disponível ou a correspondência não for verificável, bloquear localmente. Uma baseline existente não é recalibrada silenciosamente; uma edição externa incompatível exige restabelecimento controlado da referência ou restauração da versão documentada.

A baseline é vinculada às partes do pacote, incluindo `word/document.xml` e estilos. O índice CSV continua `modulo;arquivo`. Mudanças normativas são indicadas separadamente e não consomem automaticamente a pendência: os hashes normativos anteriores permanecem enquanto não houver revisão específica. Isso não autoriza reinterpretação dos originais inalterados nem bloqueia fichas independentes.

A instrumentação distingue `hash_binario` de `interpretacao_solicitada`. Ler bytes para calcular SHA-256 é necessário; a aplicação incremental recusa fichas de identidades inalteradas. O pacote efêmero de fichas está vinculado ao hash do catálogo e aos hashes efetivamente observados; revisão de ficha exige também seu digest anterior e justificativa. O log instrumenta pedidos ao agente/adaptador, não certifica por si só uma inspeção visual. Evidência visual/textual continua necessária conforme o protocolo semântico.

Renomeações usam evidência `R` do Git e hash idêntico; sem isso, tratar como adição/ausência, não identidade por semelhança ou hash isolado. Ausências permanecem como pendências com fichas e baseline preservadas. Glossário e índice reverso derivam de todas as fichas, sem reabrir seus originais; novas etiquetas locais ficam explicitamente PROPOSTAS. A coocorrência de etiquetas produz candidatos a impacto documental, não relacionamentos pedagógicos homologados.

A ferramenta preserva os blocos XML das fichas inalteradas, inclusive tabelas internas, e verifica seus digests após a aplicação. Mantém a ordem do glossário existente e altera somente vínculos afetados; novos termos são acrescentados sem ordenar novamente as entradas preservadas. Campos de cobertura são ajustados quando suas métricas mudam. Formatos não reconhecíveis são bloqueados para adaptação controlada, sem conversão ou reconstrução silenciosa.

### Revisão deliberada de fichas com originais inalterados

A operação `revisar` exige referência válida, identidade classificada como inalterada, SHA-256 observado, digest anterior, evidência e justificativa por ficha. Aplica somente as fichas indicadas; mudanças físicas e renomeações permanecem para `aplicar`. Preserva os hashes dos materiais, a procedência, as referências normativas e os digests das fichas independentes. Atualiza os hashes de integridade das partes do DOCX e recalcula os vínculos do glossário afetados. O relatório registra os digests anterior e posterior e a evidência e justificativa da revisão. Um pacote vazio preserva os bytes do candidato.

## 8. Avaliação e adoção

Os testes cobrem o incremental físico e verificam a revisão deliberada em fixtures, incluindo a preservação do DOCX quando não há correções e o uso do candidato revisado em uma atualização incremental posterior. As PRs #35, #36 e #37 demonstraram inclusão localizada no acervo real. O registro da evolução permanece nos PRs e no histórico avaliativo quando pertinente.
