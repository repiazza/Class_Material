# Protocolo de catalogação semântica autônoma

**Identificador:** `curadoria/catalogacao_semantica`
**Versão:** `0.1.1`
**Estado:** PROPOSTO — implementação e pilotos autorizados; protocolo e qualidade dos catálogos sujeitos à avaliação humana.
**Escopo:** geração e revisão de catálogos DOCX a partir dos materiais originais.

## 1. Finalidade e fronteiras

Documentar o conhecimento efetivamente representado nos materiais, com precisão suficiente para o consumo documental do Motor 1. Catalogar não é escolher vídeos, desenvolver hooks, redigir roteiros ou decidir montagens. A homologação pedagógica e editorial permanece humana; a produção posterior depende do escopo e dos contratos próprios.

Aplicam-se [AGENTS.md](../AGENTS.md), [roteirização](protocolo_roteirizacao.md), [retroalimentação](protocolo_retroalimentacao.md) e as decisões registradas no [checklist](checklist.md). Este protocolo não substitui esses contratos nem autoriza alterações de fontes, mudanças de terminologia homologada, novas RC ou produção audiovisual.

A capacidade visual já certificada não deve ser recertificada como pré-condição de cada tarefa. Isso não dispensa a inspeção efetiva dos materiais que serão catalogados, nem comprova precisão semântica geral.

## 2. Entradas, escopo e identificação

1. Identificar capítulo, revisão do checkout e autorização: criação inaugural, revisão localizada ou experimento com comparação posterior.
2. Confrontar os arquivos reais com [inventario.csv](../inventario.csv). Preservar `modulo;arquivo`; registrar ausências, entradas desatualizadas e arquivos ainda não inventariados. Atualização do inventário exige escopo autorizado.
3. Delimitar materiais didáticos, documentos de referência, derivados técnicos e pacotes auxiliares. Não recatalogar o catálogo como conteúdo pedagógico nem incluir automaticamente mapas, relatórios e evidências de produção.
4. Preservar capítulo + nome exato do arquivo como identificação operacional. Numeração ordinal, posição de parágrafo e hash não substituem essa identificação. Não introduzir UUIDs, renomear arquivos ou impor ordem de estudo.
5. Registrar a revisão das fontes, preferencialmente por commit e hashes em evidência de execução proporcional ao escopo. Não criar um cadastro semântico concorrente.

Pacotes de exercício podem constituir um registro próprio, com função e conteúdo interno identificados. Uma listagem ZIP não prova leitura do código; quando necessário, ler os membros sem executar e sem extrair caminhos não confiáveis para o checkout. Não promover membros internos a arquivos físicos independentes do inventário. Se o escopo for incerto, registrar a pendência e continuar os materiais independentes.

## 3. Inspeção dos materiais

- **PNG/JPEG:** abrir o original e examiná-lo por recurso visual efetivo. Usar recortes ou ampliação quando necessários; metadados, OCR ou nomes não substituem observação. Não atribuir elementos ausentes à imagem.
- **GIF:** decodificar e observar estados e transições relevantes, incluindo mudanças de valores, realces, ponteiros e aparecimento/desaparecimento de texto. Registrar a sequência conceitual, não uma transcrição obrigatória de quadros redundantes. Distinguir duração codificada, ordem dos estados e reprodução contínua efetivamente realizada.
- **Markdown, documentos e código:** ler o conteúdo real, incluindo tabelas e trechos de código. Distinguir enunciado, resposta, exemplo, implementação e pacote de apoio. Leitura estática não comprova compilação ou execução.
- **Ilegibilidade ou acesso parcial:** identificar precisamente o elemento não interpretado; manter o registro parcial explícito, sem completar por suposição.

Usar ferramentas efetivamente disponíveis. Registrar quais fontes foram abertas e quais evidências foram visualizadas; a mera geração de miniaturas não comprova inspeção.

## 4. Evidência, interpretação e isolamento

Distinguir, na própria redação quando suficiente: (a) o que aparece; (b) o significado sustentado; (c) o que permanece incerto. Identificar valores, expressões, comandos, componentes e conexões necessários à compreensão, preservando ressalvas técnicas.

