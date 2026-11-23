# 14_Terminal_IO — Exercício 1

## Construindo uma biblioteca de utilidades para terminal

### Objetivo

Desenvolver a primeira versão de uma biblioteca de funções reutilizáveis para apresentação de informações no terminal, aplicando formatação de texto, monoespaçamento, caracteres de controle e buffering de saída.

Esta biblioteca será utilizada e ampliada nos próximos exercícios do capítulo. Não será necessário implementar um jogo ou motor de batalha: utilizaremos apenas os dados fictícios de um personagem para demonstrar suas funcionalidades.

## 1. Estrutura do projeto

```text
terminal_project/
├── main.c
├── terminal_utils.h
├── terminal_utils.c
└── Makefile
```

- `main.c`: programa demonstrador, fornecido neste enunciado.
- `terminal_utils.h`: interface pública, fornecida neste enunciado.
- `terminal_utils.c`: implementação das funções, responsabilidade do aluno.
- `Makefile`: compilação do projeto, fornecido neste enunciado.

A biblioteca não deverá conhecer os dados ou as regras da aplicação. Suas funções deverão ser genéricas e reutilizáveis em outros programas.

## 2. Etapa A — Implementação da biblioteca

### Interface pública: terminal_utils.h

```c
#ifndef TERMINAL_UTILS_H
#define TERMINAL_UTILS_H

void vPrintLine(const char *pszText, int bNewLine);
void vPrintSeparator(char cChar, int iWidth);
void vPrintCentered(const char *pszText, int iWidth);
void vPrintProgress(int iPercent);
void vPrintBar(int iValue, int iMax, int iWidth);

#endif
```

Implemente as cinco funções em `terminal_utils.c`, incluindo o próprio header e os headers da biblioteca padrão necessários.

### A.1 — vPrintLine

Imprime o texto recebido. Se `bNewLine` for diferente de zero, acrescenta uma quebra de linha; caso contrário, permanece na mesma linha.

```c
vPrintLine("Nome: ", 0);
vPrintLine("Guerreiro", 1);
```

Saída:

```text
Nome: Guerreiro
```

O texto deve ser tratado como dado literal, inclusive quando contiver o caractere `%`. Se o ponteiro for `NULL`, não produza saída.

### A.2 — vPrintSeparator

Imprime `iWidth` ocorrências de `cChar`, seguidas de uma quebra de linha.

```c
vPrintSeparator('=', 10);
vPrintSeparator('-', 5);
```

Saída:

```text
==========
-----
```

Considere apenas caracteres ASCII imprimíveis. Se a largura for menor ou igual a zero, ou o caractere não for ASCII imprimível, não produza saída.

### A.3 — vPrintCentered

Apresenta um texto centralizado em relação à largura informada, acrescentando espaços antes do texto e uma quebra de linha ao final. Não é necessário preencher os espaços à direita.

```c
vPrintSeparator('=', 20);
vPrintCentered("RPG STATUS", 20);
vPrintSeparator('=', 20);
```

Saída:

```text
====================
     RPG STATUS
====================
```

- Considere textos ASCII imprimíveis, sem tabulações ou quebras de linha.
- Quando a quantidade de espaços disponíveis for ímpar, deixe o espaço excedente à direita.
- Se o texto for maior que a largura informada, imprima-o integralmente, sem centralização.
- Se a largura for menor ou igual a zero ou o ponteiro for `NULL`, não produza saída.

### A.4 — vPrintProgress

Apresenta um percentual de progresso, reutilizando a mesma linha do terminal a cada chamada.

```c
vPrintProgress(0);
vPrintProgress(50);
vPrintProgress(100);
```

Estados sucessivos da mesma linha (não são três linhas simultâneas):

```text
Progresso:   0%
Progresso:  50%
Progresso: 100%
```

- Reserve três posições para o valor numérico.
- Utilize os conceitos de retorno de carro e buffering estudados no capítulo.
- A função não deve acrescentar uma quebra de linha nem realizar esperas.
- Valores menores que zero devem ser apresentados como 0%; valores maiores que 100, como 100%.
- A atualização deverá ser observável mesmo sem uma quebra de linha.

### A.5 — vPrintBar

Apresenta uma barra textual proporcional ao valor recebido em relação ao máximo informado.

Utilize `#` para a parte preenchida e `-` para a parte restante. Os delimitadores `[` e `]` não fazem parte de `iWidth`.

```c
vPrintBar(75, 100, 20);
```

Saída:

```text
[###############-----]
```

Outros exemplos:

```text
vPrintBar(0,   100, 10)  -> [----------]
vPrintBar(50,  100, 10)  -> [#####-----]
vPrintBar(100, 100, 10)  -> [##########]
vPrintBar(1,     3, 10)  -> [###-------]
```

- Desconsidere frações de células (arredondamento para baixo).
- Valores negativos devem ser tratados como zero; valores acima do máximo devem ser tratados como o máximo.
- Se `iMax` ou `iWidth` forem menores ou iguais a zero, não produza saída.
- Para este exercício, considere larguras válidas de 1 a 100 e valores máximos de até 10000. Parâmetros acima desses limites não precisam ser suportados.
- Não acrescente quebra de linha ao final da barra: a aplicação deverá decidir quando encerrar a linha.

