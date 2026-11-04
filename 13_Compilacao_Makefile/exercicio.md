# 13 — Compilação e Makefile
## Exercício — Compilação modular e automatização com GNU Make

**Tema:** GCC, flags de compilação, arquivos objeto, linkedição, Makefiles e compilação incremental.

**Objetivo:** compilar um programa C composto por múltiplos módulos e, posteriormente, automatizar sua construção utilizando o GNU Make.

O exercício será dividido em duas etapas. A **Etapa A** deverá ser concluída antes da **Etapa B**, que reutilizará integralmente o projeto e os conhecimentos adquiridos.

### Projeto fornecido

O aluno receberá o arquivo `projeto_base_exercicio.zip`, contendo um programa funcional escrito em C, composto pela função `vSoma()`, uma biblioteca simples de log e seus respectivos arquivos de cabeçalho.

O pacote deverá ser extraído antes do início da Etapa A. Os arquivos fornecidos constituem a base de trabalho para ambas as etapas do exercício.

A estrutura inicial será:

```text
projeto/
├── src/
│   ├── main.c
│   ├── calc.c
│   └── log.c
├── include/
│   ├── calc.h
│   └── log.h
├── obj/
└── bin/
```

Os módulos possuem as seguintes responsabilidades:

- `main.c`: executa o programa, chama `vSoma()` e registra o resultado.
- `calc.c`: implementa a função `vSoma()`.
- `log.c`: implementa a função de registro de mensagens.
- `calc.h` e `log.h`: disponibilizam as declarações necessárias aos módulos.

**Não será necessário implementar ou modificar as funções fornecidas durante a Etapa A.**

---

## Etapa A — Compilação manual com GCC

Utilizando exclusivamente o GCC e os arquivos fornecidos, realize a compilação do projeto.

### Requisitos

1. Compile separadamente `main.c`, `calc.c` e `log.c`, gerando os respectivos arquivos objeto (`.o`) no diretório `obj/`.

2. Utilize a opção `-I` para informar ao compilador o diretório que contém os arquivos de cabeçalho.

3. Utilize as seguintes opções de compilação:

   - `-std=c89`
   - `-Wall`
   - `-Wextra`
   - `-pedantic`

4. Realize a linkedição dos três arquivos objeto, gerando o executável `bin/app`.

5. Execute o programa e verifique se o resultado da soma e as mensagens de log são apresentados corretamente.

6. Repita o processo utilizando as opções `-g -O0`, produzindo uma versão adequada à depuração.

### Resultado esperado

Ao concluir a Etapa A, o diretório `obj/` deverá conter:

```text
main.o
calc.o
log.o
```

O diretório `bin/` deverá conter o executável `app`.

**Importante:** a compilação dos arquivos `.c` e a linkedição deverão ser realizadas em comandos separados. Não utilize Makefile nesta etapa.

---

## Etapa B — Automatização com Makefile

Utilizando o mesmo projeto fornecido na Etapa A, sem substituir ou recriar os arquivos originais, desenvolva um arquivo chamado `Makefile` na raiz do projeto.

Os arquivos objeto e o executável produzidos anteriormente poderão ser removidos com `make clean`, permitindo validar a construção completa por meio do Makefile.

O objetivo é substituir os comandos manuais por um processo automatizado, capaz de identificar quais arquivos precisam ser recompilados.

### Requisitos

1. Defina variáveis para o compilador GCC, as opções de compilação e os diretórios do projeto.

2. Crie uma regra para compilar os arquivos `.c` de `src/`, gerando os respectivos `.o` em `obj/`.

3. Crie uma regra de linkedição que utilize os arquivos objeto para gerar `bin/app`.

4. Utilize variáveis automáticas do Make, como `$@`, `$<` e `$^`, quando apropriado.

5. Implemente os alvos:
   - `all`: construir o executável.
   - `clean`: remover os arquivos gerados pela compilação.

6. Declare os alvos auxiliares em `.PHONY`.

7. Utilize as opções `-MMD -MP` e inclua os arquivos `.d` gerados pelo GCC, permitindo identificar alterações nos headers.

8. Garanta que os diretórios `obj/` e `bin/` sejam criados quando necessário.

### Validação obrigatória

Execute os testes abaixo, observando os comandos realizados pelo Make.

| Teste | Procedimento | Resultado esperado |
|---|---|---|
| 1 | Execute `make` após `make clean`. | Compila os três módulos e realiza a linkedição. |
| 2 | Execute `make` novamente, sem alterações. | Não recompila nem realiza nova linkedição. |
| 3 | Modifique apenas uma mensagem em `src/main.c` e execute `make`. | Recompila somente `main.o` e refaz a linkedição. |
| 4 | Modifique apenas `src/calc.c` e execute `make`. | Recompila somente `calc.o` e refaz a linkedição. |
| 5 | Acrescente um comentário em `include/calc.h` e execute `make`. | Recompila todos os módulos que dependem desse header e refaz a linkedição. |

No Teste 5, considere que `main.c` e `calc.c` incluem `calc.h`, enquanto `log.c` não depende desse arquivo. Portanto, o resultado esperado será a recompilação de `main.o` e `calc.o`, mas não de `log.o`.

### Resultado esperado

Ao concluir a Etapa B, o aluno deverá conseguir:

- Construir todo o programa executando apenas `make`.
- Remover os arquivos gerados utilizando `make clean`.
- Recompilar somente os módulos afetados por alterações.
- Identificar automaticamente dependências entre arquivos `.c` e `.h`.
- Preservar a organização dos arquivos objeto e do executável.

---

## Restrições gerais

- Utilize GCC e GNU Make.
- Preserve a estrutura e as funções C fornecidas.
- Não utilize IDEs ou ferramentas externas para automatizar a compilação.
- Não utilize scripts auxiliares para substituir as regras do Makefile.
- Não force a recompilação completa a cada execução de `make`.
- O Makefile deverá funcionar sem exigir alterações manuais nos comandos sempre que um dos três fontes for modificado.

## Critério de conclusão

O exercício estará concluído quando o aluno demonstrar que consegue construir manualmente um programa com múltiplos módulos e automatizar essa construção com um Makefile funcional.

**A principal evidência de aprendizado será a compilação incremental:** ao modificar apenas um arquivo, o Make deverá reconstruir somente os objetos afetados e, quando necessário, gerar novamente o executável.