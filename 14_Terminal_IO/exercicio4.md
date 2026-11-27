# Exercício 4 — Construção de interfaces gráficas no terminal

## 1. Objetivo

Evoluir a interface RPG construída no Exercício 3, utilizando a biblioteca `terminal_utils` já desenvolvida. A nova apresentação deverá possuir cabeçalho colorido, molduras, painéis lado a lado, barra de HP e uma região de mensagens.

Não será necessário iniciar um novo projeto, utilizar `ncurses`, memorizar tabelas de caracteres ou implementar entrada de teclado. O objetivo é construir uma interface visual a partir de células de texto, coordenadas e atributos ANSI.

### Ponto de partida

Utilize seus arquivos atuais `main.c`, `terminal_utils.c`, `terminal_utils.h` e o Makefile do projeto. Preserve uma cópia da versão anterior.

As funções `vGotoXY`, `vPrintColor`, `vPrintFormatted`, `vPrintCentered`, `vPrintBar`, `vSaveCursor`, `vRestoreCursor` e `vShowCursor` já oferecem boa parte dos mecanismos necessários. Algumas poderão precisar de adaptações devido aos novos requisitos. Isso não significa que a implementação anterior estava inadequada ao seu objetivo original.

## Parte A — Primitivas de desenho

### A.1 — Caracteres para construção de molduras

Os caracteres abaixo pertencem ao Unicode e podem ser representados em UTF-8. Não são caracteres do ASCII tradicional, nem dependem de uma tabela ASCII estendida específica.

| Elemento | Caractere | Unicode | Bytes UTF-8 em C |
|---|---|---|---|
| Linha horizontal | `─` | U+2500 | `"\xE2\x94\x80"` |
| Linha vertical | `│` | U+2502 | `"\xE2\x94\x82"` |
| Canto superior esquerdo | `╭` | U+256D | `"\xE2\x95\xAD"` |
| Canto superior direito | `╮` | U+256E | `"\xE2\x95\xAE"` |
| Canto inferior esquerdo | `╰` | U+2570 | `"\xE2\x95\xB0"` |
| Canto inferior direito | `╯` | U+256F | `"\xE2\x95\xAF"` |
| Bloco cheio (opcional) | `█` | U+2588 | `"\xE2\x96\x88"` |

Você pode copiar estas definições para `terminal_utils.h`:

```c
#define BOX_HORIZONTAL   "─"
#define BOX_VERTICAL     "│"
#define BOX_TOP_LEFT     "╭"
#define BOX_TOP_RIGHT    "╮"
#define BOX_BOTTOM_LEFT  "╰"
#define BOX_BOTTOM_RIGHT "╯"
```

Salve os fontes em UTF-8 e utilize um terminal com fonte compatível. Se necessário, utilize as sequências de bytes da tabela no lugar dos caracteres literais. Como alternativa de compatibilidade, utilize `-`, `|` e `+`.

Experimente `printf("%s", BOX_HORIZONTAL);`. Cada símbolo de moldura ocupa normalmente uma célula no terminal utilizado neste exercício, embora sua representação UTF-8 possua três bytes.

**Dica:** sua função `vPrintSeparator(char cChar, int iWidth)` recebe um único byte e acrescenta uma quebra de linha. Ela pode continuar existindo para separadores ASCII. Para as novas molduras, será mais conveniente trabalhar com strings e controlar explicitamente a posição do cursor.

### A.2 — Desenho de linhas

Implemente:

```c
void vDrawHLine(int iX, int iY, int iWidth);
void vDrawVLine(int iX, int iY, int iHeight);
```

Adote X como coluna e Y como linha, com origem `(1, 1)`. As dimensões representam quantidades de células, não coordenadas finais.

Uma linha horizontal de cinco células iniciada em `(3, 2)` ocupa as colunas 3 a 7 da linha 2. Uma linha vertical de quatro células iniciada em `(3, 2)` ocupa as linhas 2 a 5 da coluna 3.

Exemplo de implementação orientativa da linha horizontal:

```c
int ii;

vGotoXY(iX, iY);
for(ii = 0; ii < iWidth; ii++)
  printf("%s", BOX_HORIZONTAL);
```

Para a linha vertical, utilize o seguinte raciocínio:

```c
for(ii = 0; ii < iHeight; ii++){
  vGotoXY(iX, iY + ii);
  printf("%s", BOX_VERTICAL);
}
```

Não acrescente quebras de linha. Coordenadas ou dimensões menores que 1 devem resultar em nenhuma operação. As funções devem respeitar a cor de texto atualmente ativa.

