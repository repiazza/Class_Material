# Gabarito 10 — Analisador de Números

**Módulo:** 10 — Estruturas de Controle  
**Exercício:** Analisador de Números  
**Linguagem:** C (ANSI C89)

## 1. Menu principal

**Solução esperada:**

- Utilizar `do while` para manter o menu em execução.
- Utilizar `switch` para selecionar as quatro opções.
- Utilizar `case` e `break` para separar as funcionalidades.
- Utilizar `default` para tratar opções inválidas.
- Encerrar quando a opção 4 for selecionada.

**Raciocínio esperado:**

O `do while` garante que o menu seja apresentado pelo menos uma vez. O `switch` permite selecionar a operação conforme o valor informado.

## 2. Verificar um número

**Solução esperada:**

- Número maior que zero: positivo.
- Número menor que zero: negativo.
- Número igual a zero: zero.
- Número diferente de zero com resto da divisão por 2 igual a zero: par.
- Número diferente de zero com resto diferente de zero: ímpar.

**Raciocínio esperado:**

Utilizar `if / else if / else` para classificar o número e o operador `%` para verificar a paridade.

As verificações devem evitar classificações contraditórias.

## 3. Exibir uma sequência

**Solução esperada:**

Para um limite igual a 10:

```text
1 2 4 5 7 8 10
```

- Percorrer os números de 1 até o limite informado.
- Ignorar os números divisíveis por 3.
- Rejeitar limites menores que 1.

**Raciocínio esperado:**

Utilizar uma estrutura de repetição com contador e verificar `iNumero % 3 == 0`.

Quando essa condição for verdadeira, utilizar `continue` para ignorar a impressão do número.

## 4. Somar números

**Solução esperada:**

```text
Entrada: 10, 5, -3, 0
Soma total: 12
```

- Inicializar o acumulador com zero.
- Ler números sucessivamente.
- Somar os valores informados.
- Encerrar a leitura quando o número for zero.
- Apresentar o resultado acumulado.

**Raciocínio esperado:**

Utilizar uma estrutura de repetição para receber os números e `break` para interrompê-la quando o valor zero for informado.

O zero não deve ser acumulado.

## 5. Encerrar o programa

**Solução esperada:**

Ao selecionar a opção 4, apresentar uma mensagem de encerramento e finalizar a repetição do menu.

**Raciocínio esperado:**

A condição do `do while` deve permitir que o menu continue enquanto a opção de saída não for selecionada.

O `break` de um `case` encerra o `switch`, não necessariamente o laço externo.

## 6. Orientações para avaliação

Verificar se o aluno:

- Utilizou corretamente `do while` e `switch` no menu.
- Escolheu estruturas condicionais adequadas.
- Controlou corretamente as repetições.
- Aplicou `break` e `continue` nos contextos solicitados.
- Tratou limites e opções inválidas.
- Organizou o código em blocos legíveis.
- Respeitou as regras do ANSI C89.

**Erros que merecem atenção:**

- Laços infinitos por ausência de atualização ou condição de saída.
- Uso incorreto de `break`, especialmente em estruturas aninhadas.
- Uso de `continue` antes da atualização de um contador manual, impedindo o avanço do laço.
- Acumulador não inicializado.
- Declaração de variáveis no inicializador do `for`, incompatível com C89.

## 7. Conclusão esperada

O aluno deve demonstrar que compreende **como as estruturas de controle determinam o fluxo de execução de um programa**.

Mais importante do que utilizar uma estrutura específica em todas as situações é saber escolher e justificar uma solução adequada, respeitando os requisitos do exercício.