Uma afirmação impressa no material não é automaticamente verdadeira. Se houver erro demonstrável, descrever fielmente o que aparece e registrar a ressalva, sem substituir silenciosamente o original por uma explicação corrigida. Não afirmar código compilado, tabela conferida ou animação reproduzida sem executar a verificação correspondente.

Na revisão ordinária, confrontar catálogo e original. Em experimento que exija reconstrução independente, não abrir o catálogo de referência, dossiês, roteiros ou derivados que antecipem seu conteúdo antes de concluir a versão experimental. Usar instrumentos gerais como normas, distinguindo definições terminológicas de descrições específicas de materiais. Registrar fontes consultadas, influência conhecida do contexto anterior e limites de isolamento; não alegar experimento cego quando não houver.

Congelar a versão experimental com hash e horário antes da comparação. Comparar posteriormente contra os originais, não tratar o catálogo humano como gabarito infalível. Preservar o documento congelado; melhorias decorrentes da comparação pertencem a uma revisão posterior identificada.

## 5. Contrato semântico do DOCX

Preservar formato DOCX legível, identificação do capítulo, escopo e registros individualmente localizáveis. Para cada material, fornecer informação suficiente sobre:

- Nome físico exato e tipo/função quando pertinente.
- Conteúdo e conceitos efetivamente apresentados.
- Representações, exemplos, comandos, código ou demonstrações relevantes.
- Evolução significativa dos GIFs, quando aplicável.
- Palavras-chave canônicas.
- Ressalvas, limites ou referências visuais verificadas quando necessários.

Rótulos, fontes, cores, ordem gráfica e numeração ordinal não precisam reproduzir literalmente catálogos anteriores. Campos podem ser combinados se permanecerem claros e completos. `Referências visuais verificadas` é um recurso já previsto no AGENTS, não uma obrigação de repetir evidências em todas as fichas.

O documento deve permitir ao Motor 1 fundamentar propostas editoriais sem reinterpretar cada imagem. Isso não substitui a inspeção técnica exigida na produção, não garante a correção do original e não autoriza o roteirista individual a buscar conteúdo fora do candidato selecionado.

Manter glossário independente do capítulo e índice reverso: cada palavra-chave utilizada deve ter uma entrada única com definição sustentada; cada entrada deve apontar exatamente para os registros associados. Não manter termos órfãos, materiais inexistentes ou referências excedentes. Gerar o índice a partir das atribuições efetivas evita divergências.

Não impor cotas de palavras, etiquetas, conceitos, exemplos ou relações. A profundidade acompanha a complexidade e a relevância pedagógica, sem preencher campos com definições genéricas apenas para aparentar completude.

## 6. Vocabulário e relacionamentos

Consultar [vocabulario_controlado.md](vocabulario_controlado.md). Reutilizar etiquetas e distinções existentes: lógico/bitwise, pilha de dados/stack de execução, homônimos de comandos e instruções, além dos limites locais documentados. Não normalizar exemplos de código para fazê-los parecer etiquetas.

Conceitos novos podem ser identificados e definidos localmente quando houver evidência suficiente. Identificá-los como propostas de ampliação terminológica; alterações do vocabulário mestre dependem do escopo autorizado. Dúvida localizada não paralisa conceitos independentes. Não inventar definição confiável quando faltarem elementos.

Consultar [relacionamentos_conceituais.md](relacionamentos_conceituais.md) para reutilizar vínculos entre capítulos: 26 relações homologadas, com ressalvas obrigatórias para RC-014, RC-023 e RC-024. Distinguir aprovação pedagógica de fundamentação documental. Uma relação nova não fica homologada porque foi descoberta na catalogação; etiquetas comuns tampouco demonstram dependência pedagógica.

## 7. Inconsistências e encaminhamento

Aplicar o [protocolo de retroalimentação](protocolo_retroalimentacao.md) e o checklist existente, sem criar outro cadastro de decisões:

