# Class_Material

Acervo de materiais didáticos de programação e computação, organizado em módulos temáticos. Reúne imagens PNG e JPEG, animações GIF e documentos Markdown, incluindo exercícios e gabaritos, além de arquivos-fonte em C e catálogos semânticos em DOCX.

## Organização

Cada diretório abaixo corresponde a um módulo. Seus materiais estão armazenados diretamente na respectiva pasta.

| Diretório | Assunto | Catálogo semântico |
|---|---|---|
| [01_Logica_e_Raciocinio](01_Logica_e_Raciocinio/) | Lógica e raciocínio | [01_Catalogo_Semantico.docx](01_Logica_e_Raciocinio/01_Catalogo_Semantico.docx) |
| [02_Sistemas_de_Numeracao](02_Sistemas_de_Numeracao/) | Sistemas de numeração | [02_Catalogo_Semantico.docx](02_Sistemas_de_Numeracao/02_Catalogo_Semantico.docx) |
| [03_Operacoes_Bitwise](03_Operacoes_Bitwise/) | Operações bitwise | [03_Catalogo_Semantico.docx](03_Operacoes_Bitwise/03_Catalogo_Semantico.docx) |
| [04_Argumentos_CommandLine](04_Argumentos_CommandLine/) | Argumentos de linha de comando e variáveis de ambiente em C | [04_Catalogo_Semantico.docx](04_Argumentos_CommandLine/04_Catalogo_Semantico.docx) |
| [05_Estruturas_de_Dados](05_Estruturas_de_Dados/) | Estruturas de dados | [05_Catalogo_Semantico.docx](05_Estruturas_de_Dados/05_Catalogo_Semantico.docx) |
| [06_Arquivos_e_Entrada_Saida](06_Arquivos_e_Entrada_Saida/) | Arquivos e entrada/saída | [06_Catalogo_Semantico.docx](06_Arquivos_e_Entrada_Saida/06_Catalogo_Semantico.docx) |
| [07_Tracing_e_Execucao](07_Tracing_e_Execucao/) | Tracing e execução | [07_Catalogo_Semantico.docx](07_Tracing_e_Execucao/07_Catalogo_Semantico.docx) |
| [08_Tipos_e_Memoria_C](08_Tipos_e_Memoria_C/) | Tipos e memória em C | [08_Catalogo_Semantico.docx](08_Tipos_e_Memoria_C/08_Catalogo_Semantico.docx) |
| [09_Depuracao_C](09_Depuracao_C/) | Depuração em C | [09_Catalogo_Semantico.docx](09_Depuracao_C/09_Catalogo_Semantico.docx) |
| [10_Estruturas_Controle](10_Estruturas_Controle/) | Estruturas de controle | [10_Catalogo_Semantico.docx](10_Estruturas_Controle/10_Catalogo_Semantico.docx) |
| [11_Sistemas_Operacionais](11_Sistemas_Operacionais/) | Sistemas operacionais em C — Linux/POSIX | [11_Catalogo_Semantico.docx](11_Sistemas_Operacionais/11_Catalogo_Semantico.docx) |
| [12_Organizacao_Computadores](12_Organizacao_Computadores/) | Organização de computadores e projeto de circuitos digitais | [12_Catalogo_Semantico.docx](12_Organizacao_Computadores/12_Catalogo_Semantico.docx) |

A numeração dos módulos organiza os assuntos, mas não estabelece necessariamente uma sequência obrigatória de estudo. A numeração nos nomes dos arquivos também não deve ser tomada, por si só, como uma ordem de leitura.

## Localização dos materiais

Consulte [inventario.csv](inventario.csv), o índice completo dos 255 arquivos presentes nos módulos: 243 materiais didáticos e 12 catálogos semânticos. O arquivo utiliza o separador `;` e as colunas `modulo` e `arquivo`. Para localizar um material a partir da raiz do repositório, combine os valores como `modulo/arquivo`.

As entradas estão ordenadas por módulo e, dentro de cada módulo, por nome de arquivo. O índice inclui imagens, GIFs, documentos Markdown, arquivos-fonte em C e os catálogos DOCX, cada um associado ao seu módulo. Os catálogos são documentos de referência, distintos dos materiais que descrevem. Não inclui os documentos de governança da raiz e de `curadoria/`, o próprio inventário nem este README.

## Catálogos semânticos

Cada módulo possui um documento `NN_Catalogo_Semantico.docx`, acessível na tabela acima. Esses catálogos são a fonte documental de referência para a interpretação semântica do acervo: identificam os materiais pelo nome de arquivo, descrevem conteúdos, representações, exemplos e transições relevantes dos GIFs e associam palavras-chave a cada registro. O glossário do capítulo reúne definições e um índice reverso dos materiais relacionados.

