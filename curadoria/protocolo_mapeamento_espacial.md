# Protocolo de Mapeamento Espacial e Autoauditoria Visual

**Destino no repositório:** `curadoria/protocolo_mapeamento_espacial.md`  
**Estado:** proposta operacional para revisão e homologação humana  
**Escopo:** criação, refinamento, validação e manutenção de mapas espaciais JSON de imagens e GIFs do acervo didático.

## 1. Objetivo

Produzir, por capítulo, um **mapa espacial reutilizável** que identifique regiões visuais semanticamente significativas nos materiais originais e permita apresentá-las isoladamente, sem perda de conteúdo.

O mapa **não é uma lista de cortes de vídeo**. Ele descreve o que existe e onde está. A montagem audiovisual decide posteriormente quais regiões usar, em que ordem e por quanto tempo.

A qualidade esperada é a observada no experimento **Alpha 4**: enquadramentos que valorizam o conteúdo, respeitam os limites visuais dos quadros e preservam títulos, textos, expressões e diagramas. O Alpha 4 é uma **referência de resultado**, não uma fonte obrigatória de coordenadas, um gabarito universal ou uma homologação automática de todos os seus recortes.

> **Princípio central: primeiro preservar; depois enquadrar; por último otimizar.**
>
> **Na dúvida, preservar área adicional.** Margem excedente é preferível a texto, expressão ou elemento conceitual truncado.

## 2. Responsabilidades e fontes

| Artefato | Responsabilidade | Não deve determinar |
| --- | --- | --- |
| Imagem/GIF original | Conteúdo visual real, limites, quadros, textos, símbolos, relações gráficas | Narração ou duração de cena |
| Catálogo semântico do capítulo | Significado pedagógico, identificação dos conceitos e contexto | Coordenadas presumidas sem inspeção do original |
| Inventário e hashes | Identidade e integridade dos arquivos | Qualidade de enquadramento |
| Mapa espacial JSON | Regiões identificadas, descrições, coordenadas e rastreabilidade | Uso obrigatório, ordem ou duração no vídeo |
| Autoauditoria visual | Qualidade dos recortes realmente renderizados | Homologação editorial humana |
| Produção e revisão audiovisual | Seleção, duração, omissão, repetição e sincronização das projeções | Modificação automática do significado das regiões |

**Autoridade em caso de divergência:** para geometria e conteúdo visível, prevalece o arquivo original; para significado pedagógico, consultar o catálogo semântico e sinalizar divergências. Não “corrigir” silenciosamente um material ou o catálogo por meio de um recorte.

A execução deve consultar os arquivos reais do capítulo. **Não é aceitável inferir coordenadas apenas do texto do catálogo, do JSON anterior ou de uma miniatura.**

## 3. Entradas e saídas

**Entradas mínimas**
- Arquivos originais do capítulo, com nomes e dimensões.
- Catálogo semântico correspondente.
- Inventário e SHA-256 quando disponíveis.
- Mapa anterior, se houver, apenas como referência comparativa; nunca como substituto da imagem original.

**Saídas**
1. `NN_Mapa_Espacial.json`, com as regiões propostas ou revisadas.
2. **Painel de inspeção** que apresente os recortes renderizados, identificados por arquivo e ID da região, idealmente com a referência ao quadro original.
3. **Resumo de autoauditoria**: regiões examinadas, correções, ressalvas e pendências.
4. Estado explícito da entrega: `PROPOSTO`, `AUTOAUDITADO_COM_RESSALVAS` ou `AUTOAUDITADO_SEM_DEFEITOS_IDENTIFICADOS`. A homologação humana é registrada separadamente.

Nomes concretos de arquivos podem seguir as convenções do repositório. Não criar vídeos para testar recortes, salvo solicitação específica.

## 4. Sequência obrigatória de geração

### 4.1. Reconhecer o material original

1. Abrir a imagem em resolução adequada à inspeção; para GIFs, examinar os estados/quadros necessários para compreender o conteúdo e suas mudanças.
2. Identificar **unidades visuais completas**: painéis, caixas, bordas, fundos, divisórias, títulos, blocos de texto, expressões, tabelas, legendas, setas, diagramas e agrupamentos.
3. Confrontar essas unidades com o catálogo semântico: que conceito cada região representa? Que elementos precisam aparecer juntos para manter o sentido?
4. Distinguir **fronteiras visuais reais** de alinhamentos aproximados. O conteúdo não deve ser cortado só porque uma coordenada parece simétrica.
5. Se a relação entre elementos for essencial, preferir uma região que preserve a relação a vários recortes isolados que a tornem incompreensível.

