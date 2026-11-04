# Gabarito — Uma possível implementação do Makefile

Este arquivo apresenta uma solução possível para a Etapa B do exercício de compilação.

O Makefile utiliza os mesmos arquivos C fornecidos no projeto-base e automatiza a compilação separada, a linkedição e o acompanhamento das dependências entre módulos.

## Makefile

```makefile
CC = gcc

CPPFLAGS = -Iinclude -MMD -MP
CFLAGS = -std=c89 -Wall -Wextra -pedantic -g -O0

SRC = src
OBJ = obj
BIN = bin

OBJS = $(OBJ)/main.o $(OBJ)/calc.o $(OBJ)/log.o
TARGET = $(BIN)/app

.PHONY: all clean

all: $(TARGET)

$(TARGET): $(OBJS) | $(BIN)
	$(CC) $(OBJS) -o $@

$(OBJ)/%.o: $(SRC)/%.c | $(OBJ)
	$(CC) $(CPPFLAGS) $(CFLAGS) -c $< -o $@

$(OBJ) $(BIN):
	mkdir -p $@

-include $(OBJS:.o=.d)

clean:
	rm -f $(OBJS) $(OBJS:.o=.d) $(TARGET)
```

## Como utilizar

Para construir o programa:

```bash
make
```

Para executar:

```bash
./bin/app
```

Para remover os arquivos gerados:

```bash
make clean
```

Para reconstruir o programa:

```bash
make
```

## Comportamento esperado

| Alteração realizada | Objetos recompilados |
|---|---|
| Primeira compilação | `main.o`, `calc.o`, `log.o` |
| Nenhuma alteração | Nenhum |
| `src/main.c` | `main.o` |
| `src/calc.c` | `calc.o` |
| `include/calc.h` | `main.o`, `calc.o` |

Sempre que um objeto for reconstruído, o executável também deverá ser vinculado novamente.

## Observações

- A regra `$(OBJ)/%.o: $(SRC)/%.c` permite utilizar uma única receita para compilar os três módulos.
- As opções `-MMD -MP` geram arquivos de dependência utilizados pela diretiva `-include`.
- As variáveis automáticas `$@` e `$<` evitam repetir os nomes dos arquivos nas receitas.
- A dependência de ordem `|` garante que os diretórios existam antes da compilação, sem provocar reconstruções desnecessárias.
- O alvo `clean` remove apenas os arquivos gerados, preservando os fontes e headers.

**Esta é uma solução de referência. Outras implementações são válidas desde que atendam aos requisitos e demonstrem corretamente a compilação incremental.**