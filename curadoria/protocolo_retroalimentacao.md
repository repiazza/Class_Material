# Protocolo de retroalimentação e tratamento de inconsistências

**Destino:** `curadoria/protocolo_retroalimentacao.md`  
**Finalidade:** detectar, classificar, encaminhar, corrigir quando autorizado e revalidar inconsistências encontradas em etapas posteriores à criação dos materiais.  
**Estado:** protocolo operacional sujeito à homologação humana.

## 1. Princípio e alcance

Cada etapa responde pelos artefatos que produz, mas pode detectar defeitos nas fontes das quais depende. **Detectar não significa assumir a autoria da correção.** A ocorrência retorna à camada responsável, com evidência verificável, proposta delimitada e rastreabilidade.

Este protocolo aplica-se à curadoria documental, ao mapeamento espacial e, futuramente, à produção e à revisão audiovisual. Ele **não substitui** os contratos de catalogação, roteirização, mapeamento espacial, deliberação humana ou integração Git definidos no `AGENTS.md`.

**Regra central:** preservar resultados válidos, corrigir na origem, revalidar os derivados afetados e regenerar apenas o necessário.

## 2. Classificação obrigatória

| Classe | Identificação | Conduta |
| --- | --- | --- |
| **D — Divergência documental objetiva** | A descrição afirma que um elemento aparece em determinado arquivo, mas a inspeção do arquivo real demonstra o contrário; ou há troca inequívoca de referências entre arquivos. | Produzir proposta de correção **do documento**, com antes/depois e evidência. Se a execução estiver autorizada, preparar a alteração em branch/PR; **não integrar sem aprovação humana**. |
| **P — Inconsistência pedagógica ou defeito do original** | Erro matemático, conceito incorreto, texto encoberto no original, ambiguidade de exemplo ou decisão didática. | Registrar e encaminhar à curadoria geradora. **Não alterar o material original automaticamente** nem escolher interpretação pedagógica sem deliberação. |
| **V — Ressalva visual prevista** | Visão integral pequena em 9:16, margens de segurança, espaço vazio ou pequeno fragmento de quadro vizinho, desde que o conteúdo essencial e sua legibilidade estejam preservados conforme o protocolo espacial. | Registrar como observação, se útil. **Não bloquear, reprovar ou “otimizar” compulsivamente o recorte.** |
| **G — Defeito geométrico efetivo** | Corte de palavra, expressão, borda necessária, legenda ou relação visual; distorção; projeção incorreta. | Retornar à curadoria espacial e corrigir conforme `protocolo_mapeamento_espacial.md`; renderizar e reinspecionar. |

**A classificação depende da evidência, não da aparência de gravidade.** Um erro conceitual no original não se transforma em defeito de recorte; uma descrição incorreta não autoriza editar o PNG para coincidir com ela.

## 3. Verificação antes de propor correção documental

1. Identificar capítulo, nome **exato** do arquivo, registro do catálogo e afirmação questionada.
2. Abrir o arquivo original correspondente; para GIFs, examinar os estados relevantes. Conferir se não houve confusão entre PNG e GIF de nomes semelhantes.
3. Comparar a afirmação documental com o conteúdo efetivamente exibido; consultar o vocabulário e outras referências pertinentes somente quando necessário.
4. Determinar se a divergência é **objetiva e inequívoca**. Se houver dúvida sobre intenção pedagógica, classificar como **P**, não como **D**.
5. Propor a menor alteração textual que torne a descrição fiel ao original, preservando estrutura, IDs, referências, exemplos corretos e terminologia.
6. Verificar se a correção repercute em glossário, dossiê, roteiro ou outros registros. Não modificar automaticamente artefatos fora do escopo autorizado.

**Proibição:** substituir uma descrição por conteúdo plausível sem inspeção física do arquivo; inventar quadros, durações, símbolos, exemplos ou hashes.

## 4. Registro mínimo da ocorrência

Usar `curadoria/checklist.md` como registro de deliberação, conforme `AGENTS.md`, evitando criar um segundo cadastro concorrente. Cada ocorrência deve permitir identificar:

- ID estável; classe **D/P/V/G**; capítulo, arquivo e artefato documental afetado.
- Evidência verificável: descrição atual, observação do original, estado relevante do GIF e localização da evidência (painel/relatório, quando existir).
- Responsável pela origem; impacto conhecido e dependências potencialmente afetadas.
- Ação proposta: texto antes/depois para **D**, encaminhamento para **P**, justificativa de aceitação para **V**, correção de recorte para **G**.
- Estado de deliberação (`PENDENTE`, `APROVADA`, `REJEITADA`, `APROVADA — PRESERVAÇÃO`), autorização de implementação, PR/commit e resultado da revalidação, quando aplicáveis.

