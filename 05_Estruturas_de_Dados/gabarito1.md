# 05 — Estruturas de Dados
## Gabarito A — Lista Simplesmente Encadeada

**Objetivo:** Implementar inserção, remoção, busca, exibição e liberação de uma lista simplesmente encadeada de números inteiros.

### 1. Código-fonte

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct STRUCT_ITEM {
  int iValor;
  struct STRUCT_ITEM *pNext;
} STRUCT_ITEM, *PSTRUCT_ITEM;

PSTRUCT_ITEM InserirElemento(PSTRUCT_ITEM pstLista, int iValor);
PSTRUCT_ITEM RemoverElemento(PSTRUCT_ITEM pstLista, int iValor);
PSTRUCT_ITEM LiberarLista(PSTRUCT_ITEM pstLista);

int BuscarElemento(PSTRUCT_ITEM pstLista, int iValor);
void ExibirLista(PSTRUCT_ITEM pstLista);

int main(void)
{
  PSTRUCT_ITEM pstLista;
  int iOpcao;
  int iValor;
  int iLeitura;

  pstLista = NULL;
  iOpcao = 0;

  do {
    printf("\n--- LISTA ENCADEADA ---\n");
    printf("[1] - Inserir elemento\n");
    printf("[2] - Remover elemento\n");
    printf("[3] - Buscar elemento\n");
    printf("[4] - Exibir lista\n");
    printf("[5] - Encerrar\n");
    printf("Opcao: ");

    iLeitura = scanf("%d", &iOpcao);

    if (iLeitura != 1) {
      printf("Opcao invalida.\n");

      while (getchar() != '\n')
        ;

      iOpcao = 0;
      continue;
    }

    switch (iOpcao) {
      case 1:
        printf("Valor: ");

        if (scanf("%d", &iValor) != 1) {
          printf("Valor invalido.\n");
          while (getchar() != '\n')
            ;
          break;
        }

        pstLista = InserirElemento(pstLista, iValor);
        break;

      case 2:
        printf("Valor a remover: ");

        if (scanf("%d", &iValor) != 1) {
          printf("Valor invalido.\n");
          while (getchar() != '\n')
            ;
          break;
        }

        pstLista = RemoverElemento(pstLista, iValor);
        break;

      case 3:
        printf("Valor a buscar: ");

        if (scanf("%d", &iValor) != 1) {
          printf("Valor invalido.\n");
          while (getchar() != '\n')
            ;
          break;
        }

        if (BuscarElemento(pstLista, iValor))
          printf("Elemento encontrado.\n");
        else
          printf("Elemento nao encontrado.\n");

        break;

      case 4:
        ExibirLista(pstLista);
        break;

      case 5:
        pstLista = LiberarLista(pstLista);
        printf("Programa encerrado.\n");
        break;

      default:
        printf("Opcao invalida.\n");
        break;
    }

  } while (iOpcao != 5);

  return 0;
}

/* Insere um elemento no final da lista. */
PSTRUCT_ITEM InserirElemento(PSTRUCT_ITEM pstLista, int iValor)
{
  PSTRUCT_ITEM pstNovo;
  PSTRUCT_ITEM pstAtual;

  pstNovo = (PSTRUCT_ITEM)malloc(sizeof(STRUCT_ITEM));

  if (pstNovo == NULL) {
    printf("Erro ao alocar memoria.\n");
    return pstLista;
  }

  pstNovo->iValor = iValor;
  pstNovo->pNext = NULL;

  if (pstLista == NULL) {
    printf("Elemento %d inserido.\n", iValor);
    return pstNovo;
  }

  pstAtual = pstLista;

  while (pstAtual->pNext != NULL)
    pstAtual = pstAtual->pNext;

  pstAtual->pNext = pstNovo;

  printf("Elemento %d inserido.\n", iValor);

  return pstLista;
}

