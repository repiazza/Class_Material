# 05 — Estruturas de Dados
## Exercício B — Fila de Atendimento Drive-thru

**Tema:** Filas encadeadas, alocação dinâmica e comportamento FIFO.

### 1. Objetivo

Desenvolver em linguagem C um sistema de atendimento de veículos em um drive-thru, utilizando uma fila simplesmente encadeada.

O programa deverá controlar a entrada e o atendimento dos veículos, respeitando a ordem de chegada.

### 2. Cenário

Um estabelecimento possui uma única fila de atendimento.

Cada veículo que chega recebe automaticamente um número de identificação sequencial, começando em **1**.

Os veículos devem ser atendidos na mesma ordem em que chegaram.

**Exemplo:**

```text
Entrada: Veículo 1
Entrada: Veículo 2
Entrada: Veículo 3

Fila: 1 -> 2 -> 3 -> NULL

Atender próximo veículo: 1

Fila: 2 -> 3 -> NULL
```

### 3. Estrutura de dados

Cada elemento da fila deverá armazenar:

- O número de identificação do veículo.
- Um ponteiro para o próximo veículo.

A fila deverá iniciar vazia.

O número de identificação deverá ser gerado automaticamente, sem reutilizar números de veículos já atendidos.

### 4. Menu de operações

O programa deverá apresentar o seguinte menu:

```text
[1] - Entrada de veículo
[2] - Atender próximo veículo
[3] - Exibir fila
[4] - Encerrar
```

**Opção 1 — Entrada de veículo**

- Gerar o próximo número de identificação.
- Alocar dinamicamente um novo elemento.
- Inserir o veículo no final da fila.
- Exibir o número do veículo que entrou.
- Atualizar a numeração somente quando a inserção for bem-sucedida.

**Opção 2 — Atender próximo veículo**

- Identificar o primeiro veículo da fila.
- Exibir o número do veículo atendido.
- Remover esse elemento da fila.
- Liberar sua memória.
- Informar quando não houver veículos aguardando.

**Opção 3 — Exibir fila**

- Percorrer a fila desde o primeiro veículo.
- Exibir os números na ordem de atendimento.
- Informar quando a fila estiver vazia.

**Opção 4 — Encerrar**

- Liberar todos os elementos ainda presentes na fila.
- Encerrar o programa.

### 5. Requisitos obrigatórios

1. Implementar a fila utilizando uma lista simplesmente encadeada.
2. Utilizar `struct`, `malloc()` e `free()`.
3. Implementar funções separadas para inserir, atender, exibir e liberar a fila.
4. Inserir novos veículos exclusivamente no final da fila.
5. Atender veículos exclusivamente no início da fila.
6. Tratar corretamente fila vazia e fila com apenas um veículo.
7. Verificar falhas de alocação de memória.
8. Não utilizar vetores para armazenar os veículos.
9. Não utilizar índices ou posições numéricas para controlar a fila.
10. Utilizar uma variável inteira apenas para gerar os números sequenciais de identificação dos veículos.

### 6. Cenário de validação

Execute as seguintes operações, nesta ordem:

| Operação | Resultado esperado |
|---|---|
| Exibir fila | Fila vazia |
| Atender veículo | Nenhum veículo aguardando |
| Entrada de veículo | Veículo 1 |
| Entrada de veículo | Veículo 2 |
| Entrada de veículo | Veículo 3 |
| Exibir fila | 1 → 2 → 3 |
| Atender veículo | Veículo 1 |
| Exibir fila | 2 → 3 |
| Entrada de veículo | Veículo 4 |
| Exibir fila | 2 → 3 → 4 |
| Atender veículo | Veículo 2 |
| Atender veículo | Veículo 3 |
| Atender veículo | Veículo 4 |
| Exibir fila | Fila vazia |
| Entrada de veículo | Veículo 5 |
| Exibir fila | 5 |
| Encerrar | Memória liberada |

### 7. Entrega

O programa deverá ser entregue em código-fonte C, compilável e executável, contendo todas as operações solicitadas.

**Resultado esperado:** uma fila dinâmica que preserve a ordem de chegada dos veículos, permita novas entradas e atendimentos sucessivos e mantenha corretamente os vínculos entre os elementos.

**Conceito principal:** FIFO (*First In, First Out*) — o primeiro veículo que entra na fila deve ser o primeiro a ser atendido.