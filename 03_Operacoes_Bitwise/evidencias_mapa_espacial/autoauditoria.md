# Autoauditoria espacial — capítulo 03

**Estado: AUTOAUDITADO_COM_RESSALVAS. Homologação humana: PENDENTE.**

[Abrir painel navegável com todas as projeções](painel_inspecao.html) · [Visão geral dos 18 originais](painel_geral.jpg) · [Mapa entregue](../03_Mapa_Espacial.json) · [Resultados por região](autoauditoria_regioes.json)

## Resultado e escopo

Base sincronizada com main: 58a0d4a77fe15bfa97fc2f0689a9637952842752. Mapeamento inclusivo dos 18 materiais visuais: 13 PNGs e cinco GIFs, sem restrição às mídias de V03-003. Exercício/gabarito são documentos textuais, sem regiões espaciais; não foram alterados. Catálogo lido integralmente (corpo e verificação de ausência de tabelas), inventário e termos pertinentes do vocabulário consultados.

123 regiões, 215 projeções 1080×1920 e 62 painéis de inspeção. Todas as regiões e todas as projeções foram examinadas visualmente nos painéis, comparadas aos originais; dúvidas pontuais também foram abertas em quadro original completo/ampliado. Não há região não inspecionada. Foram inspecionados todos os 37 quadros decodificados dos GIFs, não somente o primeiro/último. Não houve vídeo nem inspeção de playback contínuo: os estados e metadados temporais foram conferidos estaticamente.

Resultado espacial por região: 52 aprovadas na autoauditoria sem ressalva específica e 71 com ressalva visual e/ou de conteúdo de origem. Zero pendências geométricas impeditivas identificadas. Aprovação espacial não certifica a correção pedagógica da fonte. Os registros P/D abaixo permanecem PENDENTES para deliberação, e podem impedir uso de certas regiões em produção sem invalidar o acervo espacial íntegro.

## Método, refinamento e reprodutibilidade

As caixas foram definidas pela inspeção dos originais, usando painéis completos e preservando títulos, símbolos, bordas e relações. Cada caixa primária abrangente admitia até oito pixels adicionais em cada lado; o refinamento conservador retirou somente faixas de margem junto às divisórias. Caixas primárias e finais em pixels estão em refinamentos.json. Nenhuma caixa foi herdada dos mapas 01/02; somente a convenção do JSON foi consultada. Nenhum refinamento foi usado para esconder erro de origem.

Todas as projeções efetivas foram renderizadas e inspecionadas. Não foi identificado defeito geométrico impeditivo que exigisse uma rodada posterior de correção; não se registra correção fictícia. Pequenos resíduos de bordas vizinhas permaneceram quando não prejudicam a unidade, especialmente get_bits2.png/resumo e mascara_bitwise.png/valor_original. Visões integrais e faixas largas ficam inclusivas, com ressalva de leitura pequena em telefone; não foram reprovadas nem deformadas para preencher 9:16.

Algoritmo de renderizar.py: converter coordenadas por round(normalizado×dimensão), caixa exclusiva de Pillow, RGB, recorte integral, escala Lanczos pelo menor fator 1080/largura e 1920/altura, centralização com fundo RGB(22,22,22). O produtor futuro deve usar esse algoritmo ou demonstrar equivalência antes de reutilizar a validação. PNGs individuais não têm rótulos sobrepostos; identificação está nos painéis e no índice. Painéis finais usam as mesmas caixas do JSON entregue; a alteração posterior do campo de confiança não modificou a geometria nem os pixels inspecionados.

Reprodução: `python 03_Operacoes_Bitwise/evidencias_mapa_espacial/renderizar.py --saida /tmp/mapa03-reproducao`. Não sobrescrever originais. A ferramenta confere hashes e dimensões de entrada. Ferramentas desta execução: Python 3.12.14, Pillow 12.3.0 e view_image para inspeção visual. Não se usou geração de imagem ou OCR como substituto da inspeção.

## Cobertura por material

