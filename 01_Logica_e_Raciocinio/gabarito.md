# Gabarito 01 — Controle de Acesso

**Módulo:** 01 — Lógica e Raciocínio  
**Exercício:** Controle de Acesso

## 1. Identificação das proposições

O problema apresenta duas condições que determinam a permissão de entrada:

- **p:** O aluno solicitante possui um cartão de identificação válido.
- **q:** O aluno solicitante está acompanhado de um professor.

Cada proposição pode assumir dois valores:

- `1` — Verdadeiro: a condição é satisfeita.
- `0` — Falso: a condição não é satisfeita.

**Raciocínio esperado:**

O aluno deve reconhecer que as duas condições podem ser avaliadas independentemente.

A presença de um cartão válido não determina se a pessoa está acompanhada de um professor, e vice-versa.

As letras utilizadas são arbitrárias. O aluno pode escolher outros identificadores, desde que mantenha a correspondência entre as proposições.

## 2. Representação lógica

### Política A — Cartão e acompanhamento

A entrada exige cartão válido **E** acompanhamento de um professor.

**Expressão:**

`p AND q`

Ou, utilizando notação matemática:

\[
A = p \land q
\]

**Raciocínio esperado:**

O operador AND (E) representa a necessidade de satisfazer simultaneamente as duas condições.

Se qualquer uma delas for falsa, a entrada não será permitida.

### Política B — Cartão ou acompanhamento

A entrada exige cartão válido **OU** acompanhamento de um professor.

**Expressão:**

`p OR q`

Ou:

\[
B = p \lor q
\]

**Raciocínio esperado:**

O operador OR (OU) permite a entrada quando pelo menos uma das condições é verdadeira.

Se ambas forem verdadeiras, a entrada também será permitida.

É importante verificar se o aluno compreendeu que o OU lógico apresentado neste exercício é inclusivo, e não exclusivo.

## 3. Tabelas-verdade

### Política A — AND

| p | q | A = p AND q |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

A entrada é permitida somente quando as duas condições são verdadeiras.

### Política B — OR

| p | q | B = p OR q |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

A entrada é permitida quando pelo menos uma condição é verdadeira.

**Raciocínio esperado:**

Com duas proposições, cada uma podendo assumir dois valores, existem:

\[
2^2 = 4 \text{ combinações}
\]

O aluno deve considerar todas as combinações possíveis, sem repetir ou omitir cenários.

A ordem das linhas pode variar, desde que todas as combinações estejam representadas corretamente.

Também é válida a construção de uma única tabela contendo os resultados de AND e OR.

## 4. Interpretação dos resultados

**A. Em quais situações a entrada é permitida na política A?**

Somente quando a pessoa possui cartão válido e está acompanhada de um professor.

**B. Em quais situações a entrada é permitida na política B?**

Quando a pessoa possui cartão válido, está acompanhada de um professor ou satisfaz ambas as condições.

**C. Qual é a diferença entre E e OU?**

O operador E exige que todas as condições sejam verdadeiras.

O operador OU exige que pelo menos uma das condições seja verdadeira.

## 5. Orientações para avaliação

O mais importante não é a memorização das tabelas, mas a compreensão de como os operadores modificam o resultado de uma expressão lógica.

Durante a correção, observar se o aluno:

- Consegue identificar proposições a partir de um problema escrito em linguagem natural.
- Compreende que cada proposição possui um valor de verdade independente.
- Reconhece a diferença entre AND e OR.
- Constrói todas as combinações possíveis sem omissões.
- Consegue justificar os resultados obtidos.

**Erros que merecem atenção:**

- Confundir AND com OR.
- Considerar que OR é verdadeiro somente quando uma das condições é verdadeira, mas não ambas.
- Esquecer alguma combinação na tabela-verdade.
- Interpretar o resultado da expressão como o valor de uma das proposições isoladamente.

## 6. Conclusão esperada

O aluno deve compreender que **uma mesma combinação de condições pode produzir resultados diferentes dependendo do operador lógico utilizado**.

Na política A, as duas condições são obrigatórias.

Na política B, basta que uma delas seja satisfeita.

Essa compreensão será utilizada posteriormente na construção de expressões condicionais e estruturas de controle em linguagens de programação.