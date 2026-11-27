# 14_Terminal_IO --- Gabarito 4

## Construção de interfaces gráficas no terminal

Referência para correção do `exercicio4.md`. A solução responde às partes A e B integralmente e utiliza a biblioteca construída nos exercícios anteriores, preservando suas interfaces públicas. O resultado é uma implementação de referência, não a única organização aceitável.

## 1. Solução de referência

### Parte A --- Primitivas de desenho

As quatro primitivas são incorporadas à biblioteca. Mantemos `vPrintSeparator`, `vPrintCentered`, `vPrintBar` e as demais funções existentes. O contrato de `vGotoXY` passa a ser explicitamente X = coluna e Y = linha. Utilizamos os caracteres UTF-8 fornecidos no enunciado.

### terminal_utils.h

``` c
#ifndef TERMINAL_UTILS_H
  #define TERMINAL_UTILS_H

  #define ANSI_RESET  "\033[0m"
  #define ANSI_END   ((const char *)0)

  #define  TCOLOR_BLACK   ((const char *)"30")
  #define  TCOLOR_RED     ((const char *)"31")
  #define  TCOLOR_GREEN   ((const char *)"32")
  #define  TCOLOR_YELLOW  ((const char *)"33")
  #define  TCOLOR_BLUE    ((const char *)"34")
  #define  TCOLOR_MAGENTA ((const char *)"35")
  #define  TCOLOR_CIAN    ((const char *)"36")
  #define  TCOLOR_WHITE   ((const char *)"37")

  #define  BGCOLOR_BLACK   ((const char *)"40")
  #define  BGCOLOR_RED     ((const char *)"41")
  #define  BGCOLOR_GREEN   ((const char *)"42")
  #define  BGCOLOR_YELLOW  ((const char *)"43")
  #define  BGCOLOR_BLUE    ((const char *)"44")
  #define  BGCOLOR_MAGENTA ((const char *)"45")
  #define  BGCOLOR_CIAN    ((const char *)"46")
  #define  BGCOLOR_WHITE   ((const char *)"47")

  #define BOX_HORIZONTAL   "─"
  #define BOX_VERTICAL     "│"
  #define BOX_TOP_LEFT     "╭"
  #define BOX_TOP_RIGHT    "╮"
  #define BOX_BOTTOM_LEFT  "╰"
  #define BOX_BOTTOM_RIGHT "╯"

  #define COLOR_PREFIX ((const char *)"\033[")
  #define ANSI_LINE_END "m"

  #define BOLD_TEXT      ((const char *)"\033[1m")
  #define DIM_TEXT       ((const char *)"\033[2m")
  #define ITALIC_TEXT    ((const char *)"\033[3m")
  #define UNDERLINE_TEXT ((const char *)"\033[4m")
  #define INVERTION_TEXT ((const char *)"\033[7m")
  #define TAXED_TEXT     ((const char *)"\033[9m")

  void vPrintFormatted(const char *pszText, ...);

  void vPrintLine     (const char *pszText, int bNewLine);
  void vPrintSeparator(char cChar, int iWidth);
  void vPrintCentered (const char *pszText, int iWidth, ...);
  void vPrintProgress (int iPercent);
  void vPrintBar      (int iValue, int iMax, int iWidth, const char *pszColor);
  void vPrintColor    (const char *pszColor);
  
  int bIsTColor (const char *pszColor);
  int bIsBGColor(const char *pszColor);

  void vGotoXY(int iX, int iY);
  void vClearScreen(void);
  void vClearLine(void);
  void vSaveCursor(void);
  void vRestoreCursor(void);
  void vShowCursor(int bShow);

  void vDrawHLine(int iX, int iY, int iWidth);
  void vDrawVLine(int iX, int iY, int iHeight);
  void vDrawBox(int iX, int iY, int iWidth, int iHeight);
  void vFillRect(int iX, int iY, int iWidth, int iHeight,
                 const char *pszColor);

#endif
```

### terminal_utils.c

