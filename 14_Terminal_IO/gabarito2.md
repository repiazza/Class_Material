# 14_Terminal_IO — Gabarito 2

## Padronizando a formatação visual no terminal

Referência para correção do `exercicio2.md` e continuidade da Terminal Utils v2. A solução é uma implementação possível, não um algoritmo obrigatório.

## 1. Solução de referência

As cinco funções anteriores são preservadas. As cores escolhidas para o demonstrador são exemplos; o destaque combinado foi aplicado à mensagem de carregamento, mantendo a centralização original.

### terminal_utils.h

```c
#ifndef TERMINAL_UTILS_H
#define TERMINAL_UTILS_H

#define ANSI_RESET "\033[0m"
#define ANSI_END ((const char *)0)

/* TEXT_COLOR */
#define TEXT_COLOR_BLACK ((const char *)"\033[30m")
#define TEXT_COLOR_RED ((const char *)"\033[31m")
#define TEXT_COLOR_GREEN ((const char *)"\033[32m")
#define TEXT_COLOR_YELLOW ((const char *)"\033[33m")
#define TEXT_COLOR_BLUE ((const char *)"\033[34m")
#define TEXT_COLOR_MAGENTA ((const char *)"\033[35m")
#define TEXT_COLOR_CYAN ((const char *)"\033[36m")
#define TEXT_COLOR_WHITE ((const char *)"\033[37m")

/* BACKGROUND_COLOR */
#define BACKGROUND_COLOR_BLACK ((const char *)"\033[40m")
#define BACKGROUND_COLOR_RED ((const char *)"\033[41m")
#define BACKGROUND_COLOR_GREEN ((const char *)"\033[42m")
#define BACKGROUND_COLOR_YELLOW ((const char *)"\033[43m")
#define BACKGROUND_COLOR_BLUE ((const char *)"\033[44m")
#define BACKGROUND_COLOR_MAGENTA ((const char *)"\033[45m")
#define BACKGROUND_COLOR_CYAN ((const char *)"\033[46m")
#define BACKGROUND_COLOR_WHITE ((const char *)"\033[47m")

/* Atributos visuais */
#define BOLD_TEXT ((const char *)"\033[1m")
#define DIM_TEXT ((const char *)"\033[2m")
#define ITALIC_TEXT ((const char *)"\033[3m")
#define UNDERLINE_TEXT ((const char *)"\033[4m")
#define REVERSE_TEXT ((const char *)"\033[7m")
#define STRIKETHROUGH_TEXT ((const char *)"\033[9m")

void vPrintLine(const char *pszText, int bNewLine);
void vPrintSeparator(char cChar, int iWidth);
void vPrintCentered(const char *pszText, int iWidth);
void vPrintProgress(int iPercent);
void vPrintBar(int iValue, int iMax, int iWidth);
void vPrintFormatted(const char *pszText, ...);

#endif
```

### terminal_utils.c