**Não é necessário registrar cada margem visual aceitável como pendência.** Agrupar observações repetitivas sem perder a identificação dos casos relevantes.

## 5. Autonomia, aprovação e Git

- A detecção, inspeção, classificação, elaboração de proposta e análise de impacto são autônomas dentro da tarefa autorizada.
- **Sem autorização para editar o catálogo**, preparar a proposta e pedir deliberação; não alterar arquivos persistentes.
- **Com autorização explícita para implementar correções documentais objetivas**, o Codex pode aplicar a mudança delimitada, validar o DOCX e abrir PR conforme `AGENTS.md`, **sem merge**. O PR é proposta de integração, não aprovação humana.
- Modificações pedagógicas dos originais, mudanças de exemplos conceituais e decisões editoriais continuam exigindo aprovação específica.
- Não usar uma correção documental como pretexto para modificar PNGs, GIFs, mapas ou roteiros fora do escopo.
- Quando houver alterações independentes de governança e de conteúdo, preferir PRs de escopo separado. Não reescrever histórico ou refazer PR válida apenas para agregar o novo procedimento.

## 6. Revalidação e continuidade

Após uma correção autorizada e integrada:

1. Identificar quais arquivos e registros mudaram; conferir hashes dos binários alterados.
2. Reexaminar a correspondência semântica entre catálogo e originais.
3. Verificar os derivados **realmente dependentes**: regiões do mapa, dossiês, roteiros e, quando existirem, montagens.
4. **Se mudou apenas a descrição**, preservar as coordenadas e os recortes espacialmente válidos; revalidar a vinculação semântica e atualizar referências somente quando necessário.
5. **Se mudou o original**, verificar integridade e geometria das regiões afetadas, atualizar hashes e renderizar/reinspecionar as projeções pertinentes. Recalcular caixas apenas se o conteúdo ou sua disposição exigir.
6. Registrar o resultado e retomar a execução no ponto seguro. Não reiniciar todo o capítulo por padrão.

O objetivo operacional futuro é permitir que um pedido como **“Gerar vídeo VNN-XXX”** termine em **`GERADO_OK`** (produção técnica concluída, ainda sujeita à revisão/publicação humana) ou **`PENDENTE_REVISAO`** (ocorrência delimitada e, quando autorizado, PR de correção). **Este protocolo não implementa nem antecipa o contrato de produção audiovisual**; estabelece somente o tratamento das inconsistências e a continuidade.

## 7. Caso de referência — PR #13, capítulo 02

A experiência do mapa espacial do capítulo 02 demonstrou duas capacidades a preservar:

- **Acerto espacial:** regiões abrangentes, refinamento conservador, projeção 9:16, inspeção real e correção dirigida de caixas. **Não desfazer recortes válidos para eliminar margens ou fragmentos visualmente aceitáveis.**
- **Crítica à fonte:** divergências detectadas durante a autoauditoria foram relatadas sem adulterar os materiais.

Aplicação das classes:

| Ocorrência | Classe | Encaminhamento |
| --- | --- | --- |
| Descrição de `signed_unsigned.png` divergente do PNG real, possivelmente confundida com o GIF | **D**, após conferência direta | Propor correção do catálogo; preservar o mapa enquanto geometricamente válido |
| Peso incorreto em `msb_lsb.png` | **P** | Solicitar correção pedagógica do original; depois revalidar derivados afetados |
| Texto encoberto no original de `signed_unsigned.gif` | **P** | Solicitar correção do material original; depois reinspecionar estados e regiões afetados |
| Margens, visões integrais pequenas e fragmentos laterais aceitáveis | **V** | Aceitar como resultado intencional da preservação do conteúdo |
| Borda cortada pelo recorte, caso ocorra | **G** | Corrigir geometria e reinspecionar conforme protocolo espacial |

A PR #13 **não é automaticamente aprovada ou integrada por este documento**. A correção documental e os defeitos do original podem seguir fluxos de aprovação próprios; a entrega espacial válida deve ser preservada.

## 8. Critério de conclusão

Uma ocorrência está tratada quando sua origem foi identificada, a ação foi executada **ou** a pendência foi explicitamente encaminhada, e os derivados afetados foram revalidados quando cabível. **Não declarar `GERADO_OK` quando houver pendência impeditiva para o conteúdo efetivamente utilizado.**

**Síntese:** a curadoria espacial preserva a imagem; a crítica identifica a divergência; a curadoria responsável corrige a fonte mediante autorização; os derivados são revalidados sem perder trabalho válido.
