
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

int main(int argc, char *argv[])
{
    STRUCT_CONFIG stConfig;
    int iResultado;

    memset(&stConfig, 0, sizeof(stConfig));

    if (argc != 4)
    {
        printf("Uso: %s <operacao> <valor1> <valor2>\n",
               argv[0]);
        return 1;
    }

    if (strcmp(argv[1], "soma") != 0 &&
        strcmp(argv[1], "subtrai") != 0)
    {
        printf("Erro: operacao desconhecida: %s\n",
               argv[1]);
        return 1;
    }

    if (!iConverterValor(argv[2], &stConfig.iValor1))
    {
        printf("Erro: valor1 invalido: %s\n", argv[2]);
        return 1;
    }

    if (!iConverterValor(argv[3], &stConfig.iValor2))
    {
        printf("Erro: valor2 invalido: %s\n", argv[3]);
        return 1;
    }

    strcpy(stConfig.szOperacao, argv[1]);

    if (strcmp(stConfig.szOperacao, "soma") == 0)
        iResultado = stConfig.iValor1 + stConfig.iValor2;
    else
        iResultado = stConfig.iValor1 - stConfig.iValor2;

    printf("Resultado: %d\n", iResultado);

    return 0;
}

Compilacao e testes

gcc -Wall -Wextra -std=c89 calc.c -o calc

./calc soma 3 10
# Resultado: 13

./calc subtrai 3 10
# Resultado: -7

./calc soma 100000 100000
# Resultado: 200000

./calc soma 3 10abc
# Erro: valor2 invalido: 10abc

./calc multiplica 3 10
# Erro: operacao desconhecida: multiplica

Pontos importantes do gabarito
Trecho	Conceito demonstrado
argc != 4	Contrato de quantidade de argumentos
strcmp()	Comparação do conteúdo das strings
strtol()	Conversão numérica verificável
pEnd == pszTexto	Nenhum caractere numérico convertido
*pEnd != 0	Caracteres restantes após a conversão
errno == ERANGE	Valor fora da capacidade de representação de long
lValor < 0 ou > 100000	Restrição definida pelo exercício
STRUCT_CONFIG	Armazenamento da configuração validada
iResultado	Estado produzido pelo processamento, separado da configuração

Um detalhe importante: usamos strcpy() somente depois de confirmar que a operação é exatamente "soma" ou "subtrai". Portanto, neste caso, sabemos que o texto cabe em szOperacao[16].

Também vale observar que strtol() aceita algumas representações que podem surpreender, como +10 e espaços iniciais. Isso não viola o enunciado atual, mas pode render uma discussão posterior sobre validar um número versus impor uma sintaxe textual específica.

Compreender porque argc é 4, depois a validação de argv[2] e argv[3] e, finalmente, se manteve a STRUCT_CONFIG restrita aos parâmetros da execução. Esses são os três objetivos centrais do exercício.