```c
#include <stdio.h>
#include <string.h>
#include <stdarg.h>
#include "terminal_utils.h"

void vPrintLine(const char *pszText, int bNewLine)
{
  if (pszText == NULL)
    return;
  fputs(pszText, stdout);
  if (bNewLine)
    putchar('\n');
}

void vPrintSeparator(char cChar, int iWidth)
{
  int i;
  if (iWidth <= 0 || cChar < 32 || cChar > 126)
    return;
  for (i = 0; i < iWidth; i++)
    putchar(cChar);
  putchar('\n');
}

void vPrintCentered(const char *pszText, int iWidth)
{
  size_t zLen;
  int iPadding;
  int i;
  if (pszText == NULL || iWidth <= 0)
    return;
  zLen = strlen(pszText);
  iPadding = 0;
  if (zLen < (size_t)iWidth)
    iPadding = (iWidth - (int)zLen) / 2;
  for (i = 0; i < iPadding; i++)
    putchar(' ');
  vPrintLine(pszText, 1);
}

void vPrintProgress(int iPercent)
{
  if (iPercent < 0)
    iPercent = 0;
  else if (iPercent > 100)
    iPercent = 100;
  printf("\rProgresso: %3d%%", iPercent);
  fflush(stdout);
}

void vPrintBar(int iValue, int iMax, int iWidth)
{
  int i;
  int iFilled;
  if (iMax <= 0 || iWidth <= 0 || iMax > 10000 || iWidth > 100)
    return;
  if (iValue < 0)
    iValue = 0;
  else if (iValue > iMax)
    iValue = iMax;
  iFilled = (int)((long)iValue * iWidth / iMax);
  putchar('[');
  for (i = 0; i < iWidth; i++)
    putchar(i < iFilled ? '#' : '-');
  putchar(']');
}

void vPrintFormatted(const char *pszText, ...)
{
  va_list args;
  const char *pszAttr;

  if (pszText == NULL)
    return;

  va_start(args, pszText);
  while ((pszAttr = va_arg(args, const char *)) != ANSI_END)
    printf("%s", pszAttr);
  va_end(args);

  printf("%s%s", pszText, ANSI_RESET);
}
```

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
  char szBuffer[128];

  vPrintSeparator('=', iWidth);
  vPrintCentered("RPG STATUS", iWidth);
  vPrintSeparator('=', iWidth);
  vPrintLine("", 1);

  printf("%-12s %9s\n", "Nome:", pszName);
  printf("%-12s %9d\n", "Nivel:", iLevel);
  sprintf(szBuffer, "%-12s %9d", "Ataque:", iAttack);
  vPrintFormatted(szBuffer, TEXT_COLOR_RED, ANSI_END);
  vPrintLine("", 1);
  sprintf(szBuffer, "%-12s %9d", "Defesa:", iDefense);
  vPrintFormatted(szBuffer, TEXT_COLOR_CYAN, ANSI_END);
  vPrintLine("", 1);

  vPrintLine("", 1);
  printf("HP: %d/%d\n", iHP, iMaxHP);
  vPrintBar(iHP, iMaxHP, 20);
  vPrintLine("", 1);
  vPrintLine("", 1);

  vPrintSeparator('-', iWidth);
  vPrintFormatted("Carregando inventario...", TEXT_COLOR_WHITE,
                  BACKGROUND_COLOR_BLUE, UNDERLINE_TEXT, ANSI_END);
  vPrintLine("", 1);
  for (iPercent = 0; iPercent <= 100; iPercent += 10) {
    vPrintProgress(iPercent);
    if (iPercent < 100)
      usleep(200000);
  }
  vPrintLine("", 1);
  vPrintFormatted("Carregamento concluido!", TEXT_COLOR_GREEN,
                  BOLD_TEXT, ANSI_END);
  vPrintLine("", 1);
  return 0;
}
```

### Makefile (sem alterações)

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

## 2. Fundamentação da solução

### Organização das constantes

Os códigos SGR 30–37 selecionam a cor do texto e 40–47 a cor do fundo. Os atributos 1, 2, 3, 4, 7 e 9 correspondem respectivamente a negrito/intensidade aumentada, intensidade reduzida, itálico, sublinhado, inversão e tachado. O suporte visual depende do terminal.

As macros de atributos têm tipo `const char *`, compatível com `va_arg(args, const char *)`. `ANSI_END` é um ponteiro nulo desse mesmo tipo, não uma sequência enviada ao terminal. A ausência da sentinela ou argumentos de tipo incompatível podem provocar comportamento indefinido; não há como descobrir automaticamente o fim da lista.

### Ordem da impressão

A função envia cada sequência na ordem recebida, imprime o texto uma única vez e envia `ANSI_RESET`. O terminal interpreta os códigos e mantém seu estado entre chamadas. O reset restaura os atributos padrão, não os atributos personalizados anteriores, e não altera o texto já exibido.

`printf("%s", pszAttr)` e `printf("%s%s", pszText, ANSI_RESET)` tratam os argumentos como dados, inclusive quando contêm `%`. A função não acrescenta quebra de linha nem exige concatenação ou alocação dinâmica. Sem atributos, imprime o texto sob o estado vigente e depois restaura o padrão; não promete neutralizar atributos externos antes da impressão.

### Informações dinâmicas

O demonstrador prepara as linhas de ataque e defesa com `sprintf()` e só depois aplica os atributos. O buffer é suficiente para os valores do exemplo no ambiente de referência. Não se deve generalizar esse uso para textos de comprimento arbitrário sem controle de tamanho. As sequências ANSI não ocupam colunas visíveis; o alinhamento é calculado sobre o conteúdo textual, não sobre a sequência decorada.

## 3. Verificação e investigação complementar

Execute `make` e `./terminal_demo`. A ficha mantém os dados, separadores, alinhamento, barra de vida e progresso da versão anterior. Ataque aparece em vermelho, defesa em ciano, carregamento em branco sobre azul e sublinhado, e conclusão em verde e negrito. O progresso continua na mesma linha.

Na investigação C.1, vermelho seguido de verde produz texto verde; verde seguido de vermelho produz texto vermelho. A última seleção da mesma categoria prevalece. Cor de texto e fundo são estados distintos e podem coexistir. Não é necessário detectar conflitos nem reorganizar argumentos.

### Casos de verificação

Na tabela, `ESC` representa o byte 0x1B e `\n` uma quebra de linha, não texto literal.

| Chamada | Bytes esperados |
|---|---|
| `vPrintFormatted("OK", ANSI_END)` | `OK ESC[0m` |
| `vPrintFormatted("100%", TEXT_COLOR_RED, ANSI_END)` | `ESC[31m 100% ESC[0m` |
| `vPrintFormatted("X", TEXT_COLOR_WHITE, BACKGROUND_COLOR_BLUE, UNDERLINE_TEXT, ANSI_END)` | `ESC[37m ESC[44m ESC[4m X ESC[0m` |
| `vPrintFormatted("X", TEXT_COLOR_RED, TEXT_COLOR_GREEN, ANSI_END)` | `ESC[31m ESC[32m X ESC[0m` |
| `vPrintFormatted("X", TEXT_COLOR_GREEN, TEXT_COLOR_RED, ANSI_END)` | `ESC[32m ESC[31m X ESC[0m` |
| `vPrintFormatted("", ANSI_END)` | `ESC[0m` |
| `vPrintFormatted(NULL, ANSI_END)` | Nenhum byte |

Os espaços entre os componentes da coluna de bytes são apenas separadores ilustrativos. Não devem ser emitidos. Teste também duas chamadas consecutivas sem quebra de linha e um `printf()` comum após uma impressão decorada. Não execute chamadas sem sentinela para tentar verificar seu comportamento.

## 4. Sugestão de olhar avaliativo

### 4.1 O que é essencial e o que constitui desvio

| Conceito | Evidência de assimilação | Desvio que exige correção |
|---|---|---|
| Padronização | Macros agrupadas, oito cores de cada categoria e seis atributos | Códigos espalhados pelo demonstrador ou categorias obrigatórias ausentes |
| Argumentos variáveis | Percorre a lista até a sentinela tipada | Quantidade fixa, leitura além da sentinela ou tipos incompatíveis |
| Estado do terminal | Aplica atributos antes do texto e restaura ao final | Reset antes do texto, ausência de reset ou impressão repetida do texto |
| Ordem | Preserva a ordem recebida e explica conflitos | Ordena, descarta ou substitui atributos arbitrariamente |
| Segurança da impressão | Texto literal, inclusive `%` | `printf(pszText)` ou uso de texto arbitrário como formato |
| Composição | Não impõe quebra de linha; preserva funções anteriores | Quebra obrigatória, mudança de assinaturas ou perda de funcionalidades |
| Separação de responsabilidades | Biblioteca genérica; aplicação prepara dados | Regras de RPG na biblioteca ou uso dos varargs para substituições de formato |

### 4.2 Variações aceitáveis

- `fputs()`, `printf("%s", ...)` ou reutilização de `vPrintLine(..., 0)` para emitir texto e atributos.
- Laços diferentes, nomes locais distintos e funções auxiliares privadas, desde que preservem o contrato público.
- Nomes diferentes para macros não fornecidas, desde que consistentes e que o demonstrador compile; manter os nomes usados nos exemplos fornecidos ou disponibilizar aliases.
- Uma estratégia de concatenação pode ser aceita se segura, sem limite artificial de atributos e com comportamento equivalente, embora seja complexidade desnecessária.
- Escolhas visuais diferentes das da referência, desde que cumpram os requisitos mínimos e preservem a legibilidade e o alinhamento.
- Diferenças de renderização de itálico, intensidade ou tachado não são falhas do aluno quando os bytes ANSI estão corretos.

Não exigir RGB, 256 cores, detecção de terminal, restauração do estado personalizado anterior, movimentação do cursor ou limpeza de tela. Esses recursos não são objetivos desta etapa.

### 4.3 Como conduzir a correção

**Solução assimilada:** atende ao contrato e o aluno explica por que os atributos vêm antes do texto, por que o reset vem depois e por que a ordem de duas cores conflitantes importa. Não exigir reprodução literal da referência.

**Solução com ajustes pontuais:** uma macro incorreta, nomenclatura inconsistente, atributo faltante ou pequeno desalinhamento pode ser corrigido localmente. Verificar se o aluno compreende a categoria do código e consegue corrigir o caso sem reescrever a biblioteca.

**Conceito ainda não assimilado:** texto impresso dentro do laço de atributos, reset ausente, interpretação equivocada dos argumentos como valores de formato, lista variádica insegura ou dependência da aplicação dentro da biblioteca. Retomar o mecanismo específico antes de avançar. Não invalidar automaticamente as partes corretas.

Uma verificação de autonomia consiste em pedir ao aluno que preveja a saída de uma chamada sem atributos, inverta duas cores de texto, combine fundo e sublinhado e imprima `100%` seguido de texto comum. A explicação deve preceder a execução.

## 5. Continuidade — Terminal Utils v2

Preservar a solução válida do aluno, incluindo as cinco funções anteriores e a nova interface. No Exercício 3 serão acrescentados posicionamento e limpeza, sem exigir a substituição desta implementação.

O objetivo não é memorizar códigos ANSI nem reproduzir um laço específico de `stdarg.h`, mas compreender como a ordem de emissão controla o estado visual e como uma biblioteca genérica encapsula essa responsabilidade.