| Situação | Tratamento |
| --- | --- |
| Erro demonstrável ou ambiguidade pedagógica no original | P; evidência e encaminhamento humano, sem editar o material |
| Contradição objetiva entre catálogo e original | D; proposta documental mínima, preservando a fonte |
| Descrição insuficiente | Identificar o conteúdo ausente e seu impacto; não afirmar contradição sem evidência |
| Limitação de interpretação/acesso visual | Registrar elemento, região/quadro e alcance da incerteza; não atribuir automaticamente erro ao original |
| Problema geométrico produzido em recorte/projeção | G; retorno à camada espacial, conforme autorização |
| Margem ou apresentação prevista sem prejuízo demonstrado | V; preservar resultados válidos |

Referenciar arquivo, revisão/hash, região ou quadro pertinente, observação e consequência para o consumo documental. Um problema descoberto por outro motor pode usar a mesma rastreabilidade e retornar à fonte responsável. Não implementar correção automática ou homologação por detecção.

Registrar ocorrências no checklist quando a tarefa autorizar documentação persistente; em investigações somente de leitura, apresentá-las na conversa ou no laudo autorizado. Preservar estados e justificativas anteriores; não reabrir uma ocorrência conhecida como se fosse descoberta inédita.

## 8. Validação e entrega

Antes de entregar:

1. Conferir a cobertura contra o escopo físico/inventário conciliado: cada material incluído tem registro, e toda exclusão/limitação está explícita.
2. Verificar grafia e existência das referências; separar membros de pacotes dos arquivos reais do capítulo.
3. Conferir conteúdo, evidência visual/textual, sequência de GIFs, palavras-chave, glossário e igualdade do índice reverso com as atribuições dos registros.
4. Verificar integridade e abertura do DOCX, corpo e tabelas, além de legibilidade/paginação quando houver ferramenta disponível. Não confundir arquivo íntegro com semântica correta.
5. Documentar fontes, ferramentas, revisão, abrangência efetivamente inspecionada, incertezas e ocorrências. Avaliar suficiência documental para o Motor 1 sem declarar execução editorial que não ocorreu.
6. Confirmar a preservação dos materiais, catálogos vigentes e inventário fora do escopo autorizado.

Experimentos devem manter catálogo e laudo acessíveis em área temporária/de artefatos não versionados, sem substituir o documento vigente. Catálogos ordinários usam `NN_Catalogo_Semantico.docx` no capítulo, somente quando sua criação/revisão estiver autorizada. Não sobrescrever existentes sem autorização; distinguir geração, validação estrutural, qualidade semântica observada e homologação pedagógica humana.

Publicação documental segue AGENTS e a instrução da tarefa: commit, push e PR apenas dos arquivos autorizados, sem merge automático. Não incorporar quadros extraídos, cópias redundantes ou artefatos experimentais ao Git quando a tarefa determinar preservação externa. Fornecer links reais para revisão; não presumir acesso, download ou persistência futura do workspace.

## 9. Revisões e impacto

Para capítulo já catalogado, o padrão é a manutenção localizada do [contrato incremental](contrato_catalogacao_incremental.md), implementada em `ferramentas/catalogacao_incremental.py`. A referência de hashes fica vinculada ao DOCX, sem acrescentar colunas ao inventário. Sem referência confiável, não adotar os hashes atuais como se fossem os da versão catalogada nem reconstruir o capítulo silenciosamente. A catalogação inaugural continua completa. A ferramenta preserva fichas inalteradas; a interpretação efetiva dos novos/modificados permanece responsabilidade do agente e requer inspeção, não geração automática de texto por hash.


Revisar a menor unidade afetada e preservar histórico e identidades. Se mudar apenas a descrição, revalidar vínculos dependentes; não regenerar mapas, dossiês, roteiros e vídeos válidos por padrão. Se mudar o original mediante autorização, conferir hash e revisar regiões/descrições realmente afetadas. Distinguir detecção, autorização, implementação e homologação.

A primeira adoção deve ser avaliada por pilotos. A conformidade com este documento não constitui prova de precisão geral, nem transforma aprovação da PR do protocolo em homologação dos catálogos experimentais.
