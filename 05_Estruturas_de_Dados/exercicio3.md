# 05 — Estruturas de Dados
## Exercício C — Calculadora com Pilha de Desfazimento (Undo)

**Tema:** Pilhas encadeadas, alocação dinâmica, operações Push e Pop e comportamento LIFO.

### 1. Objetivo

Desenvolver em linguagem C uma calculadora simples que permita realizar operações de soma e subtração, mantendo um histórico dos resultados anteriores por meio de uma pilha simplesmente encadeada.

O programa deverá permitir desfazer a última operação realizada, restaurando o valor anterior da calculadora.

### 2. Cenário

A calculadora deverá iniciar com o valor **0**.

O usuário poderá somar ou subtrair um número inteiro do valor atual.

Antes de cada operação aritmética, o valor atual deverá ser armazenado na pilha, permitindo sua recuperação posteriormente.

A operação **Desfazer (Undo)** deverá restaurar o último valor armazenado e removê-lo da pilha.

**Exemplo:**

```text
Valor inicial: 0

Somar 10
Valor atual: 10

Somar 5
Valor atual: 15

Subtrair 3
Valor atual: 12

Desfazer
Valor atual: 15

Desfazer
Valor atual: 10

Somar 2
Valor atual: 12
```

### 3. Estrutura de dados

Cada elemento da pilha deverá armazenar:

- Um número inteiro representando um valor anterior da calculadora.
- Um ponteiro para o próximo elemento da pilha.

A pilha deverá iniciar vazia, com seu topo apontando para `NULL`.

As operações deverão respeitar o comportamento **LIFO (Last In, First Out)**.

### 4. Menu de operações

O programa deverá apresentar o seguinte menu:

```text
Valor atual: 0

[1] - Somar
[2] - Subtrair
[3] - Desfazer
[4] - Encerrar
```

**Opção 1 — Somar**

- Solicitar um número inteiro ao usuário.
- Armazenar o valor atual da calculadora no topo da pilha.
- Somar o número informado ao valor atual.
- Exibir o novo resultado.
- Não realizar a soma caso o armazenamento do histórico falhe.

**Opção 2 — Subtrair**

- Solicitar um número inteiro ao usuário.
- Armazenar o valor atual da calculadora no topo da pilha.
- Subtrair o número informado do valor atual.
- Exibir o novo resultado.
- Não realizar a subtração caso o armazenamento do histórico falhe.

**Opção 3 — Desfazer**

- Verificar se existe algum valor armazenado na pilha.
- Recuperar o valor existente no topo.
- Remover o elemento do topo e liberar sua memória.
- Restaurar o valor recuperado como resultado atual da calculadora.
- Informar quando não houver operações disponíveis para desfazer.

**Opção 4 — Encerrar**

- Liberar todos os elementos restantes da pilha.
- Encerrar o programa.

### 5. Requisitos obrigatórios

1. Implementar o histórico utilizando uma pilha simplesmente encadeada.
2. Utilizar `struct`, `malloc()` e `free()`.
3. Implementar funções separadas para as operações `Push`, `Pop` e liberação da pilha.
4. Inserir e remover elementos exclusivamente pelo topo da pilha.
5. Armazenar o valor anterior antes de cada soma ou subtração.
6. Permitir múltiplas operações consecutivas de desfazimento.
7. Tratar corretamente a tentativa de desfazer com a pilha vazia.
8. Não modificar o resultado atual caso uma operação de `Push` falhe.
9. Não utilizar vetores para armazenar o histórico.
10. Não utilizar contadores ou índices para controlar as posições da pilha.
11. Não implementar a operação Redo.

### 6. Cenário de validação

Execute as operações abaixo, nesta ordem:

| Operação | Valor atual esperado |
|---|---:|
| Iniciar programa | 0 |
| Somar 10 | 10 |
| Somar 5 | 15 |
| Somar 7 | 22 |
| Desfazer | 15 |
| Subtrair 3 | 12 |
| Somar 8 | 20 |
| Desfazer | 12 |
| Desfazer | 15 |
| Desfazer | 10 |
| Desfazer | 0 |
| Desfazer novamente | 0 |
| Subtrair 4 | -4 |
| Somar 9 | 5 |
| Encerrar | Memória liberada |

Ao tentar desfazer uma operação quando a pilha estiver vazia, o programa deverá informar que não existe histórico disponível, preservando o valor atual.

### 7. Entrega

O programa deverá ser entregue em código-fonte C, compilável e executável, contendo todas as operações solicitadas.

**Resultado esperado:** uma calculadora que utilize uma pilha dinâmica para preservar e restaurar resultados anteriores, permitindo desfazer operações sucessivas na ordem inversa em que foram realizadas.

**Conceito principal:** LIFO (*Last In, First Out*) — o último estado armazenado será o primeiro a ser recuperado.