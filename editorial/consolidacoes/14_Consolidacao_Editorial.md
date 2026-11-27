# 14 — Terminal I/O — Consolidação editorial

**Versão** 1.0 · proposta de consolidação pendente de deliberação humana.

**Fonte** [14_Dossie_Editorial.docx](../dossies/14_Dossie_Editorial.docx), versão 1.0.

**Escopo autorizado** investigação e consolidação de propostas do capítulo 14; preparação audiovisual conforme as dependências do workflow.

## Identidades provisórias

Cada linha identifica uma oportunidade pela ficha de origem, sem atribuição de novo ID. Os hooks alternativos estão nas próprias fichas.

| Candidato e seção do dossiê | Pergunta | Promessa |
|---|---|---|
| V14-001 — Quando o terminal esquece que está em vermelho? | Por que a mensagem seguinte herda a cor do aviso? | Prever o estilo da próxima escrita e saber quando emitir reset. |
| V14-002 — Progresso sem pilha de mensagens | Como informar progresso sem gerar uma linha para cada percentual? | Explicar retorno de carro, largura fixa e fflush(stdout) na mesma linha. |
| V14-003 — O personagem perdeu vida. Por que a tela inteira não mudou? | Como mudar HP e status sem redesenhar toda a interface? | Entender desenho inicial e atualização localizada de campos em coordenadas da tela. |
| V14-004 — Uma moldura de terminal é feita de texto | Como compor painéis a partir de operações simples sobre caracteres? | Reconhecer linhas, cantos e preenchimento como primitivas reutilizáveis em C. |
| V14-005 — Por que “poção” bagunça o alinhamento? | Por que medir bytes pode deslocar nomes com acentos numa tabela? | Distinguir tamanho em bytes, caracteres e largura em colunas. |

## Relações propostas

- **V14-002 e V14-003 — SOBREPOSICAO_PARCIAL.** Os dois apresentam indicadores dinâmicos. O primeiro demonstra reescrita de uma linha e descarga da saída. O segundo usa regiões endereçáveis para preservar dados estáticos enquanto muda HP e status.
- **V14-003 e V14-004 — SOBREPOSICAO_PARCIAL.** Ambos usam RPG. A variação de HP explica atualização após o desenho inicial. Os quadros que acrescentam painéis explicam composição e reutilização de primitivas. Combinar exige revisão autorizada do dossiê.
- **V14-001 e V14-004 — INDEPENDENTE.** A cor apoia a composição; a sequência de escritas do primeiro demonstra persistência e efeito do reset.
- **V14-004 e V14-005 — INDEPENDENTE.** Ambos apresentam Unicode. Um constrói contornos com glifos; o outro explica por que bytes e largura exibida diferem na tabulação.

## Deliberação e encaminhamento

**Fonte preferencial sugerida** V14-003, no dossiê 1.0, pelo contraste visível entre HP variável e áreas estáticas.

**Deliberação humana** pendente para propostas e relações. Todos os candidatos permanecem PROPOSTO.

**Encaminhamento para roteiro** sem autorização registrada. A continuidade exige indicação explícita do candidato e do dossiê 1.0 como fonte do roteiro. A montagem depende desse roteiro e das verificações de mídia e mapa.
