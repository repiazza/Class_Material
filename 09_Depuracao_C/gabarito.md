# Gabarito 09 — Investigando uma Falha de Segmentação

**Módulo:** 09 — Depuração em C  
**Exercício:** Investigando uma Falha de Segmentação  
**Linguagem:** ANSI C89  
**Ferramenta:** GDB

## 1. Compilação

**Comando esperado:**

```bash
gcc -g -O0 main.c -o programa
```

**Raciocínio esperado:**

- `-g` inclui informações de depuração.
- `-O0` desabilita otimizações que poderiam dificultar a correspondência entre o código-fonte e a execução.

## 2. Investigação com GDB

**Exemplo de sequência de comandos:**

```gdb
gdb ./programa

break main
break vProcessar
break vExibirItem

run
next
step
continue

backtrace
frame 0
print pItem
frame 1
print pItem
frame 2
print pItem
```

Os comandos devem ser utilizados conforme o estado da execução. A sequência apresentada é ilustrativa, não uma lista para execução ininterrupta.

**Raciocínio esperado:**

O aluno deve compreender que:

- `break` estabelece pontos de parada.
- `run` inicia a execução.
- `next` avança sem entrar nas chamadas de funções.
- `step` permite entrar nas funções chamadas.
- `continue` prossegue até outra parada ou evento.
- `backtrace` apresenta a pilha de chamadas.
- `frame` seleciona um contexto da pilha.
- `print` permite inspecionar expressões e variáveis.

## 3. Diagnóstico da falha

**Função responsável pela falha:**

`vExibirItem()`

**Instrução problemática:**

```c
printf("Valor: %d\n", pItem->iValor);
```

**Valor do ponteiro:**

```text
pItem = NULL
```

**Pilha de chamadas esperada:**

```text
#0 vExibirItem(pItem=0x0)
#1 vProcessar(pItem=0x0)
#2 main()
```

A apresentação exata dos endereços e argumentos depende do compilador e do ambiente.

**Causa:**

O ponteiro é inicializado com `NULL` em `main()` e transmitido pelas funções sem validação.

Ao executar `pItem->iValor`, o programa tenta acessar um membro de uma estrutura por meio de um ponteiro nulo.

Esse acesso possui **comportamento indefinido** em C e, no ambiente proposto, provoca uma falha de segmentação (`SIGSEGV`).

**Raciocínio esperado:**

O aluno deve distinguir a instrução em que a falha se manifesta da origem do valor inválido.

O `backtrace` demonstra o caminho percorrido, enquanto `frame` e `print` permitem verificar que o ponteiro já estava nulo nas chamadas anteriores.

## 4. Correção

Uma solução válida consiste em verificar o ponteiro antes de acessar a estrutura.

**Exemplo de correção:**

```c
void vExibirItem(PSTRUCT_ITEM pItem)
{
    if(pItem == NULL)
    {
        printf("Item invalido.\n");
        return;
    }

    printf("Valor: %d\n", pItem->iValor);
}
```

**Resultado esperado com o programa original:**

```text
Item invalido.
```

O programa deverá terminar normalmente, sem provocar a falha.

**Raciocínio esperado:**

A validação impede o acesso a um objeto inexistente.

Também é válida uma solução que inicialize uma estrutura real em `main()` e transmita seu endereço, desde que o aluno demonstre que compreendeu a causa do problema.

## 5. Validação

Após a correção, o aluno deverá:

1. Recompilar o programa.
2. Executá-lo novamente no GDB.
3. Confirmar que não ocorre `SIGSEGV`.
4. Verificar que a execução termina normalmente.

**Resultado esperado:** encerramento normal do programa, com código de saída `0`.

## 6. Orientações para avaliação

Verificar se o aluno:

- Compilou utilizando informações de depuração.
- Utilizou breakpoints para acompanhar o fluxo.
- Diferenciou `next` de `step`.
- Identificou a instrução que provoca a falha.
- Utilizou `backtrace` para reconstruir a sequência de chamadas.
- Utilizou `frame` e `print` para investigar o ponteiro.
- Explicou corretamente o acesso inválido.
- Corrigiu e validou o programa.

**Erros que merecem atenção:**

- Corrigir o programa sem demonstrar a investigação.
- Confundir a origem do ponteiro nulo com o local da falha.
- Interpretar `NULL` como uma estrutura válida contendo valores zerados.
- Considerar que `backtrace` identifica automaticamente a causa do erro.
- Modificar o código sem recompilar antes da validação.

## 7. Conclusão esperada

O aluno deve compreender que **o GDB permite investigar não apenas onde um programa falhou, mas também o estado das variáveis e a sequência de chamadas que conduziu à falha**.

A principal competência avaliada é a capacidade de utilizar evidências obtidas durante a depuração para formular um diagnóstico, realizar uma correção e validar seu resultado.