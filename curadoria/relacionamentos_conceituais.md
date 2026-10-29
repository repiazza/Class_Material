# Relacionamentos conceituais do acervo — proposta inicial

**Estado:** proposta para deliberação humana; não homologada como trilha de aprendizagem.  
**Base documental:** 12 catálogos semânticos atualizados, [inventario.csv](../inventario.csv) e [vocabulário controlado](vocabulario_controlado.md), recebidos em 28/10/2026.
**Escopo:** relações selecionadas entre materiais de capítulos diferentes. Nenhum material original foi modificado.

**Uso operacional:** fonte documental auxiliar de propostas. Os catálogos semânticos e o vocabulário mestre continuam sendo as fontes primárias para os conteúdos e conceitos. A integração deste arquivo não homologa relações nem autoriza alterações nos materiais. Consulte o laudo ao final antes de utilizar uma relação com ressalvas.

## Finalidade e limites

Este mapa explicita ligações pedagógicas **propostas** entre conceitos já descritos nos catálogos. Ele não determina ordem obrigatória de capítulos, não substitui os registros individuais nem comprova inspeção visual dos PNG/JPEG/GIF. Os nomes dos arquivos são chaves de referência, preservadas literalmente. Relações não listadas não são necessariamente inexistentes: esta é uma seleção inicial, não um grafo exaustivo.

**Tipos utilizados:**

- **Pré-requisito conceitual:** conhecimento que facilita compreender ou implementar outro, sem impor cronologia didática.
- **Aprofundamento:** um segundo conjunto retoma o conceito com maior especificidade ou em outra camada de abstração.
- **Aplicação:** um conceito é utilizado em um contexto técnico diferente.
- **Contraste:** aproximação útil para distinguir conceitos parecidos ou homônimos; não representa equivalência.
- **Contextualização:** material que oferece enquadramento técnico para outro.

Cada relação é identificada por `RC-###`, tem justificativa, arquivos de origem/destino e ressalva. A direção origem → destino indica a **leitura sugerida da relação**, não necessariamente pré-requisito nem ordem de estudo. Não há inferência automática por mera coincidência de palavra-chave.

## Visão geral

| ID | Origem | Destino | Tipo | Núcleo da relação |
|---|---|---|---|---|
| RC-001 | 01 | 10 | aplicação | As proposições e conectivos lógicos apresentados no módulo 01 são empregados como condições em `if`, `else` e expressões lógicas do módulo 10 |
| RC-002 | 01 | 12 | aprofundamento | Os conectivos e as tabelas-verdade introdutórios são retomados em linguagem algébrica e representação de circuitos |
| RC-003 | 01 | 03 | contraste | Os materiais permitem comparar conectivos lógicos sobre proposições com operadores aplicados bit a bit a operandos binários |
| RC-004 | 02 | 03 | pré-requisito conceitual | A leitura de operandos binários e posições de bits sustenta a interpretação de máscaras, deslocamentos e operações bitwise |
| RC-005 | 02 | 08 | aprofundamento | A representação de valores e o conceito de byte reaparecem na discussão sobre tipos, tamanho de objetos e organização de memória |
| RC-006 | 02 | 12 | aplicação | Combinações de valores binários são usadas como entradas de tabelas-verdade de funções lógicas e circuitos digitais |
| RC-007 | 03 | 12 | aplicação | As operações AND, OR e NOT são documentadas tanto na manipulação bitwise em C do capítulo 03 quanto nas funções booleanas e portas descritas em algebra_booleana.png e circuitos_simplificados.png do capítulo 12. |
| RC-008 | 10 | 04 | aplicação | Estruturas condicionais e validação de entrada sustentam decisões de parsing e tratamento de argumentos de linha de comando |
| RC-009 | 08 | 04 | aplicação | Strings, arrays e ponteiros ajudam a compreender `argv` e a manipulação textual dos argumentos |
| RC-010 | 04 | 11 | aprofundamento | A passagem de argumentos e ambiente é retomada no contexto de processos e da família `exec` |
| RC-011 | 08 | 05 | pré-requisito conceitual | Ponteiros, alocação dinâmica e acesso indireto fundamentam a implementação das estruturas encadeadas descritas no módulo 05 |
| RC-012 | 05 | 08 | contraste | A navegação em estruturas encadeadas e a indexação em arrays são comparadas nos materiais de memória |
| RC-013 | 08 | 09 | aplicação | Endereços, ponteiros e estado de memória são objetos de inspeção em sessões de depuração com GDB |
| RC-014 | 05 | 09 | aplicação | Propõe-se aplicar os recursos de depuração do capítulo 09 à investigação de operações sobre estruturas encadeadas do capítulo 05, como o encadeamento e a liberação de nós. Os destinos descrevem erros de memória e inspeção de ponteiros, não uma sessão de depuração da lista do capítulo 05. |
| RC-015 | 07 | 09 | contraste | O registro por trace/log é apresentado como forma de observação distinta da depuração interativa |
| RC-016 | 06 | 07 | aplicação | A persistência entre execuções e o ciclo de gravação/leitura com fopen, fprintf, fscanf e fclose descritos em arquivos1.png e arquivos2.png oferecem base para os registros de execução em arquivo mantido em append propostos no exercício e no gabarito de TRACE do capítulo 07. |
| RC-017 | 06 | 11 | aprofundamento | Operações de entrada/saída são retomadas no nível de descritores, redirecionamento, buffering e comunicação com o kernel |
| RC-018 | 04 | 11 | aplicação | Variáveis de ambiente e argumentos reaparecem na criação e execução de processos |
| RC-019 | 10 | 11 | aplicação | Os textos e códigos de referência do capítulo 11 demonstram a aplicação de laços e decisões ao gerenciamento de processos: os dois gabaritos usam for (;;) e if no menu e na distinção pai/filho; iAguardarFilho usa do/while com waitpid; a versão B usa while e if nas rotinas de leitura/escrita dos pipes. |
| RC-020 | 11 | 09 | contextualização | A distinção entre programa e processo e a noção de espaço de endereçamento contextualizam o estado observado durante a depuração |
| RC-021 | 08 | 11 | aprofundamento | As representações de memória do programa são retomadas na anatomia de processos, incluindo heap e stack |
| RC-022 | 01 | 12 | aprofundamento | Os fundamentos de proposições, valores lógicos, conectivos e tabelas-verdade documentados no capítulo 01 são retomados e aprofundados no capítulo 12 por leis de De Morgan e mapas de Karnaugh para transformar e simplificar expressões booleanas. |
| RC-023 | 03 | 08 | contextualização | Os exemplos de máscaras e deslocamentos em C do capítulo 03 oferecem um contexto de uso para discutir a representação, os tamanhos e os limites dos tipos documentados em data_types.png e sizeof_C.png do capítulo 08. |
| RC-024 | 07 | 11 | contextualização | Propõe-se contextualizar a observação de eventos por TRACE do capítulo 07 em relação aos conceitos de fluxos de saída e buffering descritos no capítulo 11, distinguindo o registro de eventos, os destinos das mensagens e o envio de dados após fflush. |
| RC-025 | 05 | 11 | contraste | O termo pilha aparece em estruturas de dados e na organização da execução de processos; os materiais permitem explicitar a diferença |
| RC-026 | 09 | 10 | contraste | Os termos `break` e `continue` aparecem como comandos do GDB e como instruções da linguagem C, com semânticas distintas |

