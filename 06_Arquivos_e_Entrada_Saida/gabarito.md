# 06 — Arquivos e Entrada/Saída
## Gabarito — Explorador de Arquivos em C

**Objetivo:** Implementar operações de gravação, leitura sequencial, posicionamento e leitura parcial de arquivos, utilizando as funções da biblioteca padrão de C.

## Etapa A — Gravação e leitura sequencial

### 1. Código-fonte

Arquivo: `explorador_a.c`

```c
#include <stdio.h>
#include <string.h>

#define TAM_BUFFER 128
#define NOME_ARQUIVO "dados.txt"

int AdicionarTexto(void);
int ExibirArquivo(void);
void LimparEntrada(void);

int main(void)
{
  int iOpcao;

  iOpcao = 0;

  do {
    printf("\n--- EXPLORADOR DE ARQUIVOS ---\n");
    printf("[1] - Adicionar texto ao arquivo\n");
    printf("[2] - Exibir conteudo do arquivo\n");
    printf("[3] - Encerrar\n");
    printf("Opcao: ");

    if (scanf("%d", &iOpcao) != 1) {
      printf("Opcao invalida.\n");
      LimparEntrada();
      iOpcao = 0;
      continue;
    }

    LimparEntrada();

    switch (iOpcao) {
      case 1:
        AdicionarTexto();
        break;

      case 2:
        ExibirArquivo();
        break;

      case 3:
        printf("Programa encerrado.\n");
        break;

      default:
        printf("Opcao invalida.\n");
        break;
    }

  } while (iOpcao != 3);

  return 0;
}

/* Acrescenta uma linha ao arquivo. */
int AdicionarTexto(void)
{
  FILE *pArquivo;
  char cBuffer[TAM_BUFFER];
  size_t nTamanho;

  printf("Digite o texto: ");

  if (fgets(cBuffer, sizeof(cBuffer), stdin) == NULL) {
    printf("Erro na leitura do texto.\n");
    return 0;
  }

  nTamanho = strlen(cBuffer);

  if (nTamanho > 0 && cBuffer[nTamanho - 1] == '\n') {
    cBuffer[nTamanho - 1] = 0;
  }
  else {
    /* Descarta caracteres excedentes da linha. */
    if (nTamanho == sizeof(cBuffer) - 1)
      LimparEntrada();
  }

  pArquivo = fopen(NOME_ARQUIVO, "a");

  if (pArquivo == NULL) {
    printf("Erro ao abrir o arquivo.\n");
    return 0;
  }

  if (fprintf(pArquivo, "%s\n", cBuffer) < 0) {
    printf("Erro ao gravar o arquivo.\n");
    fclose(pArquivo);
    return 0;
  }

  if (fclose(pArquivo) != 0) {
    printf("Erro ao finalizar a gravacao.\n");
    return 0;
  }

  printf("Texto gravado com sucesso.\n");

  return 1;
}

/* Percorre o arquivo sequencialmente. */
int ExibirArquivo(void)
{
  FILE *pArquivo;
  char cBuffer[TAM_BUFFER];
  int iEncontrouDados;

  pArquivo = fopen(NOME_ARQUIVO, "r");

  if (pArquivo == NULL) {
    printf("Arquivo inexistente ou indisponivel.\n");
    return 0;
  }

  iEncontrouDados = 0;

  printf("\n--- CONTEUDO ---\n");

  while (fgets(cBuffer, sizeof(cBuffer), pArquivo) != NULL) {
    iEncontrouDados = 1;
    printf("%s", cBuffer);
  }

  if (ferror(pArquivo)) {
    printf("\nErro durante a leitura.\n");
    fclose(pArquivo);
    return 0;
  }

  if (!iEncontrouDados)
    printf("Arquivo vazio.\n");

  if (fclose(pArquivo) != 0) {
    printf("Erro ao fechar o arquivo.\n");
    return 0;
  }

  return 1;
}

/* Descarta o restante da linha de entrada. */
void LimparEntrada(void)
{
  int iChar;

  while ((iChar = getchar()) != '\n' && iChar != EOF)
    ;
}
```

