# Exercício 02 — Evolução da Calculadora Parametrizável

**Módulo:** 04 — Fundamentos de C  
**Tema:** Parsing de linha de comando, opções longas, curtas, posicionais e opcionais.

## Objetivo

Evoluir a calculadora do Exercício 01 para interpretar diferentes formatos de argumentos de linha de comando, mantendo as operações de soma e subtração.

O programa deverá realizar uma única operação por execução, sem solicitar informações interativamente.

## 1. Formato de execução

A calculadora deverá reconhecer os seguintes parâmetros:

| Parâmetro | Tipo | Obrigatório | Finalidade |
|---|---|---|---|
| `--operacao=VALOR` | Opção longa | Sim | Define `soma` ou `subtrai` |
| `-a VALOR` | Opção curta | Sim | Define o primeiro operando |
| `VALOR` | Posicional (unnamed) | Sim | Define o segundo operando |
| `--verbose` | Flag opcional | Não | Exibe informações adicionais |
| `--version` | Opção especial | Não | Exibe a versão e encerra |

Exemplos:

```bash
./calc --operacao=soma -a 3 10
Resultado: 13
```

```bash
./calc --operacao=subtrai -a 3 10
Resultado: -7
```

```bash
./calc --operacao=soma -a 3 10 --verbose
Operacao: soma
Valor 1: 3
Valor 2: 10
Resultado: 13
```

```bash
./calc --version
Calculadora v2.0
```

## 2. Requisitos obrigatórios

**A. Interpretação dos argumentos**

- Percorrer os argumentos recebidos em `argv`.
- Reconhecer as opções longas e curtas.
- Identificar o argumento posicional.
- Permitir diferentes ordens de apresentação dos parâmetros.
- Consumir corretamente o argumento seguinte quando uma opção exigir valor.

**B. Operação e valores**

- Aceitar somente `soma` e `subtrai`.
- Manter o intervalo de 0 a 100000 para os dois operandos.
- Reutilizar a validação numérica com `strtol()` do Exercício 01.
- Rejeitar valores ausentes, inválidos ou fora do intervalo.

**C. Opções especiais**

- `--verbose`: quando presente, exibir a operação e os operandos antes do resultado.
- `--version`: quando presente, exibir `Calculadora v2.0` e encerrar com sucesso, sem exigir os demais parâmetros.
- A opção `--version` deverá ser utilizada isoladamente.

**D. Validação do contrato**

- Rejeitar opções desconhecidas.
- Rejeitar parâmetros obrigatórios ausentes.
- Rejeitar opções repetidas, inclusive `--verbose`.
- Rejeitar argumentos posicionais excedentes.
- Exibir uma mensagem de erro e a sintaxe esperada quando a chamada for inválida.

**E. Estrutura de configuração**

Reutilizar a `STRUCT_CONFIG` do Exercício 01, acrescentando somente o campo necessário para o modo detalhado:

```c
typedef struct STRUCT_CONFIG
{
    char szOperacao[16];
    int iValor1;
    int iValor2;
    int iVerbose;
} STRUCT_CONFIG, *PSTRUCT_CONFIG;
```

A estrutura deverá armazenar exclusivamente os parâmetros validados. O resultado da operação deverá permanecer em uma variável separada.

## 3. Casos de teste

| Comando | Resultado esperado |
|---|---|
| `./calc --operacao=soma -a 3 10` | `Resultado: 13` |
| `./calc 10 -a 3 --operacao=subtrai` | `Resultado: -7` |
| `./calc --operacao=soma -a 3 10 --verbose` | Saída detalhada e resultado 13 |
| `./calc --version` | Exibe a versão e encerra |
| `./calc --operacao=soma -a 3` | Erro: argumento posicional ausente |
| `./calc --operacao=soma -a abc 10` | Erro: valor inválido |
| `./calc --operacao=multiplica -a 3 10` | Erro: operação desconhecida |
| `./calc --operacao=soma -a 3 10 20` | Erro: argumento excedente |
| `./calc --operacao=soma -a 3 10 --xyz` | Erro: opção desconhecida |
| `./calc --operacao=soma -a 3 10 -a 5` | Erro: opção duplicada |
| `./calc --version --verbose` | Erro: uso inválido de `--version` |

## 4. Restrições

- Não utilizar `scanf()`, `fgets()` ou menus interativos.
- Não utilizar `atoi()` para converter os operandos.
- Não utilizar `getopt()`, `getopt_long()` ou bibliotecas externas de parsing.
- Não implementar novas operações matemáticas.
- Não utilizar variáveis de ambiente neste exercício.
- Não armazenar o resultado na `STRUCT_CONFIG`.

É permitido reutilizar funções e trechos de código do Exercício 01.

## 5. Compilação

```bash
gcc -Wall -Wextra -std=c89 calc.c -o calc
```

## 6. Critério de conclusão

O exercício estará concluído quando a calculadora conseguir interpretar corretamente opções longas, curtas, posicionais e opcionais, independentemente da ordem permitida pelo contrato, validando os parâmetros e produzindo o resultado esperado.

**O objetivo principal é evoluir a interface de execução da calculadora, preservando sua lógica de processamento.**