## Relações propostas e evidências documentais

### RC-001 — 01 → 10 · aplicação

**Justificativa documental:** As proposições e conectivos lógicos apresentados no módulo 01 são empregados como condições em `if`, `else` e expressões lógicas do módulo 10.

**Origem (01_Logica_e_Raciocinio):** [`logica_booleana2.png`](../01_Logica_e_Raciocinio/logica_booleana2.png), [`problemas_condicoes3.png`](../01_Logica_e_Raciocinio/problemas_condicoes3.png).

**Destino (10_Estruturas_Controle):** [`if.png`](../10_Estruturas_Controle/if.png), [`operadores_logicos.png`](../10_Estruturas_Controle/operadores_logicos.png).

**Limite de interpretação:** Não implica que todo uso de estruturas de controle exija estudo formal prévio de tabelas-verdade.

### RC-002 — 01 → 12 · aprofundamento

**Justificativa documental:** Os conectivos e as tabelas-verdade introdutórios são retomados em linguagem algébrica e representação de circuitos.

**Origem (01_Logica_e_Raciocinio):** [`p_and_q.gif`](../01_Logica_e_Raciocinio/p_and_q.gif), [`p_or_q.gif`](../01_Logica_e_Raciocinio/p_or_q.gif), [`logica_booleana2.png`](../01_Logica_e_Raciocinio/logica_booleana2.png).

**Destino (12_Organizacao_Computadores):** [`algebra_booleana.png`](../12_Organizacao_Computadores/algebra_booleana.png), [`fundamentos.png`](../12_Organizacao_Computadores/fundamentos.png).

**Limite de interpretação:** Os materiais tratam contextos diferentes: proposições e projeto de circuitos.

### RC-003 — 01 → 03 · contraste

**Justificativa documental:** Os materiais permitem comparar conectivos lógicos sobre proposições com operadores aplicados bit a bit a operandos binários.

**Origem (01_Logica_e_Raciocinio):** [`logica_booleana2.png`](../01_Logica_e_Raciocinio/logica_booleana2.png), [`p_xor_q.gif`](../01_Logica_e_Raciocinio/p_xor_q.gif).

**Destino (03_Operacoes_Bitwise):** [`operacao_bit_a_bit.png`](../03_Operacoes_Bitwise/operacao_bit_a_bit.png), [`xor.png`](../03_Operacoes_Bitwise/xor.png).

**Limite de interpretação:** Não confundir AND lógico com AND bitwise.

### RC-004 — 02 → 03 · pré-requisito conceitual

**Justificativa documental:** A leitura de operandos binários e posições de bits sustenta a interpretação de máscaras, deslocamentos e operações bitwise.

**Origem (02_Sistemas_de_Numeracao):** [`bit.png`](../02_Sistemas_de_Numeracao/bit.png), [`msb_lsb.png`](../02_Sistemas_de_Numeracao/msb_lsb.png), [`combinacao_bits.png`](../02_Sistemas_de_Numeracao/combinacao_bits.png).