### 2. Compilação

```bash
gcc -std=c89 -Wall -Wextra -pedantic explorador_a.c -o explorador_a
./explorador_a
```

### 3. Pontos importantes da Etapa A

**Abertura para escrita**

```c
pArquivo = fopen(NOME_ARQUIVO, "a");
```

O modo `a` permite acrescentar conteúdo ao final do arquivo, preservando as informações existentes.

**Leitura sequencial**

```c
while (fgets(cBuffer, sizeof(cBuffer), pArquivo) != NULL) {
  printf("%s", cBuffer);
}
```

O programa lê sucessivos trechos do arquivo até alcançar o final.

Como `fgets` respeita o tamanho do buffer, arquivos maiores que 128 bytes podem ser exibidos em múltiplas leituras.

**Fechamento**

O programa verifica o retorno de `fclose`, inclusive após operações de escrita, pois uma falha pode ser identificada durante o fechamento.

---

## Etapa B — Posicionamento e leitura parcial

### 4. Evolução do programa

A Etapa B mantém as funções:

- `AdicionarTexto()`
- `ExibirArquivo()`
- `LimparEntrada()`

Serão acrescentadas:

- `LerTrecho()`
- `ConsultarTamanho()`

O programa continuará utilizando `dados.txt` e o buffer de 128 bytes.

### 5. Código-fonte completo

Arquivo: `explorador_b.c`

