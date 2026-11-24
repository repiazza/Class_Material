# 14_Terminal_IO — Exercício 2

## Padronizando a formatação visual no terminal

### Objetivo

Evoluir a biblioteca de utilidades para terminal desenvolvida no Exercício 1, acrescentando suporte a cores de texto, cores de fundo e atributos visuais por meio de sequências ANSI.

Nesta etapa, construiremos uma interface que permita combinar diferentes atributos em uma única chamada de função, sem que a aplicação precise conhecer diretamente os códigos ANSI utilizados.

A biblioteca deverá continuar genérica, independente dos dados e das regras da aplicação.

## 1. Continuidade do projeto

Utilize os arquivos produzidos no Exercício 1:

```text
terminal_project/
├── main.c
├── terminal_utils.h
├── terminal_utils.c
└── Makefile
```

As cinco funções anteriormente implementadas deverão ser preservadas:

```c
void vPrintLine(const char *pszText, int bNewLine);
void vPrintSeparator(char cChar, int iWidth);
void vPrintCentered(const char *pszText, int iWidth);
void vPrintProgress(int iPercent);
void vPrintBar(int iValue, int iMax, int iWidth);
```

Não será necessário alterar o Makefile nem acrescentar novos arquivos ao projeto.

## 2. Etapa A — Padronização dos atributos ANSI

Até o momento, podemos aplicar atributos visuais diretamente utilizando `printf()`:

```c
printf("\033[37m\033[44m\033[4m");
printf("Texto destacado");
printf("\033[0m");
```

Entretanto, essa abordagem exige que a aplicação conheça os códigos ANSI e controle diretamente a restauração dos atributos.

Para facilitar a utilização desses recursos, vamos organizar as sequências ANSI por meio de constantes no arquivo `terminal_utils.h`.

### A.1 — Organização das constantes

Utilize as seguintes definições como ponto de partida:

```c
/* Controle */
#define ANSI_RESET "\033[0m"
#define ANSI_END   ((const char *)0)

/* Cores de texto */
#define TEXT_COLOR_WHITE ((const char *)"\033[37m")

/* Cores de fundo */
#define BACKGROUND_COLOR_BLUE ((const char *)"\033[44m")

/* Atributos visuais */
#define UNDERLINE_TEXT ((const char *)"\033[4m")
```

Complete as definições utilizando os conhecimentos adquiridos nos materiais do capítulo.

A biblioteca deverá disponibilizar:

**Cores de texto:**

- Preto;
- Vermelho;
- Verde;
- Amarelo;
- Azul;
- Magenta;
- Ciano;
- Branco.

**Cores de fundo:**

- As mesmas oito cores disponíveis para o texto.

**Atributos visuais:**

- Negrito;
- Intensidade reduzida;
- Itálico;
- Sublinhado;
- Inversão das cores;
- Tachado.

Mantenha uma nomenclatura consistente e organize as constantes de acordo com suas respectivas categorias.

Todas as constantes destinadas à lista de argumentos variáveis deverão seguir o tipo `const char *`, conforme os exemplos fornecidos.

Não será necessário implementar a paleta de 256 cores, cores intensas ou cores RGB nesta etapa.

## 3. Etapa B — Implementação da função de impressão formatada

Acrescente a seguinte declaração à interface pública da biblioteca, em `terminal_utils.h`:

```c
void vPrintFormatted(const char *pszText, ...);
```

Essa função deverá receber um texto e uma quantidade variável de atributos visuais.

### B.1 — Exemplos de utilização

Impressão utilizando apenas uma cor:

```c
vPrintFormatted("Texto vermelho",
                TEXT_COLOR_RED,
                ANSI_END);
```

Impressão combinando diferentes atributos:

```c
vPrintFormatted("Texto destacado",
                TEXT_COLOR_WHITE,
                BACKGROUND_COLOR_BLUE,
                UNDERLINE_TEXT,
                ANSI_END);
```

Impressão sem atributos adicionais:

```c
vPrintFormatted("Texto comum",
                ANSI_END);
```

A constante `ANSI_END` indica o término da lista de argumentos e deverá estar presente em todas as chamadas.

### B.2 — Estrutura sugerida da implementação

A estrutura de leitura dos argumentos variáveis é fornecida abaixo. Utilize-a como base para completar a implementação em `terminal_utils.c`.

```c
#include <stdio.h>
#include <stdarg.h>
#include "terminal_utils.h"

void vPrintFormatted(const char *pszText, ...)
{
  va_list args;
  const char *pszAttr;

  if (pszText == NULL)
    return;

  va_start(args, pszText);

  while ((pszAttr = va_arg(args, const char *)) != ANSI_END) {
    /* Processamento de cada atributo */
  }

  va_end(args);

  /* Complete a implementacao */
}
```

A mecânica de leitura dos argumentos já está disponível. O desafio consiste em determinar como esses argumentos deverão ser utilizados para produzir corretamente o resultado no terminal.

Considere as seguintes questões durante a implementação:

- Em qual momento os atributos deverão ser enviados ao terminal?
- Em qual momento o texto deverá ser impresso?
- Como garantir que todos os atributos recebidos sejam aplicados?
- Em qual momento os atributos deverão ser restaurados?

### B.3 — Contrato da função

A implementação deverá respeitar as seguintes condições:

- Aceitar qualquer quantidade de atributos, incluindo nenhum.
- Processar os atributos na ordem em que foram recebidos.
- Imprimir o texto recebido uma única vez.
- Restaurar os atributos visuais padrão do terminal ao final da impressão.
- Não acrescentar automaticamente uma quebra de linha.
- Não produzir saída quando `pszText` for `NULL`.
- Tratar o texto como dado literal, inclusive quando contiver o caractere `%`.