**Destino (03_Operacoes_Bitwise):** [`operadores_bitwise.png`](../03_Operacoes_Bitwise/operadores_bitwise.png), [`mascara_bitwise.png`](../03_Operacoes_Bitwise/mascara_bitwise.png), [`bitwise_shift.png`](../03_Operacoes_Bitwise/bitwise_shift.png).

**Limite de interpretação:** Pré-requisito conceitual, não ordem obrigatória de apresentação dos arquivos.

### RC-005 — 02 → 08 · aprofundamento

**Justificativa documental:** A representação de valores e o conceito de byte reaparecem na discussão sobre tipos, tamanho de objetos e organização de memória.

**Origem (02_Sistemas_de_Numeracao):** [`bit_byte_nibble.png`](../02_Sistemas_de_Numeracao/bit_byte_nibble.png), [`signed_unsigned.png`](../02_Sistemas_de_Numeracao/signed_unsigned.png).

**Destino (08_Tipos_e_Memoria_C):** [`data_types.png`](../08_Tipos_e_Memoria_C/data_types.png), [`sizeof_C.png`](../08_Tipos_e_Memoria_C/sizeof_C.png), [`sizeof_ptr_vs_var.png`](../08_Tipos_e_Memoria_C/sizeof_ptr_vs_var.png).

**Limite de interpretação:** Byte no contexto de `sizeof` segue a definição da linguagem C; não universalizar oito bits.

### RC-006 — 02 → 12 · aplicação

**Justificativa documental:** Combinações de valores binários são usadas como entradas de tabelas-verdade de funções lógicas e circuitos digitais.

**Origem (02_Sistemas_de_Numeracao):** [`combinacao_bits.png`](../02_Sistemas_de_Numeracao/combinacao_bits.png), [`contagem_0_a_15.gif`](../02_Sistemas_de_Numeracao/contagem_0_a_15.gif).

**Destino (12_Organizacao_Computadores):** [`tabela_verdade_4_5_variaveis.png`](../12_Organizacao_Computadores/tabela_verdade_4_5_variaveis.png), [`canonicas.png`](../12_Organizacao_Computadores/canonicas.png).

**Limite de interpretação:** A relação é de representação, não equivalência entre numeração e lógica.

### RC-007 — 03 → 12 · aplicação

**Justificativa documental:** As operações AND, OR e NOT são documentadas tanto na manipulação bitwise em C do capítulo 03 quanto nas funções booleanas e portas descritas em `algebra_booleana.png` e `circuitos_simplificados.png` do capítulo 12.

**Origem (03_Operacoes_Bitwise):** [`operadores_bitwise.png`](../03_Operacoes_Bitwise/operadores_bitwise.png), [`xor.png`](../03_Operacoes_Bitwise/xor.png).

**Destino (12_Organizacao_Computadores):** [`algebra_booleana.png`](../12_Organizacao_Computadores/algebra_booleana.png), [`circuitos_simplificados.png`](../12_Organizacao_Computadores/circuitos_simplificados.png).

**Limite de interpretação:** A relação restringe-se a AND, OR e NOT, sem equiparar a semântica dos operadores C à das funções booleanas. `xor.png` permanece como referência da origem para contraste OR/XOR; sua presença não constitui evidência de XOR nos destinos do capítulo 12.

### RC-008 — 10 → 04 · aplicação

**Justificativa documental:** Estruturas condicionais e validação de entrada sustentam decisões de parsing e tratamento de argumentos de linha de comando.

**Origem (10_Estruturas_Controle):** [`if_elseif_else.png`](../10_Estruturas_Controle/if_elseif_else.png), [`switch_case.png`](../10_Estruturas_Controle/switch_case.png).

**Destino (04_Argumentos_CommandLine):** [`arg_validation.png`](../04_Argumentos_CommandLine/arg_validation.png), [`parsing_argc_argv.png`](../04_Argumentos_CommandLine/parsing_argc_argv.png).

**Limite de interpretação:** Não afirmar que os materiais estabelecem dependência formal entre capítulos.

### RC-009 — 08 → 04 · aplicação

**Justificativa documental:** Strings, arrays e ponteiros ajudam a compreender `argv` e a manipulação textual dos argumentos.

**Origem (08_Tipos_e_Memoria_C):** [`array_ponteiros.png`](../08_Tipos_e_Memoria_C/array_ponteiros.png), [`percorrendo_string.png`](../08_Tipos_e_Memoria_C/percorrendo_string.png).

**Destino (04_Argumentos_CommandLine):** [`argc_argv.png`](../04_Argumentos_CommandLine/argc_argv.png), [`string_parsing.png`](../04_Argumentos_CommandLine/string_parsing.png).

**Limite de interpretação:** Relacionar estruturas de dados de C aos argumentos, sem supor implementação interna não descrita.

### RC-010 — 04 → 11 · aprofundamento

**Justificativa documental:** A passagem de argumentos e ambiente é retomada no contexto de processos e da família `exec`.

**Origem (04_Argumentos_CommandLine):** [`argc_argv.png`](../04_Argumentos_CommandLine/argc_argv.png), [`envp.png`](../04_Argumentos_CommandLine/envp.png), [`env_fork.png`](../04_Argumentos_CommandLine/env_fork.png).

