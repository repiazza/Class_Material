# Gabarito 02 — Interpretando um Byte

**Módulo:** 02 — Sistemas de Numeração  
**Exercício:** Interpretando um Byte

## 1. Representação numérica

**Valor original:** `11010110`

**Decimal (unsigned):**

128 + 64 + 16 + 4 + 2 = **214**

**Hexadecimal:**

Separando o byte em dois nibbles:

`1101 0110`

- `1101` = 13 = D
- `0110` = 6

**Resultado:** `0xD6`

**Quantidade de nibbles:** 2

**Raciocínio esperado:**

O aluno deve compreender que cada posição binária possui um peso correspondente a uma potência de 2.

Na conversão hexadecimal, cada grupo de quatro bits corresponde a um dígito hexadecimal.

## 2. Posição dos bits

| Posição | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
|---|---|---|---|---|---|---|---|---|
| Bit | 1 | 1 | 0 | 1 | 0 | 1 | 1 | 0 |
| Peso | 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |

- **MSB:** bit 7, valor 1.
- **LSB:** bit 0, valor 0.
- **Pesos das posições com bit 1:** 128, 64, 16, 4 e 2.

**Raciocínio esperado:**

O aluno deve identificar que MSB e LSB representam as posições mais e menos significativas, respectivamente, independentemente do valor armazenado nessas posições.

## 3. Representação com e sem sinal

**Unsigned (8 bits):**

`11010110` = **214**

**Signed (8 bits, complemento de dois):**

Como o bit mais significativo é 1, o valor é negativo.

Invertendo os bits:

`00101001`

Somando 1:

`00101010` = 42

**Resultado:** −42

**Raciocínio esperado:**

O aluno deve compreender que a sequência de bits permanece a mesma, mas sua interpretação depende da representação numérica utilizada.

Em complemento de dois, o bit mais significativo participa da representação de valores negativos.

Também é válido calcular diretamente:

214 − 256 = **−42**

## 4. Combinações possíveis

O número de combinações possíveis com `n` bits é:

\[
2^n
\]

| Quantidade | Combinações |
|---|---|
| 4 bits | 16 |
| 8 bits | 256 |

**Intervalos de 8 bits:**

| Representação | Intervalo |
|---|---|
| Unsigned | 0 a 255 |
| Signed (complemento de dois) | −128 a 127 |

**Raciocínio esperado:**

Cada bit possui duas possibilidades: 0 ou 1.

Com `n` bits, existem \(2^n\) combinações. Na representação com sinal em complemento de dois, parte dessas combinações representa valores negativos.

## 5. Orientações para avaliação

Verificar se o aluno:

- Compreende o valor posicional dos bits.
- Converte corretamente entre binário, decimal e hexadecimal.
- Identifica MSB, LSB e nibbles.
- Diferencia representações signed e unsigned.
- Compreende o funcionamento do complemento de dois.
- Calcula corretamente as combinações e os intervalos.

**Erros que merecem atenção:**

- Confundir posição do bit com seu valor.
- Somar pesos de posições cujo bit é zero.
- Interpretar o MSB como um bit adicional.
- Considerar que signed e unsigned modificam fisicamente os bits.
- Confundir quantidade de combinações com o maior valor representável.

## 6. Conclusão esperada

O aluno deve compreender que **uma sequência de bits não possui necessariamente um único significado numérico**.

A base, a quantidade de bits e a representação escolhida determinam como o valor será interpretado.

Esse conhecimento fundamenta o estudo dos tipos de dados, operações bitwise e representação de valores na memória.