**Dica de evolução:** confira o contrato de `vGotoXY()` com uma posição assimétrica, por exemplo `(10, 3)`. A sequência ANSI recebe primeiro a linha e depois a coluna:

```c
printf("%s%d;%d%s", ANSI_PREFIX_INIT, iY, iX, CUR_LINE_END);
```

Se sua implementação atual utiliza outra convenção, adapte-a e revise os pontos de chamada. A necessidade de uma convenção consistente torna-se mais evidente agora que desenhamos em duas dimensões.

### A.3 — Desenho de molduras

Implemente:

```c
void vDrawBox(int iX, int iY, int iWidth, int iHeight);
```

A largura e a altura incluem as bordas. Considere dimensões mínimas de duas células em cada direção. Dimensões inválidas não devem produzir saída.

```text
╭────────╮
│        │
│        │
╰────────╯
```

O exemplo acima corresponde a uma caixa de largura 10 e altura 4.

As coordenadas dos cantos são:

| Canto | X | Y |
|---|---|---|
| Superior esquerdo | `iX` | `iY` |
| Superior direito | `iX + iWidth - 1` | `iY` |
| Inferior esquerdo | `iX` | `iY + iHeight - 1` |
| Inferior direito | `iX + iWidth - 1` | `iY + iHeight - 1` |

Reutilize as funções da etapa anterior para desenhar os segmentos entre os cantos:

```c
/* Trecho orientativo, após validar as dimensões. */
vDrawHLine(iX + 1, iY, iWidth - 2);
vDrawHLine(iX + 1, iY + iHeight - 1, iWidth - 2);
vDrawVLine(iX, iY + 1, iHeight - 2);
vDrawVLine(iX + iWidth - 1, iY + 1, iHeight - 2);
```

Complete a função posicionando e imprimindo os quatro cantos. A moldura não deve apagar seu conteúdo interno.

Para desenhar uma moldura verde, reutilize os recursos existentes:

```c
vPrintColor(TCOLOR_GREEN);
vDrawBox(2, 4, 28, 6);
printf("%s", ANSI_RESET);
```

**Dica:** não é obrigatório criar uma nova versão variádica de cada função. Separar a seleção de cor do desenho já permite compor operações reutilizáveis.

### A.4 — Preenchimento de regiões

Implemente:

```c
void vFillRect(int iX, int iY, int iWidth, int iHeight,
               const char *pszColor);
```

Uma região colorida pode ser construída imprimindo espaços com uma cor de fundo ativa. Utilize as constantes `BGCOLOR_*` e a função `vPrintColor()` que você já possui.

```c
/* Trecho orientativo, após validar os parâmetros. */
int iRow, iCol;

vPrintColor(pszColor);
for(iRow = 0; iRow < iHeight; iRow++){
  vGotoXY(iX, iY + iRow);
  for(iCol = 0; iCol < iWidth; iCol++)
    putchar(' ');
}
printf("%s", ANSI_RESET);
```

Valide coordenadas, dimensões positivas e a cor de fundo (inclusive ponteiro nulo antes de chamar `bIsBGColor`). A função deve preencher exatamente a região solicitada, substituindo seu conteúdo anterior por espaços, e retornar aos atributos padrão ao terminar.

**Dica:** observe que sua barra de progresso já utiliza espaços coloridos. O novo recurso generaliza essa ideia para uma região de várias linhas. Não é necessário reescrever `vPrintBar()` para implementar `vFillRect()`.

### A.5 — Teste isolado das primitivas

Antes de modificar o RPG, experimente desenhar duas caixas lado a lado, uma linha horizontal, uma linha vertical e uma região preenchida. Utilize cores diferentes e coordenadas assimétricas. Verifique também uma caixa 2 × 2 e dimensões inválidas. Posicione o cursor fora do desenho ao finalizar.

## Parte B — Evolução da interface RPG

### B.1 — Planejamento espacial

Utilize as primitivas da Parte A para construir uma interface semelhante à seguinte. As cores são descritas abaixo, pois o Markdown não representa os atributos ANSI do terminal.

```text
                 RPG STATUS

╭──────────────────────────╮ ╭──────────────────────────╮
│ PERSONAGEM               │ │ ATRIBUTOS                │
│ Nome: Guerreiro          │ │ Ataque: 25               │
│ Nivel: 5                 │ │ Defesa: 12               │
╰──────────────────────────╯ ╰──────────────────────────╯

╭───────────────────────────────────────────────────────╮
│ HP: 100/100                                           │
│ [████████████████████]                                │
╰───────────────────────────────────────────────────────╯

╭───────────────────────────────────────────────────────╮
│ STATUS: Pronto                                        │
╰───────────────────────────────────────────────────────╯
```