### 4.2. Gerar a região primária — abrangente

1. Definir primeiro o **menor quadro visual completo** que contenha todos os elementos necessários, incluindo cabeçalho e margens de segurança.
2. Quando o material tiver painéis claramente separados, tomar essas divisórias como referência inicial; não atravessá-las arbitrariamente.
3. Se a fronteira não for clara, começar mais abrangente, não mais restrito.
4. Verificar que nenhuma letra, sinal, expoente, operador, borda relevante ou parte de diagrama esteja fora da área.
5. Registrar a região candidata com ID estável, descrição semântica e coordenadas.

**Proibido como estratégia inicial:** herdar um recorte estreito de uma versão anterior e reduzi-lo ainda mais sem voltar à imagem original. O defeito pode se acumular a cada revisão.

### 4.3. Refinamento redutivo — conservador

Partindo da região primária abrangente:

1. Identificar espaços comprovadamente dispensáveis (fundo vazio, margens desproporcionais ou área sem função visual).
2. Reduzir **gradualmente** os limites, sem modificar o conjunto de elementos essenciais.
3. Manter respiro suficiente para que títulos, expressões, bordas e demais elementos não pareçam comprimidos contra o enquadramento.
4. Se uma redução comprometer integridade ou contexto, **reverter à última região íntegra**.
5. Parar de reduzir quando o ganho de destaque não justificar o risco de perda de informação.

A meta **não** é obter a menor caixa possível. É obter o **melhor enquadramento íntegro**.

### 4.4. Renderizar a projeção real

Para **cada região candidata**:

1. Recortar a imagem original usando as coordenadas registradas.
2. Projetar o recorte no quadro de destino **vertical 9:16**, preservando a proporção.
3. **Ampliar proporcionalmente até o maior tamanho que caiba inteiro no quadro**; não deformar nem cortar conteúdo para preencher a tela.
4. Completar o espaço restante com fundo preto ou neutro.
5. Gerar uma imagem estática de inspeção, representativa do que o vídeo exibiria.

**Importante:** a inspeção deve usar o **mesmo algoritmo de recorte e projeção** previsto para a produção. Inspecionar uma caixa no original não substitui inspecionar o resultado em 9:16.

### 4.5. Autoauditar visualmente — obrigatório

Examinar **cada recorte efetivamente renderizado** e confrontá-lo com a região correspondente na imagem original. Não basta validar coordenadas numericamente.

**Checklist por região:**

- [ ] Título/cabeçalho completo e legível, quando pertencente ao quadro.
- [ ] Nenhuma palavra, linha, número ou símbolo cortado.
- [ ] Expressões e operadores lógicos/matemáticos completos (inclusive negações, parênteses, índices e sinais).
- [ ] Diagramas, tabelas, setas, legendas e relações visuais preservados.
- [ ] Bordas, separadores e fundos dos painéis respeitados quando relevantes à composição.
- [ ] Ausência de fragmentos indesejados de quadros vizinhos, quando for possível eliminá-los sem perda do conteúdo principal.
- [ ] Projeção 9:16 proporcional, sem distorção nem clipping.
- [ ] Conteúdo suficientemente destacado e legível, sem redução excessiva para acomodar uma área dispensável.
- [ ] Identidade do arquivo original e correspondência semântica da região verificadas.

**Ordem de prioridade em caso de conflito:**

1. Integridade de textos, símbolos e elementos conceituais.
2. Preservação das relações semânticas e da unidade visual.
3. Legibilidade no enquadramento de destino.
4. Separação estética de quadros e eliminação de resíduos.
5. Centralização e otimização de margens.

Uma expressão incompleta **reprova o recorte**, ainda que ele esteja visualmente centralizado. Uma margem adicional pode ser aceita se for necessária para preservar o conteúdo.

### 4.6. Corrigir e reinspecionar

Quando houver defeito:

