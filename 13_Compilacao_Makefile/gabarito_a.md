# 13 — Compilação e Makefile
## Gabarito — Etapa A: Compilação manual com GCC

### 1. Objetivo da etapa

Demonstrar a compilação de um programa C composto por três arquivos-fonte, utilizando headers próprios, flags de diagnóstico, geração de arquivos objeto e linkedição separada.

O aluno deverá compreender que cada módulo pode ser compilado independentemente e que os objetos resultantes precisam ser vinculados para produzir o executável.

---

## 2. Arquivos fornecidos ao aluno

Estrutura inicial:

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

### include/calc.h

```c
#ifndef CALC_H
#define CALC_H

void vSoma(int iA, int iB, int *piResultado);

#endif
```

### include/log.h

```c
#ifndef LOG_H
#define LOG_H

void vLog(const char *pcMensagem);

#endif
```

### src/calc.c

```c
#include "calc.h"

void vSoma(int iA, int iB, int *piResultado)
{
  if(piResultado == NULL)
    return;

  *piResultado = iA + iB;
}
```

**Observação:** para utilizar `NULL`, o arquivo deverá incluir `<stddef.h>`. A versão completa e compilável é:

```c
#include <stddef.h>
#include "calc.h"

void vSoma(int iA, int iB, int *piResultado)
{
  if(piResultado == NULL)
    return;

  *piResultado = iA + iB;
}
```

### src/log.c

```c
#include <stdio.h>
#include "log.h"

void vLog(const char *pcMensagem)
{
  if(pcMensagem == NULL)
    return;

  printf("[LOG] %s\n", pcMensagem);
}
```

**Observação:** assim como `calc.c`, `log.c` precisa de uma definição de `NULL`. Como `<stdio.h>` a fornece, não é necessário acrescentar outro header.

### src/main.c

```c
#include <stdio.h>
#include "calc.h"
#include "log.h"

int main(void)
{
  int iResultado;

  iResultado = 0;

  vLog("Iniciando calculadora");

  vSoma(10, 5, &iResultado);

  printf("Resultado: %d\n", iResultado);

  vLog("Calculadora finalizada");

  return 0;
}
```

### Saída esperada

```text
[LOG] Iniciando calculadora
Resultado: 15
[LOG] Calculadora finalizada
```

---

## 3. Compilação dos módulos

Os comandos devem ser executados a partir da raiz do projeto.

### Compilação de main.c

```bash
gcc -std=c89 -Wall -Wextra -pedantic \
    -Iinclude -c src/main.c -o obj/main.o
```

### Compilação de calc.c

```bash
gcc -std=c89 -Wall -Wextra -pedantic \
    -Iinclude -c src/calc.c -o obj/calc.o
```

### Compilação de log.c

```bash
gcc -std=c89 -Wall -Wextra -pedantic \
    -Iinclude -c src/log.c -o obj/log.o
```

Ao final, o diretório `obj/` deverá conter:

```text
obj/
├── main.o
├── calc.o
└── log.o
```

Cada comando deverá gerar um arquivo objeto sem produzir o executável.

---

## 4. Linkedição

Após compilar os três módulos:

```bash
gcc obj/main.o obj/calc.o obj/log.o -o bin/app
```

O GCC deverá utilizar os arquivos objeto para produzir o executável.

A linkedição será bem-sucedida porque:

- `main.o` contém a função `main()`.
- `calc.o` contém a implementação de `vSoma()`.
- `log.o` contém a implementação de `vLog()`.

Os headers disponibilizam declarações durante a compilação, mas não substituem os objetos que contêm as implementações.

### Execução

```bash
./bin/app
```

Resultado:

```text
[LOG] Iniciando calculadora
Resultado: 15
[LOG] Calculadora finalizada
```

---

## 5. Compilação para depuração

O aluno deverá repetir a compilação utilizando `-g -O0`.

```bash
gcc -std=c89 -Wall -Wextra -pedantic \
    -g -O0 -Iinclude -c src/main.c -o obj/main.o

gcc -std=c89 -Wall -Wextra -pedantic \
    -g -O0 -Iinclude -c src/calc.c -o obj/calc.o

gcc -std=c89 -Wall -Wextra -pedantic \
    -g -O0 -Iinclude -c src/log.c -o obj/log.o

gcc obj/main.o obj/calc.o obj/log.o -o bin/app
```

A execução deverá apresentar o mesmo resultado funcional.

As opções utilizadas possuem finalidades distintas:

| Opção | Finalidade |
|---|---|
| `-g` | Inclui informações para depuração. |
| `-O0` | Desabilita as otimizações de compilação. |
| `-Wall` | Habilita um conjunto comum de avisos. |
| `-Wextra` | Habilita avisos adicionais. |
| `-pedantic` | Solicita diagnósticos de construções não conformes ao padrão selecionado. |
| `-std=c89` | Seleciona o padrão ISO C90/C89. |
| `-Iinclude` | Adiciona o diretório de busca dos headers. |
| `-c` | Produz o objeto sem executar a linkedição. |
| `-o` | Define o nome e o caminho do arquivo de saída. |

---

## 6. Considerações específicas para avaliação

### A. Compilação independente

O aluno deve compreender que cada `.c` pode ser compilado separadamente.

Não é necessário fornecer os três arquivos-fonte no mesmo comando.

**Esperado:** três comandos de compilação, produzindo três objetos.

### B. Headers e implementações

O aluno deve distinguir a declaração de uma função da sua implementação.

Por exemplo, `calc.h` permite que `main.c` conheça a assinatura de `vSoma()`, mas é `calc.o` que fornece sua implementação durante a linkedição.

**Esperado:** utilização correta de `-Iinclude` e inclusão de todos os objetos necessários na linkedição.

### C. Compilação e linkedição

O aluno deve reconhecer que `-c` interrompe a construção antes da linkedição.

**Esperado:** arquivos `.o` produzidos individualmente e um comando posterior para gerar `bin/app`.

### D. Flags de diagnóstico

O aluno deve utilizar as flags solicitadas e compreender que elas permitem identificar problemas durante a compilação.

**Esperado:** compilação sem erros e sem avisos com as flags especificadas.

### E. Debug e otimização

O aluno deve reconhecer que `-g` adiciona informações para depuração e que `-O0` desabilita otimizações.

**Esperado:** reconstrução dos três objetos com essas opções, seguida de nova linkedição.

Não é necessário executar o GDB nesta etapa.

### F. Organização dos arquivos

O aluno deve manter os fontes e headers em seus diretórios originais, colocando os objetos em `obj/` e o executável em `bin/`.

**Esperado:** nenhum arquivo objeto ou executável gerado diretamente na raiz do projeto.

---

## 7. Critérios de aprovação

A Etapa A será considerada concluída quando:

- Os três arquivos-fonte forem compilados separadamente.
- Os objetos forem gerados em `obj/`.
- A opção `-Iinclude` for utilizada corretamente.
- As flags de diagnóstico solicitadas estiverem presentes.
- A linkedição gerar `bin/app`.
- O executável apresentar o resultado esperado.
- A recompilação com `-g -O0` for realizada com sucesso.

**Não será exigida a criação de Makefile nesta etapa.**

---

## 8. Preparação para a Etapa B

Ao concluir a Etapa A, o aluno terá executado manualmente quatro comandos principais: três compilações e uma linkedição.

Na Etapa B, esses comandos deverão ser incorporados a um Makefile.

A diferença fundamental será que o GNU Make poderá determinar quais comandos precisam ser executados novamente, considerando as dependências entre os arquivos.

**A Etapa A ensina a construir o programa. A Etapa B ensina a automatizar e controlar essa construção.**