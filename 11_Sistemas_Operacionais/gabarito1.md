A ideia é que o aluno consiga comparar os códigos e perceber que a principal evolução está no mecanismo de comunicação, não na organização geral do programa.

Vou manter C com ponteiros explícitos, variáveis em notação húngara, fork(), waitpid() e tratamento dos retornos. Para que o gabarito seja executável isoladamente, utilizarei uma pequena função de registro com fopen() e fprintf(), que poderá ser substituída pelo módulo de log já desenvolvido pelo aluno.
Parte A — Criação de processos e herança de memória
Nesta primeira implementação, o número é informado antes de fork(). O filho herda o valor e o registra no arquivo numeros.log.

Pai: menu e leitura do número
			|
            \/
fork() — filho herda o valor
			|
            \/
Pai           Filho
waitpid()     Registra e encerra
			|
            \/
Pai retorna ao menu

O que a Parte B acrescenta
A segunda versão preserva o menu e a lógica de criação e espera do filho. Acrescenta duas funções auxiliares, iEscreverTudo() e iLerTudo(), para lidar com transferências parciais e interrupções por sinais.

Também utiliza uma resposta interna ER quando o registro falha, evitando que o pai interprete uma operação malsucedida como OK.

Um detalhe importante para a correção do exercício: a ordem das mensagens exibidas pelo pai e pelo filho pode variar, porque são processos escalonados independentemente. O comportamento correto deve ser avaliado pela transferência dos dados, confirmação e término, não por uma ordem rígida das mensagens no terminal.