| Original | Regiões | Quadros inspecionados | Projeções | Painéis finais |
|---|---:|---|---:|---|
| [bitwise_10_12_em_C.gif](../bitwise_10_12_em_C.gif) | 3 | 0–6 | 21 | [1](painel_bitwise_10_12_em_C_01.jpg) · [2](painel_bitwise_10_12_em_C_02.jpg) · [3](painel_bitwise_10_12_em_C_03.jpg) · [4](painel_bitwise_10_12_em_C_04.jpg) · [5](painel_bitwise_10_12_em_C_05.jpg) · [6](painel_bitwise_10_12_em_C_06.jpg) |
| [bitwise_deslocamento.gif](../bitwise_deslocamento.gif) | 2 | 0–4 | 10 | [1](painel_bitwise_deslocamento_01.jpg) · [2](painel_bitwise_deslocamento_02.jpg) · [3](painel_bitwise_deslocamento_03.jpg) |
| [bitwise_mascaras.gif](../bitwise_mascaras.gif) | 3 | 0–5 | 18 | [1](painel_bitwise_mascaras_01.jpg) · [2](painel_bitwise_mascaras_02.jpg) · [3](painel_bitwise_mascaras_03.jpg) · [4](painel_bitwise_mascaras_04.jpg) · [5](painel_bitwise_mascaras_05.jpg) |
| [bitwise_not.png](../bitwise_not.png) | 10 | 0 | 10 | [1](painel_bitwise_not_01.jpg) · [2](painel_bitwise_not_02.jpg) · [3](painel_bitwise_not_03.jpg) |
| [bitwise_shift.png](../bitwise_shift.png) | 9 | 0 | 9 | [1](painel_bitwise_shift_01.jpg) · [2](painel_bitwise_shift_02.jpg) · [3](painel_bitwise_shift_03.jpg) |
| [bitwise_shift2.png](../bitwise_shift2.png) | 7 | 0 | 7 | [1](painel_bitwise_shift2_01.jpg) · [2](painel_bitwise_shift2_02.jpg) |
| [bitwise_shift3.png](../bitwise_shift3.png) | 7 | 0 | 7 | [1](painel_bitwise_shift3_01.jpg) · [2](painel_bitwise_shift3_02.jpg) |
| [bitwise_shift_em_c.gif](../bitwise_shift_em_c.gif) | 3 | 0–8 | 27 | [1](painel_bitwise_shift_em_c_01.jpg) · [2](painel_bitwise_shift_em_c_02.jpg) · [3](painel_bitwise_shift_em_c_03.jpg) · [4](painel_bitwise_shift_em_c_04.jpg) · [5](painel_bitwise_shift_em_c_05.jpg) · [6](painel_bitwise_shift_em_c_06.jpg) · [7](painel_bitwise_shift_em_c_07.jpg) |
| [get_bits.png](../get_bits.png) | 7 | 0 | 7 | [1](painel_get_bits_01.jpg) · [2](painel_get_bits_02.jpg) |
| [get_bits2.png](../get_bits2.png) | 10 | 0 | 10 | [1](painel_get_bits2_01.jpg) · [2](painel_get_bits2_02.jpg) · [3](painel_get_bits2_03.jpg) |
| [getbits.gif](../getbits.gif) | 3 | 0–9 | 30 | [1](painel_getbits_01.jpg) · [2](painel_getbits_02.jpg) · [3](painel_getbits_03.jpg) · [4](painel_getbits_04.jpg) · [5](painel_getbits_05.jpg) · [6](painel_getbits_06.jpg) · [7](painel_getbits_07.jpg) · [8](painel_getbits_08.jpg) |
| [mascara_bitwise.png](../mascara_bitwise.png) | 10 | 0 | 10 | [1](painel_mascara_bitwise_01.jpg) · [2](painel_mascara_bitwise_02.jpg) · [3](painel_mascara_bitwise_03.jpg) |
| [mascara_bitwise2.png](../mascara_bitwise2.png) | 9 | 0 | 9 | [1](painel_mascara_bitwise2_01.jpg) · [2](painel_mascara_bitwise2_02.jpg) · [3](painel_mascara_bitwise2_03.jpg) |
| [mascara_bitwise3.png](../mascara_bitwise3.png) | 9 | 0 | 9 | [1](painel_mascara_bitwise3_01.jpg) · [2](painel_mascara_bitwise3_02.jpg) · [3](painel_mascara_bitwise3_03.jpg) |
| [mascara_bitwise4.png](../mascara_bitwise4.png) | 8 | 0 | 8 | [1](painel_mascara_bitwise4_01.jpg) · [2](painel_mascara_bitwise4_02.jpg) |
| [operacao_bit_a_bit.png](../operacao_bit_a_bit.png) | 7 | 0 | 7 | [1](painel_operacao_bit_a_bit_01.jpg) · [2](painel_operacao_bit_a_bit_02.jpg) |
| [operadores_bitwise.png](../operadores_bitwise.png) | 9 | 0 | 9 | [1](painel_operadores_bitwise_01.jpg) · [2](painel_operadores_bitwise_02.jpg) · [3](painel_operadores_bitwise_03.jpg) |
| [xor.png](../xor.png) | 7 | 0 | 7 | [1](painel_xor_01.jpg) · [2](painel_xor_02.jpg) |

