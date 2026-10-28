# 05 — Estruturas de Dados
## Gabarito C — Calculadora com Pilha de Desfazimento (Undo)

**Objetivo:** Implementar uma calculadora com soma, subtração e desfazimento de operações, utilizando uma pilha simplesmente encadeada para armazenar os estados anteriores.

### 1. Código-fonte

```c
#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

typedef struct STRUCT_ITEM {
  int iValor;
  struct STRUCT_ITEM *pNext;
} STRUCT_ITEM, *PSTRUCT_ITEM;

int Push(PSTRUCT_ITEM *ppstTopo, int iValor);
int Pop(PSTRUCT_ITEM *ppstTopo, int *piValor);

PSTRUCT_ITEM LiberarPilha(PSTRUCT_ITEM pstTopo);

void LimparEntrada(void);

int main(void)
{
  PSTRUCT_ITEM pstTopo;
  int iOpcao;
  int iValorAtual;
  int iOperando;
  int iValorAnterior;
  int iNovoValor;
  long lResultado;

  pstTopo = NULL;
  iOpcao = 0;
  iValorAtual = 0;

  do {
    printf("\n--- CALCULADORA COM UNDO ---\n");
    printf("Valor atual: %d\n\n", iValorAtual);
    printf("[1] - Somar\n");
    printf("[2] - Subtrair\n");
    printf("[3] - Desfazer\n");
    printf("[4] - Encerrar\n");
    printf("Opcao: ");

    if (scanf("%d", &iOpcao) != 1) {
      printf("Opcao invalida.\n");
      LimparEntrada();
      iOpcao = 0;
      continue;
    }

    switch (iOpcao) {
      case 1:
      case 2:
        printf("Informe o valor: ");

        if (scanf("%d", &iOperando) != 1) {
          printf("Valor invalido.\n");
          LimparEntrada();
          break;
        }

        /*
         * Calcula primeiro, sem modificar o estado.
         * A conversao para long evita overflow na
         * operacao intermediaria em plataformas
         * onde long comporta o resultado.
         */
        if (iOpcao == 1)
          lResultado = (long)iValorAtual + (long)iOperando;
        else
          lResultado = (long)iValorAtual - (long)iOperando;

        if (lResultado > INT_MAX || lResultado < INT_MIN) {
          printf("Resultado fora dos limites de int.\n");
          break;
        }

        iNovoValor = (int)lResultado;

        /*
         * Guarda o estado anterior antes de
         * atualizar o resultado da calculadora.
         */
        if (!Push(&pstTopo, iValorAtual)) {
          printf("Operacao cancelada.\n");
          break;
        }

        iValorAtual = iNovoValor;

        printf("Novo valor: %d\n", iValorAtual);
        break;

      case 3:
        if (Pop(&pstTopo, &iValorAnterior)) {
          iValorAtual = iValorAnterior;
          printf("Operacao desfeita.\n");
          printf("Valor restaurado: %d\n", iValorAtual);
        }
        else {
          printf("Nao existem operacoes para desfazer.\n");
        }

        break;

      case 4:
        pstTopo = LiberarPilha(pstTopo);
        printf("Programa encerrado.\n");
        break;

      default:
        printf("Opcao invalida.\n");
        break;
    }

  } while (iOpcao != 4);

  return 0;
}

/* Armazena um novo valor no topo da pilha. */
int Push(PSTRUCT_ITEM *ppstTopo, int iValor)
{
  PSTRUCT_ITEM pstNovo;

  if (ppstTopo == NULL)
    return 0;

  pstNovo = (PSTRUCT_ITEM)malloc(sizeof(STRUCT_ITEM));

  if (pstNovo == NULL) {
    printf("Erro ao alocar memoria.\n");
    return 0;
  }

  pstNovo->iValor = iValor;
  pstNovo->pNext = *ppstTopo;

  *ppstTopo = pstNovo;

  return 1;
}

/* Recupera e remove o elemento do topo. */
int Pop(PSTRUCT_ITEM *ppstTopo, int *piValor)
{
  PSTRUCT_ITEM pstRemover;

  if (ppstTopo == NULL || piValor == NULL)
    return 0;

  if (*ppstTopo == NULL)
    return 0;

  pstRemover = *ppstTopo;

  *piValor = pstRemover->iValor;
  *ppstTopo = pstRemover->pNext;

  free(pstRemover);

  return 1;
}

/* Libera todos os elementos restantes. */
PSTRUCT_ITEM LiberarPilha(PSTRUCT_ITEM pstTopo)
{
  PSTRUCT_ITEM pstAtual;
  PSTRUCT_ITEM pstProximo;

  pstAtual = pstTopo;

  while (pstAtual != NULL) {
    pstProximo = pstAtual->pNext;
    free(pstAtual);
    pstAtual = pstProximo;
  }

  return NULL;
}

/* Descarta caracteres restantes da entrada. */
void LimparEntrada(void)
{
  int iChar;

  while ((iChar = getchar()) != '\n' && iChar != EOF)
    ;
}
```