**Destino (11_Sistemas_Operacionais):** [`args_env.png`](../11_Sistemas_Operacionais/args_env.png), [`exec2.png`](../11_Sistemas_Operacionais/exec2.png).

**Limite de interpretação:** Distinguir argumentos recebidos em `main` daqueles fornecidos a uma nova imagem de processo.

### RC-011 — 08 → 05 · pré-requisito conceitual

**Justificativa documental:** Ponteiros, alocação dinâmica e acesso indireto fundamentam a implementação das estruturas encadeadas descritas no módulo 05.

**Origem (08_Tipos_e_Memoria_C):** [`ponteiros_simplificado.png`](../08_Tipos_e_Memoria_C/ponteiros_simplificado.png), [`malloc_free.png`](../08_Tipos_e_Memoria_C/malloc_free.png), [`struct_operador_seta.png`](../08_Tipos_e_Memoria_C/struct_operador_seta.png).

**Destino (05_Estruturas_de_Dados):** [`lista1.jpeg`](../05_Estruturas_de_Dados/lista1.jpeg), [`exercicio1.md`](../05_Estruturas_de_Dados/exercicio1.md), [`fila.jpeg`](../05_Estruturas_de_Dados/fila.jpeg).

**Limite de interpretação:** Relação de fundamentos para implementação, não prescrição de sequência de aulas.

### RC-012 — 05 → 08 · contraste

**Justificativa documental:** A navegação em estruturas encadeadas e a indexação em arrays são comparadas nos materiais de memória.

**Origem (05_Estruturas_de_Dados):** [`lista1.jpeg`](../05_Estruturas_de_Dados/lista1.jpeg), [`lista_remocao_meio.gif`](../05_Estruturas_de_Dados/lista_remocao_meio.gif).

**Destino (08_Tipos_e_Memoria_C):** [`array_vs_lista_navegacao.gif`](../08_Tipos_e_Memoria_C/array_vs_lista_navegacao.gif), [`indices_enderecos_array.png`](../08_Tipos_e_Memoria_C/indices_enderecos_array.png).

**Limite de interpretação:** Não tratar lista encadeada como memória contígua.

### RC-013 — 08 → 09 · aplicação

**Justificativa documental:** Endereços, ponteiros e estado de memória são objetos de inspeção em sessões de depuração com GDB.

**Origem (08_Tipos_e_Memoria_C):** [`enderecamento_ponteiros.png`](../08_Tipos_e_Memoria_C/enderecamento_ponteiros.png), [`acesso_inderecao.png`](../08_Tipos_e_Memoria_C/acesso_inderecao.png).

**Destino (09_Depuracao_C):** [`inspecao_memoria.gif`](../09_Depuracao_C/inspecao_memoria.gif), [`runtime.png`](../09_Depuracao_C/runtime.png).

**Limite de interpretação:** Inspeção de memória não equivale a prova de ausência de erros.

### RC-014 — 05 → 09 · aplicação

**Justificativa documental:** Propõe-se aplicar os recursos de depuração do capítulo 09 à investigação de operações sobre estruturas encadeadas do capítulo 05, como o encadeamento e a liberação de nós. Os destinos descrevem erros de memória e inspeção de ponteiros, não uma sessão de depuração da lista do capítulo 05.

**Origem (05_Estruturas_de_Dados):** [`exercicio1.md`](../05_Estruturas_de_Dados/exercicio1.md), [`lista_remocao_inicio.gif`](../05_Estruturas_de_Dados/lista_remocao_inicio.gif).

**Destino (09_Depuracao_C):** [`erros_memoria.png`](../09_Depuracao_C/erros_memoria.png), [`exercicio.md`](../09_Depuracao_C/exercicio.md).

**Limite de interpretação:** É uma possibilidade de transferência pedagógica. Não há exercício integrado documentado entre esses capítulos, e o exercício do GDB não deve ser apresentado como reprodução da lista encadeada do capítulo 05.

### RC-015 — 07 → 09 · contraste

**Justificativa documental:** O registro por trace/log é apresentado como forma de observação distinta da depuração interativa.

**Origem (07_Tracing_e_Execucao):** [`trace.png`](../07_Tracing_e_Execucao/trace.png), [`funcao_trace.jpeg`](../07_Tracing_e_Execucao/funcao_trace.jpeg).

**Destino (09_Depuracao_C):** [`output_vs_log_vs_debug.png`](../09_Depuracao_C/output_vs_log_vs_debug.png), [`comandos_gdb.png`](../09_Depuracao_C/comandos_gdb.png).

**Limite de interpretação:** São técnicas complementares, não substitutas universais.

### RC-016 — 06 → 07 · aplicação

**Justificativa documental:** A persistência entre execuções e o ciclo de gravação/leitura com fopen, fprintf, fscanf e fclose descritos em `arquivos1.png` e `arquivos2.png` oferecem base para os registros de execução em arquivo mantido em append propostos no exercício e no gabarito de TRACE do capítulo 07.

**Origem (06_Arquivos_e_Entrada_Saida):** [`arquivos1.png`](../06_Arquivos_e_Entrada_Saida/arquivos1.png), [`arquivos2.png`](../06_Arquivos_e_Entrada_Saida/arquivos2.png).

