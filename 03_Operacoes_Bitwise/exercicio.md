# Exercício 03 — Operações Bitwise

**Módulo:** 03 — Operações Bitwise

## O problema

Considere dois valores inteiros positivos, representados em 8 bits:

```text
A = 10  →  00001010
B = 12  →  00001100
```

Utilizando esses valores, realize as operações abaixo.

## 1. Operações bit a bit

Calcule o resultado das seguintes expressões:

- `A & B` — AND
- `A | B` — OR
- `A ^ B` — XOR
- `~A` — NOT

Apresente os resultados em binário e decimal.

Para a operação NOT, considere somente os 8 bits apresentados e interprete o resultado como um valor sem sinal.

## 2. Deslocamento de bits

Calcule:

- `A << 1`
- `B >> 2`

Apresente os resultados em binário e decimal.

Explique brevemente o que acontece com os bits em cada deslocamento.

## 3. Máscaras de bits

Considere a variável `A` e as posições dos bits numeradas de 0 a 7, da direita para a esquerda.

Utilizando operações bitwise:

- Verifique se o bit da posição 3 está ligado.
- Ligue o bit da posição 2, preservando os demais.
- Desligue o bit da posição 1, preservando os demais.
- Inverta somente o bit da posição 3.

Considere cada operação independente, sempre partindo do valor original de `A`.

## Requisitos

- Demonstrar as operações utilizando representações binárias de 8 bits.
- Apresentar os resultados em binário e decimal.
- Utilizar os operadores bitwise adequados.
- Não utilizar operadores lógicos (`&&`, `||`) no lugar dos operadores bitwise.
- Não é necessário desenvolver um programa em C.