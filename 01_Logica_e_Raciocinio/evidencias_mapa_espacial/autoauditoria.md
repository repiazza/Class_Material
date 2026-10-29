# Autoauditoria do mapa espacial — capítulo 01

**Estado:** AUTOAUDITADO_COM_RESSALVAS. **Homologação humana: PENDENTE.** Aprovação na autoauditoria significa preservação do enquadramento inspecionado; não homologa conceitos das fontes nem a futura montagem.

## Escopo, fontes e preservação

Base: main cdb7036. Fontes lidas: AGENTS.md, protocolo_mapeamento_espacial.md, protocolo_retroalimentacao.md, inventario.csv, catálogo semântico 01 completo (14 registros e glossário), checklist histórico e os 12 originais visuais do capítulo. Foram abertas as oito imagens originais em resolução de inspeção e todos os 14 quadros dos quatro GIFs. Não se auditou o acervo geral, os exercícios ou outros capítulos. Não se usaram coordenadas antigas, Alpha 4 ou capítulo 02 como geometria.

A entrega abrange o capítulo, incluindo lógica booleana, conectivos, combinações, árvore, problema contextual, definição de proposições, conjunção intermediária e expressão final. Cada arquivo mantém região integral, além de painéis e cartões completos quando separáveis. Tabelas não foram divididas em linhas isoladas; operandos, setas, resultados e legendas permaneceram juntos. A divisão preserva contexto e não define seleção ou ordem audiovisual.

## Procedimento executado e cobertura

1. Identificação visual das unidades e confronto com os registros semânticos.
2. Caixas primárias abrangentes, com margens de segurança de quatro pixels além da caixa refinada quando o limite do original permitia.
3. Redução conservadora apenas dessas faixas externas; não se buscou a menor caixa possível. Os pares primária/final constam na tabela por região.
4. Serialização do JSON e renderização de cada região a partir do JSON reaberto, não de caixas transitórias.
5. Inspeção dos 32 painéis renderizados, confronto com originais e ampliações individuais dirigidas: tabela_final, construcao_expressao, conclusao da conjunção e operação XOR. Não se afirma leitura minuciosa de textos pequenos só pela miniatura.
6. Consolidação das ressalvas; verificação técnica independente dos limites, hashes e pixels da projeção.

Algoritmo de referência: bbox normalizada → round(coordenada × dimensão) em pixels; limite direito/inferior exclusivo; recorte do original RGB; fator único min(1080/largura, 1920/altura); dimensões redimensionadas arredondadas ao pixel mais próximo; Lanczos; centralização em 1080×1920 com fundo RGB (22,22,22). Sem preenchimento por esticamento e sem clipping adicional. O arredondamento da rasterização é de até meio pixel por dimensão. Futura montagem deve adotar o mesmo algoritmo para reproduzir estas evidências.

- **12 arquivos visuais:** oito PNGs e quatro GIFs.
- **74 regiões:** 66 em PNGs e oito em GIFs.
- **94 projeções finais inspecionadas:** 66 estáticas e 28 de GIFs, cobrindo cada estado de cada região.
- **32 painéis** identificados, com projeções reduzidas a 540×960 para navegação; PNGs individuais em 1080×1920 para revisão detalhada.
- Resultado: **33 aprovadas na autoauditoria, 41 com ressalvas e 0 pendentes de inspeção/correção geométrica**. As decisões pedagógicas históricas continuam pendentes conforme checklist.

Não foi encontrado defeito G impeditivo nos resultados renderizados que exigisse nova rodada de alteração das caixas. Houve apenas o refinamento conservador primária→final registrado; portanto, não há comparação antes/depois de defeito corrigido a alegar. Fragmentos adjacentes aceitáveis foram mantidos como V, sem otimização compulsiva.

## GIFs — cobertura real

Todos os quadros originais foram inspecionados nas folhas de estados. O estado final do AND foi aberto também em resolução original. Cada um dos mesmos quadros foi renderizado e inspecionado para as duas regiões (integral e operacao_completa), sem amostragem parcial dos estados:

| Arquivo / registro | Quadros, índice zero | Sequência observada | Duração do arquivo | Projeções |
|---|---|---|---|---|
| not_p.gif / 04 | 0–1 | P→R: 0→1; 1→0 | 3.000 ms/quadro; 6 s nominais por ciclo | 4 |
| p_and_q.gif / 05 | 0–3 | P,Q→R: 00→0; 01→0; 10→0; 11→1 | 3.000 ms/quadro; 12 s nominais por ciclo | 8 |
| p_or_q.gif / 06 | 0–3 | 00→0; 01→1; 10→1; 11→1 | 3.000 ms/quadro; 12 s nominais por ciclo | 8 |
| p_xor_q.gif / 07 | 0–3 | 00→0; 01→1; 10→1; 11→0 | 3.000 ms/quadro; 12 s nominais por ciclo | 8 |

