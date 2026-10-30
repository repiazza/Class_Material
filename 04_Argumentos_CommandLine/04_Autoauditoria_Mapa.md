# Autoauditoria espacial — capítulo 04

Estado: AUTOAUDITADO_COM_RESSALVAS. Mapa 1.0 experimental, sem homologação humana.

Foram inspecionados diretamente os 28 originais estáticos e todos os 42 quadros dos três GIFs (14, 16 e 12). As 253 regiões de 31 materiais foram projetadas em 1080 × 1920, com proporção preservada e fundo neutro, e examinadas nos 32 painéis. Markdown, exercícios e gabaritos não são fontes visuais do mapa. A cobertura é inclusiva e independente de V04-004.

## Geometria e evidências

Os painéis `evidencias_mapa_espacial/painel-01.jpg` a `painel-32.jpg` mostram todas as projeções finais; cada posição corresponde ao registro de `autoauditoria.json`. Foram corrigidas 32 caixas que truncavam cabeçalhos, texto ou bordas. Duas caixas de `cmdline_standard2.png` precisaram de um segundo ajuste. Os registros anterior/corrigido permitem verificar cada intervenção. As projeções alteradas foram reinspecionadas após a correção; as regiões válidas foram preservadas.

Ressalva V: visões integrais, diagramas largos, tabelas extensas e código denso podem apresentar letras pequenas em 9:16. Servem para contexto, não pressupõem leitura integral no vídeo. Margens e fragmentos de painéis adjacentes foram conservados quando não impedem a unidade principal. O mapa não determina utilização, duração ou sequência.

Nos GIFs, os painéis representam o último quadro. Os estados originais foram examinados integralmente; isso não equivale a reproduzir todas as 253 projeções como animações. Em `argumentos_processos.gif`, `relacao_processos` e `explicacao_estado` são evidenciadas no estado final, quadro 13; para outras etapas, usar `conteudo_estado`/`integral` ou verificar a região no estado pretendido. Os demais GIFs mantêm painéis fixos de código, memória/configuração, explicação e terminal. A montagem deve registrar qualquer seleção temporal.

## Ocorrências nas fontes, sem correção automática

- **P04-001 — PENDENTE, defeito do original:** `strtok_execucao_tokens.gif`, quadro 3 (9 s), exibe todos os delimitadores já substituídos por `\0` na primeira tokenização. `strtok` altera o delimitador que encerra o token retornado naquela chamada; os demais delimitadores só são substituídos quando alcançados por chamadas posteriores. O estado final é compatível com a tokenização concluída, mas a evolução intermediária antecipa alterações. Evidência: [quadro original](evidencias_mapa_espacial/P04-001-strtok-quadro03.png). Não integra V04-004; original preservado, correção depende de deliberação humana.
- **Limite interpretativo preservado:** `resumo2.png/ordem_aplicacao_valores` mostra a atribuição incremental padrão → ambiente → argumentos. A busca com maior prioridade primeiro é outra forma de implementar a mesma política, exibida em `env4.png/fluxo_precedencia`. Não confundir a ordem de atribuição com a ordem de consulta. Nenhuma fonte foi redesenhada.

A inspeção espacial não homologa código ou explicações dos originais. Não foi realizada auditoria técnica geral do capítulo, nem correção documental do catálogo. A autoauditoria não substitui revisão humana.

## Painéis finais para revisão humana

[01](evidencias_mapa_espacial/painel-01.jpg) · [02](evidencias_mapa_espacial/painel-02.jpg) · [03](evidencias_mapa_espacial/painel-03.jpg) · [04](evidencias_mapa_espacial/painel-04.jpg) · [05](evidencias_mapa_espacial/painel-05.jpg) · [06](evidencias_mapa_espacial/painel-06.jpg) · [07](evidencias_mapa_espacial/painel-07.jpg) · [08](evidencias_mapa_espacial/painel-08.jpg) · [09](evidencias_mapa_espacial/painel-09.jpg) · [10](evidencias_mapa_espacial/painel-10.jpg) · [11](evidencias_mapa_espacial/painel-11.jpg) · [12](evidencias_mapa_espacial/painel-12.jpg) · [13](evidencias_mapa_espacial/painel-13.jpg) · [14](evidencias_mapa_espacial/painel-14.jpg) · [15](evidencias_mapa_espacial/painel-15.jpg) · [16](evidencias_mapa_espacial/painel-16.jpg) · [17](evidencias_mapa_espacial/painel-17.jpg) · [18](evidencias_mapa_espacial/painel-18.jpg) · [19](evidencias_mapa_espacial/painel-19.jpg) · [20](evidencias_mapa_espacial/painel-20.jpg) · [21](evidencias_mapa_espacial/painel-21.jpg) · [22](evidencias_mapa_espacial/painel-22.jpg) · [23](evidencias_mapa_espacial/painel-23.jpg) · [24](evidencias_mapa_espacial/painel-24.jpg) · [25](evidencias_mapa_espacial/painel-25.jpg) · [26](evidencias_mapa_espacial/painel-26.jpg) · [27](evidencias_mapa_espacial/painel-27.jpg) · [28](evidencias_mapa_espacial/painel-28.jpg) · [29](evidencias_mapa_espacial/painel-29.jpg) · [30](evidencias_mapa_espacial/painel-30.jpg) · [31](evidencias_mapa_espacial/painel-31.jpg) · [32](evidencias_mapa_espacial/painel-32.jpg)
