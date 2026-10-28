# Organização_Computadores
## Exercício 12.10.2 — Projeto de um Circuito Digital

**Tema:** Tabelas-verdade, álgebra booleana, mapas de Karnaugh e circuitos combinacionais.

### Objetivo

Projetar um circuito digital a partir de uma especificação de funcionamento, obtendo sua expressão booleana e implementando uma versão simplificada com portas lógicas.

### 1. Cenário

Um sistema de iluminação automática possui quatro entradas digitais:

| Entrada | Descrição |
|---|---|
| A | Sistema habilitado |
| B | Sensor de presença ativado |
| C | Ambiente escuro |
| D | Acionamento manual solicitado |

Cada entrada assume os valores **0 (falso)** ou **1 (verdadeiro)**.

O circuito possui uma única saída, **L**, que determina se a iluminação deve ser acionada.

### 2. Regras de funcionamento

A iluminação deverá ser acionada quando:

1. O sistema estiver habilitado, houver presença e o ambiente estiver escuro.
2. O sistema estiver habilitado e houver solicitação de acionamento manual, independentemente da presença ou luminosidade.
3. O sistema estiver desabilitado, mas houver simultaneamente presença e solicitação de acionamento manual.

Em qualquer outra combinação, a iluminação deverá permanecer desligada.

### 3. Atividades

**A — Tabela-verdade**

Construa a tabela-verdade completa utilizando as quatro entradas A, B, C e D e a saída L.

**B — Expressão canônica**

A partir da tabela-verdade:

- Identifique os mintermos para os quais L = 1.
- Escreva a função na forma canônica de soma de produtos (SOP).

**C — Simplificação**

- Construa o mapa de Karnaugh de quatro variáveis.
- Identifique os agrupamentos válidos.
- Obtenha a expressão booleana simplificada.

**D — Implementação**

Desenhe o circuito digital correspondente à expressão simplificada, utilizando portas AND, OR e NOT.

**E — Verificação**

- Verifique se o circuito simplificado respeita todas as regras de funcionamento.
- Compare a expressão canônica com a simplificada.
- Informe a quantidade de portas utilizadas em cada implementação, considerando portas AND e OR com múltiplas entradas e inversores compartilhados.

### 4. Requisitos

- Utilizar as 16 combinações possíveis das quatro entradas.
- Respeitar a ordem Gray no mapa de Karnaugh.
- Utilizar agrupamentos de tamanhos válidos.
- Apresentar a expressão antes e depois da simplificação.
- Não utilizar código de programação para implementar a solução.

### 5. Entrega

O exercício deverá conter:

1. Tabela-verdade completa.
2. Expressão canônica SOP.
3. Mapa de Karnaugh com agrupamentos identificados.
4. Expressão booleana simplificada.
5. Diagrama do circuito digital.
6. Comparação entre as duas implementações.