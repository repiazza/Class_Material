# Gabarito — Exercício 02: Evolução da Calculadora Parametrizável

**Módulo:** 04 — Fundamentos de C  
**Tema:** Parsing de linha de comando, opções longas, curtas, posicionais e opcionais.

## 1. Implementação — `calc.c`

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>

#define MAX_VALOR 100000

typedef struct STRUCT_CONFIG
{
    char szOperacao[16];
    int iValor1;
    int iValor2;
    int iVerbose;
} STRUCT_CONFIG, *PSTRUCT_CONFIG;

int iConverterValor(const char *pszTexto, int *piValor)
{
    char *pEnd;
    long lValor;

    if (pszTexto == NULL || pszTexto[0] == 0)
        return 0;

    errno = 0;
    pEnd = NULL;

    lValor = strtol(pszTexto, &pEnd, 10);

    if (pEnd == pszTexto || *pEnd != 0)
        return 0;

    if (errno == ERANGE)
        return 0;

    if (lValor < 0 || lValor > MAX_VALOR)
        return 0;

    *piValor = (int)lValor;

    return 1;
}

void vExibirUso(const char *pszPrograma)
{
    printf("Uso: %s --operacao=OP -a VALOR VALOR [--verbose]\n",
           pszPrograma);
    printf("     %s --version\n", pszPrograma);
}

