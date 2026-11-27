# Exercício 3 — Manipulação espacial do terminal

## Objetivo

Evoluir a biblioteca `terminal_utils` desenvolvida nos exercícios anteriores, permitindo posicionar o cursor, controlar a apresentação do terminal e atualizar regiões da tela independentemente.

Utilize como ponto de partida os fontes `main.c`, `terminal_utils.c` e `terminal_utils.h` da sua implementação atual. Preserve as funcionalidades já desenvolvidas, incluindo as barras coloridas e a formatação com argumentos variáveis.

## Parte A — Evolução da biblioteca

Implemente e declare em `terminal_utils.h` as seguintes funções:

```c
void vGotoXY(int iX, int iY);
void vClearScreen(void);
void vClearLine(void);
void vSaveCursor(void);
void vRestoreCursor(void);
void vShowCursor(int bShow);
```

| Função | Comportamento esperado |
|---|---|
| `vGotoXY` | Posiciona o cursor na coluna `iX` e na linha `iY`, com origem em (1,1). Ignora coordenadas menores que 1. |
| `vClearScreen` | Limpa toda a tela e posiciona o cursor em (1,1). |
| `vClearLine` | Limpa toda a linha atual, sem alterar a posição do cursor. |
| `vSaveCursor` | Salva a posição atual do cursor. |
| `vRestoreCursor` | Restaura a posição anteriormente salva. |
| `vShowCursor` | Oculta o cursor quando `bShow` for zero e o exibe caso contrário. |

Utilize as sequências de escape estudadas neste capítulo, em um terminal compatível. Lembre-se de que a sequência ANSI de posicionamento recebe primeiro a linha e depois a coluna.

Antes de prosseguir, revise as chamadas variádicas existentes: todas devem terminar com `ANSI_END`, e os argumentos devem corresponder ao tipo recuperado por `va_arg()`. Garanta também que textos sejam impressos como dados, e não como strings de formato.

## Parte B — Interface dinâmica RPG

Modifique o demonstrador RPG existente para organizar a tela em regiões independentes:

```text
========================================
               RPG STATUS
========================================
PERSONAGEM             ATRIBUTOS
Nome: Guerreiro        Ataque: 25
Nivel: 5               Defesa: 12
----------------------------------------
HP: 100/100
[####################]
----------------------------------------
STATUS: Pronto
========================================
```

A representação acima é apenas uma referência de organização. Utilize as cores, atributos e barras já disponíveis na sua biblioteca. Os caracteres `#` representam visualmente a parte preenchida da barra colorida.

Separe o desenho inicial da interface das operações de atualização. Para isso, implemente na aplicação funções com as seguintes responsabilidades:

```c
void vDrawInterface(void);
void vUpdateHP(int iHP, int iMaxHP);
void vUpdateStatus(const char *pszStatus);
```

Essas funções pertencem à aplicação RPG, não à biblioteca genérica `terminal_utils`.

### B.1 — Desenho inicial: `vDrawInterface()`

Esta função deve apresentar a estrutura fixa da interface: cabeçalho, separadores, nome, nível, ataque e defesa. Reserve também posições para o valor de HP, a barra e a mensagem de estado.

Utilize `vGotoXY()` para posicionar os elementos, inclusive aqueles que aparecem lado a lado. Por exemplo:

```c
vGotoXY(1, 4);
vPrintLine("PERSONAGEM", 0);

vGotoXY(24, 4);
vPrintLine("ATRIBUTOS", 0);
```

Uma possibilidade é definir as posições das regiões dinâmicas por meio de constantes no `main.c`:

```c
#define HP_LINE      8
#define BAR_LINE     9
#define STATUS_LINE 11
#define BAR_WIDTH   20
```

Essas coordenadas correspondem ao layout sugerido acima. Caso organize a interface de outra maneira, adapte as constantes. A ideia é que o desenho inicial e as funções de atualização utilizem as mesmas referências espaciais.

### B.2 — Atualização da vida: `vUpdateHP()`