### 2. Compilação

```bash
gcc -std=c89 -Wall -Wextra -pedantic calculadora.c -o calculadora
./calculadora
```

**Observação:** o cálculo intermediário utiliza `long` e verifica os limites de `int`. Em plataformas nas quais `long` e `int` possuem a mesma largura, seria necessário outro tratamento para evitar overflow. Esse detalhe não faz parte do objetivo principal do exercício.

### 3. Pontos importantes da implementação

**Push — Armazenamento do estado anterior**

Antes de executar uma soma ou subtração, o programa armazena o resultado atual da calculadora.

```c
pstNovo->iValor = iValor;
pstNovo->pNext = *ppstTopo;

*ppstTopo = pstNovo;
```

O novo elemento aponta para o topo anterior e passa a ser o novo topo da pilha.

A função retorna `1` quando a operação é concluída e `0` quando ocorre uma falha.

**Pop — Recuperação do estado anterior**

A função recupera o valor armazenado no topo, atualiza o ponteiro da pilha e libera o elemento removido.

```c
pstRemover = *ppstTopo;

*piValor = pstRemover->iValor;
*ppstTopo = pstRemover->pNext;

free(pstRemover);
```

O valor recuperado é utilizado para restaurar o resultado atual da calculadora.

Quando a pilha está vazia, a função retorna `0` e nenhum estado é alterado.

**Undo — Desfazimento**

```c
if (Pop(&pstTopo, &iValorAnterior))
  iValorAtual = iValorAnterior;
```

O desfazimento não executa uma operação matemática inversa. Ele simplesmente restaura o estado anterior.

Por isso, funciona igualmente para somas e subtrações.

### 4. Cenário de validação

A sequência abaixo representa o funcionamento esperado:

| Operação | Valor atual | Pilha (topo primeiro) |
|---|---:|---|
| Iniciar | 0 | Vazia |
| Somar 10 | 10 | 0 |
| Somar 5 | 15 | 10 → 0 |
| Somar 7 | 22 | 15 → 10 → 0 |
| Desfazer | 15 | 10 → 0 |
| Subtrair 3 | 12 | 15 → 10 → 0 |
| Somar 8 | 20 | 12 → 15 → 10 → 0 |
| Desfazer | 12 | 15 → 10 → 0 |
| Desfazer | 15 | 10 → 0 |
| Desfazer | 10 | 0 |
| Desfazer | 0 | Vazia |
| Desfazer novamente | 0 | Vazia |
| Subtrair 4 | -4 | 0 |
| Somar 9 | 5 | -4 → 0 |

### 5. Comparação com os exercícios anteriores

| Característica | A — Lista | B — Fila | C — Pilha |
|---|---|---|---|
| Inserção | Final | Final | Topo |
| Remoção | Por valor | Início | Topo |
| Comportamento | Lista genérica | FIFO | LIFO |
| Estrutura | Encadeada | Encadeada | Encadeada |
| Memória | Dinâmica | Dinâmica | Dinâmica |

### 6. Conclusão

O exercício demonstra como uma pilha encadeada pode ser utilizada para preservar o histórico de estados de uma aplicação.

As operações fundamentais são:

- `Push`: armazenar o estado atual antes de modificá-lo.
- `Pop`: recuperar e remover o último estado armazenado.
- `Undo`: restaurar o valor recuperado.
- `LiberarPilha`: liberar os elementos restantes ao encerrar.

**Conceito principal:** LIFO (*Last In, First Out*) — o último estado armazenado é o primeiro a ser recuperado.

**Fim dos exercícios do módulo 05 — Estruturas de Dados.**