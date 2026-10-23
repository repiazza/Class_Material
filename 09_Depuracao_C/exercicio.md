# Exercício 09 — Investigando uma Falha de Segmentação

**Módulo:** 09 — Depuração em C  
**Linguagem:** ANSI C89  
**Ferramenta:** GDB

## Objetivo

Utilizar o GDB para investigar uma falha de execução, identificar sua origem por meio da pilha de chamadas e corrigir o problema.

## 1. Programa para investigação

Considere o seguinte programa:

```c
#include <stdio.h>

typedef struct STRUCT_ITEM {
    int iValor;
} STRUCT_ITEM, *PSTRUCT_ITEM;

void vExibirItem(PSTRUCT_ITEM pItem)
{
    printf("Valor: %d\n", pItem->iValor);
}

void vProcessar(PSTRUCT_ITEM pItem)
{
    vExibirItem(pItem);
}

int main(void)
{
    PSTRUCT_ITEM pItem = NULL;

    vProcessar(pItem);

    return 0;
}
```

O programa compila, mas apresenta uma falha durante a execução.

## 2. Atividades

**1. Compilação**

Compile o programa utilizando as opções `-g` e `-O0`, preservando as informações necessárias para a depuração.

**2. Investigação com GDB**

Utilize o depurador para:

- Executar o programa e observar a falha.
- Definir breakpoints nas funções envolvidas.
- Acompanhar a execução utilizando `next`, `step` e `continue`.
- Executar `backtrace` após a falha.
- Utilizar `frame` para navegar pela pilha de chamadas.
- Inspecionar os valores dos argumentos e variáveis utilizando `print`.

**3. Diagnóstico**

Responda:

- Em qual função e instrução ocorre a falha?
- Qual é o valor do ponteiro envolvido?
- Qual é a sequência de chamadas que levou ao problema?
- Por que a instrução provoca uma falha de segmentação?

**4. Correção**

Corrija o programa para que a execução ocorra sem falhas.

Execute novamente utilizando o GDB para verificar o comportamento após a correção.

## 3. Requisitos

- Utilizar efetivamente o GDB durante a investigação.
- Identificar a origem da falha antes de modificar o código.
- Demonstrar a utilização de `backtrace`, `frame` e `print`.
- Preservar a organização das três funções.
- Não utilizar ferramentas adicionais como requisito obrigatório.

## 4. Entrega

Apresentar:

1. O diagnóstico da falha e sua causa.
2. A sequência de comandos utilizada na investigação.
3. O código corrigido.
4. O resultado da execução após a correção.

**Importante:** identificar o erro apenas pela leitura do código não é suficiente. O objetivo é demonstrar como o depurador permite investigar o fluxo de execução e os valores envolvidos na falha.