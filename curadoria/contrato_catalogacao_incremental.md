# Contrato proposto — manutenção incremental dos catálogos semânticos

**Estado:** PROPOSTO — especificação para implementação e validação; não autoriza alteração automática de catálogos canônicos.
**Referências:** `AGENTS.md`, `inventario.csv`, `curadoria/protocolo_catalogacao_semantica.md`, `curadoria/protocolo_retroalimentacao.md`, `ferramentas/reconciliar_documentacao.py`.

## 1. Responsabilidades

- **Reconciliador físico:** descobre arquivos e atualiza `inventario.csv` e regiões geradas do `README.md`. Continua independente da catalogação.
- **Catalogador incremental:** confronta a identidade operacional `modulo/arquivo` e os hashes dos originais com a evidência de última catalogação; inspeciona semanticamente somente os arquivos novos ou cujo conteúdo mudou; preserva fichas válidas.
- **Histórico avaliativo:** avaliações de execuções e pilotos ficam em `curadoria/avaliacoes/`. Não são normas nem fontes semânticas substitutas. Regras gerais permanecem em `curadoria/protocolo_*.md`; decisões persistentes continuam no checklist e nos contratos responsáveis.

## 2. Detecção e identidade

1. Antes de qualquer leitura visual ou textual dos originais, executar ou conferir a reconciliação documental e obter a relação física do capítulo.
2. Comparar cada caminho `modulo/arquivo` com a evidência de hashes SHA-256 correspondente à versão catalogada. O `inventario.csv` **não contém hashes**; portanto, não afirmar que o CSV sozinho detecta alteração de conteúdo. Definir um manifesto de evidências mínimo, associado à revisão do catálogo, sem criar cadastro semântico concorrente.
3. Classificar `inalterado`, `novo`, `conteúdo alterado`, `ausente` e `renomeação comprovada`. Identidade por caminho e integridade por hash são dimensões diferentes; hash igual não prova identidade semântica de dois arquivos distintos.
4. Se não houver evidência confiável de baseline ou não for possível ler a estrutura do catálogo, bloquear **a atualização incremental daquele capítulo** e solicitar uma linha de base controlada. Não reinterpretar tudo silenciosamente.
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

A detecção, classificação de mudanças, elaboração de fichas novas e validação estrutural podem ser autônomas. **Publicar alterações em catálogo canônico permanece sujeito à autorização de implementação e ao fluxo de PR sem merge automático.** Mudanças de conteúdo pedagógico, correções de originais, homologação de terminologia e resolução de inconsistências continuam humanas conforme os contratos vigentes. O agente não deve parar a análise de arquivos independentes por causa de uma pendência localizada.

## 5. Prova de funcionamento antes de adoção

Implementar em etapa própria, com testes automatizados e evidência verificável:
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
