# Avaliação dos pilotos de catalogação semântica

**Estado:** execução experimental concluída; protocolo e catálogos sujeitos à avaliação humana. Não constitui homologação pedagógica.
**Base das fontes:** `725b9f4`.
**Protocolo proposto:** [protocolo_catalogacao_semantica.md](../protocolo_catalogacao_semantica.md).

## A. Implementação

O protocolo cobre finalidade, entradas/identificação, inspeção, evidência, contrato DOCX, vocabulário/relacionamentos, inconsistências, validação e revisões. Reutiliza AGENTS, inventário, vocabulário, mapa de relações, roteirização e retroalimentação. A remissão em AGENTS distingue revisão ordinária de reconstrução experimental com consulta posterior à referência. Não muda o contrato do Motor 1 nem cria identificadores ou cadastro semântico concorrente.

## B. Experimento do capítulo 04

- **Cobertura:** 35 materiais: 27 PNG, 1 JPEG, 3 GIF e 4 Markdown. Imagens abertas diretamente, textos lidos e todos os 42 estados dos GIFs examinados em ordem, por quadros. Não houve reprodução contínua temporizada nem compilação/execução dos códigos.
- **Isolamento:** o catálogo vigente e derivados não foram consultados durante a geração. A versão experimental foi congelada antes da extração da referência. O vocabulário foi projetado em termos/definições sem associações. Contexto anterior nesta conversa e conhecimento de P04-001 pelo checklist impedem caracterizar o teste como cego.
- **Comparação posterior:** ambos cobrem os mesmos 35 arquivos; referência com 39 etiquetas, experimental com 67, todas já existentes no mestre. Contagem não mede qualidade. Ambos têm glossário e reverso coerentes com suas atribuições.
- **Diferenças fundamentadas:** ordem de atribuição em `resumo2.png` e descrição de `typedef.jpeg` motivam C04-D-001/002. O experimental explicita ressalvas das fontes, inclusive P04-001, sem corrigi-las. A ficha experimental de `typedef.jpeg` poderia explicitar melhor a função de alias no corpo; a definição já aparece no glossário. Preservada a versão congelada, sem revisão posterior silenciosa.

## C. Piloto inaugural do capítulo 13

- **Escopo:** 24 arquivos físicos: 19 PNG, 4 Markdown e 1 ZIP. Imagens inspecionadas, textos lidos e cinco membros textuais do ZIP lidos integralmente, sem executar. O pacote tem nove membros: cinco arquivos e quatro diretórios.
- **Papéis:** enunciado de duas etapas, gabarito A, gabarito B e alternativa concisa de Makefile têm funções distintas; o ZIP é apoio às duas etapas. A sobreposição dos gabaritos não motivou remoções.
- **Inventário:** nenhuma linha do capítulo 13 no índice oficial. Proposta externa de 24 adições `modulo;arquivo`, sem membros internos ou catálogo experimental. Não aplicada. Eventual promoção de catálogo canônico requer decisão e linha próprias.
- **Vocabulário:** 40 etiquetas, sendo 27 existentes e 13 propostas locais fundamentadas. Estas distinguem, entre outros, dependência de compilação de relação pedagógica, biblioteca de ligação de biblioteca C, configuração de compilação de configuração da aplicação e montagem de código de montagem audiovisual. Mestre e relações homologadas preservados.

## D. Inconsistências e encaminhamento

[Checklist](../checklist.md): 13 novas ocorrências PENDENTES, 11 P e 2 D, com fontes, hashes, evidências e encaminhamentos. P04-001 permanece no registro anterior, sem duplicação ou mudança de estado.

Os casos incluem literal modificável indevidamente por `strtok`, variável não inicializada em conversão, identificação de `argc`, nomes distintos de macro, limpeza com `$^` vazio, regra incompatível com `src/`, dependências não consumidas e mudança de configuração sem reconstrução demonstrada. Não se atribuem esses problemas ao catálogo ou à geometria; nenhuma correção de fonte ou catálogo vigente foi implementada.

Limitações adicionais estão nas fichas e laudos: código visual denso não foi transcrito integralmente, exemplos de desempenho/tamanho são ilustrativos e pequenas ambiguidades de apresentação não foram elevadas a erros demonstrados. Não se auditou novamente o acervo nem se repetiu a certificação visual.

## E. Validação e evidências externas

Os dois DOCX foram reabertos, tiveram integridade ZIP verificada e foram convertidos por LibreOffice para PDF. A validação do documento serializado confirmou registros únicos, nomes físicos existentes, hashes, glossário completo sem duplicatas e índice reverso exato. Nomes e etiquetas aparecem nos PDFs. Inspeção visual amostral de quatro páginas do 04 e seis do 13: 04 com 19 páginas; 13 com 13 páginas. Sem corte ou sobreposição observado na amostra; fichas podem continuar na página seguinte.

Artefatos preservados **fora do checkout**, em `/workspace/artifacts/catalogacao-pilotos-04-13/`:

| Evidência | Caminho relativo à área de artefatos | SHA-256 |
| --- | --- | --- |
| Catálogo experimental 04 | `04/04_Catalogo_Semantico_Experimental.docx` | `b20c77dd8b4aba18552f4708e9758e23eb13a067e289f76fff5b4a6a0c4cd8b6` |
| Catálogo experimental 13 | `13/13_Catalogo_Semantico_Experimental.docx` | `04316c54f7de4d9e5eb3c0fc702736a260823e9d72d34fd550982f9ce5366aa0` |
| Laudo comparativo 04 | `04/Laudo_Comparacao.md` | Consultar `Manifesto_Artefatos.json` |
| Laudo inaugural 13 | `13/Laudo_Inaugural.md` | Consultar `Manifesto_Artefatos.json` |
| Relatório consolidado | `Relatorio_Consolidado.md` | Consultar `Manifesto_Artefatos.json` |
| Conciliação proposta, não aplicada | `13/Proposta_Adicoes_Inventario.csv` | Consultar `Manifesto_Artefatos.json` |
| Validações e congelamento | `Validacoes.json`; `04/congelamento.json` | Consultar `Manifesto_Artefatos.json` |

A entrega na conversa fornece links para esses arquivos reais e PDFs. A PR não hospeda os catálogos ou laudos experimentais; o acesso depende da preservação deste workspace. Não se presume download ou armazenamento duradouro na interface. Scripts temporários de geração, manifestos de fontes e quadros examinados permanecem nessa mesma área, fora do Git.

## F. Conclusão e limites

- **Capacidade de execução:** geração dos dois pilotos e verificações pertinentes concluídas.
- **Qualidade semântica observada:** descrições sustentadas, com diferenças e limites apresentados; revisão humana ainda necessária.
- **Compatibilidade documental:** DOCX e campos suficientes para avaliação pelo Motor 1, sem novo contrato. Não houve execução do Motor 1 ou produção de dossiê.
- **Homologação:** protocolo, catálogos, propostas terminológicas e correções pendentes não são aprovados automaticamente pela geração. Integração do protocolo não promove os catálogos experimentais ao acervo.

Materiais originais, catálogos vigentes, inventário, vocabulário, relações, motores e derivados foram preservados. A validação de preservação compara os arquivos rastreados com os hashes iniciais; o checklist recebeu somente acréscimo, mantendo integralmente decisões anteriores. Nenhuma etapa posterior foi iniciada.