**Destino (07_Tracing_e_Execucao):** [`exercicio.md`](../07_Tracing_e_Execucao/exercicio.md), [`gabarito.md`](../07_Tracing_e_Execucao/gabarito.md).

**Limite de interpretação:** A relação associa operações de arquivo à persistência de logs, sem equiparar seus propósitos nem afirmar que os exemplos dos dois capítulos formam um único programa.

### RC-017 — 06 → 11 · aprofundamento

**Justificativa documental:** Operações de entrada/saída são retomadas no nível de descritores, redirecionamento, buffering e comunicação com o kernel.

**Origem (06_Arquivos_e_Entrada_Saida):** [`arquivos1.png`](../06_Arquivos_e_Entrada_Saida/arquivos1.png), [`arquivos2.png`](../06_Arquivos_e_Entrada_Saida/arquivos2.png).

**Destino (11_Sistemas_Operacionais):** [`stdin_stdout_stderr.png`](../11_Sistemas_Operacionais/stdin_stdout_stderr.png), [`stdio_ao_kernel.png`](../11_Sistemas_Operacionais/stdio_ao_kernel.png), [`buffering.png`](../11_Sistemas_Operacionais/buffering.png).

**Limite de interpretação:** Distinguir abstrações de `stdio` e descritores do sistema operacional.

### RC-018 — 04 → 11 · aplicação

**Justificativa documental:** Variáveis de ambiente e argumentos reaparecem na criação e execução de processos.

**Origem (04_Argumentos_CommandLine):** [`env.png`](../04_Argumentos_CommandLine/env.png), [`envp.png`](../04_Argumentos_CommandLine/envp.png).

**Destino (11_Sistemas_Operacionais):** [`args_env.png`](../11_Sistemas_Operacionais/args_env.png), [`fork_exec_wait.png`](../11_Sistemas_Operacionais/fork_exec_wait.png).

**Limite de interpretação:** Não confundir `fork` com `exec`.

### RC-019 — 10 → 11 · aplicação

**Justificativa documental:** Os textos e códigos de referência do capítulo 11 demonstram a aplicação de laços e decisões ao gerenciamento de processos: os dois gabaritos usam `for (;;)` e `if` no menu e na distinção pai/filho; `iAguardarFilho` usa `do/while` com waitpid; a versão B usa `while` e `if` nas rotinas de leitura/escrita dos pipes.

**Origem (10_Estruturas_Controle):** [`while.png`](../10_Estruturas_Controle/while.png), [`for.png`](../10_Estruturas_Controle/for.png), [`if.png`](../10_Estruturas_Controle/if.png).

**Destino (11_Sistemas_Operacionais):** [`exercicio.md`](../11_Sistemas_Operacionais/exercicio.md), [`gabarito1a.c`](../11_Sistemas_Operacionais/gabarito1a.c), [`gabarito1b.c`](../11_Sistemas_Operacionais/gabarito1b.c).

**Limite de interpretação:** A aplicação foi constatada por leitura dos gabaritos, sem executar ou certificar a correção dos programas. Não se afirma o uso de switch nesses códigos.

### RC-020 — 11 → 09 · contextualização

**Justificativa documental:** A distinção entre programa e processo e a noção de espaço de endereçamento contextualizam o estado observado durante a depuração.

**Origem (11_Sistemas_Operacionais):** [`programa_vs_processo.png`](../11_Sistemas_Operacionais/programa_vs_processo.png), [`anatomia_processo.png`](../11_Sistemas_Operacionais/anatomia_processo.png).

**Destino (09_Depuracao_C):** [`runtime.png`](../09_Depuracao_C/runtime.png), [`backtrace_callstack.png`](../09_Depuracao_C/backtrace_callstack.png).

**Limite de interpretação:** Não equiparar call stack, stack trace e pilha de dados.

### RC-021 — 08 → 11 · aprofundamento

**Justificativa documental:** As representações de memória do programa são retomadas na anatomia de processos, incluindo heap e stack.

**Origem (08_Tipos_e_Memoria_C):** [`representacao.png`](../08_Tipos_e_Memoria_C/representacao.png), [`malloc_explicacao.png`](../08_Tipos_e_Memoria_C/malloc_explicacao.png).

**Destino (11_Sistemas_Operacionais):** [`anatomia_processo.png`](../11_Sistemas_Operacionais/anatomia_processo.png), [`programa_vs_processo.png`](../11_Sistemas_Operacionais/programa_vs_processo.png).

**Limite de interpretação:** Alocação de memória em C e organização do processo são níveis distintos de abstração.

### RC-022 — 01 → 12 · aprofundamento

**Justificativa documental:** Os fundamentos de proposições, valores lógicos, conectivos e tabelas-verdade documentados no capítulo 01 são retomados e aprofundados no capítulo 12 por leis de De Morgan e mapas de Karnaugh para transformar e simplificar expressões booleanas.

**Origem (01_Logica_e_Raciocinio):** [`logica_booleana.png`](../01_Logica_e_Raciocinio/logica_booleana.png), [`problemas_condicoes4.png`](../01_Logica_e_Raciocinio/problemas_condicoes4.png).