1. Identificar o arquivo, a região, o tipo de falha e sua localização.
2. Voltar ao **original completo** e à região primária abrangente; não ajustar cegamente a imagem já recortada.
3. Corrigir a caixa candidata, priorizando **ampliação** quando houver conteúdo truncado.
4. Renderizar novamente **a região alterada** e reinspecioná-la.
5. Se o problema persistir, tentar outro enquadramento que preserve o conceito; se não houver solução confiável, registrar ressalva e seguir para os demais materiais.

Evitar ciclos ilimitados: uma rodada inicial e refinamentos dirigidos por defeitos observáveis. Se as tentativas deixarem de produzir melhoria verificável, classificar como pendente em vez de declarar sucesso.

**A autoauditoria deve ser real e demonstrável.** Um script que apenas verifica `0 <= x0 < x1 <= 1` não constitui autoauditoria visual. Se o ambiente não permitir abrir/inspecionar as imagens renderizadas, registrar a limitação e **não** afirmar que os recortes foram visualmente validados.

### 4.7. Consolidar o JSON final e as evidências

- Atualizar somente as regiões que necessitaram de correção; preservar IDs e significado das demais.
- Conferir novamente dimensões, coordenadas e identidade do arquivo.
- Gerar painel final a partir do **JSON efetivamente entregue**, não de uma versão intermediária.
- Registrar defeitos encontrados, mudanças realizadas e ressalvas remanescentes.
- Apresentar para homologação humana. **Autoauditoria não equivale a aprovação editorial.**

## 5. Contrato mínimo do JSON

O formato deve preservar compatibilidade com o mapa experimental do capítulo 01, sempre que possível. Campos existentes incluem:

```json
{
  "schema": "mapa_espacial_capitulo",
  "versao": "identificador-da-versao",
  "capitulo": "NN_Nome_do_Capitulo",
  "fonte_semantica": "NN_Catalogo_Semantico.docx",
  "sistema_coordenadas": "[x0,y0,x1,y1] normalizado entre 0 e 1, origem no canto superior esquerdo",
  "estado": "PROPOSTO",
  "materiais": [
    {
      "arquivo": "imagem.png",
      "tipo": "png",
      "dimensoes_px": [1312, 1199],
      "sha256": "hash-real-do-arquivo",
      "regioes": [
        {
          "id": "conclusao",
          "descricao": "Unidade visual de conclusão",
          "bbox_normalizada": [0.65, 0.54, 0.99, 0.98],
          "confianca": "preliminar_inspecao_visual"
        }
      ]
    }
  ]
}
```

**Os valores numéricos acima são exclusivamente ilustrativos**, não coordenadas recomendadas para qualquer material.

Regras mínimas:

- Coordenadas normalizadas `[x0, y0, x1, y1]`, com origem no canto superior esquerdo e `0 <= x0 < x1 <= 1`, `0 <= y0 < y1 <= 1`.
- IDs de regiões **estáveis dentro de cada arquivo**; a referência inequívoca é a combinação **capítulo + arquivo + ID**. Não renumerar IDs por ordem de apresentação audiovisual.
- `descricao` explica a unidade semântica, não apenas sua posição (“caixa da direita”).
- Hashes devem ser **calculados dos binários reais**, nunca inventados. Se indisponíveis, registrar a ausência.
- O JSON deve representar o **acervo disponível**, não apenas as regiões escolhidas para um vídeo específico.
- Informações de autoauditoria podem ser mantidas em relatório separado; **não é necessário alterar o esquema JSON** só para registrar cada tentativa de ajuste.
- Se o conteúdo original mudar, verificar hash e revisar as regiões afetadas antes de reutilizá-las.

## 6. Tratamento de GIFs e materiais heterogêneos

Os mesmos princípios de integridade valem para GIFs, mas uma caixa espacial pode ser adequada em um instante e inadequada em outro.

- Inspecionar estados representativos, incluindo aparecimento/desaparecimento de textos, objetos ou destaques.
- Quando uma região muda ao longo do GIF, registrar o limite temporal ou o estado relevante **se o formato já permitir**; caso contrário, documentar a limitação e propor uma extensão específica, sem inventar precisão temporal.
- Não pressupor que todos os materiais tenham grade, borda ou divisão retangular explícita.
- Não impor número fixo de regiões por arquivo ou capítulo.
- Para imagens com conteúdo não separável, é aceitável uma região abrangente ou o quadro inteiro.

