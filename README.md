# Class_Material

Acervo de materiais didáticos de programação, organizado em módulos temáticos. Reúne imagens PNG e JPEG, animações GIF e documentos Markdown, incluindo exercícios e gabaritos, além de arquivos-fonte em C.

## Organização

Cada diretório abaixo corresponde a um módulo. Seus materiais estão armazenados diretamente na respectiva pasta.

| Diretório | Assunto |
|---|---|
| [01_Logica_e_Raciocinio](01_Logica_e_Raciocinio/) | Lógica e raciocínio |
| [02_Sistemas_de_Numeracao](02_Sistemas_de_Numeracao/) | Sistemas de numeração |
| [03_Operacoes_Bitwise](03_Operacoes_Bitwise/) | Operações bitwise |
| [04_Fundamentos_de_C](04_Fundamentos_de_C/) | Fundamentos de C |
| [05_Estruturas_de_Dados](05_Estruturas_de_Dados/) | Estruturas de dados |
| [06_Arquivos_e_Entrada_Saida](06_Arquivos_e_Entrada_Saida/) | Arquivos e entrada/saída |
| [07_Tracing_e_Execucao](07_Tracing_e_Execucao/) | Tracing e execução |
| [08_Tipos_e_Memoria_C](08_Tipos_e_Memoria_C/) | Tipos e memória em C |
| [09_Depuracao_C](09_Depuracao_C/) | Depuração em C |
| [10_Estruturas_Controle](10_Estruturas_Controle/) | Estruturas de controle |
| [11_Sistemas_Operacionais](11_Sistemas_Operacionais/) | Sistemas operacionais em C — Linux/POSIX |

A numeração dos módulos organiza os assuntos, mas não estabelece necessariamente uma sequência obrigatória de estudo. A numeração nos nomes dos arquivos também não deve ser tomada, por si só, como uma ordem de leitura.

## Localização dos materiais

Consulte [inventario.csv](inventario.csv), o índice completo dos 178 materiais presentes nos módulos. O arquivo utiliza o separador `;` e as colunas `modulo` e `arquivo`. Para localizar um material a partir da raiz do repositório, combine os valores como `modulo/arquivo`.

As entradas estão ordenadas por módulo e, dentro de cada módulo, por nome de arquivo. O índice inclui os documentos Markdown e os arquivos-fonte em C dos módulos. Não inclui os documentos de governança, o próprio inventário nem este README.

Os módulos 01, 02, 03, 07, 08, 09 e 10 possuem `exercicio.md` e `gabarito.md` nas respectivas pastas. Consulte o primeiro para o enunciado e o segundo para as respostas e orientações correspondentes. Os módulos 04, 05 e 06 não possuem esses arquivos.

O módulo [11 — Sistemas Operacionais](11_Sistemas_Operacionais/) contém o [exercício de processos e comunicação entre processos](11_Sistemas_Operacionais/exercicio.md), as [orientações do gabarito](11_Sistemas_Operacionais/gabarito1.md) e os códigos das [partes A](11_Sistemas_Operacionais/gabarito1a.c) e [B](11_Sistemas_Operacionais/gabarito1b.c).

## Curadoria e governança

O diretório [curadoria](curadoria/) reúne o [checklist de observações, decisões e pendências](curadoria/checklist.md). As [regras operacionais para o Codex](AGENTS.md) ficam na raiz. Esses documentos acompanham a manutenção do acervo e não são materiais didáticos indexados no CSV.