GIFs: bitwise_10_12_em_C — sete estados de declaração/AND/printf, 14 s; bitwise_deslocamento — cinco estados 3→6→12→6→3, 10 s; bitwise_mascaras — seis estados de alvo, máscara, teste, alternância, limpeza e ativação, 18 s; bitwise_shift_em_c — nove estados sincronizados com código/terminal, 18 s; getbits — dez estados de decomposição, 30 s (divergência com cabeçalho registrada). As caixas de cada GIF mantêm a união espacial dos elementos em todos os seus estados. A seleção de um quadro isolado pode requerer contexto que está no original integral; o mapa não fixa uma seleção audiovisual.

## Ressalvas e ocorrências nas fontes

Estas ocorrências foram detectadas incidentalmente durante o reconhecimento, não constituem auditoria pedagógica exaustiva. A classificação P/D é distinta de G (geometria) e V (ressalva visual). As propostas formais e estados estão no [checklist](../../curadoria/checklist.md); a relação a seguir fornece evidência espacial e encaminhamento, sem cadastro de decisão concorrente.

### M03-P-001 — P — bitwise_not.png

Regiões: interpretacao; complemento_dois.

**Evidência:** A coluna signed do painel 4 mostra um glifo ~ antes de 11; o painel 5 também imprime 1111 0101₂ = ~11₁₀, enquanto sua própria conta conclui -11. O sinal do valor negativo fica ambíguo/incorreto na fonte.

**Encaminhamento proposto, sem execução:** Submeter à revisão gráfica/pedagógica a distinção de til e sinal de menos; não substituir o PNG nesta etapa.

**Impacto:** Pode afetar a futura escolha de painéis para V03-003; a região exemplo_8_bits continua geometricamente válida. Não se modifica roteiro nem se decide montagem.

**Confiança:** alta para a divergência gráfica, média para intenção do glifo.

### M03-P-002 — P — mascara_bitwise3.png

Regiões: valor_original; aplicacao_xor.

**Evidência:** O original 0xAC=10101100 tem bits 2 e 1 em 1 e 0, mas o painel 2 afirma 1 e 1. O painel 4 desenha resultado 10100000; 0xAC XOR 0x06 é 10101010 (0xAA), conforme o terminal e a legenda do próprio painel 6.

**Encaminhamento proposto, sem execução:** Revisar coerência dos bits, agrupamentos e resultado na fonte, após deliberação. Preservar o recorte e o terminal correto.

**Impacto:** Restringe reutilização não qualificada desses dois painéis em propostas sobre alternância, incluindo V03-007.

**Confiança:** alta.

### M03-P-003 — P — mascara_bitwise4.png

Regiões: desligar_and_not.

**Evidência:** No painel de desligar o bit 2, a linha Depois (&) desenha 00001110, mas informa decimal 10/0x0A e afirma ter zerado o bit 2. Com 00001010 & 11111011 o padrão esperado é 00001010.

**Encaminhamento proposto, sem execução:** Submeter a linha binária inconsistente à correção do original; não alterar por recorte.

**Impacto:** Afeta demonstrações de limpeza, como o suporte de V03-006, sem invalidar os demais painéis.

**Confiança:** alta.

### M03-P-004 — P — get_bits.png

Regiões: outros_exemplos.

**Evidência:** Na tabela do painel 5, a linha Bit único usa p=2 e n=1 e informa resultado 2/0x02; um campo de um bit só pode resultar em 0 ou 1, e o bit 2 de 0xB2 é 0. A mesma linha contém um dígito 2 dentro do desenho dos bits.

**Encaminhamento proposto, sem execução:** Encaminhar revisão da tabela e de seus desenhos, preservando o PNG e as demais regiões nesta etapa.

**Impacto:** Afeta eventual seleção desse quadro em V03-008; não confundir com defeito geométrico.

**Confiança:** alta.

### M03-P-005 — P — get_bits2.png; getbits.gif

Regiões: Regiões que incluem a expressão e a construção da máscara; GIF em todos os quadros com código.