/* Remove a primeira ocorrencia do valor. */
PSTRUCT_ITEM RemoverElemento(PSTRUCT_ITEM pstLista, int iValor)
{
  PSTRUCT_ITEM pstAtual;
  PSTRUCT_ITEM pstAnterior;

  if (pstLista == NULL) {
    printf("Lista vazia.\n");
    return NULL;
  }

  pstAtual = pstLista;
  pstAnterior = NULL;

  while (pstAtual != NULL) {
    if (pstAtual->iValor == iValor)
      break;

    pstAnterior = pstAtual;
    pstAtual = pstAtual->pNext;
  }

  if (pstAtual == NULL) {
    printf("Elemento nao encontrado.\n");
    return pstLista;
  }

  if (pstAnterior == NULL)
    pstLista = pstAtual->pNext;
  else
    pstAnterior->pNext = pstAtual->pNext;

  free(pstAtual);

  printf("Elemento %d removido.\n", iValor);

  return pstLista;
}

/* Busca um valor sem modificar a lista. */
int BuscarElemento(PSTRUCT_ITEM pstLista, int iValor)
{
  PSTRUCT_ITEM pstAtual;

  pstAtual = pstLista;

  while (pstAtual != NULL) {
    if (pstAtual->iValor == iValor)
      return 1;

    pstAtual = pstAtual->pNext;
  }

  return 0;
}

/* Exibe os elementos na ordem da lista. */
void ExibirLista(PSTRUCT_ITEM pstLista)
{
  PSTRUCT_ITEM pstAtual;

  if (pstLista == NULL) {
    printf("Lista vazia.\n");
    return;
  }

  pstAtual = pstLista;

  printf("Lista: ");

  while (pstAtual != NULL) {
    printf("%d -> ", pstAtual->iValor);
    pstAtual = pstAtual->pNext;
  }

  printf("NULL\n");
}

/* Libera todos os elementos da lista. */
PSTRUCT_ITEM LiberarLista(PSTRUCT_ITEM pstLista)
{
  PSTRUCT_ITEM pstAtual;
  PSTRUCT_ITEM pstProximo;

  pstAtual = pstLista;

  while (pstAtual != NULL) {
    pstProximo = pstAtual->pNext;
    free(pstAtual);
    pstAtual = pstProximo;
  }

  return NULL;
}
```

### 2. Compilação

```bash
gcc -std=c89 -Wall -Wextra -pedantic lista.c -o lista
./lista
```

### 3. Pontos importantes da implementação

**Inserção**

A função percorre a lista até encontrar o último elemento, cujo `pNext` é `NULL`. O novo elemento é conectado ao final.

Quando a lista está vazia, o novo elemento passa a ser o primeiro.

**Remoção**

A função utiliza dois ponteiros:

- `pstAtual`: elemento sendo examinado.
- `pstAnterior`: elemento imediatamente anterior.

Após localizar o valor, existem duas situações fundamentais:

```c
if (pstAnterior == NULL)
  pstLista = pstAtual->pNext;
else
  pstAnterior->pNext = pstAtual->pNext;

free(pstAtual);
```

Quando `pstAnterior` é `NULL`, estamos removendo o primeiro elemento. Nos demais casos, o elemento anterior passa a apontar para o sucessor do elemento removido.

Isso também resolve a remoção do último elemento, pois seu sucessor será `NULL`.

**Busca**

A função percorre a lista até encontrar o valor ou atingir `NULL`, sem modificar os vínculos entre os elementos.

**Liberação**

Antes de liberar cada elemento, a função guarda o endereço do próximo. Isso evita acessar um nó depois de executar `free()`.

### 4. Validação

A sequência principal de operações deverá produzir:

```text
Lista vazia.

Inserir 10
Inserir 20
Inserir 30
Inserir 40

Lista: 10 -> 20 -> 30 -> 40 -> NULL

Buscar 30
Elemento encontrado.

Buscar 99
Elemento nao encontrado.

Remover 10
Lista: 20 -> 30 -> 40 -> NULL

Remover 30
Lista: 20 -> 40 -> NULL

Remover 40
Lista: 20 -> NULL

Remover 20
Lista vazia.

Inserir 50
Inserir 50
Lista: 50 -> 50 -> NULL

Remover 50
Lista: 50 -> NULL
```

### 5. Conclusão

O exercício demonstra que uma lista simplesmente encadeada pode ser manipulada utilizando apenas referências entre elementos, sem índices ou posições numéricas.

As operações fundamentais são:

- Inserir um novo nó.
- Percorrer os nós existentes.
- Localizar um valor.
- Remover um nó preservando os vínculos.
- Liberar a memória alocada.

**Conceito principal:** a integridade de uma lista encadeada depende da atualização correta dos ponteiros, especialmente durante as operações de remoção.