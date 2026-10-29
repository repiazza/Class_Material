# Autoauditoria do mapa espacial — capítulo 02

**Estado:** AUTOAUDITADO_COM_RESSALVAS. Homologação humana PENDENTE. Esta entrega não homologa conceitos ou enquadramentos e não define montagem, duração ou ordem de estudo.

## Escopo e procedimento

Fontes efetivamente consultadas: AGENTS.md; protocolo_mapeamento_espacial.md; inventario.csv; catálogo 02 atual (14 registros e glossário); checklist histórico. Base Git: d8c3457. Foram abertas as nove imagens originais em resolução de inspeção e examinados todos os 38 quadros decodificados dos três GIFs. Não foram usados mapas/coordenadas do capítulo 01.

Reconheceram-se painéis pelos seus fundos, bordas, títulos e agrupamentos. Setas e resultados ficaram com seus operandos; tabelas não foram fragmentadas; cada material conserva uma região integral, inclusive conteúdo fora dos painéis. As caixas primárias foram abrangentes, com margem de três pixels além da caixa refinada quando havia espaço. A redução limitou-se a margens externas; não se buscou a menor caixa possível. A tabela abaixo registra as duas geometrias. A primeira rodada revelou duas bordas incompletas, corrigidas por ampliação (detalhes adiante).

Projeção empregada: ler o JSON final; converter coordenadas normalizadas por round(coordenada × dimensão), com x1/y1 exclusivos; recortar o original; escala min(1080/largura, 1920/altura); dimensões redimensionadas pelo mesmo fator, arredondadas ao pixel mais próximo; centralizar em 1080×1920, fundo RGB (22,22,22), filtro Lanczos. Não há esticamento para preencher tela nem corte adicional. O arredondamento de raster é de até meio pixel por dimensão. Este é o algoritmo de referência desta entrega; compatibilidade com um futuro editor ainda depende de sua adoção.

## Quantidades e cobertura

- 12 arquivos visuais: nove PNGs e três GIFs; 67 regiões.
- 81 projeções finais 1080×1920: 60 estáticas e 21 relativas a GIFs (sete regiões × três estados).
- Todas as 67 regiões tiveram projeções examinadas: 27 painéis finais de inspeção; ampliações individuais dirigidas às dúvidas. Não se declara leitura minuciosa de todo texto pequeno em miniatura; as ressalvas de legibilidade estão individualizadas.
- Resultados: 38 aprovadas na autoauditoria; 25 aprovadas com ressalva; 4 pendentes.
- Todas as classificações referem-se à autoauditoria do agente, não a aprovação humana. Regiões pendentes continuam inclusas e identificadas; não devem ser tratadas como validadas.

## Correções realizadas e evidências

1. As caixas internas dos GIFs de contagem tinham bbox [32,225,1325,826] e eliminavam parte da borda direita dos quadros. Retorno aos originais, ampliação para [30,220,1370,835], nova projeção e reinspeção dos estados 0, 7 e 15. São duas regiões corrigidas, seis projeções finais. Não se alterou o significado ou os IDs.
   - Decimal: [antes](antes_contagem_decimal.png) e [depois](contagem_0_a_15_gif__contagem_e_calculo__f15.png).
   - Hexadecimal: [antes](antes_contagem_hexa.png) e [depois](contagem_0_a_15_hexa_gif__tres_representacoes__f15.png).

2. A primeira exportação usava nomes sem extensão do original: PNG e GIF signed_unsigned colidiam na região integral. Os nomes foram corrigidos para incluir png/gif; as 81 projeções e 27 painéis foram regenerados do JSON final. Foi reinspecionada a região integral do PNG, que antes mostrava incorretamente o GIF. A validação final verifica também correspondência pixel a pixel das projeções com a renderização de sua fonte. Nenhuma referência final aponta para a evidência trocada.

## GIFs: estados observados e limites

Índices começam em zero. Durações são os metadados lidos dos originais, não sugestões de duração audiovisual.