**Destino (12_Organizacao_Computadores):** [`demorgan.png`](../12_Organizacao_Computadores/demorgan.png), [`karnaugh1.png`](../12_Organizacao_Computadores/karnaugh1.png).

**Limite de interpretação:** As leis de equivalência e os métodos de simplificação pertencem aos destinos do capítulo 12; não se atribui sua apresentação às origens do capítulo 01 nem se impõe sequência curricular obrigatória.

### RC-023 — 03 → 08 · contextualização

**Justificativa documental:** Os exemplos de máscaras e deslocamentos em C do capítulo 03 oferecem um contexto de uso para discutir a representação, os tamanhos e os limites dos tipos documentados em `data_types.png` e `sizeof_C.png` do capítulo 08.

**Origem (03_Operacoes_Bitwise):** [`bitwise_mascaras.gif`](../03_Operacoes_Bitwise/bitwise_mascaras.gif), [`bitwise_shift_em_c.gif`](../03_Operacoes_Bitwise/bitwise_shift_em_c.gif).

**Destino (08_Tipos_e_Memoria_C):** [`data_types.png`](../08_Tipos_e_Memoria_C/data_types.png), [`sizeof_C.png`](../08_Tipos_e_Memoria_C/sizeof_C.png).

**Limite de interpretação:** A direção 03 → 08 indica usar operações bitwise como contexto para a discussão dos tipos. Os exemplos de sizeof não demonstram diretamente máscaras ou deslocamentos, não fixam a largura de int e não constituem demonstração prática integrada; o enquadramento pedagógico permanece proposto.

### RC-024 — 07 → 11 · contextualização

**Justificativa documental:** Propõe-se contextualizar a observação de eventos por TRACE do capítulo 07 em relação aos conceitos de fluxos de saída e buffering descritos no capítulo 11, distinguindo o registro de eventos, os destinos das mensagens e o envio de dados após fflush.

**Origem (07_Tracing_e_Execucao):** [`trace2.png`](../07_Tracing_e_Execucao/trace2.png), [`trace3.png`](../07_Tracing_e_Execucao/trace3.png).

**Destino (11_Sistemas_Operacionais):** [`printf_fflush.gif`](../11_Sistemas_Operacionais/printf_fflush.gif), [`stdin_stdout_stderr.png`](../11_Sistemas_Operacionais/stdin_stdout_stderr.png).

**Limite de interpretação:** É uma associação conceitual proposta, não uma demonstração documentada dos efeitos do buffering sobre os logs citados. Preserva-se a leitura 07 → 11 para discussão de observabilidade, sem equiparar log, stdout e stderr nem inverter automaticamente a direção.

### RC-025 — 05 → 11 · contraste

**Justificativa documental:** O termo pilha aparece em estruturas de dados e na organização da execução de processos; os materiais permitem explicitar a diferença.

**Origem (05_Estruturas_de_Dados):** [`pilha.jpeg`](../05_Estruturas_de_Dados/pilha.jpeg), [`pilha_conceitos.png`](../05_Estruturas_de_Dados/pilha_conceitos.png).

**Destino (11_Sistemas_Operacionais):** [`anatomia_processo.png`](../11_Sistemas_Operacionais/anatomia_processo.png).

**Limite de interpretação:** Não unificar pilha de dados, stack de execução e call stack.

### RC-026 — 09 → 10 · contraste

**Justificativa documental:** Os termos `break` e `continue` aparecem como comandos do GDB e como instruções da linguagem C, com semânticas distintas.

**Origem (09_Depuracao_C):** [`comandos_gdb.png`](../09_Depuracao_C/comandos_gdb.png), [`comandos_gdb2.png`](../09_Depuracao_C/comandos_gdb2.png).

**Destino (10_Estruturas_Controle):** [`break.png`](../10_Estruturas_Controle/break.png), [`continue.png`](../10_Estruturas_Controle/continue.png).

**Limite de interpretação:** Homônimos: não converter em relação de equivalência ou pré-requisito.

## Assuntos que exigem deliberação ou verificação posterior

1. **Homônimos `break` e `continue`:** diferenciar comando do GDB e instrução da linguagem C; a relação RC-026 é de contraste, não equivalência.
2. **`byte`:** distinguir a apresentação de oito bits no módulo 02 da unidade definida por `sizeof` no contexto da linguagem C (módulo 08); não impor generalizações indevidas.
3. **Pilha e stack:** distinguir estrutura de dados, pilha de execução, call stack e stack trace; não fundir termos só por semelhança.
4. **Exercícios e gabaritos:** as relações propostas não certificam que exercícios de capítulos distintos possam ser reutilizados uns nos outros sem adaptação.
5. **Checklist histórico:** `curadoria/checklist.md` contém deliberações de curadoria anteriores. Este mapa não altera seus estados nem transforma propostas antigas em autorização de execução.

## Critérios para revisão e manutenção

