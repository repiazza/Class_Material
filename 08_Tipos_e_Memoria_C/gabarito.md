# Gabarito 08 — Valores, Ponteiros e Memória

**Módulo:** 08 — Tipos e Memória em C  
**Exercício:** Valores, Ponteiros e Memória  
**Linguagem:** ANSI C89

## 1. Análise do programa

**Saída esperada:**

```text
15
15
20
```

**Respostas:**

1. `iA` apresenta o valor 15, `*pA` também apresenta 15 e `aiValores[1]` apresenta 20.
2. `&iA` representa o endereço de memória da variável `iA`.
3. `pA` contém o endereço de `iA`, enquanto `*pA` acessa o valor armazenado no objeto apontado.
4. A atribuição `*pA = 15` modifica diretamente o objeto `iA`, pois `pA` aponta para ele.
5. `iB` permanece com valor 20, pois nenhuma instrução modifica essa variável.

**Raciocínio esperado:**

O aluno deve compreender que um ponteiro armazena um endereço e que o operador `*` permite acessar ou modificar o objeto localizado nesse endereço.

Modificar `*pA` não altera o endereço armazenado em `pA`, mas o conteúdo da variável apontada.

## 2. Arrays e endereçamento

**Respostas:**

1. O array possui **3 elementos**.
2. `aiValores[1]` contém o valor **20**.
3. `aiValores[1]` e `*(aiValores + 1)` acessam o mesmo elemento.
4. Considerando `sizeof(int) == 4`, a distância entre os endereços dos elementos 0 e 2 é de **8 bytes**.

**Raciocínio esperado:**

Os elementos de um array ocupam posições consecutivas na memória.

A aritmética de ponteiros considera o tamanho do tipo apontado. Portanto, `aiValores + 1` avança um elemento do tipo `int`, e não necessariamente um byte.

O deslocamento entre os elementos 0 e 2 corresponde a:

`2 * sizeof(int) = 8 bytes`

## 3. Representação da memória

**Exemplo de representação esperada:**

```text
Variável iA
Endereço: 1000
Valor:    15
             ▲
             │
             │ aponta para
             │
Ponteiro pA ─┘
Conteúdo: 1000


Array aiValores

Endereço     Elemento       Valor
2000         aiValores[0]    10
2004         aiValores[1]    20
2008         aiValores[2]    30
```

Os endereços apresentados são fictícios e consideram `int` com 4 bytes.

**Raciocínio esperado:**

O aluno deve representar corretamente a relação entre o ponteiro e a variável apontada, além da disposição contígua dos elementos do array.

Não é necessário utilizar endereços reais. O importante é preservar as relações entre os objetos.

## 4. Orientações para avaliação

Verificar se o aluno:

- Diferencia valor e endereço de memória.
- Compreende os operadores `&` e `*`.
- Reconhece que um ponteiro permite modificar o objeto apontado.
- Identifica corretamente os índices de um array.
- Compreende a equivalência entre indexação e aritmética de ponteiros.
- Considera o tamanho do tipo ao calcular deslocamentos.

**Erros que merecem atenção:**

- Confundir `pA` com `*pA`.
- Considerar que `*pA = 15` modifica o endereço do ponteiro.
- Acreditar que a primeira posição de um array possui índice 1.
- Considerar que `aiValores + 1` sempre avança um byte.
- Confundir o valor armazenado em um elemento com seu endereço.

## 5. Conclusão esperada

O aluno deve compreender que **variáveis armazenam valores, ponteiros armazenam endereços e arrays organizam elementos consecutivos de um mesmo tipo na memória**.

A principal competência avaliada é a capacidade de relacionar valores, endereços e operações de indireção, compreendendo como esses elementos interagem durante a execução de um programa.