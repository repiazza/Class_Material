# 14_Terminal_IO — Gabarito 3

## Manipulação espacial do terminal

Referência para correção do `exercicio3.md` e continuidade da Terminal Utils. A solução é uma implementação possível, não um algoritmo obrigatório. Utiliza como base os fontes do aluno, preservando os nomes, as barras coloridas e a centralização variádica.

## 1. Solução de referência

As funções existentes são preservadas, com correções pontuais no contrato variádico e na impressão literal. As seis novas funções encapsulam o controle espacial. O demonstrador anterior é substituído pela simulação RPG solicitada.

### terminal_utils.h

```c
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

#endif
```

### terminal_utils.c

```c
#include "terminal_utils.h"
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdarg.h>

void vPrintColor(const char *pszColor){
  printf("%s%s%s", COLOR_PREFIX, pszColor, ANSI_LINE_END);
}

int bIsBGColor(const char *pszColor){
  if(atoi(pszColor) < atoi(BGCOLOR_BLACK) || atoi(pszColor) > atoi(BGCOLOR_WHITE)) return 0;
  
  return 1;
}

int bIsTColor (const char *pszColor){
  if(atoi(pszColor) < atoi(TCOLOR_BLACK) || atoi(pszColor) > atoi(TCOLOR_WHITE)) return 0;
  
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
```

### main.c