| Arquivo | Inspeção do original | Projeções inspecionadas por região | Duração declarada | Observação |
|---|---|---|---|---|
| contagem_0_a_15.gif | Todos os quadros 0–15 | 0, 7, 15 | 1.500 ms/quadro; ciclo nominal 24 s | Pesos fixos, estados 0000–1111, rótulos ATIVO, valor decimal e cálculos variáveis. |
| contagem_0_a_15_hexa.gif | Todos os quadros 0–15 | 0, 7, 15 | 1.500 ms/quadro; ciclo nominal 24 s | Binário, decimal, hexadecimal e literais C variam sincronizados; A–F observados nos quadros 10–15. |
| signed_unsigned.gif | Todos os quadros 0–5 | 0, 2, 5 | 2.000 ms/quadro; ciclo nominal 12 s | Inicialmente só unsigned; depois signed; marcação “mesmos bits”; duas saídas são acrescentadas ao terminal. |

Os 38 quadros originais foram visualizados em folhas de estados; o quadro 2 de signed_unsigned foi aberto também individualmente. Projeções finais dos GIFs são amostras espaciais: não são GIFs recortados, nem ensaio de fluidez/transições/loop. Quadros não amostrados não receberam projeção 9:16 independente. Os limites escolhidos preservam agrupamentos fixos nos estados observados, mas a entrega não certifica execução audiovisual contínua.

O catálogo não descreve detalhadamente a sequência temporal. A inspeção mostrou que o GIF signed_unsigned introduz os objetos progressivamente; o padrão 11111111 dos objetos é igual quando ambos estão exibidos, não existe a linha signed completa em todos os estados. No quadro 2, a frase “Os dois objetos apresentam o mesmo padrão de 8 bits neste mo…” já é interrompida/encoberta na composição original: [evidência do quadro original](original_signed_unsigned_quadro02.png). Essa limitação não é causada pelo recorte, não foi ocultada nem corrigida por reconstrução.

## Divergências documentais e conteúdo de origem

- Catálogo, registro 10, descreve signed_unsigned.png com oito bits, 255/−1 e terminal. O PNG efetivo usa 1010, quatro bits, 10/−6, tabelas e notas sobre C; terminal está no GIF. As descrições do mapa seguem o original. Revisão do catálogo fica para decisão humana, sem edição nesta execução.
- msb_lsb.png: posição 3 aparece com peso 2⁴=16; esperado 2³=8. Regiões integral e byte_extremos permanecem pendentes por dúvida semântica demonstrada, embora a geometria preserve a fonte.
- A linha hexadecimal dos símbolos em sistemas_representacao_numericas.png apresenta glifos sobrepostos/duplicados em torno de 5/6. Isso já existe no original; o mapa não o retoca e não atesta correção editorial do material.
- O catálogo menciona que combinacao_bits.png distingue quantidade e máximo. A imagem inspecionada enfatiza a contagem 2ⁿ, sem uma comparação explícita com 2ⁿ−1. Não se atribui ao recorte essa explicação ausente.

## Painéis finais para revisão humana

Cada painel contém três projeções reduzidas a 540×960, com rótulo fora da área 9:16. Abra os PNGs individuais, vinculados abaixo, para ver 1080×1920. Nenhum painel determina ordem de montagem.

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

## Registro por região

Coordenadas em pixels: [x0,y0,x1,y1), origem superior esquerda. A caixa primária é registro de proposição, não evidência de validação por si só. Para os dois GIFs corrigidos, a coluna primária abaixo é a abrangência da rodada final; a tentativa defeituosa está registrada acima. As pequenas margens em painéis contíguos podem deixar resíduos de bordas vizinhas: prioridade foi preservar título e conteúdo.

