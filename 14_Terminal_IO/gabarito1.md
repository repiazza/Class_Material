# 14_Terminal_IO — Gabarito 1

## Construindo uma biblioteca de utilidades para terminal

Material de referência para correção do `exercicio1.md` e continuidade do projeto Terminal Utils v1.

A solução abaixo representa uma implementação completa do contrato proposto. Não é a única implementação válida. A avaliação deve considerar o comportamento, a compreensão dos mecanismos de terminal e a separação de responsabilidades, e não a reprodução literal deste código.

## 1. Solução de referência

### terminal_utils.h

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

### terminal_utils.c

```c
#include <stdio.h>
#include <string.h>
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
```

### main.c (fornecido no enunciado, sem alterações)

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

### Makefile (fornecido no enunciado, sem alterações)

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

## 2. Comportamento esperado

```bash
make
./terminal_demo
```

Ao final da execução, em um terminal convencional:

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

Durante a simulação, o percentual avança de 0 a 100 em passos de 10, reutilizando a mesma linha. O tempo de espera pertence ao demonstrador, não à biblioteca.

**Nota de revisão do enunciado:** a saída ilustrativa original da ficha contém menos espaços do que o `printf()` do `main.c` fornecido efetivamente produz. A saída acima preserva o código original e representa seu alinhamento real. Essa diferença não constitui erro do aluno.

## 3. Fundamentação da solução

### vPrintLine

O texto é um dado, não uma string de formato. `fputs()` permite imprimir inclusive `%` literalmente. `printf("%s", pszText)` é igualmente válido. A quebra de linha depende de qualquer valor não nulo de `bNewLine`.

### vPrintSeparator

A repetição de um caractere permite construir separadores sem fixar sua largura no código. Os limites 32 e 126 correspondem ao intervalo ASCII imprimível no ambiente de referência.

### vPrintCentered

Para ASCII imprimível, `strlen()` fornece a largura em colunas. A diferença entre a largura disponível e a ocupada pelo texto, dividida por dois com divisão inteira, fornece o preenchimento à esquerda. A divisão descarta a fração e deixa a coluna excedente à direita. Textos maiores que a largura são preservados. A comparação com `size_t` evita converter prematuramente o tamanho da string para `int`.

### vPrintProgress

O `\r` retorna ao início da linha, `%3d` mantém a largura do campo e `%%` imprime o percentual literal. `fflush(stdout)` descarrega o buffer de saída da biblioteca C sem depender de uma quebra de linha. Não é uma garantia de renderização instantânea pelo terminal. A função não dorme nem encerra a linha.

### vPrintBar

A quantidade preenchida é calculada por `valor * largura / maximo`, após limitar o valor ao intervalo válido. A multiplicação precede a divisão para preservar a proporção. A divisão inteira descarta frações. A conversão para `long` protege a multiplicação dentro dos limites propostos. A rejeição de larguras acima de 100 e máximos acima de 10000 é uma escolha da referência; o enunciado não exige comportamento nesses casos. A ausência de quebra de linha permite compor a barra com outros elementos.

## 4. Casos de verificação

Na tabela, `\n` e `\r` representam bytes de controle, não texto literal. “Sem saída” significa nenhum byte, nem mesmo uma quebra de linha.

| Chamada | Resultado esperado |
|---|---|
| `vPrintLine("100%", 0)` | `100%` |
| `vPrintLine("OK", 2)` | `OK\n` |
| `vPrintLine(NULL, 1)` | Sem saída |
| `vPrintSeparator('=', 3)` | `===\n` |
| `vPrintSeparator('=', 0)` | Sem saída |
| `vPrintSeparator('\n', 3)` | Sem saída |
| `vPrintCentered("abc", 6)` | Um espaço + `abc\n` |
| `vPrintCentered("abcdef", 3)` | `abcdef\n` |
| `vPrintCentered("abc", 0)` | Sem saída |
| `vPrintCentered(NULL, 5)` | Sem saída |
| `vPrintProgress(-1)` | `\rProgresso:   0%` |
| `vPrintProgress(50)` | `\rProgresso:  50%` |
| `vPrintProgress(101)` | `\rProgresso: 100%` |
| `vPrintBar(1, 3, 10)` | `[###-------]` |
| `vPrintBar(-1, 10, 3)` | `[---]` |
| `vPrintBar(11, 10, 3)` | `[###]` |
| `vPrintBar(1, 0, 3)` | Sem saída |
| `vPrintBar(1, 3, 0)` | Sem saída |

Teste também a transição de 100% para 5% para verificar se não restam dígitos da atualização anterior. Observe o progresso em um terminal interativo: redirecionar para um arquivo preserva os bytes de retorno de carro e não reproduz o comportamento visual do terminal.

## 5. Investigação complementar — UTF-8

Considerando as palavras em UTF-8 com caracteres precompostos:

| Texto | Bytes (sem NUL) | Colunas usuais | Espaços à esquerda para largura 20 |
|---|---:|---:|---:|
| `licao` | 5 | 5 | 7 |
| `lição` | 7 | 5 | 6 |

```text
====================
       licao
      lição
====================
```