```c
#include <stdio.h>
#include <unistd.h>
#include "terminal_utils.h"

#define SCREEN_WIDTH 40
#define HP_LINE 8
#define BAR_LINE 9
#define STATUS_LINE 11
#define BAR_WIDTH 20

void vDrawInterface(void)
{
  vGotoXY(1, 1);
  vPrintSeparator('=', SCREEN_WIDTH);
  vGotoXY(1, 2);
  vPrintCentered("RPG STATUS", SCREEN_WIDTH, BGCOLOR_BLUE,
                 TCOLOR_WHITE, BOLD_TEXT, ANSI_END);
  vGotoXY(1, 3);
  vPrintSeparator('=', SCREEN_WIDTH);
  vGotoXY(1, 4);
  vPrintFormatted("PERSONAGEM", TCOLOR_CIAN, ANSI_END);
  vGotoXY(24, 4);
  vPrintFormatted("ATRIBUTOS", TCOLOR_CIAN, ANSI_END);
  vGotoXY(1, 5);
  vPrintLine("Nome: Guerreiro", 0);
  vGotoXY(24, 5);
  printf("Ataque: %d", 25);
  vGotoXY(1, 6);
  printf("Nivel: %d", 5);
  vGotoXY(24, 6);
  printf("Defesa: %d", 12);
  vGotoXY(1, 7);
  vPrintSeparator('-', SCREEN_WIDTH);
  vGotoXY(1, 10);
  vPrintSeparator('-', SCREEN_WIDTH);
  vGotoXY(1, 12);
  vPrintSeparator('=', SCREEN_WIDTH);
}

void vUpdateHP(int iHP, int iMaxHP)
{
  if (iMaxHP <= 0)
    return;
  if (iHP < 0)
    iHP = 0;
  if (iHP > iMaxHP)
    iHP = iMaxHP;

  vSaveCursor();
  vGotoXY(1, HP_LINE);
  vClearLine();
  printf("HP: %d/%d", iHP, iMaxHP);
  vGotoXY(1, BAR_LINE);
  vPrintBar(iHP, iMaxHP, BAR_WIDTH, BGCOLOR_GREEN);
  vRestoreCursor();
}

void vUpdateStatus(const char *pszStatus)
{
  if (pszStatus == NULL)
    return;
  vSaveCursor();
  vGotoXY(1, STATUS_LINE);
  vClearLine();
  vPrintFormatted("STATUS: ", TCOLOR_YELLOW, ANSI_END);
  printf("%.*s", SCREEN_WIDTH - 8, pszStatus);
  vRestoreCursor();
}

int main(void)
{
  int i;
  int aiHP[] = {100, 75, 50, 90, 90};
  const char *apszStatus[] = {"Pronto", "Dano recebido!",
                             "Em perigo!", "Cura recebida!", "Fim"};

  vClearScreen();
  vShowCursor(0);
  vDrawInterface();
  for (i = 0; i < 5; i++) {
    vUpdateHP(aiHP[i], 100);
    vUpdateStatus(apszStatus[i]);
    fflush(stdout);
    if (i < 4)
      sleep(1);
  }
  vGotoXY(1, 13);
  vShowCursor(1);
  fflush(stdout);
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

### Posicionamento e limpeza

`vGotoXY(iX, iY)` recebe coluna e linha, mas emite `ESC[linha;colunaH`. A origem adotada é (1,1). Coordenadas inferiores a 1 são ignoradas; não há consulta às dimensões do terminal. A limpeza `ESC[2J` não implica reposicionamento, por isso `vClearScreen()` chama também `vGotoXY(1, 1)`. Já `ESC[2K` apaga a linha atual sem mover o cursor.

### Estado do cursor

As sequências `ESC[s` e `ESC[u` salvam e restauram a posição em terminais compatíveis. Não se pressupõe uma pilha de posições salvas nem restauração dos atributos visuais. `ESC[?25l` oculta o cursor e `ESC[?25h` o exibe. Ao terminar normalmente, o programa posiciona o cursor abaixo da interface e o exibe novamente.

### Separação entre desenho e atualização

`vDrawInterface()` é chamada uma única vez. As coordenadas dos campos dinâmicos são constantes da aplicação, não da biblioteca. O exemplo ocupa 40 colunas e 12 linhas; recomenda-se um terminal com pelo menos 41 colunas e 13 linhas para evitar efeitos de quebra automática na borda.

`vUpdateHP()` limpa a linha numérica antes de escrever o novo valor. A barra é inteiramente sobrescrita com a mesma largura de 20 células, incluindo as células vazias, de modo que não é necessário limpar sua linha. `vUpdateStatus()` limpa sua linha antes de imprimir o rótulo e a mensagem. O limite de 32 bytes para a mensagem é adequado aos textos ASCII da simulação; não é uma solução geral para largura visual Unicode ou caracteres de controle.

Ambas as funções salvam e restauram a posição do chamador, sem chamadas aninhadas de salvamento. O `fflush(stdout)` ocorre depois das duas atualizações e antes da espera, permitindo observar cada estado completo. Não é necessário redesenhar a estrutura fixa nem chamar `vClearScreen()` dentro do laço.

### Preservação da biblioteca do aluno

As macros de cores numéricas continuam separadas do prefixo e do sufixo ANSI, mas passam a ter tipo `const char *`, correspondente ao `va_arg()`. Todas as chamadas variádicas terminam em `ANSI_END`. Textos e atributos são emitidos com formato literal `%s`. A validação da largura em `vPrintCentered()` precede `va_start()`, garantindo que não exista retorno sem o correspondente `va_end()`.

A formatação do percentual foi simplificada para `%3d%%`, evitando `snprintf()` (C99) sem alterar a composição da barra com o percentual. A alocação da barra e a classificação das cores do aluno foram mantidas para não transformar este exercício em uma refatoração geral. A classificação por `atoi()` pressupõe os códigos válidos fornecidos pelas macros; validação estrita de entradas arbitrárias não é objetivo desta etapa.

## 3. Verificação e investigação complementar

Execute `make` e `./terminal_demo` em um terminal compatível com as sequências utilizadas. A interface permanece na mesma posição e os estados são apresentados aproximadamente a cada segundo, sem entrada interativa.

| Estado | HP | Células preenchidas (de 20) | Mensagem |
|---|---|---:|---|
| 1 | 100/100 | 20 | Pronto |
| 2 | 75/100 | 15 | Dano recebido! |
| 3 | 50/100 | 10 | Em perigo! |
| 4 | 90/100 | 18 | Cura recebida! |
| 5 | 90/100 | 18 | Fim |

O último estado deve permanecer visível, sem resíduos da mensagem anterior. O cursor deve estar visível na linha 13, coluna 1.

### Casos de verificação

`ESC` representa o byte 0x1B. Os espaços entre sequências são apenas separadores ilustrativos.

| Chamada | Bytes esperados |
|---|---|
| `vGotoXY(5, 3)` | `ESC[3;5H` |
| `vGotoXY(0, 3)` | Nenhum byte |
| `vGotoXY(5, -1)` | Nenhum byte |
| `vClearScreen()` | `ESC[2J ESC[1;1H` |
| `vClearLine()` | `ESC[2K` |
| `vSaveCursor()` | `ESC[s` |
| `vRestoreCursor()` | `ESC[u` |
| `vShowCursor(0)` | `ESC[?25l` |
| `vShowCursor(1)` | `ESC[?25h` |

Teste também a redução de HP de 100 para 75 e a substituição de `Cura recebida!` por `Fim`. Verifique que a barra diminui e que não sobra texto. Posicione o cursor em uma linha livre antes de chamar uma função de atualização e confirme que ele retorna à posição original.

### Validação da referência

A solução foi compilada com `make` e também com `-Wformat=2`, sem avisos. A execução com saída redirecionada confirmou uma limpeza de tela, uma ocorrência do cabeçalho, dez limpezas de linha, dez pares de salvamento/restauração e a sequência final de reposicionamento e exibição do cursor. A renderização visual em um terminal interativo não foi testada nesta validação.

## 4. Sugestão de olhar avaliativo

### 4.1 O que é essencial e o que constitui desvio

| Conceito | Evidência de assimilação | Desvio que exige correção |
|---|---|---|
| Coordenadas | Converte X/Y em linha/coluna; ignora valores inferiores a 1 | Inverte os eixos ou utiliza origem incompatível |
| Limpeza | Limpa tela e reposiciona; limpa linha sem mover | Confunde limpeza com movimentação |
| Atualização parcial | Desenha uma vez e altera somente campos dinâmicos | Limpa ou redesenha toda a tela a cada estado |
| Sobrescrita | Barra de largura fixa e mensagens sem resíduos | Restos de texto ou células preenchidas indevidamente |
| Cursor | Salva/restaura em pelo menos uma atualização e exibe ao final | Perde posição do chamador ou deixa cursor oculto |
| Buffering | Estados visíveis antes da espera | Atualizações acumuladas sem exibição durante a simulação |
| Composição | Reutiliza a barra e a formatação existentes | Duplica a biblioteca dentro da aplicação |
| Modularidade | Coordenadas e dados RPG na aplicação | Regras específicas de RPG na biblioteca genérica |
| Contrato anterior | Sentinela tipada e impressão literal | Lista variádica sem terminador ou texto usado como formato |

### 4.2 Variações aceitáveis

- Layout, cores, nomes de constantes e coordenadas diferentes, desde que as regiões não se sobreponham.
- Limpeza localizada ou preenchimento com espaços para remover resíduos, preservando o restante da interface.
- Chamadas explícitas em sequência em vez dos vetores e do laço da referência.
- Sequências alternativas de salvamento/restauração suportadas pelo terminal utilizado.
- Refatorações locais da biblioteca, inclusive eliminação da alocação da barra, desde que preservem suas funcionalidades e contratos.

Não exigir detecção do tamanho do terminal, molduras gráficas, Unicode, tratamento de sinais, entrada de teclas ou `ncurses`. A restauração em caso de interrupção anormal é uma melhoria futura, não requisito desta simulação.

### 4.3 Como conduzir a correção

**Solução assimilada:** o aluno explica a inversão dos argumentos de posicionamento, a diferença entre limpar e mover, e por que a interface fixa não precisa ser redesenhada. Demonstra a redução da barra e a remoção de resíduos.

**Solução com ajustes pontuais:** coordenada deslocada, mensagem residual, ausência de flush ou cursor oculto ao final podem ser corrigidos localmente. Peça que o aluno identifique qual responsabilidade precisa ser ajustada.

**Conceito ainda não assimilado:** redesenho completo dentro do laço, mistura de regras RPG com a biblioteca ou incapacidade de atualizar uma região independentemente. Retomar a composição entre posicionamento, limpeza e impressão antes de avançar.

Uma verificação de autonomia consiste em pedir ao aluno que mude a posição da barra sem alterar `vPrintBar()` e substitua uma mensagem longa por outra curta, explicando previamente o efeito esperado.

## 5. Continuidade — Terminal Utils v3

Preservar a implementação válida do aluno. A biblioteca agora fornece primitivas de apresentação, formatação e manipulação espacial. A aplicação decide onde e quando utilizá-las. O próximo bloco poderá introduzir entrada de dados e interatividade sem exigir uma nova implementação da saída.