A regra de integridade prevalece sobre a tentativa de fragmentar toda imagem em múltiplos recortes.

## 7. Classificação da autoauditoria e entrega

| Resultado por região | Critério |
| --- | --- |
| **Aprovada na autoauditoria** | Recorte renderizado e inspecionado; nenhum defeito impeditivo identificado |
| **Aprovada com ressalva** | Conteúdo essencial íntegro, mas há limitação visual documentada |
| **Pendente** | Corte de conteúdo, dúvida semântica relevante ou impossibilidade de inspeção suficiente |

O relatório final deve resumir:

- Quantos arquivos e regiões foram mapeados.
- Quantas regiões foram renderizadas e efetivamente inspecionadas.
- Quais regiões foram corrigidas, com indicação sucinta do defeito.
- Quais ressalvas/pendências permanecem.
- Quais ferramentas/etapas de inspeção foram efetivamente executadas.
- Se a entrega aguarda homologação humana.

Não declarar aprovação geral se houver regiões não inspecionadas. A homologação do responsável editorial é um ato distinto.

## 8. Exemplo de aprendizado — Alphas 2, 3 e 4

**Alpha 2:** os recortes demonstraram que a seleção semântica e o ritmo visual funcionavam, mas a inspeção revelou cabeçalhos cortados, partes de quadros vizinhos e margens inadequadas.

**Alpha 3:** a tentativa de refinar geometricamente algumas caixas produziu um recorte final estreito demais, truncando textos e uma expressão lógica. **Lição:** reduzir a caixa não significa melhorar o recorte; ajustes sucessivos não podem substituir a inspeção do original.

**Alpha 4:** retomou-se uma base espacial mais abrangente e aplicou-se a sequência **quadro completo → redução conservadora → projeção 9:16 → inspeção**. O resultado foi considerado satisfatório na revisão humana do experimento.

**Generalização válida:** preservar integralidade e limites visuais do painel antes de buscar destaque estético. **Generalização inválida:** copiar coordenadas, quantidade de recortes ou composição do Alpha 4 para outros capítulos.

## 9. Independência da montagem e revisão editorial

O mapa é **inclusivo e generalista**. A existência de uma região não obriga seu uso em vídeo.

Etapas posteriores poderão:
- Manter uma região em tela por mais tempo, inclusive atravessando intervalos antes destinados a outra.
- Omitir, repetir, encurtar, substituir ou reorganizar projeções.
- Sincronizar imagens com narração e SRT.

Essas decisões **não invalidam o mapa espacial** e não exigem remover regiões do JSON. O mapa não contém, como obrigação, duração de cena, cronograma de cortes ou ordem audiovisual. O contrato específico de revisão editorial será definido futuramente.

## 10. Limites de autonomia e manutenção

- Executar autonomamente o ciclo de proposição, renderização, inspeção e correção **dentro do escopo autorizado**.
- Não editar imagens originais, catálogos semânticos ou materiais pedagógicos para “facilitar” o recorte sem autorização.
- Não declarar sucesso quando faltar acesso aos binários ou capacidade de inspeção.
- Registrar incertezas sem gerar ciclos de verificação indefinidos.
- Apresentar JSON, evidências e pendências para decisão humana antes de considerar o mapa homologado.
- Seguir as regras do `AGENTS.md` quanto a alterações no repositório, commits, push, PRs e aprovações. Este protocolo não autoriza publicação automática.

## 11. Critério de conclusão

O trabalho de mapeamento espacial está pronto **para homologação** quando:

1. As unidades visuais foram identificadas a partir dos originais e confrontadas com o catálogo.
2. As caixas foram geradas de forma abrangente e refinadas apenas quando seguro.
3. Cada região entregue foi renderizada em 9:16 e inspecionada visualmente.
4. Defeitos impeditivos foram corrigidos ou explicitamente classificados como pendências.
5. O painel final corresponde ao JSON entregue.
6. Os IDs e vínculos com arquivos originais são rastreáveis.
7. A entrega não impõe escolhas de montagem ou publicação.

**Regra de ouro:** um recorte bonito que corta uma ideia está errado. Um recorte um pouco mais abrangente que preserva a ideia é preferível.
