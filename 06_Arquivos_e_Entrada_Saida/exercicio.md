# 06 — Arquivos e Entrada/Saída
## Exercício — Explorador de Arquivos em C

**Tema:** Persistência, operações de entrada/saída, streams, posicionamento e leitura de arquivos.

### 1. Objetivo

Desenvolver em linguagem C um programa que permita gravar e consultar informações em um arquivo de texto.

O exercício será dividido em duas etapas:

- **Etapa A:** implementar a gravação e a leitura sequencial do arquivo.
- **Etapa B:** ampliar o mesmo programa para permitir consultas por posição e leitura parcial de bytes.

A Etapa B deverá reutilizar as estruturas e funções desenvolvidas na Etapa A.

### 2. Premissas gerais

O programa deverá trabalhar com um único arquivo denominado `dados.txt`.

As operações de leitura deverão utilizar um buffer fixo de 128 bytes.

O arquivo deverá permanecer disponível entre diferentes execuções do programa, preservando as informações já gravadas.

O programa não deverá carregar todo o conteúdo do arquivo na memória para realizar as consultas.

---

## Etapa A — Gravação e leitura sequencial

### 3. Menu inicial

Implementar o seguinte menu:

```text
[1] - Adicionar texto ao arquivo
[2] - Exibir conteúdo do arquivo
[3] - Encerrar
```

**Opção 1 — Adicionar texto ao arquivo**

- Solicitar uma linha de texto ao usuário.
- Acrescentar a linha ao final de `dados.txt`.
- Preservar o conteúdo gravado anteriormente.
- Exibir uma mensagem confirmando a gravação.
- Verificar possíveis falhas de abertura e escrita.

**Opção 2 — Exibir conteúdo do arquivo**

- Abrir `dados.txt` para leitura.
- Percorrer o arquivo sequencialmente.
- Exibir todo o conteúdo gravado.
- Utilizar o buffer de 128 bytes, permitindo a leitura de arquivos maiores que o buffer.
- Informar quando o arquivo estiver vazio ou ainda não existir.

**Opção 3 — Encerrar**

- Encerrar o programa, garantindo o fechamento dos arquivos utilizados.

### 4. Requisitos da Etapa A

1. Utilizar `FILE *` para manipular o arquivo.
2. Utilizar `fopen()` e `fclose()`.
3. Utilizar `fgets()` para receber o texto digitado pelo usuário.
4. Utilizar `fprintf()` ou `fputs()` para gravar o conteúdo.
5. Utilizar `fgets()` para a leitura sequencial do arquivo.
6. Implementar funções separadas para gravação e leitura.
7. Tratar falhas de abertura e operações de entrada/saída.
8. Não apagar o conteúdo anterior ao adicionar uma nova linha.
9. Não utilizar alocação dinâmica para armazenar o conteúdo do arquivo.

### 5. Cenário de validação A

Execute as seguintes operações:

| Operação | Resultado esperado |
|---|---|
| Exibir arquivo inexistente | Mensagem informativa |
| Adicionar `ABCDEFGHIJ` | Texto gravado |
| Adicionar `KLMNOPQRST` | Nova linha acrescentada |
| Exibir arquivo | As duas linhas são exibidas |
| Encerrar | Arquivo preservado |
| Executar novamente | Conteúdo anterior disponível |

**Resultado da Etapa A:** um programa capaz de persistir informações e recuperá-las sequencialmente, sem depender do tamanho total do arquivo.

---

## Etapa B — Posicionamento e leitura parcial

### 6. Evolução do programa

A partir da implementação concluída na Etapa A, ampliar o menu:

```text
[1] - Adicionar texto ao arquivo
[2] - Exibir conteúdo do arquivo
[3] - Ler trecho por posição
[4] - Consultar tamanho do arquivo
[5] - Encerrar
```

As opções 1 e 2 deverão continuar funcionando sem alterações em seu comportamento.

As novas funcionalidades deverão aproveitar a estrutura de abertura, leitura e fechamento utilizada anteriormente.

### 7. Novas operações

**Opção 3 — Ler trecho por posição**

- Solicitar uma posição inicial em bytes, considerando a primeira posição como zero.
- Solicitar a quantidade de bytes que o usuário deseja ler.
- Abrir o arquivo para leitura.
- Utilizar `fseek()` para posicionar o cursor na posição informada.
- Utilizar `fread()` para recuperar o trecho solicitado.
- Exibir os bytes efetivamente recuperados.
- Informar a quantidade de bytes solicitados e a quantidade realmente lida.

A leitura deverá respeitar a capacidade do buffer.

Quando o trecho solicitado ultrapassar o final do arquivo, o programa deverá exibir somente os bytes disponíveis.

**Opção 4 — Consultar tamanho do arquivo**

- Abrir o arquivo para leitura.
- Utilizar `fseek()` com `SEEK_END` para alcançar o final.
- Utilizar `ftell()` para obter o tamanho em bytes.
- Exibir o tamanho encontrado.
- Fechar o arquivo.

### 8. Requisitos da Etapa B

1. Preservar as funcionalidades implementadas na Etapa A.
2. Reutilizar o buffer de leitura e as rotinas existentes sempre que aplicável.
3. Utilizar `fseek()`, `ftell()` e `fread()`.
4. Tratar posições negativas ou além do final do arquivo.
5. Impedir leituras maiores que a capacidade do buffer.
6. Utilizar o valor retornado por `fread()` para determinar a quantidade de bytes recuperados.
7. Não assumir que a quantidade solicitada será sempre a quantidade lida.
8. Não interpretar o retorno de `fread()` como uma string terminada automaticamente em zero.
9. Verificar falhas de posicionamento e leitura.
10. Não carregar o arquivo inteiro na memória para localizar um trecho.

### 9. Cenário de validação B

Utilize um arquivo contendo exatamente os seguintes bytes:

```text
ABCDEFGHIJ
```

Para este teste, o arquivo não deverá conter uma quebra de linha após o último caractere.

| Posição inicial | Bytes solicitados | Resultado esperado |
|---|---:|---|
| 0 | 4 | `ABCD` |
| 3 | 4 | `DEFG` |
| 7 | 5 | `HIJ` |
| 9 | 1 | `J` |
| 10 | 4 | Nenhum byte recuperado |
| -1 | 3 | Posição inválida |
| 2 | 0 | Quantidade inválida |

A consulta de tamanho deverá retornar:

```text
Tamanho do arquivo: 10 bytes
```

**Resultado da Etapa B:** um programa capaz de consultar o conteúdo de um arquivo tanto sequencialmente quanto a partir de posições específicas, respeitando os limites de leitura.

---

### 10. Requisitos finais

- Desenvolver o programa em linguagem C.
- Utilizar funções separadas para as operações principais.
- Verificar os retornos das funções de arquivo.
- Fechar todos os arquivos abertos.
- Não utilizar vetores para armazenar todo o conteúdo do arquivo.
- Não utilizar `malloc()` ou `realloc()` para a leitura.
- Preservar o funcionamento da Etapa A após implementar a Etapa B.

### 11. Entrega

O aluno deverá entregar:

1. O código-fonte correspondente à Etapa A.
2. A versão evoluída do mesmo código-fonte, correspondente à Etapa B.
3. Um exemplo de `dados.txt` utilizado nos testes.

**Conceito principal:** um arquivo pode ser percorrido sequencialmente ou acessado a partir de uma posição específica. Em ambos os casos, a leitura deve respeitar o tamanho do buffer, a posição corrente e a quantidade de dados efetivamente disponível.