Para consultar o acervo, localize o arquivo no inventário e leia seu registro no catálogo do módulo correspondente. Relacione documento e material físico pelo nome exato do arquivo. O catálogo não substitui o original nem comprova sua integridade, correção ou validação visual; informações não descritas não devem ser presumidas. Divergências entre catálogo e arquivos devem ser relatadas separadamente.

O vocabulário controlado é cumulativo: reutilize a nomenclatura já estabelecida para o mesmo conceito, como `ponteiro`, sem introduzir `pointer` ou `apontador` como etiquetas alternativas. Conceitos distintos permanecem separados. Divergências de termos devem ser submetidas à avaliação, sem unificação automática ou edição dos catálogos.

## Exercícios e gabaritos

Os links abaixo apontam para os enunciados e seus respectivos gabaritos. Os nomes dos arquivos variam entre módulos; no módulo 04 há dois pares numerados, no módulo 05 há três, e no módulo 11 o gabarito inclui orientações e arquivos-fonte separados.

| Módulo | Exercício | Gabarito |
|---|---|---|
| 01 | [exercicio.md](01_Logica_e_Raciocinio/exercicio.md) | [gabarito.md](01_Logica_e_Raciocinio/gabarito.md) |
| 02 | [exercicio.md](02_Sistemas_de_Numeracao/exercicio.md) | [gabarito.md](02_Sistemas_de_Numeracao/gabarito.md) |
| 03 | [exercicio.md](03_Operacoes_Bitwise/exercicio.md) | [gabarito.md](03_Operacoes_Bitwise/gabarito.md) |
| 04 — Argumentos de linha de comando | [1 — Calculadora parametrizável](04_Argumentos_CommandLine/exercicio1.md) | [gabarito1.md](04_Argumentos_CommandLine/gabarito1.md) |
| 04 — Argumentos de linha de comando | [2 — Evolução da calculadora parametrizável](04_Argumentos_CommandLine/exercicio2.md) | [gabarito2.md](04_Argumentos_CommandLine/gabarito2.md) |
| 05 — Estruturas de dados | [A — Lista simplesmente encadeada](05_Estruturas_de_Dados/exercicio1.md) | [gabarito1.md](05_Estruturas_de_Dados/gabarito1.md) |
| 05 — Estruturas de dados | [B — Fila de atendimento drive-thru](05_Estruturas_de_Dados/exercicio2.md) | [gabarito2.md](05_Estruturas_de_Dados/gabarito2.md) |
| 05 — Estruturas de dados | [C — Calculadora com pilha de desfazimento](05_Estruturas_de_Dados/exercicio3.md) | [gabarito3.md](05_Estruturas_de_Dados/gabarito3.md) |
| 06 — Arquivos e entrada/saída | [Explorador de arquivos em C](06_Arquivos_e_Entrada_Saida/exercicio.md) | [gabarito.md](06_Arquivos_e_Entrada_Saida/gabarito.md) |
| 07 | [exercicio.md](07_Tracing_e_Execucao/exercicio.md) | [gabarito.md](07_Tracing_e_Execucao/gabarito.md) |
| 08 | [exercicio.md](08_Tipos_e_Memoria_C/exercicio.md) | [gabarito.md](08_Tipos_e_Memoria_C/gabarito.md) |
| 09 | [exercicio.md](09_Depuracao_C/exercicio.md) | [gabarito.md](09_Depuracao_C/gabarito.md) |
| 10 | [exercicio.md](10_Estruturas_Controle/exercicio.md) | [gabarito.md](10_Estruturas_Controle/gabarito.md) |
| 11 — Sistemas operacionais | [Processos e comunicação entre processos](11_Sistemas_Operacionais/exercicio.md) | [Orientações](11_Sistemas_Operacionais/gabarito1.md); [código da parte A](11_Sistemas_Operacionais/gabarito1a.c); [código da parte B](11_Sistemas_Operacionais/gabarito1b.c) |
| 12 — Organização de computadores | [Projeto de um circuito digital](12_Organizacao_Computadores/exercicio1.md) | [gabarito1.md](12_Organizacao_Computadores/gabarito1.md) |

Os gabaritos podem apresentar explicações, critérios de avaliação ou implementações em C. No módulo 04, `gabarito1.md` contém a implementação em C e `gabarito2.md` reúne implementação e orientações. Todos os 12 módulos possuem ao menos um enunciado de exercício e um gabarito. Os links indicam a correspondência documental; não significam que todos os conteúdos foram submetidos à auditoria técnica e pedagógica.

## Curadoria e governança

O diretório [curadoria](curadoria/) reúne o [checklist de observações, decisões e pendências](curadoria/checklist.md). As [regras operacionais para o Codex](AGENTS.md) ficam na raiz. Esses documentos acompanham a manutenção do acervo e não são materiais didáticos indexados no CSV.
