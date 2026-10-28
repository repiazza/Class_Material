# Organização_Computadores
## Gabarito 12.10.2 — Projeto de um Circuito Digital

**Tema:** Tabelas-verdade, álgebra booleana, mapas de Karnaugh e circuitos combinacionais.

### A — Tabela-verdade

Conforme as regras do exercício, a iluminação será acionada quando:

1. A = 1, B = 1 e C = 1.
2. A = 1 e D = 1.
3. A = 0, B = 1 e D = 1.

As condições não mencionadas em cada regra podem assumir qualquer valor.

| A | B | C | D | L |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 0 | 1 | 0 |
| 0 | 0 | 1 | 0 | 0 |
| 0 | 0 | 1 | 1 | 0 |
| 0 | 1 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 | **1** |
| 0 | 1 | 1 | 0 | 0 |
| 0 | 1 | 1 | 1 | **1** |
| 1 | 0 | 0 | 0 | 0 |
| 1 | 0 | 0 | 1 | **1** |
| 1 | 0 | 1 | 0 | 0 |
| 1 | 0 | 1 | 1 | **1** |
| 1 | 1 | 0 | 0 | 0 |
| 1 | 1 | 0 | 1 | **1** |
| 1 | 1 | 1 | 0 | **1** |
| 1 | 1 | 1 | 1 | **1** |

### B — Expressão canônica

Identificamos as linhas em que L = 1:

**Mintermos:** 5, 7, 9, 11, 13, 14 e 15.

Forma canônica SOP:

```text
L = Σm(5, 7, 9, 11, 13, 14, 15)
```

Expandindo os mintermos:

```text
m5  = !A ·  B · !C ·  D
m7  = !A ·  B ·  C ·  D
m9  =  A · !B · !C ·  D
m11 =  A · !B ·  C ·  D
m13 =  A ·  B · !C ·  D
m14 =  A ·  B ·  C · !D
m15 =  A ·  B ·  C ·  D
```

Portanto:

```text
L = m5 + m7 + m9 + m11 + m13 + m14 + m15
```

**Notação:** `!` representa NOT, `·` representa AND e `+` representa OR.

### C — Simplificação pelo mapa de Karnaugh

Utilizamos a ordem Gray:

**00, 01, 11, 10**

Mapa de quatro variáveis:

| AB \ CD | 00 | 01 | 11 | 10 |
|---|---|---|---|---|
| 00 | 0 | 0 | 0 | 0 |
| 01 | 0 | **1** | **1** | 0 |
| 11 | 0 | **1** | **1** | **1** |
| 10 | 0 | **1** | **1** | 0 |

**Agrupamento 1 — Quatro células**

Mintermos: 9, 11, 13 e 15.

- A permanece em 1.
- D permanece em 1.
- B e C variam e são eliminadas.

Resultado:

```text
G1 = A · D
```

**Agrupamento 2 — Quatro células**

Mintermos: 5, 7, 13 e 15.

- B permanece em 1.
- D permanece em 1.
- A e C variam e são eliminadas.

Resultado:

```text
G2 = B · D
```

**Agrupamento 3 — Duas células**

Mintermos: 14 e 15.

- A, B e C permanecem em 1.
- D varia e é eliminada.

Resultado:

```text
G3 = A · B · C
```

**Expressão simplificada:**

```text
L = A·D + B·D + A·B·C
```

Também podemos fatorar os dois primeiros termos:

```text
L = D·(A + B) + A·B·C
```

As duas expressões são equivalentes.

**Observação:** os mintermos 13 e 15 participam de mais de um agrupamento. Essa sobreposição é válida e permite obter a simplificação desejada.

### D — Implementação do circuito

Utilizando a expressão simplificada:

```text
L = A·D + B·D + A·B·C
```

Construímos três termos intermediários:

```text
G1 = A AND D
G2 = B AND D
G3 = A AND B AND C

L = G1 OR G2 OR G3
```

**Componentes necessários:**

- 2 portas AND de duas entradas.
- 1 porta AND de três entradas.
- 1 porta OR de três entradas.
- Nenhum inversor NOT.

A saída de cada porta AND será conectada a uma das entradas da porta OR.

### E — Verificação e comparação

O circuito simplificado deverá produzir L = 1 exatamente para:

```text
5, 7, 9, 11, 13, 14 e 15
```

Para todas as outras combinações, L = 0.

**Comparação das implementações:**

| Característica | Canônica | Simplificada |
|---|---|---|
| Termos de produto | 7 | 3 |
| Portas AND | 7 | 3 |
| Portas OR | 1 | 1 |
| Inversores NOT | 4 | 0 |
| Total de portas | **12** | **4** |

A contagem considera portas AND e OR com múltiplas entradas e inversores compartilhados, conforme solicitado no exercício.

A implementação simplificada reduz a quantidade de portas de 12 para 4, mantendo exatamente o mesmo comportamento lógico.

### Conclusão

O exercício demonstra o processo completo de projeto de um circuito combinacional:

1. Interpretar a especificação.
2. Construir a tabela-verdade.
3. Identificar os mintermos.
4. Escrever a expressão canônica.
5. Simplificar com Karnaugh.
6. Implementar o circuito com portas lógicas.
7. Verificar a equivalência entre as implementações.

**Resultado final:**

```text
L = A·D + B·D + A·B·C
```

A simplificação permite implementar a mesma função lógica com menos componentes, sem alterar o comportamento especificado.

**Fim da Etapa 1 — Fundamentos da lógica e dos circuitos digitais.**