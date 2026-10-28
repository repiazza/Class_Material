# 05 — Estruturas de Dados
## Gabarito B — Fila de Atendimento Drive-thru

**Objetivo:** Implementar uma fila simplesmente encadeada para controlar a entrada e o atendimento de veículos, respeitando a ordem FIFO.

### 1. Código-fonte

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct STRUCT_VEICULO {
  int iNumero;
  struct STRUCT_VEICULO *pNext;
} STRUCT_VEICULO, *PSTRUCT_VEICULO;

PSTRUCT_VEICULO InserirVeiculo(PSTRUCT_VEICULO pstFila,
                               int iNumero,
                               int *piSucesso);

PSTRUCT_VEICULO AtenderVeiculo(PSTRUCT_VEICULO pstFila);
PSTRUCT_VEICULO LiberarFila(PSTRUCT_VEICULO pstFila);

void ExibirFila(PSTRUCT_VEICULO pstFila);
void LimparEntrada(void);

int main(void)
{
  PSTRUCT_VEICULO pstFila;
  int iOpcao;
  int iProximoNumero;
  int iSucesso;

  pstFila = NULL;
  iOpcao = 0;
  iProximoNumero = 1;

  do {
    printf("\n--- DRIVE-THRU ---\n");
    printf("[1] - Entrada de veiculo\n");
    printf("[2] - Atender proximo veiculo\n");
    printf("[3] - Exibir fila\n");
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
        iSucesso = 0;

        pstFila = InserirVeiculo(pstFila,
                                iProximoNumero,
                                &iSucesso);

        if (iSucesso)
          iProximoNumero++;

        break;

      case 2:
        pstFila = AtenderVeiculo(pstFila);
        break;

      case 3:
        ExibirFila(pstFila);
        break;

      case 4:
        pstFila = LiberarFila(pstFila);
        printf("Programa encerrado.\n");
        break;

      default:
        printf("Opcao invalida.\n");
        break;
    }

  } while (iOpcao != 4);

  return 0;
}

/* Insere um veiculo no final da fila. */
PSTRUCT_VEICULO InserirVeiculo(PSTRUCT_VEICULO pstFila,
                               int iNumero,
                               int *piSucesso)
{
  PSTRUCT_VEICULO pstNovo;
  PSTRUCT_VEICULO pstAtual;

  *piSucesso = 0;

  pstNovo = (PSTRUCT_VEICULO)malloc(sizeof(STRUCT_VEICULO));

  if (pstNovo == NULL) {
    printf("Erro ao alocar memoria.\n");
    return pstFila;
  }

  pstNovo->iNumero = iNumero;
  pstNovo->pNext = NULL;

  if (pstFila == NULL) {
    pstFila = pstNovo;
  }
  else {
    pstAtual = pstFila;

    while (pstAtual->pNext != NULL)
      pstAtual = pstAtual->pNext;

    pstAtual->pNext = pstNovo;
  }

  *piSucesso = 1;

  printf("Veiculo %d entrou na fila.\n", iNumero);

  return pstFila;
}

/* Remove o primeiro veiculo da fila. */
PSTRUCT_VEICULO AtenderVeiculo(PSTRUCT_VEICULO pstFila)
{
  PSTRUCT_VEICULO pstProximo;

  if (pstFila == NULL) {
    printf("Nenhum veiculo aguardando.\n");
    return NULL;
  }

  printf("Atendendo veiculo %d.\n", pstFila->iNumero);

  pstProximo = pstFila->pNext;

  free(pstFila);

  return pstProximo;
}

/* Exibe os veiculos na ordem de atendimento. */
void ExibirFila(PSTRUCT_VEICULO pstFila)
{
  PSTRUCT_VEICULO pstAtual;

  if (pstFila == NULL) {
    printf("Fila vazia.\n");
    return;
  }

  pstAtual = pstFila;

  printf("Fila: ");

  while (pstAtual != NULL) {
    printf("%d -> ", pstAtual->iNumero);
    pstAtual = pstAtual->pNext;
  }

  printf("NULL\n");
}

