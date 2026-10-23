# Gabarito 07 — Módulo de TRACE

**Módulo:** 07 — Tracing e Execução  
**Exercício:** Módulo de TRACE  
**Linguagem:** C (ANSI C89, com extensão documentada para identificação da função)

## 1. Organização do módulo

**Estrutura esperada:**

```text
projeto/
├── main.c
├── trace.c
└── trace.h
```

**Raciocínio esperado:**

O aluno deve separar a interface pública da implementação, permitindo utilizar o TRACE em outros programas sem modificar seu código interno.

## 2. Interface e macro

**Exemplo de implementação em `trace.h`:**

```c
#ifndef TRACE_H
#define TRACE_H

void trace_init(const char *szArquivo);
void trace_write(const char *szArquivo,
                 int iLinha,
                 const char *szFuncao,
                 const char *szFormato, ...);
void trace_close(void);

#define trace_log(...) \
    trace_write(__FILE__, __LINE__, __func__, __VA_ARGS__)

#endif
```

**Raciocínio esperado:**

A macro substitui a chamada pública `trace_log()` por uma chamada à função interna `trace_write()`, acrescentando automaticamente o contexto de origem.

O aluno deve compreender que `__FILE__` e `__LINE__` são expandidos no local da chamada, e não dentro de `trace.c`.

**Observação de compatibilidade:** `__func__` pertence ao C99, enquanto macros variádicas com `__VA_ARGS__` também foram padronizadas no C99. Portanto, este exemplo exige C99 ou extensões do compilador. Para C89 estrito, é necessário adotar uma interface alternativa documentada.

## 3. Implementação do TRACE

**Comportamento esperado:**

- `trace_init()` abre o arquivo em modo append (`"a"`).
- O ponteiro `FILE *` permanece privado em `trace.c`, utilizando `static`.
- `trace_write()` recebe o contexto e os argumentos variáveis.
- `va_start`, `vfprintf` e `va_end` permitem formatar a mensagem.
- `time()` e `localtime()` permitem obter data e hora.
- `trace_close()` fecha o arquivo e invalida o ponteiro interno.

**Raciocínio esperado:**

O módulo deve manter seu próprio estado, sem exigir que o programa consumidor controle diretamente o arquivo de log.

A implementação também deve tratar falhas de abertura e evitar utilizar um `FILE *` inválido.

## 4. Programa de teste

**Exemplo de utilização em `main.c`:**

```c
#include <stdio.h>
#include "trace.h"

int iSoma(int iA, int iB)
{
    int iResultado;

    trace_log("Inicio da soma");

    iResultado = iA + iB;

    trace_log("Fim da soma: %d", iResultado);

    return iResultado;
}

int main(void)
{
    int iA, iB, iResultado;

    trace_init("programa.log");
    trace_log("Inicio da main");

    printf("Digite A: ");
    scanf("%d", &iA);
    trace_log("Entrada A: %d", iA);

    printf("Digite B: ");
    scanf("%d", &iB);
    trace_log("Entrada B: %d", iB);

    iResultado = iSoma(iA, iB);

    printf("Resultado: %d\n", iResultado);
    trace_log("Resultado: %d", iResultado);

    trace_log("Fim da main");
    trace_close();

    return 0;
}
```

**Raciocínio esperado:**

O programa consumidor utiliza somente `trace_init()`, `trace_log()` e `trace_close()`.

As informações de arquivo, linha e função não são fornecidas manualmente, demonstrando o funcionamento da macro.

Para uma implementação robusta, o aluno também deverá verificar o retorno de `scanf()` antes de utilizar os valores lidos.

## 5. Exemplo de saída do TRACE

```text
2026-10-23 09:00:00 [main.c:21:main] Inicio da main
2026-10-23 09:00:02 [main.c:25:main] Entrada A: 10
2026-10-23 09:00:04 [main.c:29:main] Entrada B: 20
2026-10-23 09:00:04 [main.c:8:iSoma] Inicio da soma
2026-10-23 09:00:04 [main.c:12:iSoma] Fim da soma: 30
2026-10-23 09:00:04 [main.c:34:main] Resultado: 30
2026-10-23 09:00:04 [main.c:36:main] Fim da main
```

Os horários e números de linha são ilustrativos.

**Raciocínio esperado:**

O aluno deve demonstrar que cada registro identifica o ponto de origem e que a sequência de mensagens permite acompanhar o fluxo de execução.

## 6. Compilação separada

```bash
gcc -c trace.c -o trace.o
gcc -c main.c -o main.o
gcc main.o trace.o -o programa
```

**Raciocínio esperado:**

O aluno deve compreender que cada arquivo-fonte pode ser compilado independentemente e que a ligação reúne os objetos em um executável.

A compilação deverá utilizar um modo compatível com a implementação escolhida para as macros e a identificação da função.

## 7. Orientações para avaliação

Verificar se o aluno:

- Separou corretamente interface e implementação.
- Utilizou `static` para proteger o estado interno.
- Implementou corretamente os argumentos variáveis.
- Utilizou a macro para capturar o contexto da chamada.
- Registrou todas as entradas e etapas exigidas.
- Manteve o arquivo aberto durante a execução.
- Fechou corretamente o arquivo ao finalizar.
- Demonstrou a compilação separada dos módulos.

**Erros que merecem atenção:**

- Utilizar `__FILE__` e `__LINE__` diretamente dentro de `trace.c`, registrando sempre a origem interna.
- Exigir que o consumidor informe manualmente arquivo, linha e função.
- Abrir e fechar o arquivo a cada mensagem.
- Expor o ponteiro interno do arquivo.
- Esquecer `va_start` ou `va_end`.
- Registrar o fim da execução somente após `trace_close()`.

## 8. Conclusão esperada

O aluno deve compreender que **um módulo de TRACE permite observar o fluxo de execução sem misturar a implementação do rastreamento com a lógica principal do programa**.

A principal competência avaliada é a capacidade de construir uma interface reutilizável, utilizando macros para capturar automaticamente informações do código-fonte e funções variádicas para registrar mensagens formatadas.