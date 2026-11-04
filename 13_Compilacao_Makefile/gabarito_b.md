# 13 — Compilação e Makefile
## Gabarito — Etapa B: Automatização com GNU Make

### 1. Objetivo

Automatizar a compilação do projeto desenvolvido na Etapa A, utilizando um Makefile capaz de identificar quais módulos precisam ser reconstruídos após alterações nos arquivos-fonte ou nos headers.

O aluno deverá preservar os arquivos C fornecidos, substituindo os comandos manuais de compilação e linkedição por regras do GNU Make.

---

## 2. Estrutura esperada

```text
exercicio13/
├── Makefile
├── src/
│   ├── main.c
│   ├── calc.c
│   └── log.c
├── include/
│   ├── calc.h
│   └── log.h
├── obj/
│   ├── main.o
│   ├── calc.o
│   ├── log.o
│   ├── main.d
│   ├── calc.d
│   └── log.d
└── bin/
    └── app
```

Os arquivos `.o`, `.d` e o executável são produzidos automaticamente. Não devem ser fornecidos como parte do projeto-base.

---

## 3. Makefile — Solução de referência

**Arquivo:** `Makefile`

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

**Atenção:** os comandos das receitas devem começar com um caractere TAB, não com espaços.

---

## 4. Explicação das regras

### 4.1. Variáveis de configuração

```makefile
CC = gcc

CPPFLAGS = -Iinclude -MMD -MP
CFLAGS = -std=c89 -Wall -Wextra -pedantic -g -O0
```

- `CC`: define o compilador.
- `CPPFLAGS`: reúne opções relacionadas ao pré-processamento e à geração das dependências.
- `CFLAGS`: define as opções de compilação C.

As opções `-g -O0` preservam a configuração de depuração utilizada na Etapa A.

### 4.2. Regra principal

```makefile
all: $(TARGET)
```

O alvo `all` depende do executável. Para construí-lo, o Make verifica se suas dependências estão atualizadas.

### 4.3. Linkedição

```makefile
$(TARGET): $(OBJS) | $(BIN)
	$(CC) $(OBJS) -o $@
```

O executável depende dos três arquivos objeto.

Se algum objeto for atualizado, a linkedição deverá ser realizada novamente.

A variável automática `$@` representa o alvo, neste caso `bin/app`.

### 4.4. Compilação dos módulos

```makefile
$(OBJ)/%.o: $(SRC)/%.c | $(OBJ)
	$(CC) $(CPPFLAGS) $(CFLAGS) -c $< -o $@
```

A regra de padrão permite compilar diferentes arquivos utilizando a mesma receita.

Por exemplo:

- `src/main.c` produz `obj/main.o`.
- `src/calc.c` produz `obj/calc.o`.
- `src/log.c` produz `obj/log.o`.

A variável `$<` representa a primeira dependência, enquanto `$@` representa o arquivo que será produzido.

### 4.5. Criação dos diretórios

```makefile
$(OBJ) $(BIN):
	mkdir -p $@
```

Os diretórios são criados quando necessário.

O caractere `|`, utilizado nas regras anteriores, estabelece dependências de ordem.

Isso garante que os diretórios existam antes da execução das receitas, sem considerar alterações em seus timestamps como motivo para recompilar os objetos ou refazer a linkedição.

### 4.6. Dependências dos headers

```makefile
-include $(OBJS:.o=.d)
```

Durante a compilação, as opções `-MMD -MP` permitem gerar arquivos `.d` contendo as dependências de cada módulo.

Por exemplo, `obj/main.d` poderá conter:

```makefile
obj/main.o: src/main.c include/calc.h include/log.h

include/calc.h:
include/log.h:
```

Com essas informações, o Make poderá identificar que uma alteração em `calc.h` exige a recompilação de `main.o`.

O prefixo `-` em `-include` permite continuar mesmo quando os arquivos `.d` ainda não existem, como acontece na primeira compilação.

### 4.7. Limpeza

```makefile
clean:
	rm -f $(OBJS) $(OBJS:.o=.d) $(TARGET)
```