As durações são metadados efetivamente lidos, não duração prescrita para cenas. Os GIFs apresentam diagramas, não tabelas tabulares. As regiões internas mantêm regra, entradas, operador, saída, cálculo e explicação do estado. A identificação do operador continua visível mesmo sem o cabeçalho global. A inspeção cobriu os estados discretos e sua ordem; não foi produzido ou assistido vídeo, nem ensaiado sincronismo de áudio, transições ou temporização de reprodução contínua. Não há homologação audiovisual implícita.

## Retroalimentação: preservar a origem das ocorrências

Os problemas encontrados já têm identificadores no checklist. Este relatório vincula regiões a esses registros, sem criar cadastro paralelo ou modificar decisões. O checklist não foi editado: é também arquivo da PR #15, cuja preservação integral foi expressamente exigida nesta tarefa.

| Classe | Evidência e registro existente | Encaminhamento / efeito espacial |
|---|---|---|
| P | problemas_condicoes4.png: segundo exemplo NOT diz “é falso” enquanto mostra p=F/¬p=V (M01-01); resumo usa “Quando inverte o valor da proposição” como critério de verdade (M01-02). | Fonte intacta; decisões/autorização do checklist preservadas. integral/not_contextual/resumo mantêm o conteúdo real, com ressalva de fonte; não usar isso como validação pedagógica. |
| P | problemas_condicoes4.png: p muda de significado na coluna OR (M01-03). | Preservar os rótulos locais; não transpor p entre os painéis como se representasse sempre chuva. Ressalva em integral/or_contextual. |
| P/contexto | r é resultado no problema contextual e variável livre na contagem; expressões “4 valores”/“8 valores” em logica_booleana3.png (M01-04/05). | Não renomear a fonte; descrever as regiões como combinações. Evitar equivalência entre três entradas independentes e uma saída derivada. |
| P/limite do modelo | Chuva e guarda-chuva usam modelo simplificado (M01-06); apresentação de 1/0 e estados físicos na lógica booleana (M01-07). | Manter ressalvas históricas. O mapa não converte o modelo simplificado em garantia física nem confunde representação e conceito. |
| V | Visões integrais, tabelas largas, margens e pequenos fragmentos de painéis vizinhos. | Aceitáveis para preservar unidades; não constituem bloqueio geométrico nem exigem nova caixa só por estética. |
| G | Nenhum corte impeditivo, distorção ou perda de relação demonstrado após a inspeção das projeções finais. | Sem correção artificial ou nova rodada desnecessária. |
| D | Não foi demonstrada nova troca objetiva de arquivos ou descrição que exija correção documental nesta tarefa. | Catálogo preservado; a inspeção não autoriza reescrever seus registros. |

A ressalva P é do original; não transforma um recorte íntegro em G. As regiões com P permanecem no acervo inclusivo e não são automaticamente liberadas para uso pedagógico. Após eventual edição autorizada da fonte: recalcular hash, conferir dimensões/caixas e renderizar/reinspecionar somente as regiões e estados efetivamente afetados. Não regenerar todo o capítulo por padrão.

## Continuidade da PR #15

A branch audiovisual/piloto-v01-003 permanece no commit 05f67b2, sem novo commit ou edição dos seus arquivos. Este mapa foi criado em branch independente a partir de main; não inclui os arquivos de preparação da PR #15. Os cinco takes e 70 segundos estimados não foram modificados, copiados para novo plano ou executados. Nenhuma seleção de regiões para o vídeo foi persistida.

Depois da aprovação e integração humana deste mapa, a montagem poderá resolver os IDs adequados nos quatro materiais já referenciados pelo roteiro (problema_condicoes.png; problemas_condicoes2.png; problemas_condicoes3.png; problemas_condicoes5.png). O mapa já oferece regiões de pergunta, proposições, conjunção, tabela final e interpretação dos cenários, mas não escolhe quais entrarão no vídeo. O plano pendente será retomado, não regenerado. Nenhum MP4, áudio ou SRT foi criado nesta etapa.

## Painéis finais

Abra os PNGs vinculados na tabela para resolução completa. Os painéis são folhas de navegação; sua ordem não determina uma sequência pedagógica.

- [Painel 01](painel-01.jpg)
- [Painel 02](painel-02.jpg)
- [Painel 03](painel-03.jpg)
- [Painel 04](painel-04.jpg)
- [Painel 05](painel-05.jpg)
- [Painel 06](painel-06.jpg)
- [Painel 07](painel-07.jpg)
- [Painel 08](painel-08.jpg)
- [Painel 09](painel-09.jpg)
- [Painel 10](painel-10.jpg)
- [Painel 11](painel-11.jpg)
- [Painel 12](painel-12.jpg)
- [Painel 13](painel-13.jpg)
- [Painel 14](painel-14.jpg)
- [Painel 15](painel-15.jpg)
- [Painel 16](painel-16.jpg)
- [Painel 17](painel-17.jpg)
- [Painel 18](painel-18.jpg)
- [Painel 19](painel-19.jpg)
- [Painel 20](painel-20.jpg)
- [Painel 21](painel-21.jpg)
- [Painel 22](painel-22.jpg)
- [Painel 23](painel-23.jpg)
- [Painel 24](painel-24.jpg)
- [Painel 25](painel-25.jpg)
- [Painel 26](painel-26.jpg)
- [Painel 27](painel-27.jpg)
- [Painel 28](painel-28.jpg)
- [Painel 29](painel-29.jpg)
- [Painel 30](painel-30.jpg)
- [Painel 31](painel-31.jpg)
- [Painel 32](painel-32.jpg)