Esta função recebe a vida atual (`iHP`) e a vida máxima (`iMaxHP`) do personagem. Ela deve atualizar duas regiões distintas: a linha que apresenta o valor numérico e a linha que apresenta a barra colorida.

Por exemplo, ao chamar:

```c
vUpdateHP(75, 100);
```

O resultado esperado na região de HP é:

```text
HP: 75/100
[###############     ]
```

Uma chamada posterior a `vUpdateHP(50, 100)` deve produzir, exatamente nas mesmas posições:

```text
HP: 50/100
[##########          ]
```

Observe que a barra continua com 20 células internas. Apenas a quantidade de células preenchidas muda. Os caracteres `#` são ilustrativos: utilize a barra colorida já implementada.

A implementação pode seguir esta sequência:

```text
Salvar a posição atual do cursor.
Posicionar o cursor no início da linha de HP.
Limpar essa linha para remover o valor anterior.
Imprimir o novo valor de HP.
Posicionar o cursor no início da linha da barra.
Desenhar novamente a barra com a mesma largura.
Restaurar a posição do cursor.
```

Para orientar a composição das funções, considere este trecho de código C:

```c
vGotoXY(1, HP_LINE);
vClearLine();
printf("HP: %d/%d", iHP, iMaxHP);

vGotoXY(1, BAR_LINE);
vPrintBar(iHP, iMaxHP, BAR_WIDTH, BGCOLOR_GREEN);
```

Complete a função com a preservação da posição do cursor e o tratamento dos valores recebidos: a vida máxima deve ser positiva e a vida atual deve permanecer entre zero e a vida máxima.

Não é necessário criar outra função para calcular ou desenhar a barra: `vPrintBar()` já possui essa responsabilidade. Também não é necessário alterar o personagem, calcular dano ou implementar uma batalha dentro de `vUpdateHP()`.

### B.3 — Atualização da mensagem: `vUpdateStatus()`

Esta função deve posicionar o cursor na região de mensagens e substituir o conteúdo anterior, preservando o restante da interface.

Considere as chamadas:

```c
vUpdateStatus("Cura recebida!");
vUpdateStatus("Fim");
```

O resultado final deve ser `STATUS: Fim`, sem caracteres restantes da mensagem anterior.

Uma possibilidade é posicionar o cursor no início da linha, limpá-la com `vClearLine()` e imprimir novamente o rótulo `STATUS:` seguido da nova mensagem. Você pode utilizar as funções de formatação já existentes na biblioteca.

### Simulação

Limpe a tela, oculte o cursor e desenhe a interface uma única vez. Em seguida, simule a sequência abaixo, com um intervalo de aproximadamente um segundo entre os estados:

| HP | Mensagem |
|---|---|
| 100/100 | Pronto |
| 75/100 | Dano recebido! |
| 50/100 | Em perigo! |
| 90/100 | Cura recebida! |
| 90/100 | Fim |

A última mensagem permite verificar se a substituição de um texto longo por um curto deixa resíduos na tela.

Utilize `vSaveCursor()` e `vRestoreCursor()` em pelo menos uma das funções de atualização para preservar a posição do cursor do chamador. Utilize `fflush(stdout)` quando necessário para que cada estado seja exibido antes da espera.

Ao finalizar, reposicione o cursor abaixo da interface e torne-o visível novamente.

## Requisitos

- A tela completa deve ser limpa e desenhada apenas no início da simulação.
- Os campos estáticos devem permanecer inalterados durante as atualizações.
- A barra de HP deve manter sua largura e refletir corretamente a redução e a recuperação da vida.
- Não devem permanecer caracteres de valores ou mensagens anteriores.
- Preserve a separação entre a biblioteca genérica e a aplicação.
- Não utilize `ncurses`, entrada interativa de teclas ou um motor de batalha. A simulação deve ser automática.
- Mantenha o projeto modular e o estilo de programação em C utilizado nos exercícios anteriores.

## Entrega

Entregue `main.c`, `terminal_utils.c`, `terminal_utils.h` e o `Makefile` utilizado para compilar o projeto.

O resultado esperado é uma interface que permanece na mesma posição do terminal enquanto apenas suas informações dinâmicas são atualizadas.
