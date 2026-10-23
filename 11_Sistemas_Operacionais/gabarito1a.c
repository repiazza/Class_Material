#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <errno.h>

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

int main(void)
{
    int iOpcao;
    int iNumero;
    pid_t iPid;

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
        fflush(NULL); /* Evita duplicar buffers de saida no fork. */
        iPid = fork();
        if (iPid < 0) {
            perror("fork");
            continue;
        }
        if (iPid == 0) {
            if (!iRegistrarNumero(iNumero)) {
                fprintf(stderr, "[Filho %ld] Falha no log.\n", (long)getpid());
                _exit(1);
            }
            printf("[Filho %ld] Numero registrado: %d\n",
                   (long)getpid(), iNumero);
            fflush(stdout);
            _exit(0);
        }
        printf("[Pai] Processo filho criado: %ld\n", (long)iPid);
        iAguardarFilho(iPid);
    }
    return 0;
}