int main(int argc, char *argv[])
{
    STRUCT_CONFIG stConfig;

    int i;
    int iResultado;
    int iTemOperacao;
    int iTemValor1;
    int iTemValor2;
    int iTemVerbose;

    const char *pszOperacao;

    memset(&stConfig, 0, sizeof(stConfig));

    iTemOperacao = 0;
    iTemValor1 = 0;
    iTemValor2 = 0;
    iTemVerbose = 0;

    if (argc == 2 && strcmp(argv[1], "--version") == 0)
    {
        printf("Calculadora v2.0\n");
        return 0;
    }

    for (i = 1; i < argc; i++)
    {
        if (strncmp(argv[i], "--operacao=", 10) == 0)
        {
            if (iTemOperacao)
            {
                fprintf(stderr, "Erro: operacao duplicada.\n");
                vExibirUso(argv[0]);
                return 1;
            }

            pszOperacao = argv[i] + 10;

            if (strcmp(pszOperacao, "soma") != 0 &&
                strcmp(pszOperacao, "subtrai") != 0)
            {
                fprintf(stderr, "Erro: operacao invalida: %s\n",
                        pszOperacao);
                vExibirUso(argv[0]);
                return 1;
            }

            strcpy(stConfig.szOperacao, pszOperacao);
            iTemOperacao = 1;
        }
        else if (strcmp(argv[i], "-a") == 0)
        {
            if (iTemValor1)
            {
                fprintf(stderr, "Erro: opcao -a duplicada.\n");
                vExibirUso(argv[0]);
                return 1;
            }

            if (i + 1 >= argc)
            {
                fprintf(stderr, "Erro: valor ausente para -a.\n");
                vExibirUso(argv[0]);
                return 1;
            }

            if (!iConverterValor(argv[i + 1],
                                 &stConfig.iValor1))
            {
                fprintf(stderr, "Erro: valor1 invalido: %s\n",
                        argv[i + 1]);
                vExibirUso(argv[0]);
                return 1;
            }

            iTemValor1 = 1;
            i++;
        }
        else if (strcmp(argv[i], "--verbose") == 0)
        {
            if (iTemVerbose)
            {
                fprintf(stderr, "Erro: --verbose duplicado.\n");
                vExibirUso(argv[0]);
                return 1;
            }

            stConfig.iVerbose = 1;
            iTemVerbose = 1;
        }
        else if (argv[i][0] == '-')
        {
            fprintf(stderr, "Erro: opcao desconhecida: %s\n",
                    argv[i]);
            vExibirUso(argv[0]);
            return 1;
        }
        else
        {
            if (iTemValor2)
            {
                fprintf(stderr,
                        "Erro: argumento posicional excedente: %s\n",
                        argv[i]);
                vExibirUso(argv[0]);
                return 1;
            }

            if (!iConverterValor(argv[i], &stConfig.iValor2))
            {
                fprintf(stderr, "Erro: valor2 invalido: %s\n",
                        argv[i]);
                vExibirUso(argv[0]);
                return 1;
            }

            iTemValor2 = 1;
        }
    }

    if (!iTemOperacao || !iTemValor1 || !iTemValor2)
    {
        fprintf(stderr, "Erro: parametros obrigatorios ausentes.\n");
        vExibirUso(argv[0]);
        return 1;
    }

    if (strcmp(stConfig.szOperacao, "soma") == 0)
        iResultado = stConfig.iValor1 + stConfig.iValor2;
    else
        iResultado = stConfig.iValor1 - stConfig.iValor2;

    if (stConfig.iVerbose)
    {
        printf("Operacao: %s\n", stConfig.szOperacao);
        printf("Valor 1: %d\n", stConfig.iValor1);
        printf("Valor 2: %d\n", stConfig.iValor2);
    }

    printf("Resultado: %d\n", iResultado);

    return 0;
}
```

## 2. Compilação

```bash
gcc -Wall -Wextra -std=c89 calc.c -o calc
```

## 3. Testes de execução

**Soma:**

```bash
./calc --operacao=soma -a 3 10
Resultado: 13
```

**Subtração com argumentos em outra ordem:**

```bash
./calc 10 -a 3 --operacao=subtrai
Resultado: -7
```

**Modo detalhado:**

```bash
./calc --operacao=soma -a 3 10 --verbose
Operacao: soma
Valor 1: 3
Valor 2: 10
Resultado: 13
```

**Versão:**

```bash
./calc --version
Calculadora v2.0
```

**Valor inválido:**

```bash
./calc --operacao=soma -a abc 10
Erro: valor1 invalido: abc
```

**Argumento posicional excedente:**

```bash
./calc --operacao=soma -a 3 10 20
Erro: argumento posicional excedente: 20
```

**Opção duplicada:**

```bash
./calc --operacao=soma -a 3 10 -a 5
Erro: opcao -a duplicada.
```

**Opção desconhecida:**

```bash
./calc --operacao=soma -a 3 10 --xyz
Erro: opcao desconhecida: --xyz
```

## 4. Conceitos aplicados

| Recurso | Aplicação |
|---|---|
| `strncmp()` | Reconhecer o prefixo `--operacao=` |
| `strcmp()` | Reconhecer opções e operações completas |
| `argv[i] + 10` | Acessar o valor após o prefixo |
| `argv[i + 1]` | Obter o valor de uma opção curta |
| `i++` | Avançar após consumir um argumento |
| `strtol()` | Converter e validar os operandos |
| `iTemOperacao`, `iTemValor1`, `iTemValor2` | Controlar presença e duplicidade |
| `iTemVerbose` | Identificar repetição da flag |
| `STRUCT_CONFIG` | Armazenar a configuração validada |
| `iResultado` | Armazenar o resultado fora da configuração |

## 5. Pontos importantes do gabarito

**A. O `argc` deixou de determinar uma quantidade fixa de argumentos.**

No Exercício 01, bastava verificar `argc == 4`. Agora, a quantidade depende das opções informadas.

Por isso, percorremos `argv` e verificamos individualmente a presença dos parâmetros obrigatórios.

**B. Nem toda opção consome o próximo argumento.**

A opção `-a` exige um valor separado:

```c
if (strcmp(argv[i], "-a") == 0)
{
    /* ... */
    i++;
}
```

Já `--verbose` apenas ativa uma flag, sem consumir outro argumento.

**C. Uma opção longa pode conter seu valor no próprio argumento.**

```c
if (strncmp(argv[i], "--operacao=", 10) == 0)
{
    pszOperacao = argv[i] + 10;
}
```

Nesse caso, não precisamos de `strtok()`, buffers auxiliares ou cópias para separar o valor.

**D. A presença de um parâmetro é diferente de seu conteúdo.**

O valor `0` é válido para os operandos. Portanto, não podemos utilizar `iValor1 == 0` para concluir que o primeiro operando está ausente.

Os indicadores `iTemValor1` e `iTemValor2` resolvem esse problema.

**E. A opção `--version` encerra antecipadamente.**

Ela é reconhecida antes do parsing normal, somente quando utilizada isoladamente. Assim, não exige operação nem operandos.

**F. Configuração e processamento continuam separados.**

A `STRUCT_CONFIG` armazena os parâmetros interpretados. O cálculo utiliza esses parâmetros e produz `iResultado`, sem alterar a finalidade da estrutura.

## 6. Critério de avaliação

O principal objetivo não é a quantidade de funções utilizadas, mas a capacidade de reconhecer corretamente cada formato de argumento.

O aluno deverá demonstrar que compreendeu:

- A diferença entre opções longas, curtas, posicionais e flags.
- Quando um argumento consome o próximo elemento de `argv`.
- Como identificar parâmetros obrigatórios, duplicados e desconhecidos.
- Como reutilizar a validação numérica existente.
- Como preservar a separação entre configuração e processamento.

**Resultado esperado:** uma calculadora com uma interface de linha de comando mais flexível, sem alterar a lógica matemática desenvolvida no Exercício 01.