O bloco cheio representa visualmente os espaços com fundo colorido da barra existente; não é obrigatório alterar a implementação da barra para utilizar esse símbolo.

Sugestão de layout em um terminal com pelo menos 60 colunas e 20 linhas:

| Região | X | Y | Largura | Altura | Cor |
|---|---:|---:|---:|---:|---|
| Cabeçalho | 2 | 2 | 57 | 1 | Fundo azul, texto branco |
| Personagem | 2 | 4 | 28 | 5 | Borda verde |
| Atributos | 31 | 4 | 28 | 5 | Borda amarela |
| HP | 2 | 10 | 57 | 4 | Borda magenta |
| Status | 2 | 15 | 57 | 3 | Borda ciano |

As dimensões são sugestões; você pode definir outras, desde que não haja sobreposição. Utilize constantes para as posições e dimensões compartilhadas entre o desenho inicial e as atualizações.

### B.2 — Desenho inicial: `vDrawInterface()`

Você já possui esta função, mas atualmente ela apresenta as informações de forma sequencial. Evolua-a para desenhar o cabeçalho, as molduras e os dados estáticos nas coordenadas planejadas.

Exemplo de composição:

```c
vFillRect(2, 2, 57, 1, BGCOLOR_BLUE);
vGotoXY(25, 2);
vPrintFormatted("RPG STATUS", (const char *)BGCOLOR_BLUE,
                (const char *)TCOLOR_WHITE, BOLD_TEXT, ANSI_END);

vPrintColor(TCOLOR_GREEN);
vDrawBox(2, 4, 28, 5);
printf("%s", ANSI_RESET);

vGotoXY(4, 5);
vPrintFormatted("PERSONAGEM", (const char *)TCOLOR_CIAN,
                ANSI_END);
vGotoXY(4, 6);
printf("Nome: %s", "Guerreiro");
vGotoXY(4, 7);
printf("Nivel: %d", 5);
```

Complete os demais painéis de forma semelhante, reutilizando os dados do RPG atual. Os títulos e valores devem permanecer dentro das molduras.

**Dica de evolução:** sua `vPrintCentered()` atualmente imprime espaços antes de ativar os atributos e acrescenta uma quebra de linha. Isso é útil na apresentação sequencial, mas pode não atender a um cabeçalho posicionado. Você pode calcular a posição central e utilizar `vPrintFormatted()`, como acima, ou adaptar/criar uma função de centralização sem quebra de linha. Não é necessário eliminar a função anterior. Em chamadas variádicas, mantenha `ANSI_END` e os tipos dos argumentos compatíveis com `va_arg()`.

### B.3 — Atualização do HP: `vUpdateHP()`

Preserve a assinatura existente:

```c
void vUpdateHP(int iHP, int iMaxHP);
```

Agora a função deverá atualizar exclusivamente o interior do painel de HP. Não deve depender da posição deixada pela impressão anterior.

Para o layout sugerido, o valor numérico fica na linha 11 e a barra na linha 12. Ambas começam na coluna 4.

```c
/* Exemplo de composição após validar os valores. */
vGotoXY(4, 11);
printf("HP: %d/%d", iHP, iMaxHP);

vGotoXY(4, 12);
vPrintBar(iHP, iMaxHP, 20, BGCOLOR_GREEN);
```

O trecho é um ponto de partida: antes de escrever o valor, limpe somente a região interna reservada ao texto (por exemplo, 53 células a partir da coluna 4, com `vFillRect()` e `BGCOLOR_BLACK`). A barra atual já sobrescreve suas 20 células e os dois colchetes. Caso altere a largura, considere também a limpeza da área anteriormente ocupada.

Mantenha o HP entre zero e o máximo; para máximo inválido, não divida por zero nem apresente uma barra enganosa. Uma opção é exibir `HP: --` e limpar a barra. Restaure os atributos padrão após a atualização.

Opcionalmente, selecione a cor da barra de acordo com o percentual: verde acima de 50%, amarelo acima de 25% até 50%, vermelho até 25%.

**Dica de evolução:** `vClearLine()` apaga a linha inteira, incluindo as bordas. No novo layout, substitua essa operação pela limpeza localizada. A função continua útil em outras situações. Observe também que `vPrintBar()` ocupa `iWidth + 2` células devido aos colchetes.

### B.4 — Atualização de mensagens: `vUpdateStatus()`