## Registro por região e evidências

Coordenadas pixel [x0,y0,x1,y1), com canto superior esquerdo como origem. O quadro completo inclui cabeçalhos globais; painéis isolados mantêm seus cabeçalhos locais e contexto próprio. Cartões individuais se apoiam no contexto do painel conjunto, também disponível.

| Arquivo / ID / registro do catálogo | Primária → final (px) | Resultado / ressalva | Projeções finais |
|---|---|---|---|
| logica_booleana.png / `integral` / 01 | [0, 0, 1312, 1199] → [0, 0, 1312, 1199] | **Aprovada com ressalva**. V: visão de contexto íntegra, com texto reduzido; não promete leitura detalhada de todos os painéis. P de origem: consultar M01-07; representação binária e implementação física não se confundem com a definição abstrata de lógica booleana. | [f0](logica_booleana_png__integral__f00.png) |
| logica_booleana.png / `representacao_vf_10` / 01 | [0, 130, 457, 633] → [2, 134, 453, 629] | **Aprovada na autoauditoria**. Título local, textos, bordas, fórmulas e relações presentes preservados; nenhum defeito geométrico impeditivo identificado. | [f0](logica_booleana_png__representacao_vf_10__f00.png) |
| logica_booleana.png / `problema_expressao` / 01 | [450, 130, 897, 633] → [454, 134, 893, 629] | **Aprovada na autoauditoria**. Título local, textos, bordas, fórmulas e relações presentes preservados; nenhum defeito geométrico impeditivo identificado. | [f0](logica_booleana_png__problema_expressao__f00.png) |
| logica_booleana.png / `tabela_vf` / 01 | [891, 130, 1312, 633] → [895, 134, 1311, 629] | **Aprovada na autoauditoria**. Título local, textos, bordas, fórmulas e relações presentes preservados; nenhum defeito geométrico impeditivo identificado. | [f0](logica_booleana_png__tabela_vf__f00.png) |
| logica_booleana.png / `tabela_10` / 01 | [0, 627, 506, 1178] → [2, 631, 502, 1174] | **Aprovada na autoauditoria**. Título local, textos, bordas, fórmulas e relações presentes preservados; nenhum defeito geométrico impeditivo identificado. | [f0](logica_booleana_png__tabela_10__f00.png) |
| logica_booleana.png / `definicao_boole` / 01 | [500, 627, 911, 1178] → [504, 631, 907, 1174] | **Aprovada com ressalva**. P de origem: consultar M01-07; representação binária e implementação física não se confundem com a definição abstrata de lógica booleana. | [f0](logica_booleana_png__definicao_boole__f00.png) |
| logica_booleana.png / `conclusao` / 01 | [904, 627, 1312, 1178] → [908, 631, 1311, 1174] | **Aprovada na autoauditoria**. Título local, textos, bordas, fórmulas e relações presentes preservados; nenhum defeito geométrico impeditivo identificado. | [f0](logica_booleana_png__conclusao__f00.png) |
| logica_booleana2.png / `integral` / 02 | [0, 0, 1312, 1199] → [0, 0, 1312, 1199] | **Aprovada com ressalva**. V: visão de contexto íntegra, com texto reduzido; não promete leitura detalhada de todos os painéis. | [f0](logica_booleana2_png__integral__f00.png) |
| logica_booleana2.png / `not` / 02 | [0, 118, 444, 834] → [2, 122, 440, 830] | **Aprovada na autoauditoria**. Título local, textos, bordas, fórmulas e relações presentes preservados; nenhum defeito geométrico impeditivo identificado. | [f0](logica_booleana2_png__not__f00.png) |
| logica_booleana2.png / `and` / 02 | [437, 118, 879, 834] → [441, 122, 875, 830] | **Aprovada na autoauditoria**. Título local, textos, bordas, fórmulas e relações presentes preservados; nenhum defeito geométrico impeditivo identificado. | [f0](logica_booleana2_png__and__f00.png) |
| logica_booleana2.png / `or` / 02 | [872, 118, 1312, 834] → [876, 122, 1311, 830] | **Aprovada na autoauditoria**. Título local, textos, bordas, fórmulas e relações presentes preservados; nenhum defeito geométrico impeditivo identificado. | [f0](logica_booleana2_png__or__f00.png) |
| logica_booleana2.png / `tamanhos_tabelas` / 02 | [0, 827, 505, 1198] → [2, 831, 501, 1194] | **Aprovada na autoauditoria**. Título local, textos, bordas, fórmulas e relações presentes preservados; nenhum defeito geométrico impeditivo identificado. | [f0](logica_booleana2_png__tamanhos_tabelas__f00.png) |
| logica_booleana2.png / `resumo_conectivos` / 02 | [498, 827, 936, 1198] → [502, 831, 932, 1194] | **Aprovada na autoauditoria**. Título local, textos, bordas, fórmulas e relações presentes preservados; nenhum defeito geométrico impeditivo identificado. | [f0](logica_booleana2_png__resumo_conectivos__f00.png) |
| logica_booleana2.png / `ideias_principais` / 02 | [929, 827, 1312, 1198] → [933, 831, 1311, 1194] | **Aprovada na autoauditoria**. Título local, textos, bordas, fórmulas e relações presentes preservados; nenhum defeito geométrico impeditivo identificado. | [f0](logica_booleana2_png__ideias_principais__f00.png) |
| logica_booleana3.png / `integral` / 03 | [0, 0, 1312, 1199] → [0, 0, 1312, 1199] | **Aprovada com ressalva**. V: visão de contexto íntegra, com texto reduzido; não promete leitura detalhada de todos os painéis. P de origem: M01-04/05; ler 4/8 como combinações, não valores de cada variável; r é entrada livre neste material. | [f0](logica_booleana3_png__integral__f00.png) |
| logica_booleana3.png / `uma_proposicao` / 03 | [0, 123, 313, 660] → [2, 127, 309, 656] | **Aprovada na autoauditoria**. Título local, textos, bordas, fórmulas e relações presentes preservados; nenhum defeito geométrico impeditivo identificado. | [f0](logica_booleana3_png__uma_proposicao__f00.png) |
| logica_booleana3.png / `duas_proposicoes` / 03 | [306, 123, 602, 660] → [310, 127, 598, 656] | **Aprovada com ressalva**. P de origem: M01-04/05; ler 4/8 como combinações, não valores de cada variável; r é entrada livre neste material. | [f0](logica_booleana3_png__duas_proposicoes__f00.png) |
| logica_booleana3.png / `tres_proposicoes` / 03 | [595, 123, 894, 660] → [599, 127, 890, 656] | **Aprovada com ressalva**. P de origem: M01-04/05; ler 4/8 como combinações, não valores de cada variável; r é entrada livre neste material. | [f0](logica_booleana3_png__tres_proposicoes__f00.png) |
| logica_booleana3.png / `tabela_tres_variaveis` / 03 | [888, 123, 1312, 660] → [892, 127, 1311, 656] | **Aprovada na autoauditoria**. Título local, textos, bordas, fórmulas e relações presentes preservados; nenhum defeito geométrico impeditivo identificado. | [f0](logica_booleana3_png__tabela_tres_variaveis__f00.png) |
| logica_booleana3.png / `padrao_geral` / 03 | [0, 653, 446, 1186] → [2, 657, 442, 1182] | **Aprovada na autoauditoria**. Título local, textos, bordas, fórmulas e relações presentes preservados; nenhum defeito geométrico impeditivo identificado. | [f0](logica_booleana3_png__padrao_geral__f00.png) |
| logica_booleana3.png / `arvore` / 03 | [440, 653, 961, 1186] → [444, 657, 957, 1182] | **Aprovada na autoauditoria**. Título local, textos, bordas, fórmulas e relações presentes preservados; nenhum defeito geométrico impeditivo identificado. | [f0](logica_booleana3_png__arvore__f00.png) |
| logica_booleana3.png / `ideias_principais` / 03 | [955, 653, 1312, 1186] → [959, 657, 1311, 1182] | **Aprovada na autoauditoria**. Título local, textos, bordas, fórmulas e relações presentes preservados; nenhum defeito geométrico impeditivo identificado. | [f0](logica_booleana3_png__ideias_principais__f00.png) |
| not_p.gif / `integral` / 04 | [0, 0, 1400, 820] → [0, 0, 1400, 820] | **Aprovada com ressalva**. V: visão de contexto íntegra, com texto reduzido; não promete leitura detalhada de todos os painéis. | [f0](not_p_gif__integral__f00.png); [f1](not_p_gif__integral__f01.png) |
| not_p.gif / `operacao_completa` / 04 | [26, 116, 1374, 799] → [30, 120, 1370, 795] | **Aprovada na autoauditoria**. Título local, textos, bordas, fórmulas e relações presentes preservados; nenhum defeito geométrico impeditivo identificado. | [f0](not_p_gif__operacao_completa__f00.png); [f1](not_p_gif__operacao_completa__f01.png) |
| p_and_q.gif / `integral` / 05 | [0, 0, 1400, 820] → [0, 0, 1400, 820] | **Aprovada com ressalva**. V: visão de contexto íntegra, com texto reduzido; não promete leitura detalhada de todos os painéis. | [f0](p_and_q_gif__integral__f00.png); [f1](p_and_q_gif__integral__f01.png); [f2](p_and_q_gif__integral__f02.png); [f3](p_and_q_gif__integral__f03.png) |
| p_and_q.gif / `operacao_completa` / 05 | [26, 116, 1374, 799] → [30, 120, 1370, 795] | **Aprovada na autoauditoria**. Título local, textos, bordas, fórmulas e relações presentes preservados; nenhum defeito geométrico impeditivo identificado. | [f0](p_and_q_gif__operacao_completa__f00.png); [f1](p_and_q_gif__operacao_completa__f01.png); [f2](p_and_q_gif__operacao_completa__f02.png); [f3](p_and_q_gif__operacao_completa__f03.png) |
| p_or_q.gif / `integral` / 06 | [0, 0, 1400, 820] → [0, 0, 1400, 820] | **Aprovada com ressalva**. V: visão de contexto íntegra, com texto reduzido; não promete leitura detalhada de todos os painéis. | [f0](p_or_q_gif__integral__f00.png); [f1](p_or_q_gif__integral__f01.png); [f2](p_or_q_gif__integral__f02.png); [f3](p_or_q_gif__integral__f03.png) |
| p_or_q.gif / `operacao_completa` / 06 | [26, 116, 1374, 799] → [30, 120, 1370, 795] | **Aprovada na autoauditoria**. Título local, textos, bordas, fórmulas e relações presentes preservados; nenhum defeito geométrico impeditivo identificado. | [f0](p_or_q_gif__operacao_completa__f00.png); [f1](p_or_q_gif__operacao_completa__f01.png); [f2](p_or_q_gif__operacao_completa__f02.png); [f3](p_or_q_gif__operacao_completa__f03.png) |
| p_xor_q.gif / `integral` / 07 | [0, 0, 1400, 820] → [0, 0, 1400, 820] | **Aprovada com ressalva**. V: visão de contexto íntegra, com texto reduzido; não promete leitura detalhada de todos os painéis. | [f0](p_xor_q_gif__integral__f00.png); [f1](p_xor_q_gif__integral__f01.png); [f2](p_xor_q_gif__integral__f02.png); [f3](p_xor_q_gif__integral__f03.png) |
| p_xor_q.gif / `operacao_completa` / 07 | [26, 116, 1374, 799] → [30, 120, 1370, 795] | **Aprovada na autoauditoria**. Título local, textos, bordas, fórmulas e relações presentes preservados; nenhum defeito geométrico impeditivo identificado. | [f0](p_xor_q_gif__operacao_completa__f00.png); [f1](p_xor_q_gif__operacao_completa__f01.png); [f2](p_xor_q_gif__operacao_completa__f02.png); [f3](p_xor_q_gif__operacao_completa__f03.png) |
| problema_condicoes.png / `integral` / 08 | [0, 0, 1312, 1199] → [0, 0, 1312, 1199] | **Aprovada com ressalva**. V: visão de contexto íntegra, com texto reduzido; não promete leitura detalhada de todos os painéis. | [f0](problema_condicoes_png__integral__f00.png) |
| problema_condicoes.png / `problema` / 08 | [0, 127, 712, 533] → [2, 131, 708, 529] | **Aprovada na autoauditoria**. Título local, textos, bordas, fórmulas e relações presentes preservados; nenhum defeito geométrico impeditivo identificado. | [f0](problema_condicoes_png__problema__f00.png) |
| problema_condicoes.png / `condicoes` / 08 | [711, 127, 1312, 533] → [715, 131, 1311, 529] | **Aprovada na autoauditoria**. Título local, textos, bordas, fórmulas e relações presentes preservados; nenhum defeito geométrico impeditivo identificado. | [f0](problema_condicoes_png__condicoes__f00.png) |
| problema_condicoes.png / `quatro_cenarios` / 08 | [0, 526, 1312, 819] → [2, 530, 1311, 815] | **Aprovada com ressalva**. V: unidade horizontal mantida completa; espaço neutro e letras menores são consequências do enquadramento proporcional. | [f0](problema_condicoes_png__quatro_cenarios__f00.png) |
| problema_condicoes.png / `respostas` / 08 | [0, 812, 1312, 1198] → [2, 816, 1311, 1194] | **Aprovada com ressalva**. V: unidade horizontal mantida completa; espaço neutro e letras menores são consequências do enquadramento proporcional. | [f0](problema_condicoes_png__respostas__f00.png) |
| problema_condicoes.png / `cenario_sem_chuva_sem_guarda_chuva` / 08 | [18, 616, 328, 810] → [22, 620, 324, 806] | **Aprovada com ressalva**. V: contexto local preservado no cartão; consultar o quadro conjunto para comparação e a definição da expressão, sem transportar o significado de r entre materiais. | [f0](problema_condicoes_png__cenario_sem_chuva_sem_guarda_chuva__f00.png) |
| problema_condicoes.png / `cenario_sem_chuva_com_guarda_chuva` / 08 | [341, 616, 652, 810] → [345, 620, 648, 806] | **Aprovada com ressalva**. V: contexto local preservado no cartão; consultar o quadro conjunto para comparação e a definição da expressão, sem transportar o significado de r entre materiais. | [f0](problema_condicoes_png__cenario_sem_chuva_com_guarda_chuva__f00.png) |
| problema_condicoes.png / `cenario_chuva_sem_guarda_chuva` / 08 | [663, 616, 976, 810] → [667, 620, 972, 806] | **Aprovada com ressalva**. V: contexto local preservado no cartão; consultar o quadro conjunto para comparação e a definição da expressão, sem transportar o significado de r entre materiais. | [f0](problema_condicoes_png__cenario_chuva_sem_guarda_chuva__f00.png) |
| problema_condicoes.png / `cenario_chuva_com_guarda_chuva` / 08 | [985, 616, 1301, 810] → [989, 620, 1297, 806] | **Aprovada com ressalva**. V: contexto local preservado no cartão; consultar o quadro conjunto para comparação e a definição da expressão, sem transportar o significado de r entre materiais. | [f0](problema_condicoes_png__cenario_chuva_com_guarda_chuva__f00.png) |
| problemas_condicoes2.png / `integral` / 09 | [0, 0, 1312, 1199] → [0, 0, 1312, 1199] | **Aprovada com ressalva**. V: visão de contexto íntegra, com texto reduzido; não promete leitura detalhada de todos os painéis. P/contexto: M01-04; r é resultado derivado de p/q aqui, não terceira entrada livre. Fonte preservada. | [f0](problemas_condicoes2_png__integral__f00.png) |
| problemas_condicoes2.png / `perguntas_proposicoes` / 09 | [0, 124, 1312, 344] → [2, 128, 1310, 340] | **Aprovada com ressalva**. V: unidade horizontal mantida completa; espaço neutro e letras menores são consequências do enquadramento proporcional. | [f0](problemas_condicoes2_png__perguntas_proposicoes__f00.png) |
| problemas_condicoes2.png / `proposicoes` / 09 | [0, 334, 1312, 676] → [2, 338, 1310, 672] | **Aprovada com ressalva**. V: unidade horizontal mantida completa; espaço neutro e letras menores são consequências do enquadramento proporcional. P/contexto: M01-04; r é resultado derivado de p/q aqui, não terceira entrada livre. Fonte preservada. | [f0](problemas_condicoes2_png__proposicoes__f00.png) |
| problemas_condicoes2.png / `valores_verdade` / 09 | [0, 668, 1312, 838] → [2, 672, 1310, 834] | **Aprovada com ressalva**. V: unidade horizontal mantida completa; espaço neutro e letras menores são consequências do enquadramento proporcional. | [f0](problemas_condicoes2_png__valores_verdade__f00.png) |
| problemas_condicoes2.png / `tabela_cenarios` / 09 | [0, 829, 1312, 1199] → [2, 833, 1310, 1195] | **Aprovada com ressalva**. V: unidade horizontal mantida completa; espaço neutro e letras menores são consequências do enquadramento proporcional. P/contexto: M01-04; r é resultado derivado de p/q aqui, não terceira entrada livre. Fonte preservada. | [f0](problemas_condicoes2_png__tabela_cenarios__f00.png) |
| problemas_condicoes2.png / `proposicao_p` / 09 | [25, 411, 435, 669] → [29, 415, 431, 665] | **Aprovada na autoauditoria**. Título local, textos, bordas, fórmulas e relações presentes preservados; nenhum defeito geométrico impeditivo identificado. | [f0](problemas_condicoes2_png__proposicao_p__f00.png) |
| problemas_condicoes2.png / `proposicao_q` / 09 | [451, 411, 868, 669] → [455, 415, 864, 665] | **Aprovada na autoauditoria**. Título local, textos, bordas, fórmulas e relações presentes preservados; nenhum defeito geométrico impeditivo identificado. | [f0](problemas_condicoes2_png__proposicao_q__f00.png) |
| problemas_condicoes2.png / `proposicao_r` / 09 | [881, 411, 1298, 669] → [885, 415, 1294, 665] | **Aprovada com ressalva**. P/contexto: M01-04; r é resultado derivado de p/q aqui, não terceira entrada livre. Fonte preservada. | [f0](problemas_condicoes2_png__proposicao_r__f00.png) |
| problemas_condicoes3.png / `integral` / 10 | [0, 0, 1312, 1199] → [0, 0, 1312, 1199] | **Aprovada com ressalva**. V: visão de contexto íntegra, com texto reduzido; não promete leitura detalhada de todos os painéis. | [f0](problemas_condicoes3_png__integral__f00.png) |
| problemas_condicoes3.png / `proposicoes` / 10 | [0, 142, 732, 638] → [2, 146, 728, 634] | **Aprovada na autoauditoria**. Título local, textos, bordas, fórmulas e relações presentes preservados; nenhum defeito geométrico impeditivo identificado. | [f0](problemas_condicoes3_png__proposicoes__f00.png) |
| problemas_condicoes3.png / `significado_and` / 10 | [726, 142, 1312, 638] → [730, 146, 1311, 634] | **Aprovada na autoauditoria**. Título local, textos, bordas, fórmulas e relações presentes preservados; nenhum defeito geométrico impeditivo identificado. | [f0](problemas_condicoes3_png__significado_and__f00.png) |
| problemas_condicoes3.png / `cenarios_and` / 10 | [0, 630, 1312, 905] → [2, 634, 1311, 901] | **Aprovada com ressalva**. V: unidade horizontal mantida completa; espaço neutro e letras menores são consequências do enquadramento proporcional. | [f0](problemas_condicoes3_png__cenarios_and__f00.png) |
| problemas_condicoes3.png / `tabela_and` / 10 | [0, 898, 662, 1199] → [2, 902, 658, 1195] | **Aprovada na autoauditoria**. Título local, textos, bordas, fórmulas e relações presentes preservados; nenhum defeito geométrico impeditivo identificado. | [f0](problemas_condicoes3_png__tabela_and__f00.png) |
| problemas_condicoes3.png / `conclusao` / 10 | [655, 898, 1312, 1199] → [659, 902, 1311, 1195] | **Aprovada na autoauditoria**. Título local, textos, bordas, fórmulas e relações presentes preservados; nenhum defeito geométrico impeditivo identificado. | [f0](problemas_condicoes3_png__conclusao__f00.png) |
| problemas_condicoes3.png / `cenario_00` / 10 | [14, 703, 343, 899] → [18, 707, 339, 895] | **Aprovada com ressalva**. V: contexto local preservado no cartão; consultar o quadro conjunto para comparação e a definição da expressão, sem transportar o significado de r entre materiais. | [f0](problemas_condicoes3_png__cenario_00__f00.png) |
| problemas_condicoes3.png / `cenario_01` / 10 | [339, 703, 659, 899] → [343, 707, 655, 895] | **Aprovada com ressalva**. V: contexto local preservado no cartão; consultar o quadro conjunto para comparação e a definição da expressão, sem transportar o significado de r entre materiais. | [f0](problemas_condicoes3_png__cenario_01__f00.png) |
| problemas_condicoes3.png / `cenario_10` / 10 | [656, 703, 977, 899] → [660, 707, 973, 895] | **Aprovada com ressalva**. V: contexto local preservado no cartão; consultar o quadro conjunto para comparação e a definição da expressão, sem transportar o significado de r entre materiais. | [f0](problemas_condicoes3_png__cenario_10__f00.png) |
| problemas_condicoes3.png / `cenario_11` / 10 | [975, 703, 1310, 899] → [979, 707, 1306, 895] | **Aprovada com ressalva**. V: contexto local preservado no cartão; consultar o quadro conjunto para comparação e a definição da expressão, sem transportar o significado de r entre materiais. | [f0](problemas_condicoes3_png__cenario_11__f00.png) |
| problemas_condicoes4.png / `integral` / 11 | [0, 0, 1312, 1199] → [0, 0, 1312, 1199] | **Aprovada com ressalva**. V: visão de contexto íntegra, com texto reduzido; não promete leitura detalhada de todos os painéis. P de origem: M01-01/02; frase NOT contraditória e/ou condição de verdade inadequada no resumo, conforme região. Sem edição da fonte. P/contexto: M01-03; p na coluna OR significa não estar chovendo, diferentemente de NOT/AND. Não unificar os símbolos entre painéis automaticamente. | [f0](problemas_condicoes4_png__integral__f00.png) |
| problemas_condicoes4.png / `not_contextual` / 11 | [0, 122, 444, 1025] → [2, 126, 440, 1021] | **Aprovada com ressalva**. P de origem: M01-01/02; frase NOT contraditória e/ou condição de verdade inadequada no resumo, conforme região. Sem edição da fonte. | [f0](problemas_condicoes4_png__not_contextual__f00.png) |
| problemas_condicoes4.png / `and_contextual` / 11 | [437, 122, 879, 1025] → [441, 126, 875, 1021] | **Aprovada na autoauditoria**. Título local, textos, bordas, fórmulas e relações presentes preservados; nenhum defeito geométrico impeditivo identificado. | [f0](problemas_condicoes4_png__and_contextual__f00.png) |
| problemas_condicoes4.png / `or_contextual` / 11 | [872, 122, 1312, 1025] → [876, 126, 1311, 1021] | **Aprovada com ressalva**. P/contexto: M01-03; p na coluna OR significa não estar chovendo, diferentemente de NOT/AND. Não unificar os símbolos entre painéis automaticamente. | [f0](problemas_condicoes4_png__or_contextual__f00.png) |
| problemas_condicoes4.png / `resumo` / 11 | [0, 1017, 1312, 1199] → [2, 1021, 1311, 1197] | **Aprovada com ressalva**. V: unidade horizontal mantida completa; espaço neutro e letras menores são consequências do enquadramento proporcional. P de origem: M01-01/02; frase NOT contraditória e/ou condição de verdade inadequada no resumo, conforme região. Sem edição da fonte. | [f0](problemas_condicoes4_png__resumo__f00.png) |
| problemas_condicoes5.png / `integral` / 12 | [0, 0, 1312, 1199] → [0, 0, 1312, 1199] | **Aprovada com ressalva**. V: visão de contexto íntegra, com texto reduzido; não promete leitura detalhada de todos os painéis. | [f0](problemas_condicoes5_png__integral__f00.png) |
| problemas_condicoes5.png / `problema_original` / 12 | [0, 120, 464, 615] → [2, 124, 460, 611] | **Aprovada na autoauditoria**. Título local, textos, bordas, fórmulas e relações presentes preservados; nenhum defeito geométrico impeditivo identificado. | [f0](problemas_condicoes5_png__problema_original__f00.png) |
| problemas_condicoes5.png / `construcao_expressao` / 12 | [458, 120, 891, 615] → [462, 124, 887, 611] | **Aprovada na autoauditoria**. Título local, textos, bordas, fórmulas e relações presentes preservados; nenhum defeito geométrico impeditivo identificado. | [f0](problemas_condicoes5_png__construcao_expressao__f00.png) |
| problemas_condicoes5.png / `definicao_tabela` / 12 | [884, 120, 1312, 615] → [888, 124, 1311, 611] | **Aprovada na autoauditoria**. Título local, textos, bordas, fórmulas e relações presentes preservados; nenhum defeito geométrico impeditivo identificado. | [f0](problemas_condicoes5_png__definicao_tabela__f00.png) |
| problemas_condicoes5.png / `tabela_e_leitura` / 12 | [0, 605, 1312, 881] → [2, 609, 1311, 877] | **Aprovada com ressalva**. V: unidade horizontal mantida completa; espaço neutro e letras menores são consequências do enquadramento proporcional. V: pequenos fragmentos de borda/cartões na margem inferior são aceitos para preservar a tabela e seu título. | [f0](problemas_condicoes5_png__tabela_e_leitura__f00.png) |
| problemas_condicoes5.png / `tabela_final` / 12 | [0, 605, 922, 881] → [2, 609, 918, 877] | **Aprovada com ressalva**. V: unidade horizontal mantida completa; espaço neutro e letras menores são consequências do enquadramento proporcional. V: pequenos fragmentos de borda/cartões na margem inferior são aceitos para preservar a tabela e seu título. | [f0](problemas_condicoes5_png__tabela_final__f00.png) |
| problemas_condicoes5.png / `interpretacao_cenarios` / 12 | [0, 872, 847, 1198] → [2, 876, 843, 1194] | **Aprovada com ressalva**. V: unidade horizontal mantida completa; espaço neutro e letras menores são consequências do enquadramento proporcional. | [f0](problemas_condicoes5_png__interpretacao_cenarios__f00.png) |
| problemas_condicoes5.png / `conclusao` / 12 | [839, 872, 1312, 1198] → [843, 876, 1311, 1194] | **Aprovada na autoauditoria**. Título local, textos, bordas, fórmulas e relações presentes preservados; nenhum defeito geométrico impeditivo identificado. | [f0](problemas_condicoes5_png__conclusao__f00.png) |
| problemas_condicoes5.png / `cenario_00` / 12 | [13, 921, 223, 1179] → [17, 925, 219, 1175] | **Aprovada com ressalva**. V: contexto local preservado no cartão; consultar o quadro conjunto para comparação e a definição da expressão, sem transportar o significado de r entre materiais. | [f0](problemas_condicoes5_png__cenario_00__f00.png) |
| problemas_condicoes5.png / `cenario_01` / 12 | [217, 921, 429, 1179] → [221, 925, 425, 1175] | **Aprovada com ressalva**. V: contexto local preservado no cartão; consultar o quadro conjunto para comparação e a definição da expressão, sem transportar o significado de r entre materiais. | [f0](problemas_condicoes5_png__cenario_01__f00.png) |
| problemas_condicoes5.png / `cenario_10` / 12 | [425, 921, 638, 1179] → [429, 925, 634, 1175] | **Aprovada com ressalva**. V: contexto local preservado no cartão; consultar o quadro conjunto para comparação e a definição da expressão, sem transportar o significado de r entre materiais. | [f0](problemas_condicoes5_png__cenario_10__f00.png) |
| problemas_condicoes5.png / `cenario_11` / 12 | [633, 921, 837, 1179] → [637, 925, 833, 1175] | **Aprovada com ressalva**. V: contexto local preservado no cartão; consultar o quadro conjunto para comparação e a definição da expressão, sem transportar o significado de r entre materiais. | [f0](problemas_condicoes5_png__cenario_11__f00.png) |

## Verificação técnica e encerramento

JSON válido; IDs únicos por arquivo; 12 originais ligados ao inventário/catálogo; dimensões e SHA-256 reais; 74 caixas dentro dos limites; 94 nomes de projeção distintos e imagens 1080×1920. As projeções são comparadas pixel a pixel com uma nova renderização das coordenadas do JSON final. Essa comparação demonstra correspondência técnica, separadamente da inspeção visual relatada acima.

Todos os arquivos preexistentes foram comparados por SHA-256 com a linha de base e permanecem inalterados. Não foram alterados inventário, catálogos, vocabulário, checklist, governança, roteiro, dossiê ou originais. Os arquivos finais restringem-se a 01_Mapa_Espacial.json e evidencias_mapa_espacial/. Scripts e quadros temporários ficaram fora do repositório. A PR #15 foi preservada.

Entrega para homologação humana, sem merge automático e sem retomada do piloto. As ressalvas de fonte continuam sob deliberação humana específica.