| Arquivo / ID / registro do catálogo | Primária → final (px) | Resultado e observação | Projeções finais |
|---|---|---|---|
| sistemas_representacao_numericas.png / `integral` / 01 | [0, 0, 1312, 1199] → [0, 0, 1312, 1199] | **Aprovada com ressalva**. Visão de conjunto: texto reduzido na projeção vertical; não equivale a legibilidade de cada painel. | [f0](sistemas_representacao_numericas_png__integral__f00.png) |
| sistemas_representacao_numericas.png / `decimal` / 01 | [0, 137, 468, 651] → [2, 140, 465, 648] | **Aprovada na autoauditoria**. Título, conteúdo e relações preservados; nenhum defeito impeditivo de enquadramento identificado. | [f0](sistemas_representacao_numericas_png__decimal__f00.png) |
| sistemas_representacao_numericas.png / `binario` / 01 | [464, 137, 889, 651] → [467, 140, 886, 648] | **Aprovada na autoauditoria**. Título, conteúdo e relações preservados; nenhum defeito impeditivo de enquadramento identificado. | [f0](sistemas_representacao_numericas_png__binario__f00.png) |
| sistemas_representacao_numericas.png / `comparacao_bases` / 01 | [885, 137, 1312, 651] → [888, 140, 1311, 648] | **Aprovada na autoauditoria**. Título, conteúdo e relações preservados; nenhum defeito impeditivo de enquadramento identificado. | [f0](sistemas_representacao_numericas_png__comparacao_bases__f00.png) |
| sistemas_representacao_numericas.png / `outros_sistemas` / 01 | [0, 647, 530, 1186] → [2, 650, 527, 1183] | **Aprovada na autoauditoria**. Título, conteúdo e relações preservados; nenhum defeito impeditivo de enquadramento identificado. | [f0](sistemas_representacao_numericas_png__outros_sistemas__f00.png) |
| sistemas_representacao_numericas.png / `valor42` / 01 | [526, 647, 982, 1186] → [529, 650, 979, 1183] | **Aprovada na autoauditoria**. Título, conteúdo e relações preservados; nenhum defeito impeditivo de enquadramento identificado. | [f0](sistemas_representacao_numericas_png__valor42__f00.png) |
| sistemas_representacao_numericas.png / `ideias_principais` / 01 | [978, 647, 1312, 1186] → [981, 650, 1311, 1183] | **Aprovada na autoauditoria**. Título, conteúdo e relações preservados; nenhum defeito impeditivo de enquadramento identificado. | [f0](sistemas_representacao_numericas_png__ideias_principais__f00.png) |
| sistemas_representacao_numerica2.png / `integral` / 02 | [0, 0, 1312, 1199] → [0, 0, 1312, 1199] | **Aprovada com ressalva**. Visão de conjunto: texto reduzido na projeção vertical; não equivale a legibilidade de cada painel. | [f0](sistemas_representacao_numerica2_png__integral__f00.png) |
| sistemas_representacao_numerica2.png / `bases` / 02 | [0, 134, 447, 559] → [2, 137, 444, 556] | **Aprovada na autoauditoria**. Título, conteúdo e relações preservados; nenhum defeito impeditivo de enquadramento identificado. | [f0](sistemas_representacao_numerica2_png__bases__f00.png) |
| sistemas_representacao_numerica2.png / `notacao_matematica` / 02 | [443, 134, 863, 559] → [446, 137, 860, 556] | **Aprovada na autoauditoria**. Título, conteúdo e relações preservados; nenhum defeito impeditivo de enquadramento identificado. | [f0](sistemas_representacao_numerica2_png__notacao_matematica__f00.png) |
| sistemas_representacao_numerica2.png / `literais_c` / 02 | [859, 134, 1312, 559] → [862, 137, 1311, 556] | **Aprovada na autoauditoria**. Título, conteúdo e relações preservados; nenhum defeito impeditivo de enquadramento identificado. | [f0](sistemas_representacao_numerica2_png__literais_c__f00.png) |
| sistemas_representacao_numerica2.png / `tabela_nibble` / 02 | [0, 555, 1312, 969] → [2, 558, 1311, 966] | **Aprovada com ressalva**. Unidade horizontal completa preservada; letras pequenas e amplo preenchimento neutro na projeção vertical. | [f0](sistemas_representacao_numerica2_png__tabela_nibble__f00.png) |
| sistemas_representacao_numerica2.png / `exemplo_pratico` / 02 | [0, 966, 562, 1199] → [2, 969, 559, 1197] | **Aprovada na autoauditoria**. Título, conteúdo e relações preservados; nenhum defeito impeditivo de enquadramento identificado. | [f0](sistemas_representacao_numerica2_png__exemplo_pratico__f00.png) |
| sistemas_representacao_numerica2.png / `ideias_principais` / 02 | [558, 966, 1312, 1199] → [561, 969, 1311, 1197] | **Aprovada na autoauditoria**. Título, conteúdo e relações preservados; nenhum defeito impeditivo de enquadramento identificado. | [f0](sistemas_representacao_numerica2_png__ideias_principais__f00.png) |
| bit.png / `integral` / 03 | [0, 0, 1312, 1199] → [0, 0, 1312, 1199] | **Aprovada com ressalva**. Visão de conjunto: texto reduzido na projeção vertical; não equivale a legibilidade de cada painel. | [f0](bit_png__integral__f00.png) |
| bit.png / `logica_booleana` / 03 | [0, 145, 439, 716] → [2, 148, 436, 713] | **Aprovada na autoauditoria**. Título, conteúdo e relações preservados; nenhum defeito impeditivo de enquadramento identificado. | [f0](bit_png__logica_booleana__f00.png) |
| bit.png / `representacao_bit` / 03 | [434, 145, 879, 717] → [437, 148, 876, 714] | **Aprovada na autoauditoria**. Título, conteúdo e relações preservados; nenhum defeito impeditivo de enquadramento identificado. | [f0](bit_png__representacao_bit__f00.png) |
| bit.png / `contextos` / 03 | [875, 145, 1312, 716] → [878, 148, 1311, 713] | **Aprovada na autoauditoria**. Título, conteúdo e relações preservados; nenhum defeito impeditivo de enquadramento identificado. | [f0](bit_png__contextos__f00.png) |
| bit.png / `representacao_visual` / 03 | [0, 717, 522, 1178] → [2, 720, 519, 1175] | **Aprovada na autoauditoria**. Título, conteúdo e relações preservados; nenhum defeito impeditivo de enquadramento identificado. | [f0](bit_png__representacao_visual__f00.png) |
| bit.png / `resumo` / 03 | [518, 717, 890, 1179] → [521, 720, 887, 1176] | **Aprovada na autoauditoria**. Título, conteúdo e relações preservados; nenhum defeito impeditivo de enquadramento identificado. | [f0](bit_png__resumo__f00.png) |
| bit.png / `ideia_principal` / 03 | [886, 717, 1312, 1179] → [889, 720, 1311, 1176] | **Aprovada na autoauditoria**. Título, conteúdo e relações preservados; nenhum defeito impeditivo de enquadramento identificado. | [f0](bit_png__ideia_principal__f00.png) |
| bit_byte_nibble.png / `integral` / 04 | [0, 0, 1312, 1199] → [0, 0, 1312, 1199] | **Aprovada com ressalva**. Visão de conjunto: texto reduzido na projeção vertical; não equivale a legibilidade de cada painel. | [f0](bit_byte_nibble_png__integral__f00.png) |
| bit_byte_nibble.png / `bit` / 04 | [0, 142, 464, 640] → [2, 145, 461, 637] | **Aprovada na autoauditoria**. Título, conteúdo e relações preservados; nenhum defeito impeditivo de enquadramento identificado. | [f0](bit_byte_nibble_png__bit__f00.png) |
| bit_byte_nibble.png / `nibble` / 04 | [460, 142, 848, 640] → [463, 145, 845, 637] | **Aprovada na autoauditoria**. Título, conteúdo e relações preservados; nenhum defeito impeditivo de enquadramento identificado. | [f0](bit_byte_nibble_png__nibble__f00.png) |
| bit_byte_nibble.png / `byte` / 04 | [844, 142, 1312, 640] → [847, 145, 1311, 637] | **Aprovada na autoauditoria**. Título, conteúdo e relações preservados; nenhum defeito impeditivo de enquadramento identificado. | [f0](bit_byte_nibble_png__byte__f00.png) |
| bit_byte_nibble.png / `comparacao` / 04 | [0, 638, 573, 1151] → [2, 641, 570, 1148] | **Aprovada na autoauditoria**. Título, conteúdo e relações preservados; nenhum defeito impeditivo de enquadramento identificado. | [f0](bit_byte_nibble_png__comparacao__f00.png) |
| bit_byte_nibble.png / `exemplos_nibbles` / 04 | [568, 638, 890, 1151] → [571, 641, 887, 1148] | **Aprovada na autoauditoria**. Título, conteúdo e relações preservados; nenhum defeito impeditivo de enquadramento identificado. | [f0](bit_byte_nibble_png__exemplos_nibbles__f00.png) |
| bit_byte_nibble.png / `exemplo_byte` / 04 | [885, 638, 1312, 1151] → [888, 641, 1311, 1148] | **Aprovada na autoauditoria**. Título, conteúdo e relações preservados; nenhum defeito impeditivo de enquadramento identificado. | [f0](bit_byte_nibble_png__exemplo_byte__f00.png) |
| combinacao_bits.png / `integral` / 05 | [0, 0, 1312, 1199] → [0, 0, 1312, 1199] | **Aprovada com ressalva**. Visão de conjunto: texto reduzido na projeção vertical; não equivale a legibilidade de cada painel. | [f0](combinacao_bits_png__integral__f00.png) |
| combinacao_bits.png / `um_bit` / 05 | [0, 142, 321, 922] → [2, 145, 318, 919] | **Aprovada na autoauditoria**. Título, conteúdo e relações preservados; nenhum defeito impeditivo de enquadramento identificado. | [f0](combinacao_bits_png__um_bit__f00.png) |
| combinacao_bits.png / `dois_bits` / 05 | [316, 142, 609, 922] → [319, 145, 606, 919] | **Aprovada na autoauditoria**. Título, conteúdo e relações preservados; nenhum defeito impeditivo de enquadramento identificado. | [f0](combinacao_bits_png__dois_bits__f00.png) |
| combinacao_bits.png / `tres_bits` / 05 | [604, 142, 927, 922] → [607, 145, 924, 919] | **Aprovada na autoauditoria**. Título, conteúdo e relações preservados; nenhum defeito impeditivo de enquadramento identificado. | [f0](combinacao_bits_png__tres_bits__f00.png) |
| combinacao_bits.png / `padrao_geral` / 05 | [922, 142, 1312, 922] → [925, 145, 1311, 919] | **Aprovada na autoauditoria**. Título, conteúdo e relações preservados; nenhum defeito impeditivo de enquadramento identificado. | [f0](combinacao_bits_png__padrao_geral__f00.png) |
| combinacao_bits.png / `ideia_principal` / 05 | [0, 920, 1312, 1187] → [2, 923, 1311, 1184] | **Aprovada com ressalva**. Unidade horizontal completa preservada; letras pequenas e amplo preenchimento neutro na projeção vertical. | [f0](combinacao_bits_png__ideia_principal__f00.png) |
| contagem_0_a_15.gif / `integral` / 06 | [0, 0, 1400, 850] → [0, 0, 1400, 850] | **Aprovada com ressalva**. Visão de conjunto: texto reduzido na projeção vertical; não equivale a legibilidade de cada painel. Projeção auditada em três estados; sem validação de reprodução contínua. | [f0](contagem_0_a_15_gif__integral__f00.png); [f7](contagem_0_a_15_gif__integral__f07.png); [f15](contagem_0_a_15_gif__integral__f15.png) |
| contagem_0_a_15.gif / `contagem_e_calculo` / 06 | [27, 217, 1373, 838] → [30, 220, 1370, 835] | **Aprovada com ressalva**. Projeção auditada em três estados; sem validação de reprodução contínua. | [f0](contagem_0_a_15_gif__contagem_e_calculo__f00.png); [f7](contagem_0_a_15_gif__contagem_e_calculo__f07.png); [f15](contagem_0_a_15_gif__contagem_e_calculo__f15.png) |
| contagem_0_a_15_hexa.gif / `integral` / 07 | [0, 0, 1400, 850] → [0, 0, 1400, 850] | **Aprovada com ressalva**. Visão de conjunto: texto reduzido na projeção vertical; não equivale a legibilidade de cada painel. Projeção auditada em três estados; sem validação de reprodução contínua. | [f0](contagem_0_a_15_hexa_gif__integral__f00.png); [f7](contagem_0_a_15_hexa_gif__integral__f07.png); [f15](contagem_0_a_15_hexa_gif__integral__f15.png) |
| contagem_0_a_15_hexa.gif / `tres_representacoes` / 07 | [27, 217, 1373, 838] → [30, 220, 1370, 835] | **Aprovada com ressalva**. Projeção auditada em três estados; sem validação de reprodução contínua. | [f0](contagem_0_a_15_hexa_gif__tres_representacoes__f00.png); [f7](contagem_0_a_15_hexa_gif__tres_representacoes__f07.png); [f15](contagem_0_a_15_hexa_gif__tres_representacoes__f15.png) |
| hexadecimal.png / `integral` / 08 | [0, 0, 1312, 1199] → [0, 0, 1312, 1199] | **Aprovada com ressalva**. Visão de conjunto: texto reduzido na projeção vertical; não equivale a legibilidade de cada painel. | [f0](hexadecimal_png__integral__f00.png) |
| hexadecimal.png / `problema` / 08 | [0, 142, 434, 826] → [2, 145, 431, 823] | **Aprovada na autoauditoria**. Título, conteúdo e relações preservados; nenhum defeito impeditivo de enquadramento identificado. | [f0](hexadecimal_png__problema__f00.png) |
| hexadecimal.png / `base16` / 08 | [430, 142, 849, 738] → [433, 145, 846, 735] | **Aprovada na autoauditoria**. Título, conteúdo e relações preservados; nenhum defeito impeditivo de enquadramento identificado. | [f0](hexadecimal_png__base16__f00.png) |
| hexadecimal.png / `correspondencias` / 08 | [844, 142, 1312, 738] → [847, 145, 1311, 735] | **Aprovada na autoauditoria**. Título, conteúdo e relações preservados; nenhum defeito impeditivo de enquadramento identificado. | [f0](hexadecimal_png__correspondencias__f00.png) |
| hexadecimal.png / `exemplo_nibble` / 08 | [0, 824, 434, 1195] → [2, 827, 431, 1192] | **Aprovada na autoauditoria**. Título, conteúdo e relações preservados; nenhum defeito impeditivo de enquadramento identificado. | [f0](hexadecimal_png__exemplo_nibble__f00.png) |
| hexadecimal.png / `exemplo_byte` / 08 | [430, 735, 889, 1195] → [433, 738, 886, 1192] | **Aprovada na autoauditoria**. Título, conteúdo e relações preservados; nenhum defeito impeditivo de enquadramento identificado. | [f0](hexadecimal_png__exemplo_byte__f00.png) |
| hexadecimal.png / `ideias_principais` / 08 | [885, 735, 1312, 1195] → [888, 738, 1311, 1192] | **Aprovada na autoauditoria**. Título, conteúdo e relações preservados; nenhum defeito impeditivo de enquadramento identificado. | [f0](hexadecimal_png__ideias_principais__f00.png) |
| msb_lsb.png / `integral` / 09 | [0, 0, 1536, 1024] → [0, 0, 1536, 1024] | **Pendente**. Visão de conjunto: texto reduzido na projeção vertical; não equivale a legibilidade de cada painel. Fonte exibe 2⁴/16 sob a posição 3, em vez de 2³/8. Preservação geométrica não valida a informação. | [f0](msb_lsb_png__integral__f00.png) |
| msb_lsb.png / `definicao` / 09 | [0, 0, 1536, 204] → [0, 0, 1536, 201] | **Aprovada com ressalva**. Unidade horizontal completa preservada; letras pequenas e amplo preenchimento neutro na projeção vertical. | [f0](msb_lsb_png__definicao__f00.png) |
| msb_lsb.png / `byte_extremos` / 09 | [0, 208, 976, 813] → [3, 211, 973, 810] | **Pendente**. Fonte exibe 2⁴/16 sob a posição 3, em vez de 2³/8. Preservação geométrica não valida a informação. | [f0](msb_lsb_png__byte_extremos__f00.png) |
| msb_lsb.png / `pratica_paridade` / 09 | [977, 208, 1536, 813] → [980, 211, 1533, 810] | **Aprovada na autoauditoria**. Título, conteúdo e relações preservados; nenhum defeito impeditivo de enquadramento identificado. | [f0](msb_lsb_png__pratica_paridade__f00.png) |
| msb_lsb.png / `explicacao_resumo` / 09 | [1, 824, 1536, 1023] → [4, 827, 1533, 1020] | **Aprovada com ressalva**. Unidade horizontal completa preservada; letras pequenas e amplo preenchimento neutro na projeção vertical. | [f0](msb_lsb_png__explicacao_resumo__f00.png) |
| signed_unsigned.png / `integral` / 10 | [0, 0, 1536, 1024] → [0, 0, 1536, 1024] | **Aprovada com ressalva**. Visão de conjunto: texto reduzido na projeção vertical; não equivale a legibilidade de cada painel. Divergência com catálogo 10: original mostra 1010 em quatro bits, 10/−6; não mostra o exemplo de oito bits 255/−1 descrito no catálogo. | [f0](signed_unsigned_png__integral__f00.png) |
| signed_unsigned.png / `ideia_principal` / 10 | [1, 100, 362, 573] → [4, 103, 359, 570] | **Aprovada com ressalva**. Divergência com catálogo 10: original mostra 1010 em quatro bits, 10/−6; não mostra o exemplo de oito bits 255/−1 descrito no catálogo. | [f0](signed_unsigned_png__ideia_principal__f00.png) |
| signed_unsigned.png / `comparacao_nibble` / 10 | [359, 100, 985, 573] → [362, 103, 982, 570] | **Aprovada com ressalva**. Divergência com catálogo 10: original mostra 1010 em quatro bits, 10/−6; não mostra o exemplo de oito bits 255/−1 descrito no catálogo. | [f0](signed_unsigned_png__comparacao_nibble__f00.png) |
| signed_unsigned.png / `peso_negativo` / 10 | [984, 100, 1536, 573] → [987, 103, 1533, 570] | **Aprovada com ressalva**. Divergência com catálogo 10: original mostra 1010 em quatro bits, 10/−6; não mostra o exemplo de oito bits 255/−1 descrito no catálogo. | [f0](signed_unsigned_png__peso_negativo__f00.png) |
| signed_unsigned.png / `faixas_nibble` / 10 | [1, 573, 528, 993] → [4, 576, 525, 990] | **Aprovada com ressalva**. Divergência com catálogo 10: original mostra 1010 em quatro bits, 10/−6; não mostra o exemplo de oito bits 255/−1 descrito no catálogo. | [f0](signed_unsigned_png__faixas_nibble__f00.png) |
| signed_unsigned.png / `exemplos` / 10 | [525, 573, 966, 993] → [528, 576, 963, 990] | **Aprovada com ressalva**. Divergência com catálogo 10: original mostra 1010 em quatro bits, 10/−6; não mostra o exemplo de oito bits 255/−1 descrito no catálogo. | [f0](signed_unsigned_png__exemplos__f00.png) |
| signed_unsigned.png / `linguagem_c` / 10 | [963, 573, 1536, 993] → [966, 576, 1533, 990] | **Aprovada com ressalva**. Divergência com catálogo 10: original mostra 1010 em quatro bits, 10/−6; não mostra o exemplo de oito bits 255/−1 descrito no catálogo. | [f0](signed_unsigned_png__linguagem_c__f00.png) |
| signed_unsigned.gif / `integral` / 11 | [0, 0, 1600, 900] → [0, 0, 1600, 900] | **Pendente**. Visão de conjunto: texto reduzido na projeção vertical; não equivale a legibilidade de cada painel. Projeção auditada em três estados; sem validação de reprodução contínua. No original, a frase explicativa do quadro 2 é encoberta na lateral direita; a caixa não recupera conteúdo ausente. | [f0](signed_unsigned_gif__integral__f00.png); [f2](signed_unsigned_gif__integral__f02.png); [f5](signed_unsigned_gif__integral__f05.png) |
| signed_unsigned.gif / `codigo_contexto` / 11 | [29, 137, 793, 863] → [32, 140, 790, 860] | **Pendente**. Projeção auditada em três estados; sem validação de reprodução contínua. No original, a frase explicativa do quadro 2 é encoberta na lateral direita; a caixa não recupera conteúdo ausente. | [f0](signed_unsigned_gif__codigo_contexto__f00.png); [f2](signed_unsigned_gif__codigo_contexto__f02.png); [f5](signed_unsigned_gif__codigo_contexto__f05.png) |
| signed_unsigned.gif / `bits_terminal` / 11 | [807, 137, 1573, 863] → [810, 140, 1570, 860] | **Aprovada com ressalva**. Projeção auditada em três estados; sem validação de reprodução contínua. | [f0](signed_unsigned_gif__bits_terminal__f00.png); [f2](signed_unsigned_gif__bits_terminal__f02.png); [f5](signed_unsigned_gif__bits_terminal__f05.png) |
| signed_unsigned2.png / `integral` / 12 | [0, 0, 1536, 1024] → [0, 0, 1536, 1024] | **Aprovada com ressalva**. Visão de conjunto: texto reduzido na projeção vertical; não equivale a legibilidade de cada painel. | [f0](signed_unsigned2_png__integral__f00.png) |
| signed_unsigned2.png / `tabela_completa` / 12 | [0, 97, 545, 804] → [2, 100, 542, 801] | **Aprovada na autoauditoria**. Título, conteúdo e relações preservados; nenhum defeito impeditivo de enquadramento identificado. | [f0](signed_unsigned2_png__tabela_completa__f00.png) |
| signed_unsigned2.png / `calculo_signed` / 12 | [542, 97, 1104, 613] → [545, 100, 1101, 610] | **Aprovada na autoauditoria**. Título, conteúdo e relações preservados; nenhum defeito impeditivo de enquadramento identificado. | [f0](signed_unsigned2_png__calculo_signed__f00.png) |
| signed_unsigned2.png / `faixas_gerais` / 12 | [1100, 97, 1536, 613] → [1103, 100, 1534, 610] | **Aprovada na autoauditoria**. Título, conteúdo e relações preservados; nenhum defeito impeditivo de enquadramento identificado. | [f0](signed_unsigned2_png__faixas_gerais__f00.png) |
| signed_unsigned2.png / `reta_nibble` / 12 | [0, 799, 606, 1024] → [2, 802, 603, 1021] | **Aprovada com ressalva**. Unidade horizontal completa preservada; letras pequenas e amplo preenchimento neutro na projeção vertical. | [f0](signed_unsigned2_png__reta_nibble__f00.png) |
| signed_unsigned2.png / `linguagem_c` / 12 | [542, 612, 1104, 1024] → [545, 615, 1101, 1021] | **Aprovada com ressalva**. Contorno irregular: fragmento da reta vizinha à esquerda; redução retangular adicional cortaria o quadro principal. Ressalva estética explícita. | [f0](signed_unsigned2_png__linguagem_c__f00.png) |
| signed_unsigned2.png / `pontos_importantes` / 12 | [1100, 612, 1536, 1024] → [1103, 615, 1534, 1021] | **Aprovada na autoauditoria**. Título, conteúdo e relações preservados; nenhum defeito impeditivo de enquadramento identificado. | [f0](signed_unsigned2_png__pontos_importantes__f00.png) |

## Integridade e encerramento

Verificações: 12 originais conferidos com inventário e nomes exatos do catálogo; dimensões e SHA-256 calculados dos binários; IDs únicos por arquivo; 67 bboxes válidas; 81 nomes de projeção distintos; proporção e pixels conferidos contra nova renderização do JSON final. Todos os arquivos previamente versionados foram comparados por SHA-256 com a linha de base: permaneceram inalterados. O inventário e documentos de governança não foram editados. Scripts e quadros temporários de processamento ficaram fora do repositório.

Entrega pronta para revisão humana com as quatro pendências expressas. Não há homologação automática, seleção de regiões para vídeo, narração, MP4 ou alteração de catálogo.