## 3. Etapa B — Programa demonstrador

Utilize o `main.c` abaixo para verificar a implementação da biblioteca. Não é necessário modificar o programa para concluir esta etapa.

### main.c

```c
#include <stdio.h>
#include <unistd.h>
#include "terminal_utils.h"

int main(void)
{
  const char *pszName = "Guerreiro";
  int iLevel = 5;
  int iAttack = 25;
  int iDefense = 12;
  int iHP = 75;
  int iMaxHP = 100;
  int iWidth = 32;
  int iPercent;

  vPrintSeparator('=', iWidth);
  vPrintCentered("RPG STATUS", iWidth);
  vPrintSeparator('=', iWidth);
  vPrintLine("", 1);

  printf("%-12s %9s\n", "Nome:", pszName);
  printf("%-12s %9d\n", "Nivel:", iLevel);
  printf("%-12s %9d\n", "Ataque:", iAttack);
  printf("%-12s %9d\n", "Defesa:", iDefense);

  vPrintLine("", 1);
  printf("HP: %d/%d\n", iHP, iMaxHP);
  vPrintBar(iHP, iMaxHP, 20);
  vPrintLine("", 1);
  vPrintLine("", 1);

  vPrintSeparator('-', iWidth);
  vPrintLine("Carregando inventario...", 1);

  for (iPercent = 0; iPercent <= 100; iPercent += 10) {
    vPrintProgress(iPercent);
    if (iPercent < 100)
      usleep(200000);
  }

  vPrintLine("", 1);
  vPrintLine("Carregamento concluido!", 1);

  return 0;
}
```

A função `usleep()` é utilizada apenas para simular o tempo de carregamento no ambiente Linux. A biblioteca não deverá controlar esse tempo.

### Makefile

```makefile
CC = gcc
CFLAGS = -std=c89 -D_DEFAULT_SOURCE -Wall -Wextra -pedantic
TARGET = terminal_demo
OBJS = main.o terminal_utils.o

all: $(TARGET)

$(TARGET): $(OBJS)
	$(CC) $(OBJS) -o $(TARGET)

main.o: main.c terminal_utils.h
	$(CC) $(CFLAGS) -c main.c -o main.o

terminal_utils.o: terminal_utils.c terminal_utils.h
	$(CC) $(CFLAGS) -c terminal_utils.c -o terminal_utils.o

clean:
	rm -f $(OBJS) $(TARGET)

.PHONY: all clean
```

As linhas de comandos do Makefile devem começar com uma tabulação. A definição `_DEFAULT_SOURCE` permite utilizar `usleep()` com a glibc no ambiente Linux de referência.

Compile e execute:

```bash
make
./terminal_demo
```

### Resultado esperado ao final da execução

```text
================================
           RPG STATUS
================================

Nome:        Guerreiro
Nivel:               5
Ataque:             25
Defesa:             12

HP: 75/100
[###############-----]

--------------------------------
Carregando inventario...
Progresso: 100%
Carregamento concluido!
```

Durante o carregamento, o percentual deverá avançar de 0% até 100%, sem criar uma nova linha para cada atualização.

## 4. Etapa C — Investigação complementar

Após concluir as etapas anteriores, experimente acrescentar temporariamente ao `main.c` as seguintes chamadas:

```c
vPrintSeparator('=', 20);
vPrintCentered("licao", 20);
vPrintCentered("lição", 20);
vPrintSeparator('=', 20);
```

Utilize um arquivo-fonte em UTF-8 e um terminal configurado para UTF-8. Observe a apresentação das duas palavras e investigue:

- As duas palavras possuem a mesma quantidade de caracteres visíveis?
- O resultado de `strlen()` é igual para ambas?
- A centralização apresenta o mesmo comportamento? Por quê?

Consulte também o ambiente utilizando `echo $LANG` e `locale`.

Não é necessário corrigir a centralização de textos UTF-8 nesta etapa. O objetivo é observar a diferença entre o tamanho de uma string em bytes e o espaço ocupado pelo texto no terminal. O suporte obrigatório da biblioteca permanece restrito a ASCII imprimível para as funções de alinhamento.

## 5. Critérios de conclusão

- [ ] As cinco funções foram implementadas em `terminal_utils.c` e respeitam os protótipos fornecidos.
- [ ] A biblioteca não possui dependências do domínio RPG nem variáveis globais da aplicação.
- [ ] O projeto compila sem avisos com o Makefile fornecido.
- [ ] A ficha do personagem apresenta alinhamento, separadores e barra de vida conforme o exemplo.
- [ ] O progresso é atualizado na mesma linha e termina em 100%.
- [ ] Foram testados valores mínimos, máximos e inválidos conforme os contratos das funções.
- [ ] A investigação complementar foi realizada, sem exigir suporte completo a UTF-8.

## 6. Continuidade do projeto

Preserve os arquivos produzidos neste exercício. Eles serão a base para o Exercício 2, no qual acrescentaremos cores, atributos visuais, posicionamento do cursor e manipulação de regiões do terminal.

Nesta primeira versão, não utilize sequências ANSI para cores ou posicionamento absoluto, limpeza de tela, ncurses ou bibliotecas gráficas.

O objetivo é construir uma base simples, funcional e reutilizável, que possa evoluir sem descartar as funcionalidades já implementadas.