A segunda palavra aparece uma coluna mais à esquerda porque a implementação mede bytes, não largura visual. `echo $LANG` e `locale` permitem investigar a configuração do ambiente. Os valores dependem da instalação; não se exige um locale específico. `setlocale()` por si só não converte strings nem corrige a centralização.

O aluno deve identificar essa diferença, não implementar suporte Unicode. Uma solução que já trate corretamente a largura visual pode ser aceita se preservar o contrato ASCII e o aluno souber explicar o motivo da diferença entre bytes e colunas.

## 6. Visão pedagógica — critérios de avaliação

### 6.1 O que é essencial

| Conceito | Evidência de assimilação | Desvio que exige correção |
|---|---|---|
| Modularização | Funções genéricas em `terminal_utils.c`, acessíveis pelo header | Lógica de RPG, valores fixos do demonstrador ou dependência de suas variáveis dentro da biblioteca |
| Saída textual | Texto literal e controle da quebra de linha | Usar texto arbitrário como formato de `printf`, ou ignorar `bNewLine` |
| Monoespaçamento | Separadores e centralização dependem dos parâmetros | Quantidade de espaços ou largura fixa para coincidir apenas com o exemplo |
| Controle de saída | Progresso reutiliza a linha, com atualização observável sem Enter | Imprimir uma linha por percentual, deixar resíduos ou depender de nova linha para descarregar a saída |
| Proporcionalidade | Barra representa valor/máximo para diferentes larguras | Fixar a barra em 20 células, dividir inteiros antes de multiplicar perdendo a proporção, ou arredondar contrariando o contrato |
| Composição | Barra e progresso não encerram a linha; tempo fica no chamador | Inserir quebras ou esperas obrigatórias dentro dessas funções |
| Encoding | Distinguir bytes de colunas no experimento | Afirmar que `strlen()` mede sempre caracteres visíveis |

### 6.2 Variações naturais que devem ser aceitas

- `printf`, `fputs`, `putchar` ou combinações equivalentes, desde que o texto seja literal e a saída respeite o contrato.
- Laços `for` ou `while`, funções auxiliares privadas, reutilização ou não de `vPrintLine()`.
- Centralização por laço de espaços ou largura dinâmica de `printf`, com comportamento equivalente.
- Cálculo proporcional por outra expressão, inclusive ponto flutuante, desde que produza a quantidade correta de células nos limites exigidos.
- Outra estratégia de buffering que assegure a atualização sem quebra de linha, desde que o aluno explique o mecanismo e não imponha efeitos desnecessários ao restante da aplicação.
- Nomes de variáveis locais, organização interna e verificações adicionais que não alterem os contratos públicos.

Não exigir alocação dinâmica, otimizações, funções auxiliares específicas, tratamento completo de Unicode ou portabilidade para Windows. Não penalizar a ausência de suporte a parâmetros explicitamente fora dos limites do enunciado.

### 6.3 Como conduzir a correção

**Solução assimilada:** o aluno atende aos contratos e consegue explicar como a saída é produzida, mesmo que o código seja diferente da referência.

**Solução com ajustes pontuais:** a arquitetura e os mecanismos estão corretos, mas há erros de fronteira, avisos de compilação, espaços excedentes ou tratamento incompleto de parâmetros. Solicitar correções localizadas; não confundir esses erros com ausência de assimilação do capítulo.

**Conceito ainda não assimilado:** a solução funciona apenas com os valores do `main.c`, não separa aplicação e biblioteca, ou não utiliza adequadamente os mecanismos de atualização textual. Retomar o conceito específico e pedir uma nova demonstração com parâmetros diferentes. Não invalidar automaticamente as demais funções corretas.

Uma forma simples de verificar autonomia é alterar a largura para 17, a vida para 1/3 e fazer o progresso decrescer de 100 para 5. O aluno deve conseguir prever a saída e explicar o resultado sem reescrever a biblioteca.

O projeto deve compilar sem avisos com o Makefile fornecido. Diferenças de estilo não são falhas conceituais; recursos incompatíveis com C89 devem ser ajustados para cumprir a premissa de compilação.

## 7. Continuidade — Terminal Utils v1

Preservar as cinco assinaturas e seus comportamentos. No próximo exercício, cores, atributos, coordenadas e limpeza serão acrescentados como novos recursos, sem exigir que o aluno descarte uma solução válida desta etapa.

A implementação de referência é uma base possível, não uma substituição obrigatória do código do aluno.

**Direcionamento pedagógico final:** o objetivo não é ensinar cinco funções isoladas, mas demonstrar que mecanismos simples de saída podem ser encapsulados em uma biblioteca genérica, combinados pela aplicação e reutilizados em contextos diferentes. A avaliação deve privilegiar essa compreensão e a capacidade de prever o comportamento do terminal. A fidelidade ao algoritmo do gabarito não é um critério de aprovação.

## 8. Validação da referência

A referência foi compilada com GCC, C89, `-Wall -Wextra -pedantic -Werror`, mantendo `_DEFAULT_SOURCE` do Makefile. O demonstrador foi executado e um teste adicional verificou por comparação de bytes casos de texto literal, parâmetros inválidos, centralização, limites do progresso e proporcionalidade da barra. A observação visual em terminal interativo e o experimento de locale ficam como verificações manuais.