O alvo `clean` remove os arquivos objeto, os arquivos de dependência e o executável.

Os fontes e headers permanecem preservados.

---

## 5. Validação obrigatória

Os testes deverão ser realizados sequencialmente, a partir da raiz do projeto.

### Teste 1 — Compilação completa

```bash
make clean
make
```

**Esperado:**

- Compilação de `main.c`.
- Compilação de `calc.c`.
- Compilação de `log.c`.
- Linkedição de `bin/app`.

Total: três compilações e uma linkedição.

### Teste 2 — Nenhuma alteração

```bash
make
```

**Esperado:**

```text
make: Nothing to be done for 'all'.
```

Nenhum módulo deverá ser recompilado.

### Teste 3 — Alteração em main.c

Modifique somente a mensagem inicial do programa:

```c
vLog("Iniciando calculadora - teste");
```

Execute:

```bash
make
```

**Esperado:**

```text
gcc ... -c src/main.c -o obj/main.o
gcc obj/main.o obj/calc.o obj/log.o -o bin/app
```

Somente `main.o` deverá ser recompilado. A linkedição deverá ser refeita.

### Teste 4 — Alteração em calc.c

Acrescente um comentário em `src/calc.c` e execute:

```bash
make
```

**Esperado:**

```text
gcc ... -c src/calc.c -o obj/calc.o
gcc obj/main.o obj/calc.o obj/log.o -o bin/app
```

Somente `calc.o` deverá ser recompilado, seguido de nova linkedição.

### Teste 5 — Alteração em calc.h

Acrescente um comentário em `include/calc.h` e execute:

```bash
make
```

**Esperado:**

```text
gcc ... -c src/main.c -o obj/main.o
gcc ... -c src/calc.c -o obj/calc.o
gcc obj/main.o obj/calc.o obj/log.o -o bin/app
```

Nesse caso, dois módulos precisam ser recompilados, pois ambos dependem de `calc.h`.

O arquivo `log.o` não deverá ser reconstruído.

---

## 6. Critérios de avaliação

| Critério | Resultado esperado |
|---|---|
| Variáveis | Compilador, flags e diretórios configurados |
| Regras de padrão | Compilação dos três módulos |
| Variáveis automáticas | Utilização correta nas receitas |
| Linkedição | Executável produzido a partir dos objetos |
| Dependências | Headers acompanhados por arquivos `.d` |
| Diretórios | Criação automática quando necessária |
| Alvos auxiliares | `all`, `clean` e `.PHONY` |
| Compilação incremental | Apenas os objetos afetados são reconstruídos |
| Execução | Programa apresenta o resultado esperado |

### Considerações para o professor

1. **Não exigir uma solução textual idêntica.** Diferentes Makefiles podem satisfazer os mesmos requisitos.

2. **Aceitar a enumeração explícita dos objetos.** Não é obrigatório utilizar `wildcard` ou `patsubst`, pois o projeto possui apenas três módulos.

3. **Exigir a compilação incremental.** Um Makefile que recompila todos os arquivos a cada execução não atende ao objetivo principal.

4. **Verificar as dependências dos headers.** A simples presença de `-MMD -MP` não é suficiente se os arquivos `.d` não forem utilizados pelo Make.

5. **Distinguir recompilação de linkedição.** Alterar somente `main.c` exige reconstruir `main.o` e vincular novamente o executável, mas não exige recompilar `calc.c` ou `log.c`.

6. **Não exigir scripts auxiliares ou configurações multiplataforma.** O foco permanece na automatização da compilação e no controle das dependências.

---

## 7. Conclusão

A Etapa A demonstrou como construir manualmente um programa modular com GCC.

A Etapa B automatizou o mesmo processo, acrescentando o controle das dependências e a reconstrução seletiva dos arquivos.

**O aprendizado central é compreender que o Make não é apenas um executor de comandos de compilação: ele utiliza as relações entre alvos e dependências para decidir quais comandos precisam ser executados novamente.**