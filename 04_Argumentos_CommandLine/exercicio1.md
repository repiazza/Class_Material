# Exercício 01 — Calculadora parametrizável

**Módulo:** 04 — Fundamentos de C  
**Tema:** `argc`, `argv`, validação e estruturas de configuração

## Objetivo

Desenvolver uma calculadora em C que realize operações de soma e subtração utilizando exclusivamente os argumentos fornecidos na linha de comando.

Cada execução deverá realizar uma única operação e encerrar.

## 1. Formato de execução

O programa deverá receber exatamente três argumentos, além do nome do executável:

```bash
./calc <operacao> <valor1> <valor2>
```

Operações aceitas:

- `soma`
- `subtrai`

Exemplos:

```bash
./calc soma 3 10
Resultado: 13
```

```bash
./calc subtrai 3 10
Resultado: -7
```

## 2. Requisitos obrigatórios

**A. Quantidade de argumentos**

- Utilizar `argc` para verificar se foram recebidos exatamente três argumentos adicionais ao executável.
- Rejeitar argumentos ausentes ou excedentes.
- Exibir a sintaxe correta em caso de erro.

**B. Operação**

- Identificar a operação por meio de `argv[1]`.
- Utilizar `strcmp()` para reconhecer `soma` e `subtrai`.
- Rejeitar qualquer operação desconhecida.

**C. Valores numéricos**

- Converter `argv[2]` e `argv[3]` utilizando `strtol()`.
- Aceitar somente números inteiros entre **0 e 100000**, inclusive.
- Rejeitar strings vazias, caracteres inválidos e valores fora do intervalo.
- Verificar erros de conversão, incluindo `ERANGE`.

**D. Estrutura de configuração**

Criar uma estrutura responsável por armazenar exclusivamente os parâmetros interpretados:

```c
typedef struct STRUCT_CONFIG
{
    char szOperacao[16];
    int iValor1;
    int iValor2;
} STRUCT_CONFIG, *PSTRUCT_CONFIG;
```

A estrutura deverá ser preenchida somente com valores validados.

**E. Processamento**

- Realizar a operação solicitada.
- Armazenar o resultado em uma variável separada da estrutura de configuração.
- Exibir o resultado e encerrar o programa.
- Retornar `0` em caso de sucesso e um valor diferente de zero em caso de erro.

## 3. Casos de teste

| Comando | Resultado esperado |
|---|---|
| `./calc soma 3 10` | `Resultado: 13` |
| `./calc subtrai 3 10` | `Resultado: -7` |
| `./calc soma 100000 100000` | `Resultado: 200000` |
| `./calc soma 3` | Erro: quantidade de argumentos |
| `./calc soma 3 10 20` | Erro: argumentos excedentes |
| `./calc multiplica 3 10` | Erro: operação desconhecida |
| `./calc soma abc 10` | Erro: valor inválido |
| `./calc soma 3 10abc` | Erro: valor inválido |
| `./calc soma -1 10` | Erro: valor fora do intervalo |
| `./calc soma 100001 10` | Erro: valor fora do intervalo |

## 4. Restrições

- Não utilizar `scanf()`, `fgets()` ou menus interativos.
- Não utilizar `atoi()` para converter os operandos.
- Não armazenar o resultado na `STRUCT_CONFIG`.
- Não implementar multiplicação, divisão ou outras operações.
- Não utilizar bibliotecas externas.

## 5. Compilação

```bash
gcc -Wall -Wextra -std=c89 calc.c -o calc
```

## 6. Critério de conclusão

O exercício estará concluído quando o mesmo executável puder ser chamado repetidamente com argumentos diferentes, validando cada chamada e produzindo o resultado correspondente, sem solicitar informações adicionais durante sua execução.