Não será necessário concatenar strings, utilizar alocação dinâmica ou construir uma string de formato dinamicamente.

A função não deverá interpretar os códigos ANSI recebidos. Essa interpretação é responsabilidade do terminal.

## 4. Etapa C — Verificação da implementação

Antes de modificar o demonstrador do Exercício 1, utilize temporariamente o `main.c` abaixo para verificar o comportamento da nova função.

```c
#include <stdio.h>
#include "terminal_utils.h"

int main(void)
{
  vPrintFormatted("Texto vermelho\n",
                  TEXT_COLOR_RED,
                  ANSI_END);

  vPrintFormatted("Texto destacado\n",
                  TEXT_COLOR_WHITE,
                  BACKGROUND_COLOR_BLUE,
                  UNDERLINE_TEXT,
                  ANSI_END);

  vPrintFormatted("Carregamento: 100%\n",
                  TEXT_COLOR_GREEN,
                  BOLD_TEXT,
                  ANSI_END);

  vPrintFormatted("Sem atributos adicionais\n",
                  ANSI_END);

  printf("Texto normal\n");

  return 0;
}
```

Observe se:

- Cada texto apresenta os atributos solicitados.
- Diferentes atributos podem ser combinados.
- O caractere `%` é apresentado corretamente.
- O último `printf()` apresenta texto normal, sem herdar os atributos anteriores.

Considere que alguns atributos, como itálico e tachado, podem apresentar diferenças de comportamento dependendo do terminal utilizado.

### C.1 — Investigação complementar

Experimente realizar as seguintes chamadas:

```c
vPrintFormatted("Primeiro teste\n",
                TEXT_COLOR_RED,
                TEXT_COLOR_GREEN,
                ANSI_END);

vPrintFormatted("Segundo teste\n",
                TEXT_COLOR_GREEN,
                TEXT_COLOR_RED,
                ANSI_END);
```

Observe o resultado e responda:

- Os dois textos apresentam a mesma cor?
- Qual é a influência da ordem dos argumentos?
- Por que é possível combinar uma cor de texto com uma cor de fundo, mas duas cores de texto não são apresentadas simultaneamente?

Não será necessário implementar mecanismos para detectar atributos conflitantes.

## 5. Etapa D — Evolução do programa demonstrador

Recupere o `main.c` desenvolvido no Exercício 1 e utilize a nova função para melhorar a apresentação visual da ficha do personagem.

O demonstrador deverá continuar apresentando as mesmas informações:

```text
================================
           RPG STATUS
================================

Nome:         Guerreiro
Nivel:                5
Ataque:              25
Defesa:              12

HP: 75/100
[###############-----]

--------------------------------
Carregando inventario...
Progresso: 100%
Carregamento concluido!
```

Acrescente formatação visual utilizando os recursos desenvolvidos neste exercício.

Como requisitos mínimos:

- Destaque o título ou uma mensagem importante utilizando uma combinação de cor de texto, cor de fundo e atributo visual.
- Utilize cores diferentes para destacar pelo menos duas informações do personagem.
- Apresente a mensagem de carregamento concluído utilizando texto verde e negrito.
- Preserve o alinhamento e o comportamento das funcionalidades anteriores.

A escolha das demais cores e atributos fica a critério do aluno.

### D.1 — Formatação de informações dinâmicas

A função `vPrintFormatted()` recebe um texto pronto para impressão. Sua lista de argumentos variáveis é destinada exclusivamente aos atributos ANSI.

Quando for necessário apresentar valores de variáveis, uma possibilidade é preparar previamente o texto utilizando `sprintf()`.

Exemplo:

```c
char szBuffer[64];
int iHP = 75;
int iMaxHP = 100;

sprintf(szBuffer, "HP: %d/%d", iHP, iMaxHP);

vPrintFormatted(szBuffer,
                TEXT_COLOR_GREEN,
                ANSI_END);

printf("\n");
```

Neste exemplo, o tamanho do buffer é suficiente para os valores inteiros utilizados.

Não modifique a assinatura de `vPrintFormatted()` para receber argumentos de substituição de texto. A preparação do conteúdo e a aplicação dos atributos são responsabilidades distintas.

## 6. Critérios de conclusão

- [ ] As constantes ANSI foram organizadas em categorias no header da biblioteca.
- [ ] As oito cores básicas de texto e de fundo estão disponíveis.
- [ ] Os atributos visuais solicitados foram definidos.
- [ ] A função `vPrintFormatted()` foi implementada conforme o contrato.
- [ ] A função permite combinar diferentes atributos em uma única chamada.
- [ ] A restauração dos atributos ocorre automaticamente.
- [ ] O aluno consegue explicar a influência da ordem dos atributos.
- [ ] O demonstrador anterior foi atualizado com os novos recursos.
- [ ] As cinco funções do Exercício 1 foram preservadas.
- [ ] O projeto compila sem avisos utilizando o Makefile anterior.

## 7. Continuidade do projeto

Preserve os arquivos produzidos neste exercício. Eles constituirão a segunda versão da biblioteca de utilidades para terminal — Terminal Utils v2.

No Exercício 3, acrescentaremos recursos de posicionamento do cursor, limpeza de linhas e tela, permitindo atualizar informações em regiões específicas do terminal.

Nesta etapa, não utilize posicionamento absoluto ou relativo do cursor, limpeza de tela, ncurses ou bibliotecas gráficas.

O objetivo deste exercício é compreender que os atributos visuais representam um estado do terminal e que esse estado pode ser manipulado de maneira organizada por uma interface genérica, sem transferir essa responsabilidade para cada trecho da aplicação.
