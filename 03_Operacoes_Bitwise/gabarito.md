# Gabarito 03 — Operações Bitwise

**Módulo:** 03 — Operações Bitwise  
**Exercício:** Operações Bitwise

## 1. Operações bit a bit

**Valores originais:**

```text
A = 10  →  00001010
B = 12  →  00001100
```

| Operação | Resultado binário | Decimal |
|---|---|---|
| `A & B` | `00001000` | 8 |
| `A \| B` | `00001110` | 14 |
| `A ^ B` | `00000110` | 6 |
| `~A` (8 bits) | `11110101` | 245 |

**Raciocínio esperado:**

- **AND (`&`):** o bit resultante é 1 somente quando ambos os bits são 1.
- **OR (`\|`):** o bit resultante é 1 quando pelo menos um dos bits é 1.
- **XOR (`^`):** o bit resultante é 1 quando os bits são diferentes.
- **NOT (`~`):** inverte todos os bits da representação considerada.

**Observação:** o resultado 245 para `~A` considera uma representação limitada a 8 bits sem sinal. Em uma expressão C com `int`, `~10` normalmente resulta em `-11`, considerando a representação usual em complemento de dois.

## 2. Deslocamento de bits

| Operação | Resultado binário | Decimal |
|---|---|---|
| `A << 1` | `00010100` | 20 |
| `B >> 2` | `00000011` | 3 |

**Raciocínio esperado:**

- **Deslocamento à esquerda (`<<`):** os bits são deslocados uma posição para a esquerda, preenchendo com zero à direita. Neste caso, equivale a multiplicar por 2.
- **Deslocamento à direita (`>>`):** os bits são deslocados duas posições para a direita. Como B é positivo, o resultado equivale à divisão inteira por 4.

Os bits que ultrapassam os limites da representação são descartados.

## 3. Máscaras de bits

**Valor original:**

`A = 00001010` (10)

As posições são numeradas da direita para a esquerda, começando em zero.

### A. Verificar o bit 3

**Máscara:** `00001000`

**Expressão:** `A & (1 << 3)`

```text
  00001010
& 00001000
----------
  00001000
```

**Resultado:** bit 3 ligado (1).

### B. Ligar o bit 2

**Máscara:** `00000100`

**Expressão:** `A | (1 << 2)`

```text
  00001010
| 00000100
----------
  00001110
```

**Resultado:** 14.

### C. Desligar o bit 1

**Máscara:** `11111101` (8 bits)

**Expressão:** `A & ~(1 << 1)`

```text
  00001010
& 11111101
----------
  00001000
```

**Resultado:** 8.

### D. Inverter o bit 3

**Máscara:** `00001000`

**Expressão:** `A ^ (1 << 3)`

```text
  00001010
^ 00001000
----------
  00000010
```

**Resultado:** 2.

**Raciocínio esperado:**

O aluno deve compreender que máscaras permitem selecionar ou modificar posições específicas sem alterar os demais bits.

- `&` permite testar ou limpar bits.
- `|` permite ligar bits.
- `^` permite inverter bits.
- `~` permite construir máscaras invertidas.

Cada operação deve utilizar o valor original de A, conforme o enunciado.

## 4. Orientações para avaliação

Verificar se o aluno:

- Aplica corretamente AND, OR, XOR e NOT.
- Diferencia operadores lógicos de operadores bitwise.
- Compreende os deslocamentos binários.
- Identifica corretamente as posições dos bits.
- Constrói máscaras adequadas.
- Preserva os bits que não devem ser modificados.

**Erros que merecem atenção:**

- Confundir AND com OR ou XOR.
- Confundir `&` com `&&` e `|` com `||`.
- Numerar os bits da esquerda para a direita.
- Inverter todos os bits quando apenas um deveria ser modificado.
- Aplicar as máscaras sobre resultados anteriores em vez do valor original.
- Desconsiderar a largura de 8 bits definida para o exercício.

## 5. Conclusão esperada

O aluno deve compreender que **operações bitwise permitem consultar e modificar individualmente os bits de um valor inteiro**.

Mais importante do que memorizar os resultados é entender como cada operador atua sobre os bits e como as máscaras permitem controlar posições específicas.

Esse conhecimento será útil no estudo de flags, registradores, protocolos e representações binárias em C.