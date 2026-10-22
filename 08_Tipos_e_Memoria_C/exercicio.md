# Exercício 08 — Valores, Ponteiros e Memória

**Módulo:** 08 — Tipos e Memória em C  
**Linguagem:** ANSI C89

## Objetivo

Compreender como variáveis, ponteiros e arrays representam e acessam dados na memória.

## 1. Análise do programa

Considere o programa:

```c
#include <stdio.h>

int main(void)
{
    int iA = 10;
    int iB = 20;
    int *pA = &iA;

    int aiValores[3] = { 10, 20, 30 };

    *pA = 15;

    printf("%d\n", iA);
    printf("%d\n", *pA);
    printf("%d\n", aiValores[1]);

    return 0;
}
```

Sem executar o programa, responda:

1. Qual será a saída apresentada?
2. O que a expressão `&iA` representa?
3. Qual é a diferença entre `pA` e `*pA`?
4. Por que a atribuição `*pA = 15` modifica o valor de `iA`?
5. O valor de `iB` foi modificado? Justifique.

## 2. Arrays e endereçamento

Considerando `aiValores`:

1. Quantos elementos existem no array?
2. Qual é o valor de `aiValores[1]`?
3. Qual é a relação entre `aiValores[1]` e `*(aiValores + 1)`?
4. Se `sizeof(int)` retornar 4, qual será a distância, em bytes, entre os endereços de `aiValores[0]` e `aiValores[2]`?

## 3. Representação da memória

Desenhe um esquema contendo:

- A variável `iA` com seu valor final.
- O ponteiro `pA` apontando para `iA`.
- Os três elementos de `aiValores`, em posições consecutivas.

Utilize endereços fictícios, caso necessário.

## Requisitos

- Explicar as respostas utilizando os conceitos de valor, endereço e indireção.
- Diferenciar o conteúdo de um ponteiro do conteúdo da região apontada.
- Identificar a relação entre índices e aritmética de ponteiros.
- Não é necessário modificar o programa ou utilizar alocação dinâmica.