# Exercício 02 — Interpretando um Byte

**Módulo:** 02 — Sistemas de Numeração

## O problema

Um computador armazenou a seguinte sequência de 8 bits:

`11010110`

Sabemos que essa sequência ocupa exatamente um byte, mas seu significado depende da forma como interpretamos os bits.

## Atividades

**1. Representação numérica**

- Converta a sequência binária para decimal, considerando um valor sem sinal (*unsigned*).
- Converta a mesma sequência para hexadecimal.
- Indique quantos nibbles existem nesse byte.

**2. Posição dos bits**

- Identifique o MSB e o LSB.
- Determine o valor decimal correspondente ao peso de cada posição que contém o bit `1`.

**3. Representação com e sem sinal**

Considere que o byte pode representar um inteiro de 8 bits.

- Qual é seu valor na representação *unsigned*?
- Qual é seu valor na representação *signed*, utilizando complemento de dois?
- Explique por que a mesma sequência de bits produz dois valores diferentes.

**4. Combinações possíveis**

- Quantos valores distintos podem ser representados utilizando 4 bits?
- Quantos valores distintos podem ser representados utilizando 8 bits?
- Qual é o intervalo de valores de um inteiro de 8 bits sem sinal?
- Qual é o intervalo de valores de um inteiro de 8 bits com sinal, em complemento de dois?

## Requisitos

- Demonstrar os cálculos utilizados nas conversões.
- Identificar corretamente as posições dos bits.
- Utilizar os conceitos de base numérica e valor posicional.
- Não é necessário escrever código em C.