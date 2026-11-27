# Terminal I/O — Autoauditoria do mapa espacial 0.1

**Estado** AUTOAUDITADO_COM_RESSALVAS. Lote parcial, sujeito a homologação humana. As regiões registradas são opções reutilizáveis de projeção, independentes de candidato, ordem e duração de montagem.

Foram mapeados cinco dos 43 materiais visuais do inventário, com seis regiões e 12 projeções inspecionadas. As oito fontes Markdown são documentais e ficam fora do mapa. Restam 38 mídias visuais sem regiões homologáveis neste lote. A cobertura parcial inclui cursor, preenchimento, coordenadas, composição e atualização localizada.

| Evidência | Regiões inspecionadas | Resultado |
|---|---|---|
| [Painel 1](painel-1.jpg) | Quatro quadros do painel RPG, incluindo mudanças de HP e status | A estrutura e as mensagens permanecem completas em todos os estados. |
| [Painel 2](painel-2.jpg) | Quatro quadros da composição de painéis | Os títulos do terceiro e quarto quadros ficam junto à borda no original. A região integral preserva os títulos e a sequência. |
| [Painel 3](painel-3.jpg) | Grade ampliada e vista integral das coordenadas, preenchimento e restauração do cursor | A caixa inicial da grade cortava a definição dos eixos e atingia conteúdo do painel abaixo. A nova caixa preserva título, grade e legenda. As vistas integrais densas servem de contexto, com legibilidade limitada para texto pequeno em 9:16. |

As projeções usaram o algoritmo de referência de [renderização dos recortes do capítulo 03](../../03_Operacoes_Bitwise/evidencias_mapa_espacial/renderizar.py), com originais do capítulo 14 e caixas normalizadas: conversão em pixels por arredondamento, ajuste proporcional Lanczos em 1080 × 1920 e fundo neutro. Os painéis apresentam reduções identificadas das projeções estáticas. Foram conferidos os binários, as dimensões e a integridade das regiões em todos os quadros dos dois GIFs deste lote. A classificação espacial preserva a ressalva semântica de cursor_restore.png sobre a posição da seta em relação ao código.

A cobertura deve ser ampliada antes de usar mídias sem região verificada. A aprovação das regiões, a escolha das mídias e a seleção de um candidato para roteiro permanecem sob decisão humana.