/* Libera todos os veiculos restantes. */
PSTRUCT_VEICULO LiberarFila(PSTRUCT_VEICULO pstFila)
{
  PSTRUCT_VEICULO pstAtual;
  PSTRUCT_VEICULO pstProximo;

  pstAtual = pstFila;

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
gcc -std=c89 -Wall -Wextra -pedantic drive_thru.c -o drive_thru
./drive_thru
```

### 3. Pontos importantes da implementação

**Inserção — Entrada de veículo**

A função `InserirVeiculo()` aloca um novo elemento e o conecta ao final da fila.

Se a fila estiver vazia, o novo veículo passa a ser o primeiro.

Caso contrário, a função percorre os elementos até encontrar aquele cujo `pNext` seja `NULL`.

O parâmetro `piSucesso` permite informar se a inserção ocorreu corretamente.

```c
iSucesso = 0;

pstFila = InserirVeiculo(pstFila,
                        iProximoNumero,
                        &iSucesso);

if (iSucesso)
  iProximoNumero++;
```

Dessa maneira, uma falha de alocação não provoca a perda de um número de identificação.

**Atendimento — Remoção do primeiro elemento**

O atendimento sempre remove o elemento inicial da fila.

```c
pstProximo = pstFila->pNext;

free(pstFila);

return pstProximo;
```

O ponteiro para o próximo veículo é preservado antes da liberação da memória.

Quando o único veículo é atendido, `pstProximo` será `NULL`, indicando que a fila ficou vazia.

**Exibição**

A função percorre a estrutura desde o primeiro elemento até encontrar `NULL`, sem modificar a fila.

**Liberação**

Ao encerrar o programa, todos os elementos restantes são liberados individualmente.

### 4. Cenário de validação

A execução das operações principais deverá produzir a seguinte sequência:

```text
Exibir fila
Fila vazia.

Atender proximo veiculo
Nenhum veiculo aguardando.

Entrada de veiculo
Veiculo 1 entrou na fila.

Entrada de veiculo
Veiculo 2 entrou na fila.

Entrada de veiculo
Veiculo 3 entrou na fila.

Exibir fila
Fila: 1 -> 2 -> 3 -> NULL

Atender proximo veiculo
Atendendo veiculo 1.

Exibir fila
Fila: 2 -> 3 -> NULL

Entrada de veiculo
Veiculo 4 entrou na fila.

Exibir fila
Fila: 2 -> 3 -> 4 -> NULL

Atender proximo veiculo
Atendendo veiculo 2.

Atender proximo veiculo
Atendendo veiculo 3.

Atender proximo veiculo
Atendendo veiculo 4.

Exibir fila
Fila vazia.

Entrada de veiculo
Veiculo 5 entrou na fila.

Exibir fila
Fila: 5 -> NULL

Encerrar
Programa encerrado.
```

### 5. Comparação com o Exercício A

| Característica | Exercício A | Exercício B |
|---|---|---|
| Estrutura | Lista encadeada | Fila encadeada |
| Inserção | Final da lista | Final da fila |
| Remoção | Por valor | Sempre no início |
| Busca | Disponível | Não necessária |
| Ordem de saída | Definida pelo usuário | FIFO |
| Controle de memória | malloc/free | malloc/free |

A principal diferença está nas regras de utilização da estrutura.

No Exercício A, qualquer elemento pode ser removido mediante uma busca.

No Exercício B, a remoção é restrita ao primeiro elemento, garantindo que a ordem de chegada seja preservada.

### 6. Conclusão

O exercício demonstra como uma lista simplesmente encadeada pode implementar uma fila dinâmica.

As operações fundamentais são:

- Inserir um veículo no final.
- Atender o primeiro veículo.
- Preservar a ordem dos veículos restantes.
- Tratar fila vazia e fila com um único elemento.
- Liberar corretamente a memória.

**Conceito principal:** FIFO (*First In, First Out*) — o primeiro elemento inserido é o primeiro a ser removido.