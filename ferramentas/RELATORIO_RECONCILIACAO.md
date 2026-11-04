# Primeira reconciliação documental — resultado

Base: `9e5d47e` (`main`, PR #29 integrada). Implementação inicial sujeita à revisão desta PR; futuras atualizações ordinárias de README/inventário têm autorização permanente nos limites registrados no AGENTS.

## Implementação

Um comando Python da biblioteca padrão separa descoberta/elegibilidade, geração do CSV, geração dos blocos do README e validação de links. Não há banco, segundo inventário, configuração de estados ou cadastro semântico. O Git é opcional e usado somente para relatar renomeações registradas como `R`, sem inferir identidade por nome ou hash. A reconciliação não depende dele nem da geração de catálogo.

A execução normal altera somente `inventario.csv` e blocos delimitados do README. `--check` não escreve e integra o workflow de GitHub Actions com permissões somente de leitura. Textos históricos e princípios editoriais permanecem fora dos blocos; a migração inicial preservou a explicação editorial e identificou o piloto V03-003 como registro histórico. Não são exigidas aprovações intermediárias de manutenção documental.

## Primeira execução real

| Indicador | Antes | Depois |
|---|---:|---:|
| Entradas do inventário | 255 | 280 |
| Capítulos representados | 12 | 13 |
| Materiais didáticos | 243 | 268 |
| Catálogos canônicos | 12 | 12 |

Adições: 24 arquivos do capítulo 13 e `12_Organizacao_Computadores/logica_circuito.png`. Nenhuma remoção nesta execução. O capítulo 13 ainda não tem catálogo canônico; experimentais fora do Git não foram promovidos. O ZIP é uma única entrada, sem indexar seus membros internos.

README: disponibilidades e contagens reais, capítulo 13, quatro papéis documentais na navegação (enunciados, respostas/orientações, implementações e pacotes), catalogação autônoma, consolidação existente e núcleo experimental do Motor 3. O fluxo incorpora a entrada de interpretação humana sem afirmar que sua finalização autônoma foi demonstrada. Estados dos contratos e capacidades declaradas pelo componente são expostos com suas fontes.

O Mermaid usa quebras explícitas de linha, dimensões de quebra configuradas e rótulos SVG em vez de caixas HTML. Mantém o caminho editorial e o mapa espacial independente, com 15 nós e links para as fontes. A retroalimentação retorna à camada responsável conforme o texto; não se confundem vínculos documentais com execução automática.

## Validações executadas

**22 testes aprovados**, com fixtures temporárias e sem alterações nos originais:

| Requisito | Evidência |
|---|---|
| Novo PNG | Inclusão, preservação de caixa/acentuação e atualização do índice |
| Novo capítulo | Descoberta e indicação de ausência de catálogo |
| Remoção/renomeação | Exclusão/adição bidirecional; correlação adicional com `R` do Git quando disponível |
| Catálogo canônico | Inclusão e extração de título por ZIP/XML |
| Derivados | Evidências PNG/MD, mapa JSON, relatório e experimental excluídos |
| Exercícios/gabaritos | Etapas e alternativa preservadas sem pareamento presumido |
| Links | Destinos, âncoras e links Mermaid inexistentes detectados |
| Idempotência | Bytes e `mtime` preservados em nova execução sem mudanças |
| Informação manual | Introdução, histórico e fontes preservados |
| Mudança contratual | Versão/estado alterados atualizam o README; FUTURO/PROPOSTO não promovidos |

Também foram verificados CSV inválido, duplicação/ordenação, marcadores ausentes, modo somente de verificação, papéis desconhecidos, cabeçalhos ilegíveis e links simbólicos. Os avisos de links quebrados no log da suíte pertencem às fixtures negativas; a reconciliação real terminou sem avisos e com zero links inválidos.

Verificações reais: 280 pares únicos, ordenados e com arquivos existentes; 12 catálogos; 24 entradas do capítulo 13 sem catálogo; ausência de mapas/evidências no índice. Duas execuções consecutivas preservaram bytes e datas de modificação dos documentos. Entre os 975 arquivos rastreados da base, somente AGENTS, README e inventário mudaram; os outros 972 permanecem byte a byte preservados, incluindo materiais, catálogos, contratos, motores, vocabulário e checklist.

Renderização local do diagrama com Mermaid, Puppeteer e Chromium: 15 nós, 15 links e nenhum rótulo fora da caixa; SVG sem `foreignObject`. Capturas em larguras de 1440 e 768 pixels examinadas visualmente. Ferramentas de renderização foram usadas somente na avaliação, fora do Git; não são dependências do reconciliador ou do CI. Evidências em `/workspace/artifacts/reconciliacao-documental/`: `arquitetura.svg`, capturas PNG, `validacao_visual.json`, `validacao.json` e `testes.log`.

## Limites e pendências

- Os cabeçalhos dos contratos ainda podem declarar PROPOSTO mesmo após integração de PRs. O README transcreve esse estado, sem reescrever contratos ou deduzir homologação. O contrato de entrega mantém uma referência à revisão como “a definir”, embora o protocolo exista; a navegação reconhece sua presença, sem corrigir o contrato fora deste escopo.
- Não há interpretação semântica geral de prosa. Mudanças de responsabilidade que não sejam expressas nos indicadores estruturados exigem análise documental do agente, conforme AGENTS; somente incertezas reais seguem para deliberação. Novos protocolos entram na tabela automaticamente, sem inventar dependências no diagrama.
- Arquivos de função incerta são informados sem bloquear registros independentes; não houve ambiguidade impeditiva na primeira execução real. Sem evidência `R` do Git, uma remoção/adição não é afirmada como identidade de renomeação.
- O CI fornece um check de divergência; sua exigência como proteção de branch depende da configuração administrativa no GitHub. O workflow não faz commits, alterações de PRs, push ou merge.
- A renderização local confirma a solução examinada, sem prometer identidade entre versões/temas do Mermaid da interface GitHub. A revisão visual humana da PR continua disponível.

Nenhuma decisão pedagógica, correção pendente, homologação semântica ou finalização audiovisual foi executada nesta etapa.
