# 10.22 — Exercício Integrador: Analisador de Números

**Módulo:** 10 — Estruturas de Controle  
**Linguagem:** C (ANSI C89)

## Objetivo

Desenvolver um programa que permita analisar números inteiros por meio de um menu interativo, utilizando estruturas de seleção, repetição e controle do fluxo de execução.

## 1. Menu principal

O programa deverá apresentar o seguinte menu:

```text
===== ANALISADOR DE NUMEROS =====

[1] Verificar um numero
[2] Exibir uma sequencia
[3] Somar numeros
[4] Sair

Escolha:
```

O menu deverá ser implementado utilizando `do while`, permanecendo disponível até que o usuário escolha a opção 4.

A seleção das opções deverá utilizar `switch / case`.

## 2. Funcionalidades

### Opção 1 — Verificar um número

Solicitar um número inteiro e informar:

- Se é positivo, negativo ou zero.
- Se for diferente de zero, se é par ou ímpar.

**Exemplo:**

```text
Digite um numero: -7

Numero negativo.
Numero impar.
```

### Opção 2 — Exibir uma sequência

Solicitar um limite inteiro positivo e exibir todos os números de 1 até esse limite, exceto os múltiplos de 3.

**Exemplo:**

```text
Digite o limite: 10

1 2 4 5 7 8 10
```

Se o limite informado for menor que 1, apresentar uma mensagem de valor inválido.

### Opção 3 — Somar números

Solicitar números inteiros sucessivamente, acumulando seus valores.

A entrada do número `0` deverá encerrar a operação e apresentar a soma total.

**Exemplo:**

```text
Digite um numero (0 para encerrar): 10
Digite um numero (0 para encerrar): 5
Digite um numero (0 para encerrar): -3
Digite um numero (0 para encerrar): 0

Soma total: 12
```

### Opção 4 — Sair

Encerrar o programa, apresentando uma mensagem de finalização.

## 3. Requisitos obrigatórios

1. Utilizar `do while` para controlar o menu principal.
2. Utilizar `switch / case` para selecionar as funcionalidades.
3. Utilizar estruturas condicionais para as verificações necessárias.
4. Utilizar estruturas de repetição para processar sequências de números.
5. Utilizar `continue` para ignorar os múltiplos de 3 na opção 2.
6. Utilizar `break` para interromper a leitura na opção 3 quando o número informado for zero.
7. Tratar opções inválidas do menu.
8. Organizar os comandos em blocos `{ }`, mantendo a indentação consistente.

## 4. Restrições

- Não utilizar `goto`.
- Não utilizar vetores, listas ou alocação dinâmica.
- Não é necessário criar funções adicionais.
- O programa poderá ser desenvolvido integralmente dentro de `main`.
- As variáveis deverão ser declaradas respeitando o padrão ANSI C89.

## 5. Critérios de avaliação

O programa deverá demonstrar:

- Uso correto das estruturas de seleção e repetição.
- Escolha adequada das estruturas para cada problema.
- Controle correto das condições de entrada e saída dos laços.
- Utilização de `break` e `continue` conforme suas finalidades.
- Organização e legibilidade do código.

**Importante:** exceto pelas estruturas explicitamente exigidas, o aluno deverá escolher como organizar o fluxo de execução, justificando suas escolhas quando solicitado.