Preserve a assinatura:

```c
void vUpdateStatus(const char *pszStatus);
```

A mensagem deve permanecer na linha 16, dentro do painel de status. Limpe apenas a área interna, reposicione o cursor e imprima a mensagem.

```c
vFillRect(4, 16, 53, 1, BGCOLOR_BLACK);
vGotoXY(4, 16);
printf("STATUS: %.45s", pszStatus);
```

O exemplo limita a mensagem a 45 bytes, adequado às mensagens ASCII deste exercício (o prefixo ocupa oito células). Trate um ponteiro nulo antes da impressão. Para textos UTF-8 arbitrários, seria necessário limitar por largura visual sem cortar uma sequência multibyte; isso não é exigido agora.

Teste a substituição de `"Dano recebido"` por `"Fim"`. Nenhum caractere da mensagem anterior deve permanecer, e as bordas devem continuar intactas.

**Dica:** você pode reutilizar `vPrintFormatted()` para colorir a mensagem. Não é necessário criar um mecanismo específico de cores para o RPG.

### B.5 — Integração com o `main.c`

Reaproveite a simulação existente. A diferença é que a interface será desenhada uma única vez, e as atualizações serão realizadas por coordenadas absolutas.

```c
vClearScreen();
vShowCursor(0);
vDrawInterface();

vUpdateHP(100, 100);
vUpdateStatus("Pronto");
fflush(stdout);
sleep(1);

vUpdateHP(75, 100);
vUpdateStatus("Dano recebido");
fflush(stdout);
sleep(1);

/* Continue a simulacao com os demais estados. */

vShowCursor(1);
vGotoXY(1, 19);
fflush(stdout);
```

Você pode preservar seu laço atual ou utilizar outra estrutura de controle. O importante é separar a mudança de estado do personagem de sua apresentação.

| Etapa | HP | Status |
|---|---:|---|
| 1 | 100/100 | Pronto |
| 2 | 75/100 | Dano recebido |
| 3 | 50/100 | Em perigo |
| 4 | 90/100 | Curado |
| 5 | 90/100 | Fim |

Não limpe nem redesenhe toda a tela entre os estados. Não é necessário salvar e restaurar o cursor a cada atualização se as funções já determinam suas próprias coordenadas. Garanta que o cursor volte a ficar visível ao terminar normalmente.

A simulação de carregamento do inventário do projeto anterior pode ser preservada abaixo da interface, ou integrada a um painel adicional como desafio opcional. Não deve sobrescrever os painéis existentes.

**Dica de arquitetura:** atualmente `vDrawInterface()`, `vUpdateHP()` e `vUpdateStatus()` estão na biblioteca. Elas podem permanecer ali durante este exercício. Se perceber que essas funções dependem exclusivamente do RPG, considere futuramente separá-las em um módulo da aplicação, mantendo na biblioteca apenas os mecanismos genéricos. Essa reorganização não é requisito de entrega.

## 3. Verificação e entrega

- [ ] O projeto anterior foi utilizado como base, sem reconstrução desnecessária.
- [ ] As quatro primitivas foram implementadas e testadas isoladamente.
- [ ] As molduras Unicode são exibidas corretamente no terminal escolhido.
- [ ] O cabeçalho possui fundo colorido e título centralizado.
- [ ] Os painéis de personagem e atributos aparecem lado a lado.
- [ ] O HP e a barra são atualizados dentro de sua região.
- [ ] Mensagens menores substituem mensagens maiores sem resíduos.
- [ ] As molduras e os dados estáticos permanecem intactos durante a simulação.
- [ ] A saída é atualizada durante as pausas e o cursor volta a ficar visível ao final.
- [ ] O projeto compila no ambiente Linux utilizado nos exercícios anteriores.

Entregue `main.c`, `terminal_utils.c`, `terminal_utils.h`, Makefile e eventuais módulos adicionais que tenha escolhido criar. Não é necessário entregar uma biblioteca gráfica externa.

## 4. Considerações finais

Uma interface visualmente mais elaborada não exige necessariamente mecanismos complexos. Neste exercício, linhas, molduras, preenchimentos e textos posicionados são suficientes para construir painéis reutilizáveis.

As adaptações sugeridas surgem de requisitos que não existiam nos exercícios anteriores: escrever dentro de regiões delimitadas, trabalhar com símbolos multibyte e controlar a posição de cada componente. Preserve as soluções que continuam atendendo ao seu propósito e adapte somente aquelas cujo contrato precisa evoluir.

O próximo passo será utilizar essa interface como base para entrada de dados e interatividade.
