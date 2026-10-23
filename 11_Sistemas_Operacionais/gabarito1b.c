#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <errno.h>
#include <signal.h>

static int iRegistrarNumero(int iNumero)
{
    FILE *pArquivo;
    int iErro;

    pArquivo = fopen("numeros.log", "a");
    if (pArquivo == NULL)
        return 0;

    iErro = (fprintf(pArquivo, "PID=%ld Numero=%d\n",
                     (long)getpid(), iNumero) < 0);
    if (fclose(pArquivo) != 0)
        iErro = 1;
    return !iErro;
}

/* Retorna 1 apenas quando todos os bytes forem transferidos. */
static int iEscreverTudo(int iFd, const void *pDados, size_t iTamanho)
{
    const unsigned char *pWork = (const unsigned char *)pDados;
    ssize_t iRetorno;

    while (iTamanho > 0) {
        iRetorno = write(iFd, pWork, iTamanho);
        if (iRetorno < 0 && errno == EINTR)
            continue;
        if (iRetorno <= 0)
            return 0;
        pWork += iRetorno;
        iTamanho -= (size_t)iRetorno;
    }
    return 1;
}

static int iLerTudo(int iFd, void *pDados, size_t iTamanho)
{
    unsigned char *pWork = (unsigned char *)pDados;
    ssize_t iRetorno;

    while (iTamanho > 0) {
        iRetorno = read(iFd, pWork, iTamanho);
        if (iRetorno < 0 && errno == EINTR)
            continue;
        if (iRetorno <= 0)
            return 0;
        pWork += iRetorno;
        iTamanho -= (size_t)iRetorno;
    }
    return 1;
}

static int iAguardarFilho(pid_t iPid)
{
    int iStatus;
    pid_t iRetorno;

    do {
        iRetorno = waitpid(iPid, &iStatus, 0);
    } while (iRetorno < 0 && errno == EINTR);
    if (iRetorno < 0) {
        perror("waitpid");
        return 0;
    }
    if (!WIFEXITED(iStatus) || WEXITSTATUS(iStatus) != 0) {
        fprintf(stderr, "[Pai] Filho terminou com falha.\n");
        return 0;
    }
    printf("[Pai] Filho finalizado.\n");
    return 1;
}

static void vExecutarFilho(int aiPaiFilho[2], int aiFilhoPai[2])
{
    int iNumero = 0; /* Nao utilizar o numero herdado do pai. */
    int iSucesso;
    const char *szResposta;

    close(aiPaiFilho[1]);
    close(aiFilhoPai[0]);

    iSucesso = iLerTudo(aiPaiFilho[0], &iNumero, sizeof(iNumero));
    close(aiPaiFilho[0]);
    if (!iSucesso) {
        fprintf(stderr, "[Filho] Falha ao receber numero.\n");
        close(aiFilhoPai[1]);
        _exit(1);
    }

    printf("[Filho %ld] Numero recebido: %d\n",
           (long)getpid(), iNumero);
    fflush(stdout);

    iSucesso = iRegistrarNumero(iNumero);
    szResposta = iSucesso ? "OK" : "ER";
    if (iSucesso) {
        printf("[Filho %ld] Registro realizado.\n", (long)getpid());
        fflush(stdout);
    } else {
        fprintf(stderr, "[Filho] Falha no registro.\n");
    }

    if (!iEscreverTudo(aiFilhoPai[1], szResposta, 2))
        iSucesso = 0;
    close(aiFilhoPai[1]);
    _exit(iSucesso ? 0 : 1);
}

static void vProcessarNumero(int iNumero)
{
    int aiPaiFilho[2];
    int aiFilhoPai[2];
    char szResposta[3] = {0, 0, 0};
    int iEnviou;
    int iRecebeu;
    int iTerminou;
    pid_t iPid;

    if (pipe(aiPaiFilho) < 0) {
        perror("pipe pai-filho");
        return;
    }
    if (pipe(aiFilhoPai) < 0) {
        perror("pipe filho-pai");
        close(aiPaiFilho[0]);
        close(aiPaiFilho[1]);
        return;
    }

    fflush(NULL);
    iPid = fork();
    if (iPid < 0) {
        perror("fork");
        close(aiPaiFilho[0]);
        close(aiPaiFilho[1]);
        close(aiFilhoPai[0]);
        close(aiFilhoPai[1]);
        return;
    }
    if (iPid == 0)
        vExecutarFilho(aiPaiFilho, aiFilhoPai);

    close(aiPaiFilho[0]);
    close(aiFilhoPai[1]);
    printf("[Pai] Processo filho criado: %ld\n", (long)iPid);

    iEnviou = iEscreverTudo(aiPaiFilho[1], &iNumero, sizeof(iNumero));
    close(aiPaiFilho[1]);
    if (iEnviou)
        printf("[Pai] Numero enviado: %d\n", iNumero);
    else
        fprintf(stderr, "[Pai] Falha ao enviar numero.\n");

    iRecebeu = iLerTudo(aiFilhoPai[0], szResposta, 2);
    close(aiFilhoPai[0]);
    iTerminou = iAguardarFilho(iPid);

    if (iEnviou && iRecebeu && iTerminou &&
        szResposta[0] == 'O' && szResposta[1] == 'K')
        printf("[Pai] Resposta recebida: OK\n");
    else
        fprintf(stderr, "[Pai] Operacao nao confirmada.\n");
}

int main(void)
{
    int iOpcao;
    int iNumero;

    /* Evita encerramento por SIGPIPE se o leitor fechar o pipe. */
    if (signal(SIGPIPE, SIG_IGN) == SIG_ERR) {
        perror("signal");
        return 1;
    }

    for (;;) {
        printf("\n[1] Informar numero\n[2] Encerrar\nOpcao: ");
        fflush(stdout);
        if (scanf("%d", &iOpcao) != 1) {
            fprintf(stderr, "Entrada invalida.\n");
            return 1;
        }
        if (iOpcao == 2)
            break;
        if (iOpcao != 1) {
            printf("Opcao invalida.\n");
            continue;
        }
        printf("Numero: ");
        fflush(stdout);
        if (scanf("%d", &iNumero) != 1) {
            fprintf(stderr, "Numero invalido.\n");
            return 1;
        }
        vProcessarNumero(iNumero);
    }
    return 0;
}