- A decisão humana poderá marcar cada `RC-###` como **APROVADA**, **REJEITADA** ou **PENDENTE** em processo posterior. Todas permanecem **PENDENTES** nesta versão.
- Uma relação aprovada poderá ser usada para sugerir combinações de materiais; isso não implica autorização para editar os originais.
- Ao atualizar uma relação, confirmar os nomes dos arquivos no inventário e a descrição correspondente nos catálogos; consultar o vocabulário mestre para distinguir etiquetas e homônimos.
- Não criar novas relações somente porque dois arquivos compartilham uma etiqueta. Exigir uma justificativa conceitual específica.
- Preservar IDs existentes ao revisar relações; novos vínculos recebem novos IDs, sem renumerar os anteriores.

## Laudo de conferência documental — integração

Este laudo verifica sustentação documental, não deliberação pedagógica. Todas as RC continuam **PENDENTES**, inclusive as marcadas como sustentadas. A integração inicial preservou tipos, direções, justificativas e limites. A revisão dirigida subsequente, explicitamente autorizada, altera somente RC-007, RC-014, RC-016, RC-019, RC-022, RC-023 e RC-024; as demais 19 propostas e seus resultados anteriores permanecem intactos.

Na conferência inicial, foram verificadas 26 propostas, 111 citações de materiais e 91 arquivos distintos: todos existem, constam do inventário e possuem registro no catálogo do capítulo indicado. A consulta inicial abrangeu os 12 catálogos e os conceitos correspondentes no vocabulário mestre. Nesta revisão, foram consultados somente os registros pertinentes às sete RC e os materiais textuais necessários, incluindo os dois gabaritos C para RC-019, sem repetir a auditoria integral. O mapa atualizado contém 113 citações e 91 materiais distintos; a contagem é estrutural, não uma nova auditoria das 26 propostas. Não houve nova inspeção visual nem execução de programas.

- **Sustentada:** as descrições documentais sustentam a relação e o tipo proposto, sem homologação curricular.
- **Plausível:** a transferência ou o enquadramento pedagógico exige interpretação ou reforço de evidências.
- **Insuficiente na formulação atual:** parte relevante da justificativa não é sustentada pelos registros citados; isso não demonstra inexistência do conteúdo visual.

| Relação | Resultado documental | Evidência e ressalva para deliberação |
|---|---|---|
| RC-001 | Sustentada | Conectivos em `logica_booleana2.png`/`problemas_condicoes3.png` e condições/operadores em `if.png`/`operadores_logicos.png` sustentam a aplicação; não estabelecem cronologia. |
| RC-002 | Sustentada | Tabelas de AND/OR no capítulo 01 e álgebra, leis e portas em `algebra_booleana.png`/`fundamentos.png` sustentam o aprofundamento. |
| RC-003 | Sustentada | `operacao_bit_a_bit.png` documenta explicitamente a comparação entre avaliação lógica e transformação de bits; o mestre distingue esses operadores. |
| RC-004 | Sustentada | Bit, pesos e posições no capítulo 02 fundamentam a leitura de operandos, máscaras e deslocamentos descritos no capítulo 03; pré-requisito é conceitual, não curricular. |
| RC-005 | Sustentada | Os registros citados tratam representação de inteiros, byte, tipos e sizeof. Preservar a ressalva sobre byte e tamanhos dependentes da implementação. |
| RC-006 | Sustentada | A enumeração de combinações no capítulo 02 corresponde às entradas de tabelas e formas canônicas descritas no capítulo 12. |
| RC-007 | Sustentada após revisão | Fundamentação restringida a AND/OR/NOT, documentados em `operadores_bitwise.png` e nos dois destinos do capítulo 12. A afirmação sobre XOR no destino foi retirada; não se realizou inspeção visual nem se presume sua presença. |
| RC-008 | Sustentada | Os registros de condicionais do capítulo 10 e de validação/parsing do capítulo 04 descrevem decisões e tratamento de parâmetros; o tipo aplicação é coerente. |
| RC-009 | Sustentada | Array de ponteiros e percurso de string no capítulo 08 articulam-se à descrição de argv e parsing textual no capítulo 04. |
| RC-010 | Sustentada, com sobreposição | Argumentos, ambiente e herança no capítulo 04 são retomados nas variantes de exec do capítulo 11. Há sobreposição parcial com RC-018, sem redundância demonstrada. |
| RC-011 | Sustentada | Indireção, ponteiros e malloc/free no capítulo 08 fundamentam os nós encadeados e a implementação exigida em `lista1.jpeg`/`exercicio1.md`; `fila.jpeg` oferece a representação da estrutura. |
| RC-012 | Sustentada | `array_vs_lista_navegacao.gif` documenta explicitamente o contraste entre indexação direta e percurso encadeado, em consonância com os materiais de lista. |
| RC-013 | Sustentada | Endereços e indireção são documentados no capítulo 08; inspeção de variáveis, ponteiros e memória está descrita em `inspecao_memoria.gif`/`runtime.png`. |
| RC-014 | Plausível; interpretação pedagógica | A redação explicita a possibilidade de aplicar depuração à manipulação/liberação de nós. As fontes não descrevem exercício integrado nem sessão GDB da lista do capítulo 05; essa transferência pedagógica continua pendente. |
| RC-015 | Sustentada | `funcao_trace.jpeg` descreve registro de eventos e `output_vs_log_vs_debug.png` compara explicitamente saída, log e depuração interativa. |
| RC-016 | Sustentada após revisão | Origens substituídas por `arquivos1.png` e `arquivos2.png`: persistência entre execuções e fopen/fprintf/fscanf/fclose. Os destinos descrevem log em append. A base documental foi fortalecida, sem afirmar identidade entre programas. |
| RC-017 | Sustentada | Persistência/stdio no capítulo 06 e descritores, buffering e chamadas ao kernel no capítulo 11 sustentam a mudança de nível de abstração. |
| RC-018 | Sustentada, com sobreposição | As descrições de ambiente/argumentos e `args_env.png` sustentam o vínculo; `fork_exec_wait.png` documenta criação, execução e espera. Comparar a finalidade com RC-010 antes de eventual consolidação humana. |
| RC-019 | Sustentada por evidência textual direta | Origens ajustadas para while/for/if e destinos para o exercício e os dois gabaritos C. A leitura confirma `for (;;)`/`if` nos menus, `do/while` em `iAguardarFilho` e `while`/`if` nas rotinas de pipes da versão B. Sem execução nem certificação dos programas. |
| RC-020 | Sustentada | Programa/processo e anatomia de memória contextualizam runtime e frames no GDB. A distinção entre call stack, stack trace e pilha de dados é mantida no mestre. |
| RC-021 | Sustentada | A representação dos dados e alocação dinâmica no capítulo 08 são retomadas no espaço de endereçamento, heap e stack documentados em `anatomia_processo.png`. |
| RC-022 | Sustentada após revisão | Tipo alterado para aprofundamento: proposições, conectivos e tabelas na origem; leis de De Morgan e Karnaugh nos destinos. Retirada a atribuição de regras de equivalência/simplificação ao capítulo 01. Homologação pedagógica continua pendente. |
| RC-023 | Plausível; contextualização explicitada | Tipo alterado para contextualização, mantida a direção 03→08; `sizeof_C2.png` substituído por `sizeof_C.png` para tratar tamanho de tipos. Os exemplos bitwise são contexto de uso, não demonstração conjunta com sizeof. O enquadramento pedagógico ainda depende de interpretação. |
| RC-024 | Plausível; enquadramento a avaliar | A redação apresenta associação conceitual entre observação, fluxos e buffering. Não afirma efeito de fflush sobre os logs citados nem demonstração conjunta; mantém tipo/direção e a distinção entre log/stdout/stderr. |
| RC-025 | Sustentada | Pilha como estrutura LIFO e stack como região de execução aparecem com sentidos distintos nas fontes. O contraste é coerente com as definições do mestre. |
| RC-026 | Sustentada | `comandos_gdb.png` descreve break/continue do GDB; `break.png`/`continue.png` descrevem as instruções C. O mestre já explicita os dois contextos; não há equivalência ou pré-requisito. |

