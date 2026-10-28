# 05 — Estruturas de Dados
## Exercício A — Lista Simplesmente Encadeada

**Tema:** Alocação dinâmica, ponteiros e manipulação de listas encadeadas.

### 1. Objetivo

Desenvolver em linguagem C um programa que gerencie uma lista simplesmente encadeada de números inteiros, permitindo inserir, consultar e remover elementos.

A implementação deverá utilizar alocação dinâmica de memória e manipulação de ponteiros.

### 2. Estrutura de dados

Cada elemento da lista deverá conter:

- Um número inteiro.
- Um ponteiro para o próximo elemento.

A lista deverá ser iniciada vazia, utilizando `NULL` como referência inicial.

### 3. Menu de operações

O programa deverá apresentar o seguinte menu:

```text
[1] - Inserir elemento
[2] - Remover elemento
[3] - Buscar elemento
[4] - Exibir lista
[5] - Encerrar
```

**Opção 1 — Inserir elemento**

- Solicitar um número inteiro ao usuário.
- Alocar dinamicamente um novo elemento.
- Inserir o elemento no final da lista.
- Exibir uma mensagem confirmando a inserção.
- Permitir valores repetidos.

**Opção 2 — Remover elemento**

- Solicitar o valor do elemento a ser removido.
- Localizar a primeira ocorrência do valor informado.
- Remover o elemento, ajustando os ponteiros necessários.
- Liberar a memória do elemento removido.
- Informar quando o valor não for encontrado.

A mesma operação deverá tratar corretamente:

- Remoção do primeiro elemento.
- Remoção de um elemento intermediário.
- Remoção do último elemento.
- Remoção do único elemento existente.
- Tentativa de remoção em lista vazia.

**Opção 3 — Buscar elemento**

- Solicitar um número inteiro.
- Percorrer a lista procurando o valor.
- Informar se o elemento foi encontrado.
- Não modificar a lista durante a busca.

**Opção 4 — Exibir lista**

- Percorrer a lista desde o primeiro elemento.
- Exibir os valores na ordem de inserção.
- Informar quando a lista estiver vazia.

Exemplo:

```text
Lista: 10 -> 20 -> 30 -> NULL
```

**Opção 5 — Encerrar**

- Liberar todos os elementos ainda existentes.
- Encerrar o programa.

### 4. Requisitos obrigatórios

1. Utilizar uma lista simplesmente encadeada.
2. Utilizar `struct` para representar os elementos.
3. Utilizar `malloc()` e `free()` para gerenciar a memória.
4. Implementar funções separadas para inserção, remoção, busca, exibição e liberação da lista.
5. Verificar o resultado das alocações de memória.
6. Tratar corretamente ponteiros `NULL`.
7. Preservar os demais elementos e sua ordem após uma remoção.
8. Não utilizar vetores para armazenar os elementos da lista.
9. Não utilizar contadores ou índices para controlar as posições dos elementos.

### 5. Cenário de validação

Execute as operações abaixo, nesta ordem:

| Operação | Resultado esperado |
|---|---|
| Exibir lista vazia | Mensagem de lista vazia |
| Inserir 10 | 10 |
| Inserir 20 | 10 → 20 |
| Inserir 30 | 10 → 20 → 30 |
| Inserir 40 | 10 → 20 → 30 → 40 |
| Buscar 30 | Elemento encontrado |
| Buscar 99 | Elemento não encontrado |
| Remover 10 | 20 → 30 → 40 |
| Remover 30 | 20 → 40 |
| Remover 40 | 20 |
| Remover 20 | Lista vazia |
| Remover 99 | Mensagem de lista vazia |
| Inserir 50 | 50 |
| Inserir 50 | 50 → 50 |
| Remover 50 | 50 |
| Encerrar | Memória liberada |

### 6. Entrega

O programa deverá ser entregue em código-fonte C, compilável e executável, contendo todas as operações solicitadas.

**Resultado esperado:** uma lista dinâmica que permita adicionar, buscar e remover elementos sem perder a integridade dos vínculos entre os nós, inclusive nos casos de início, meio, fim e lista vazia.