**Evidência:** A expressão em C usa ~(~0 << n), sem sufixo unsigned no literal. Em implementações de complemento de dois, ~0 é int negativo; o deslocamento à esquerda de valor signed negativo tem comportamento indefinido em C11/C17. O retorno unsigned não torna unsigned os intermediários. O PNG afirma que ~0 já gera o valor na largura do tipo unsigned.

**Encaminhamento proposto, sem execução:** Deliberar a revisão do código/texto quanto a tipo sem sinal e limites válidos; não executar código nem substituir silenciosamente expressões.

**Impacto:** Não reutilizar como código C portátil validado; pode repercutir em V03-008. O mapa preserva integralmente o que está na fonte.

**Confiança:** alta para o risco sob C11/C17; nenhuma versão C foi executada/certificada.

### M03-P-006 — P — get_bits2.png; getbits.gif

Regiões: ordem_apresentada; calculo_posicao; operacao_e_resultado; outras regiões que exibem a sequência.

**Evidência:** O PNG rotula uma sequência de subexpressões como Ordem de avaliação (precedência) e diz que p+1-n é avaliado primeiro; o GIF apresenta ordem fixa por precedência. Precedência/parentetização não estabelecem essa ordem geral entre os operandos de &.

**Encaminhamento proposto, sem execução:** Deliberar distinção entre ordem didática de apresentação e ordem de avaliação da linguagem, sem modificar os arquivos nesta PR.

**Impacto:** A produção futura deve preservar a ressalva já presente na proposta V03-008; a geometria não corrige a afirmação do original.

**Confiança:** alta.

### M03-P-007 — P — getbits.gif

Regiões: integral.

**Evidência:** O cabeçalho informa 2,5 s por etapa, mas cada um dos dez quadros tem duração codificada de 3000 ms: ciclo de 30 s.

**Encaminhamento proposto, sem execução:** Encaminhar discrepância texto/temporização ao responsável pelo GIF; usar os tempos codificados se futuramente autorizado reproduzir a animação.

**Impacto:** Afeta sincronismo futuro, sem demandar alteração das caixas espaciais.

**Confiança:** alta.

### M03-D-001 — D — mascara_bitwise.png / registro no 03_Catalogo_Semantico.docx

Regiões: objetivo; mascara; aplicacao; exemplo_c.

**Evidência:** O registro afirma uso de AND para consultar o estado de um bit e construção por posição. O PNG efetivo exemplifica preservação dos quatro bits inferiores com 0x0F: 0xAD & 0x0F = 0x0D, não uma consulta de posição única.

**Encaminhamento proposto, sem execução:** Proposta documental mínima para deliberação: antes — Demonstra o uso de AND para consultar o estado de um bit; depois — Demonstra o uso de AND para preservar os quatro bits menos significativos de um valor de oito bits, zerando os demais com a máscara 0x0F. Ajustar também a referência visual à máscara do nibble, em vez de atribuir construção por posição ao exemplo. Não alterar catálogo/glossário nesta PR.

**Impacto:** Reavaliar apenas referências que dependam dessa descrição, por exemplo a função proposta dessa mídia em V03-005; demais fontes do candidato podem sustentar o teste de bit. Preservar regiões espacialmente válidas.

**Confiança:** alta.

## Validação e limites de continuidade

Verificações automáticas: JSON legível; 18 fontes exatamente correspondentes aos visuais do capítulo e ao inventário; hashes/dimensões reais; coordenadas válidas e IDs únicos por material; 123 caixas reproduzíveis; 215 PNGs decodificáveis e com 1080×1920; cobertura de todos os pares região/quadro, sem falta ou duplicação; índice, painéis e links locais íntegros. Comparação pixel a pixel das projeções com o recorte/projeção recalculado das fontes confirma correspondência ao JSON final. Essas verificações complementam, não substituem, as 62 inspeções visuais dos painéis.

Hashes do baseline confirmam preservação de todos os arquivos preexistentes, exceto a adição delimitada de ocorrências ao checklist. Originais, catálogo, dossiê, roteiro, inventário, AGENTS.md e protocolos não foram modificados. A única alteração fora do diretório do mapa é esse registro de rastreabilidade exigido pelo protocolo de retroalimentação, sem reestruturar o histórico.

Nenhum mapa ou recorte está homologado por esta entrega. O problema numérico e gráfico de uma região de origem não implica que outro painel correto do mesmo PNG esteja inválido; a montagem futura deverá confrontar os IDs efetivamente escolhidos com as ressalvas. Não houve nova redação do roteiro V03-003 nem escolha antecipada de suas regiões. Nenhum vídeo foi gerado.