``` c
#include "terminal_utils.h"
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdarg.h>

void vPrintColor(const char *pszColor){
  printf("%s%s%s", COLOR_PREFIX, pszColor, ANSI_LINE_END);
}

int bIsBGColor(const char *pszColor){
  if(pszColor == NULL || strlen(pszColor) != 2 ||
     pszColor[0] != '4' || pszColor[1] < '0' || pszColor[1] > '7') return 0;
  
  return 1;
}

int bIsTColor (const char *pszColor){
  if(pszColor == NULL || strlen(pszColor) != 2 ||
     pszColor[0] != '3' || pszColor[1] < '0' || pszColor[1] > '7') return 0;
  
  return 1;
}

void vPrintFormatted(const char *pszText, ...){
  va_list args;
  const char *pszAttr;

  if (pszText == NULL)
    return;

  va_start(args, pszText);

  while ((pszAttr = va_arg(args, const char *)) != ANSI_END){
    if(bIsTColor(pszAttr) || bIsBGColor(pszAttr))
      vPrintColor(pszAttr);

    else
      printf("%s", pszAttr);
  }

  va_end(args);
  printf("%s", pszText);
  printf(ANSI_RESET);
}

void vPrintProgress(int iPercent){
  if(iPercent < 0) iPercent = 0;
  if(iPercent > 100) iPercent = 100;

  vPrintLine("Progresso: ", 0);

  printf("%3d%%\r", iPercent);

  fflush(stdout);
}

void vPrintCentered(const char *pszText, int iWidth, ...){
  int iSpaces;
  va_list args;
  const char *pszAttr;

  if (pszText == NULL || iWidth <= 0)
    return;

  va_start(args, iWidth);

  if((int)strlen(pszText) >= iWidth){
    while ((pszAttr = va_arg(args, const char *)) != ANSI_END) {
      if(bIsTColor(pszAttr) || bIsBGColor(pszAttr))
      vPrintColor(pszAttr);
      
      else
        printf("%s", pszAttr);
    }
    printf("%s\n", pszText);
    va_end(args);
    printf(ANSI_RESET);
    return;
  }
  iSpaces = (iWidth - strlen(pszText)) / 2;

  for(; iSpaces > 0; iSpaces--)
    printf(" ");
  
  while ((pszAttr = va_arg(args, const char *)) != ANSI_END) {
    if(bIsTColor(pszAttr) || bIsBGColor(pszAttr))
      vPrintColor(pszAttr);
      
    else
      printf("%s", pszAttr);
  }
  va_end(args);
  vPrintLine(pszText, 1);

  printf(ANSI_RESET);
}
void vPrintSeparator(char cChar, int iWidth){
  for(; iWidth >= 0; iWidth--)
    iWidth ? printf("%c", cChar) : printf("\n");
}

void vPrintLine(const char *pszText, int bNewLine){
  bNewLine ? printf("%s\n", pszText) : printf("%s", pszText);
}
void vPrintBar(int iValue, int iMax, int iWidth, const char *pszColor){
  double dFullBar;
  char *szBar;
  int ii = 0;
  
  if(!bIsBGColor(pszColor))return;

  if(iWidth > 100) iWidth = 100;
  if(iMax <= 0 || iWidth <= 0) return;

  if(iValue < 0) iValue = 0;
  if(iValue > iMax) iValue = iMax;

  szBar = calloc(iWidth + 3, sizeof(char));
  if(szBar == NULL) return;
 
  dFullBar = ((double)iValue / (double)iMax) * iWidth;    /*deu até fome*/

  szBar[ii] = '[';

  for(ii = 1; ii <= iWidth; ii++)
      szBar[ii] = ' ';

  szBar[ii] = ']';

  for(ii = 0; ii <= iWidth +1; ii++){
    printf(ANSI_RESET);
    if(ii <= dFullBar && szBar[ii] == ' ')
      vPrintColor(pszColor);
      
    printf("%c", szBar[ii]);
  }
  free(szBar);
}

void vGotoXY(int iX, int iY)
{
  if (iX < 1 || iY < 1)
    return;
  printf("\033[%d;%dH", iY, iX);
}

void vClearScreen(void)
{
  printf("\033[2J");
  vGotoXY(1, 1);
}

void vClearLine(void)
{
  printf("\033[2K");
}

void vSaveCursor(void)
{
  printf("\033[s");
}

void vRestoreCursor(void)
{
  printf("\033[u");
}

void vShowCursor(int bShow)
{
  printf("%s", bShow ? "\033[?25h" : "\033[?25l");
}

void vDrawHLine(int iX, int iY, int iWidth)
{
  int ii;

  if(iX < 1 || iY < 1 || iWidth < 1)
    return;
  vGotoXY(iX, iY);
  for(ii = 0; ii < iWidth; ii++)
    printf("%s", BOX_HORIZONTAL);
}

void vDrawVLine(int iX, int iY, int iHeight)
{
  int ii;

  if(iX < 1 || iY < 1 || iHeight < 1)
    return;
  for(ii = 0; ii < iHeight; ii++){
    vGotoXY(iX, iY + ii);
    printf("%s", BOX_VERTICAL);
  }
}

void vDrawBox(int iX, int iY, int iWidth, int iHeight)
{
  int iRight, iBottom;

  if(iX < 1 || iY < 1 || iWidth < 2 || iHeight < 2)
    return;
  iRight = iX + iWidth - 1;
  iBottom = iY + iHeight - 1;
  vDrawHLine(iX + 1, iY, iWidth - 2);
  vDrawHLine(iX + 1, iBottom, iWidth - 2);
  vDrawVLine(iX, iY + 1, iHeight - 2);
  vDrawVLine(iRight, iY + 1, iHeight - 2);
  vGotoXY(iX, iY);
  printf("%s", BOX_TOP_LEFT);
  vGotoXY(iRight, iY);
  printf("%s", BOX_TOP_RIGHT);
  vGotoXY(iX, iBottom);
  printf("%s", BOX_BOTTOM_LEFT);
  vGotoXY(iRight, iBottom);
  printf("%s", BOX_BOTTOM_RIGHT);
}

void vFillRect(int iX, int iY, int iWidth, int iHeight,
               const char *pszColor)
{
  int iRow, iCol;

  if(iX < 1 || iY < 1 || iWidth < 1 || iHeight < 1 ||
     !bIsBGColor(pszColor))
    return;
  printf("%s", ANSI_RESET);
  vPrintColor(pszColor);
  for(iRow = 0; iRow < iHeight; iRow++){
    vGotoXY(iX, iY + iRow);
    for(iCol = 0; iCol < iWidth; iCol++)
      putchar(' ');
  }
  printf("%s", ANSI_RESET);
}
```