```c
#include <stdio.h>
#include <string.h>

#define TAM_BUFFER 128
#define NOME_ARQUIVO "dados.txt"

int AdicionarTexto(void);
int ExibirArquivo(void);
int LerTrecho(void);
int ConsultarTamanho(void);

void LimparEntrada(void);

int main(void)
{
  int iOpcao;

  iOpcao = 0;

  do {
    printf("\n--- EXPLORADOR DE ARQUIVOS ---\n");
    printf("[1] - Adicionar texto ao arquivo\n");
    printf("[2] - Exibir conteudo do arquivo\n");
    printf("[3] - Ler trecho por posicao\n");
    printf("[4] - Consultar tamanho do arquivo\n");
    printf("[5] - Encerrar\n");
    printf("Opcao: ");

    if (scanf("%d", &iOpcao) != 1) {
      printf("Opcao invalida.\n");
      LimparEntrada();
      iOpcao = 0;
      continue;
    }

    LimparEntrada();

    switch (iOpcao) {
      case 1:
        AdicionarTexto();
        break;

      case 2:
        ExibirArquivo();
        break;

      case 3:
        LerTrecho();
        break;

      case 4:
        ConsultarTamanho();
        break;

      case 5:
        printf("Programa encerrado.\n");
        break;

      default:
        printf("Opcao invalida.\n");
        break;
    }

  } while (iOpcao != 5);

  return 0;
}

/* Mantida da Etapa A. */
int AdicionarTexto(void)
{
  FILE *pArquivo;
  char cBuffer[TAM_BUFFER];
  size_t nTamanho;

  printf("Digite o texto: ");

  if (fgets(cBuffer, sizeof(cBuffer), stdin) == NULL) {
    printf("Erro na leitura do texto.\n");
    return 0;
  }

  nTamanho = strlen(cBuffer);

  if (nTamanho > 0 && cBuffer[nTamanho - 1] == '\n') {
    cBuffer[nTamanho - 1] = 0;
  }
  else {
    if (nTamanho == sizeof(cBuffer) - 1)
      LimparEntrada();
  }

  pArquivo = fopen(NOME_ARQUIVO, "a");

  if (pArquivo == NULL) {
    printf("Erro ao abrir o arquivo.\n");
    return 0;
  }

  if (fprintf(pArquivo, "%s\n", cBuffer) < 0) {
    printf("Erro ao gravar o arquivo.\n");
    fclose(pArquivo);
    return 0;
  }

  if (fclose(pArquivo) != 0) {
    printf("Erro ao finalizar a gravacao.\n");
    return 0;
  }

  printf("Texto gravado com sucesso.\n");

  return 1;
}

/* Mantida da Etapa A. */
int ExibirArquivo(void)
{
  FILE *pArquivo;
  char cBuffer[TAM_BUFFER];
  int iEncontrouDados;

  pArquivo = fopen(NOME_ARQUIVO, "r");

  if (pArquivo == NULL) {
    printf("Arquivo inexistente ou indisponivel.\n");
    return 0;
  }

  iEncontrouDados = 0;

  printf("\n--- CONTEUDO ---\n");

  while (fgets(cBuffer, sizeof(cBuffer), pArquivo) != NULL) {
    iEncontrouDados = 1;
    printf("%s", cBuffer);
  }

  if (ferror(pArquivo)) {
    printf("\nErro durante a leitura.\n");
    fclose(pArquivo);
    return 0;
  }

  if (!iEncontrouDados)
    printf("Arquivo vazio.\n");

  if (fclose(pArquivo) != 0) {
    printf("Erro ao fechar o arquivo.\n");
    return 0;
  }

  return 1;
}

/* Nova funcao: leitura por posicao. */
int LerTrecho(void)
{
  FILE *pArquivo;
  char cBuffer[TAM_BUFFER];
  long lPosicao;
  long lTamanhoArquivo;
  int iQuantidade;
  size_t nLidos;

  printf("Posicao inicial: ");

  if (scanf("%ld", &lPosicao) != 1) {
    printf("Posicao invalida.\n");
    LimparEntrada();
    return 0;
  }

  LimparEntrada();

  printf("Quantidade de bytes (1 a %d): ", TAM_BUFFER);

  if (scanf("%d", &iQuantidade) != 1) {
    printf("Quantidade invalida.\n");
    LimparEntrada();
    return 0;
  }

  LimparEntrada();

  if (lPosicao < 0) {
    printf("Posicao invalida.\n");
    return 0;
  }

  if (iQuantidade <= 0 || iQuantidade > TAM_BUFFER) {
    printf("Quantidade fora dos limites.\n");
    return 0;
  }

  pArquivo = fopen(NOME_ARQUIVO, "rb");

  if (pArquivo == NULL) {
    printf("Erro ao abrir o arquivo.\n");
    return 0;
  }

  if (fseek(pArquivo, 0, SEEK_END) != 0) {
    printf("Erro ao posicionar no final.\n");
    fclose(pArquivo);
    return 0;
  }

  lTamanhoArquivo = ftell(pArquivo);

  if (lTamanhoArquivo < 0) {
    printf("Erro ao consultar tamanho.\n");
    fclose(pArquivo);
    return 0;
  }

  if (lPosicao > lTamanhoArquivo) {
    printf("Posicao alem do final do arquivo.\n");
    fclose(pArquivo);
    return 0;
  }

  if (fseek(pArquivo, lPosicao, SEEK_SET) != 0) {
    printf("Erro ao posicionar no arquivo.\n");
    fclose(pArquivo);
    return 0;
  }

  nLidos = fread(cBuffer, 1, (size_t)iQuantidade, pArquivo);

  if (ferror(pArquivo)) {
    printf("Erro durante a leitura.\n");
    fclose(pArquivo);
    return 0;
  }

  printf("Bytes solicitados: %d\n", iQuantidade);
  printf("Bytes recuperados: %lu\n", (unsigned long)nLidos);

  printf("Conteudo: ");

  if (nLidos > 0)
    fwrite(cBuffer, 1, nLidos, stdout);

  printf("\n");

  if (fclose(pArquivo) != 0) {
    printf("Erro ao fechar o arquivo.\n");
    return 0;
  }

  return 1;
}

/* Nova funcao: consulta tamanho do arquivo. */
int ConsultarTamanho(void)
{
  FILE *pArquivo;
  long lTamanho;

  pArquivo = fopen(NOME_ARQUIVO, "rb");

  if (pArquivo == NULL) {
    printf("Erro ao abrir o arquivo.\n");
    return 0;
  }

  if (fseek(pArquivo, 0, SEEK_END) != 0) {
    printf("Erro ao posicionar no arquivo.\n");
    fclose(pArquivo);
    return 0;
  }

  lTamanho = ftell(pArquivo);

  if (lTamanho < 0) {
    printf("Erro ao obter tamanho.\n");
    fclose(pArquivo);
    return 0;
  }

  printf("Tamanho do arquivo: %ld bytes\n", lTamanho);

  if (fclose(pArquivo) != 0) {
    printf("Erro ao fechar o arquivo.\n");
    return 0;
  }

  return 1;
}

/* Mantida da Etapa A. */
void LimparEntrada(void)
{
  int iChar;

  while ((iChar = getchar()) != '\n' && iChar != EOF)
    ;
}
```

