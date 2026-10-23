# Exercício 07 — Módulo de TRACE

**Módulo:** 07 — Tracing e Execução  
**Linguagem:** C (ANSI C89)

## Objetivo

Desenvolver um módulo independente de TRACE para registrar a execução de um programa, utilizando macros, funções variádicas e informações do código-fonte.

## 1. Módulo de TRACE

Criar dois arquivos independentes:

- `trace.h` — Declarações e macros.
- `trace.c` — Implementação das funções.

O módulo deverá disponibilizar:

- `trace_init()` — Inicializar o arquivo de log.
- `trace_log()` — Registrar mensagens formatadas.
- `trace_close()` — Encerrar o rastreamento.

A utilização de `trace_log()` deverá ocorrer por meio de uma **macro de mesmo nome**, responsável por acrescentar automaticamente:

- `__FILE__` — Arquivo de origem.
- `__LINE__` — Linha da chamada.
- `__func__` — Função de origem (ou equivalente compatível com C89).

Cada registro deverá conter data, hora, arquivo, linha, função e mensagem.

O arquivo de log deverá ser aberto em modo *append* e permanecer aberto até `trace_close()`.

## 2. Programa de teste

Criar um programa `main.c` que:

1. Inicialize o TRACE.
2. Solicite dois números inteiros ao usuário.
3. Execute a soma por meio de uma função `iSoma()`.
4. Apresente o resultado.
5. Encerre o TRACE.

## 3. Registros obrigatórios

O arquivo de log deverá registrar:

- Início e fim da função `main()`.
- Os dois valores informados pelo usuário.
- Início e fim da função `iSoma()`.
- Resultado da operação.

## 4. Requisitos

- Separar o programa em `main.c`, `trace.c` e `trace.h`.
- Utilizar uma macro para acrescentar automaticamente as informações de origem.
- Permitir mensagens formatadas com argumentos variáveis.
- Não exigir que o código consumidor informe manualmente arquivo, linha ou função.
- Compilar os arquivos separadamente e realizar a ligação dos objetos.
- Demonstrar o conteúdo do arquivo de log após a execução.

**Importante:** o programa `main.c` deverá utilizar exclusivamente a interface pública do módulo, sem acessar seus recursos internos.