### Parte B --- Interface RPG

Nesta referência, as três funções específicas do RPG ficam no `main.c`, como funções internas. Essa separação é uma escolha de organização, não uma exigência do exercício. O carregamento do inventário é opcional e não foi incluído.

### main.c

``` c
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include "terminal_utils.h"

#define UI_X          2
#define UI_WIDTH      57
#define HEADER_Y      2
#define PANEL_Y       4
#define PANEL_WIDTH   28
#define PANEL_HEIGHT  5
#define ATTR_X        (UI_X + PANEL_WIDTH + 1)
#define HP_Y          10
#define HP_HEIGHT     4
#define STATUS_Y      15
#define STATUS_HEIGHT 3
#define CONTENT_X     (UI_X + 2)
#define CONTENT_WIDTH (UI_WIDTH - 4)
#define BAR_WIDTH     20
#define END_Y         19

static void vDrawInterface(void)
{
  const char *pszTitle = "RPG STATUS";
  int iTitleX;

  vFillRect(UI_X, HEADER_Y, UI_WIDTH, 1, BGCOLOR_BLUE);
  iTitleX = UI_X + (UI_WIDTH - (int)strlen(pszTitle)) / 2;
  vGotoXY(iTitleX, HEADER_Y);
  vPrintFormatted(pszTitle, BGCOLOR_BLUE, TCOLOR_WHITE,
                  BOLD_TEXT, ANSI_END);

  vPrintColor(TCOLOR_GREEN);
  vDrawBox(UI_X, PANEL_Y, PANEL_WIDTH, PANEL_HEIGHT);
  printf("%s", ANSI_RESET);
  vPrintColor(TCOLOR_YELLOW);
  vDrawBox(ATTR_X, PANEL_Y, PANEL_WIDTH, PANEL_HEIGHT);
  printf("%s", ANSI_RESET);
  vPrintColor(TCOLOR_MAGENTA);
  vDrawBox(UI_X, HP_Y, UI_WIDTH, HP_HEIGHT);
  printf("%s", ANSI_RESET);
  vPrintColor(TCOLOR_CIAN);
  vDrawBox(UI_X, STATUS_Y, UI_WIDTH, STATUS_HEIGHT);
  printf("%s", ANSI_RESET);

  vGotoXY(CONTENT_X, PANEL_Y + 1);
  vPrintFormatted("PERSONAGEM", TCOLOR_CIAN, BOLD_TEXT, ANSI_END);
  vGotoXY(CONTENT_X, PANEL_Y + 2);
  printf("Nome: %s", "Guerreiro");
  vGotoXY(CONTENT_X, PANEL_Y + 3);
  printf("Nivel: %d", 5);
  vGotoXY(ATTR_X + 2, PANEL_Y + 1);
  vPrintFormatted("ATRIBUTOS", TCOLOR_CIAN, BOLD_TEXT, ANSI_END);
  vGotoXY(ATTR_X + 2, PANEL_Y + 2);
  printf("Ataque: %d", 25);
  vGotoXY(ATTR_X + 2, PANEL_Y + 3);
  printf("Defesa: %d", 12);
}

static void vUpdateHP(int iHP, int iMaxHP)
{
  const char *pszColor;
  double dRatio;

  vFillRect(CONTENT_X, HP_Y + 1, CONTENT_WIDTH, 2, BGCOLOR_BLACK);
  vGotoXY(CONTENT_X, HP_Y + 1);
  if(iMaxHP <= 0){
    vPrintLine("HP: --", 0);
    return;
  }
  if(iHP < 0) iHP = 0;
  if(iHP > iMaxHP) iHP = iMaxHP;
  printf("HP: %d/%d", iHP, iMaxHP);
  dRatio = (double)iHP / iMaxHP;
  pszColor = BGCOLOR_GREEN;
  if(dRatio <= 0.25)
    pszColor = BGCOLOR_RED;
  else if(dRatio <= 0.50)
    pszColor = BGCOLOR_YELLOW;
  vGotoXY(CONTENT_X, HP_Y + 2);
  vPrintBar(iHP, iMaxHP, BAR_WIDTH, pszColor);
  printf("%s", ANSI_RESET);
}

static void vUpdateStatus(const char *pszStatus)
{
  vFillRect(CONTENT_X, STATUS_Y + 1, CONTENT_WIDTH, 1, BGCOLOR_BLACK);
  vGotoXY(CONTENT_X, STATUS_Y + 1);
  vPrintColor(TCOLOR_YELLOW);
  printf("STATUS: %.*s", CONTENT_WIDTH - 8,
         pszStatus != NULL ? pszStatus : "");
  printf("%s", ANSI_RESET);
}

int main(void)
{
  int ii;
  const int aiHP[] = {100, 75, 50, 90, 90};
  const char *apszStatus[] = {"Pronto", "Dano recebido", "Em perigo",
                             "Curado", "Fim"};

  printf("%s", ANSI_RESET);
  vClearScreen();
  vShowCursor(0);
  vDrawInterface();
  for(ii = 0; ii < 5; ii++){
    vUpdateHP(aiHP[ii], 100);
    vUpdateStatus(apszStatus[ii]);
    fflush(stdout);
    if(ii < 4)
      sleep(1);
  }
  vShowCursor(1);
  vGotoXY(1, END_Y);
  fflush(stdout);
  return 0;
}
```