### 6. Compilação

```bash
gcc -std=c89 -Wall -Wextra -pedantic explorador_b.c -o explorador_b
./explorador_b
```

### 7. Pontos importantes da Etapa B

**Posicionamento**

```c
fseek(pArquivo, lPosicao, SEEK_SET);
```

A função posiciona o cursor de leitura no deslocamento solicitado, considerando o início do arquivo como referência.

**Consulta de tamanho**

```c
fseek(pArquivo, 0, SEEK_END);
lTamanhoArquivo = ftell(pArquivo);
```

Ao posicionar o cursor no final, podemos consultar o deslocamento correspondente ao tamanho do arquivo.

**Leitura parcial**

```c
nLidos = fread(cBuffer, 1, (size_t)iQuantidade, pArquivo);
```

O segundo argumento informa o tamanho de cada elemento, e o terceiro informa quantos elementos serão lidos.

Como cada elemento possui um byte, o retorno representa diretamente a quantidade de bytes recuperados.

**Exibição segura do conteúdo**

```c
fwrite(cBuffer, 1, nLidos, stdout);
```

Diferentemente de `fgets`, a função `fread` não acrescenta automaticamente um terminador de string.

Por isso, utilizamos `fwrite` para exibir exatamente os bytes recuperados, sem depender de um caractere zero no final do buffer.

### 8. Cenário de validação

Para validar os deslocamentos, crie um arquivo `dados.txt` contendo exatamente:

```text
ABCDEFGHIJ
```

Sem quebra de linha ao final.

Os resultados esperados são:

| Posição | Quantidade | Resultado | Bytes lidos |
|---|---:|---|---:|
| 0 | 4 | ABCD | 4 |
| 3 | 4 | DEFG | 4 |
| 7 | 5 | HIJ | 3 |
| 9 | 1 | J | 1 |
| 10 | 4 | Vazio | 0 |
| -1 | 3 | Posição inválida | — |
| 2 | 0 | Quantidade inválida | — |

O tamanho consultado deverá ser de 10 bytes.

### 9. Comparação entre as etapas

| Característica | Etapa A | Etapa B |
|---|---|---|
| Gravação em arquivo | Sim | Reutilizada |
| Leitura sequencial | Sim | Reutilizada |
| Buffer fixo | 128 bytes | 128 bytes |
| Posicionamento com fseek | Não | Sim |
| Consulta com ftell | Não | Sim |
| Leitura com fread | Não | Sim |
| Leitura parcial | Via fgets | Via fread |
| Persistência entre execuções | Sim | Sim |

### 10. Conclusão

O exercício demonstra duas maneiras de acessar informações persistidas em arquivos.

Na Etapa A, o programa percorre o conteúdo sequencialmente, utilizando as operações tradicionais de entrada e saída.

Na Etapa B, o programa passa a controlar a posição corrente e a quantidade de bytes recuperados, sem precisar carregar todo o arquivo na memória.

**Conceito principal:** o conteúdo de um arquivo pode ser acessado sequencialmente ou por deslocamento, desde que o programa respeite os limites do buffer, a posição corrente e os retornos das funções de leitura.

**Fim do módulo 06 — Arquivos e Entrada/Saída.**