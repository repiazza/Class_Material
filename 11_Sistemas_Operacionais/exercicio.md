# Exercício 01 — Processos e comunicação entre processos

**Módulo:** 11 — Sistemas Operacionais em C  
**Referência:** Slides 12 a 21  
**Linguagem:** C — Linux/POSIX

## Objetivo

Desenvolver um programa que utilize processos independentes para registrar números em um arquivo de log.

O exercício será dividido em duas etapas. A primeira utilizará a criação de processos e a herança de memória. A segunda acrescentará comunicação bidirecional por meio de pipes.

## Parte A — Criação e gerenciamento de processos

O programa principal deverá apresentar o seguinte menu:

```text
[1] Informar número
[2] Encerrar
```

Ao selecionar a opção 1:

1. Solicitar ao usuário um número inteiro.
2. Criar um processo filho utilizando `fork()`.
3. O processo filho deverá registrar o número recebido em um arquivo de log, identificando seu PID.
4. Após registrar o número, o filho deverá encerrar sua execução.
5. O processo pai deverá aguardar o término do filho utilizando `waitpid()`.
6. Após o término, o pai deverá retornar ao menu.

**Requisitos:**

- O menu deverá ser executado exclusivamente pelo processo pai.
- O número deverá ser informado antes da chamada de `fork()`.
- O filho deverá utilizar o valor herdado no momento de sua criação.
- Tratar falhas na criação do processo.
- O processo pai deverá verificar o término do filho.
- O arquivo de log deverá ser aberto e fechado pelo próprio filho, utilizando o módulo de log já desenvolvido.
- A opção 2 deverá encerrar o programa.

**Exemplo de execução:**

```text
[1] Informar número
[2] Encerrar

Opção: 1
Número: 25

[Pai] Processo filho criado: 12346
[Filho 12346] Número registrado: 25
[Pai] Filho finalizado.

[1] Informar número
[2] Encerrar
```

## Parte B — Comunicação entre processos

Utilizando o programa desenvolvido na Parte A, modificar a maneira como o número é entregue ao processo filho e acrescentar uma confirmação de recebimento.

Nesta etapa, o pai e o filho deverão trocar informações por meio de **dois pipes**.

Ao selecionar a opção 1:

1. O processo pai deverá solicitar um número inteiro.
2. Criar dois pipes: um para enviar o número e outro para receber a confirmação.
3. Criar o processo filho utilizando `fork()`.
4. O pai deverá transmitir o número ao filho utilizando `write()`.
5. O filho deverá receber o número utilizando `read()`.
6. Após receber o número, o filho deverá registrá-lo no arquivo de log.
7. O filho deverá enviar a mensagem `OK` ao pai, indicando que o registro foi realizado.
8. O pai deverá receber a confirmação, aguardar o término do filho e retornar ao menu.

**Requisitos adicionais:**

- A transmissão do número deverá ocorrer exclusivamente pelo pipe, não pela leitura da variável herdada.
- Utilizar um pipe para cada direção da comunicação.
- Fechar as extremidades dos pipes que não serão utilizadas por cada processo.
- Verificar os retornos de `pipe()`, `read()`, `write()` e `waitpid()`.
- Tratar leituras e escritas parciais, garantindo a transferência completa dos dados esperados.
- A confirmação `OK` somente deverá ser enviada após o registro bem-sucedido do número.
- Em caso de falha, não apresentar `OK` como confirmação de sucesso.
- Preservar o menu, o módulo de log e a estrutura principal da Parte A.

**Exemplo de execução:**

```text
[1] Informar número
[2] Encerrar

Opção: 1
Número: 25

[Pai] Processo filho criado: 12346
[Pai] Número enviado: 25
[Filho 12346] Número recebido: 25
[Filho 12346] Registro realizado.
[Pai] Resposta recebida: OK
[Pai] Filho finalizado.

[1] Informar número
[2] Encerrar
```

## Orientação de desenvolvimento

Desde a Parte A, procure organizar o programa separando as responsabilidades do processo pai e do processo filho.

A Parte B deverá reutilizar essa organização, substituindo a obtenção do número por herança de memória pela comunicação através de pipes.

**Resultado esperado:** compreender a diferença entre criar processos independentes, compartilhar um estado inicial por herança e transmitir informações entre processos durante a execução.