**Síntese após revisão dirigida:** os 19 resultados anteriores foram preservados. RC-007, RC-016, RC-019 e RC-022 tiveram sua fundamentação fortalecida; RC-014, RC-023 e RC-024 continuam plausíveis com ressalvas. O laudo passa a reunir 23 relações sustentadas e três plausíveis, sem relação ainda insuficientemente fundamentada na formulação revista. Isso não equivale a uma revalidação integral nem a homologação pedagógica: todas as 26 permanecem PENDENTES. RC-010 e RC-018 permanecem relações distintas, sem consolidação; compartilham parte do escopo. RC-002/RC-022 também aproximam os mesmos capítulos, mas têm destinos e propósitos diferentes. Não se demonstrou redundância que justifique exclusão automática. Nenhuma contradição global entre relações foi demonstrada: por exemplo, RC-011 e RC-012 têm direções opostas e tipos distintos, sem impor uma sequência curricular circular.

**Correções documentais executadas:** o mapa foi transferido de `12_Organizacao_Computadores/relacionamentos_conceituais.md` para `curadoria/relacionamentos_conceituais.md`, destino solicitado. Na integração inicial, os 111 links de materiais já usavam `../capítulo/arquivo` e permanecem corretos no novo local. As referências administrativas foram convertidas em links relativos e a navegação foi acrescentada ao README e às instruções operacionais. Nenhum arquivo material citado precisou ser substituído, renomeado ou removido. O inventário não foi alterado: seus 255 arquivos continuam nos capítulos, enquanto este mapa é governança documental fora desse escopo.

Na revisão dirigida, as referências de RC-016 e RC-019 foram ajustadas às evidências mais diretas, e RC-023 passou a citar sizeof de tipos. Nenhum material físico foi modificado. As ressalvas persistentes de RC-014, RC-023 e RC-024, as sobreposições já registradas e a homologação de todas as propostas dependem de deliberação humana. Não foram alterados os catálogos, o vocabulário mestre ou o checklist histórico.

## Proveniência

A fundamentação é **documental**: descrições e representações registradas nos catálogos, associadas aos arquivos existentes no inventário. Na integração inicial não houve revisão dos arquivos `.c`. A revisão dirigida posterior incluiu leitura estática de `gabarito1a.c` e `gabarito1b.c` exclusivamente para fundamentar RC-019, sem execução, modificação ou auditoria de correção dos programas. Não houve nova homologação visual dos materiais nem validação pedagógica externa. O documento continua sendo uma proposta para deliberação humana.