### Makefile

``` makefile
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

### A.1 e A.2 --- Unicode e coordenadas

Os símbolos de moldura são strings UTF-8 de três bytes, normalmente exibidas em uma célula no terminal Linux adotado. O laço conta células, não bytes. Não usamos `%c` para imprimir uma moldura Unicode. A sequência CUP recebe Y antes de X; por exemplo, `vGotoXY(10, 3)` emite `\033[3;10H`. As linhas não acrescentam quebras nem alteram a cor ativa.

### A.3 --- Molduras

Largura e altura incluem os cantos. Uma caixa 10 × 4 contém oito segmentos horizontais entre os cantos e dois segmentos verticais em cada lateral. Uma caixa 2 × 2 possui somente os quatro cantos. O interior não é preenchido nem apagado. A composição reutiliza as duas primitivas de linha.

### A.4 --- Preenchimento

Cada linha é posicionada explicitamente e recebe exatamente a quantidade solicitada de espaços. A cor de fundo é validada antes de emitir qualquer saída. O reset inicial evita herdar atributos como inversão; o final retorna aos atributos padrão, não ao estado anterior. As coordenadas e dimensões devem caber no terminal; clipping e redimensionamento não são requisitos.

### B.1 e B.2 --- Desenho inicial

O cabeçalho ocupa colunas 2 a 58 na linha 2. O título ASCII de dez células começa na coluna 25. Os painéis superiores ocupam colunas 2--29 e 31--58, linhas 4--8. HP ocupa linhas 10--13 e status 15--17. O desenho ocorre uma vez. A centralização sequencial anterior permanece disponível; não precisamos reescrevê-la para posicionar um título.

### B.3 --- HP

As duas linhas internas são limpas em uma faixa de 53 células (colunas 4--56), sem tocar as bordas 2 e 58. O texto e a barra têm coordenadas próprias. A barra existente ocupa 22 células, contando colchetes. Para máximo inválido, mostramos `HP: --` e deixamos a barra vazia. O HP é limitado ao intervalo válido. A cor proporcional é uma extensão opcional adotada nesta solução: verde acima de 50%, amarelo acima de 25% até 50%, vermelho nos demais casos.

### B.4 --- Status

O preenchimento localizado elimina os resíduos de mensagens anteriores. O limite de 45 bytes mais o prefixo de oito células cabe na região de 53 células. O contrato aqui é de mensagens ASCII imprimíveis, como no enunciado; não é um mecanismo de truncamento Unicode geral. Um ponteiro nulo resulta em mensagem vazia. Não utilizamos `vClearLine`, pois ela apagaria as bordas.

### B.5 --- Integração

O vetor de estados substitui o laço que alterava HP para controlar a saída. Não é obrigatório utilizar vetores: um `do/while`, `switch` ou chamadas explícitas também servem. A interface é desenhada antes do laço, as atualizações são independentes da posição anterior e `fflush(stdout)` antecede cada pausa. O cursor é restaurado no encerramento normal.

### Preservação da biblioteca do aluno

As funções variádicas conservam o contrato com `ANSI_END`, com constantes tipadas e impressão literal por `%s`. A validação das cores foi ajustada para rejeitar ponteiros nulos e códigos parcialmente numéricos. A barra continua com a estratégia de alocação e espaços coloridos do aluno. A versão de referência mantém o comportamento sequencial de `vPrintCentered` e `vPrintSeparator`. Essas correções pontuais não são uma exigência de refatoração geral do projeto entregue.

## 3. Verificação e investigação complementar

### A.5 --- Teste isolado

Antes da integração, pode-se compilar temporariamente o seguinte `main` no lugar do demonstrador:

``` c
#include <stdio.h>
#include "terminal_utils.h"

int main(void)
{
  vClearScreen();
  vPrintColor(TCOLOR_GREEN);
  vDrawBox(2, 2, 20, 5);
  vPrintColor(TCOLOR_YELLOW);
  vDrawBox(24, 2, 20, 5);
  printf("%s", ANSI_RESET);
  vDrawHLine(10, 9, 5);
  vDrawVLine(3, 9, 4);
  vDrawBox(20, 10, 2, 2);
  vFillRect(24, 10, 10, 3, BGCOLOR_BLUE);
  vDrawBox(1, 1, 1, 2); /* Sem efeito. */
  vFillRect(1, 1, 2, 2, NULL); /* Sem efeito. */
  vGotoXY(1, 15);
  fflush(stdout);
  return 0;
}
```

### Casos de verificação

  Caso                                    Resultado esperado
  --------------------------------------- -----------------------------------------
  Linha horizontal em (10,3), largura 5   Colunas 10--14 da linha 3
  Linha vertical em (3,2), altura 4       Linhas 2--5 da coluna 3
  Caixa 2 × 2                             Quatro cantos, sem segmentos adicionais
  Caixa sobre conteúdo existente          Interior preservado
  Dimensão ou coordenada inválida         Nenhuma saída
  Fundo nulo ou código `42abc`            Nenhuma saída
  HP 100, 75, 50, 90, 90                  20, 15, 10, 18, 18 células preenchidas
  HP negativo ou acima do máximo          Limitado a zero ou ao máximo
  Máximo zero                             HP indisponível, barra limpa
  Mensagem longa seguida de `Fim`         Sem resíduos nem bordas apagadas
  Encerramento                            Cursor visível, abaixo dos painéis

### Validação da referência

Executados `make`, compilação GCC C89 com `-Wall -Wextra -pedantic -Wformat=2 -Werror`, execução completa e comparação das sequências emitidas por um teste isolado de linhas, caixa mínima, preenchimento e entradas inválidas. Confirmados os cinco estados, uma única limpeza de tela, quatro molduras e restauração final do cursor. A renderização visual em terminal interativo e os demais casos de investigação da tabela devem ser conferidos pelo aluno; não foram todos executados nesta validação.

## 4. Sugestão de olhar avaliativo

### 4.1 O que é essencial e o que constitui desvio

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------
  Aspecto                 Isso tudo bem                                                   Sem isso não dá
  ----------------------- --------------------------------------------------------------- ------------------------------------------------------------------------
  Coordenadas             Outra distribuição de painéis                                   Convenção consistente e posicionamento correto

  Linhas e caixas         ASCII de compatibilidade ou outro estilo Unicode                Primitivas reutilizáveis, dimensões corretas e interior preservado

  Preenchimento           Outra estratégia de repetição de espaços                        Região exata, validação e reset dos atributos

  Cabeçalho               Adaptar centralização ou calcular posição                       Faixa colorida e título centralizado

  Organização             Outras dimensões, cores ou módulos                              Painéis lado a lado, sem sobreposição, HP e status delimitados

  HP                      Barra existente, outra cor ou outra implementação equivalente   Atualização proporcional, localizada, sem divisão por zero

  Status                  Preenchimento, espaços ou outra limpeza localizada              Mensagem menor sem resíduos e sem apagar bordas

  Simulação               Vetores, laço próprio ou chamadas explícitas                    Cinco estados solicitados, desenho inicial único e atualização parcial

  Biblioteca              Manter funções RPG na biblioteca ou separá-las                  Reutilização efetiva das primitivas e do trabalho anterior

  Execução                Outras pausas ou organização do fluxo                           Atualizações visíveis, compilação e cursor restaurado
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------

### 4.2 Variações aceitáveis

Não exigir a mesma assinatura de funções auxiliares internas, os mesmos nomes de constantes, a mesma estratégia de alocação da barra ou uma refatoração variádica. As quatro assinaturas públicas solicitadas e as assinaturas de atualização devem ser preservadas. A alternativa ASCII é aceitável quando justificada pela compatibilidade do terminal, desde que o aluno compreenda a representação Unicode fornecida. Não exigir memorização de pontos de código, sprites, entrada de teclado, clipping, tratamento de sinais ou `ncurses`.

### 4.3 Como conduzir a correção

Primeiro, peça ao aluno para demonstrar as primitivas isoladamente. Depois, observe a interface durante a simulação e solicite que explique quais células são alteradas. Se a solução redesenha tudo, apaga molduras ou depende da posição deixada pela última impressão, o objetivo central ainda não foi atingido, mesmo que a imagem final seja bonita. Peça uma correção localizada e uma nova demonstração.

Se uma função antiga precisar evoluir, identifique com o aluno o requisito novo que motivou a alteração. Uma implementação anterior não deve ser desqualificada apenas porque não antecipou esse requisito. Diferencie problemas que impedem o comportamento exigido de melhorias opcionais de organização e estilo.

## 5. Continuidade --- Terminal Utils v4

A biblioteca agora oferece formatação, atributos ANSI, posicionamento, linhas, molduras e preenchimento. A aplicação combina esses mecanismos para desenhar e atualizar regiões independentes. A próxima evolução será a entrada de dados e interatividade, preservando esta base visual.
