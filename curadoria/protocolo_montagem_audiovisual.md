# Protocolo de montagem audiovisual

**Destino:** `curadoria/protocolo_montagem_audiovisual.md`  
**Estado:** proposta sujeita à homologação humana.

## 1. Objetivo e responsabilidades

Transformar um roteiro individual em plano de montagem reproduzível, associando falas, regiões visuais, sequência e duração. A montagem não é nova roteirização nem nova curadoria dos materiais originais.

- **Dossiê:** origem e fundamentação editorial do candidato.
- **Roteiro individual:** fonte principal da narrativa, falas, tese, ressalvas e ordem lógica.
- **Mapa espacial:** acervo inclusivo de regiões, identificadores, geometria e evidências; não determina seleção, ordem ou duração.
- **Originais PNG/GIF:** fonte do conteúdo visual real e dos estados temporais.
- **Plano de montagem:** escolhas específicas de um vídeo, sem modificar as fontes.
- **Protocolo de retroalimentação:** tratamento de divergências encontradas durante a montagem.

O `AGENTS.md` continua responsável pela governança, autorização e integração Git.

## 2. Entrada e pré-condições

O comando `Preparar montagem VNN-XXX` identifica o vídeo e exige:
1. Roteiro `editorial/roteiros/NN-XXX_Roteiro_Individual.docx`, lido integralmente, incluindo tabelas.
2. Mapa `NN_Mapa_Espacial.json` do capítulo, com regiões verificáveis.
3. Acesso aos originais usados.
4. Estado conhecido das aprovações e pendências. Arquivo existente ou PR aberta não equivale a homologação.

Registrar caminhos e commit ou hash das fontes efetivamente usadas. Se uma fonte estiver em branch ou PR, identificar sua revisão e verificar compatibilidade com as demais.

Preparar montagem não autoriza publicar vídeo nem alterar os originais.

## 3. Autoridade do roteiro e liberdade editorial

Preservar tese, conteúdo técnico, ressalvas, texto de fala e ordem pedagógica do roteiro.

A montagem pode:
- Selecionar, omitir ou repetir regiões do mapa.
- Alternar detalhe e visão geral, dividir falas entre regiões e ajustar duração.
- Inserir pausas visuais e fundos neutros quando úteis.
- Selecionar estados estáticos ou trechos animados dos GIFs, respeitando sua sequência real.
- Ajustar o ritmo sem modificar o significado das falas.

A montagem não pode:
- Reescrever explicações, alterar conceitos ou suprimir ressalvas sem autorização.
- Atribuir a um arquivo elementos presentes somente em outro.
- Alterar coordenadas do mapa silenciosamente.
- Ocultar defeitos relevantes do original ou alegar aprovação humana inexistente.

Ajustes de tempo e escolha visual são ordinários; mudanças de conteúdo pedagógico exigem deliberação.

## 4. Seleção e preservação visual

Para cada trecho, identificar sua função didática e selecionar regiões reais que a sustentem. Conferir o original e os quadros relevantes do GIF sempre que a correspondência não estiver demonstrada.

**Primeiro preservar, depois enquadrar, por último otimizar.** Preferir a menor região completa e inteligível, não a caixa numericamente mais estreita. Preservar títulos, fórmulas, bordas, legendas e relações conceituais. Margens e pequenos fragmentos de painéis vizinhos são aceitáveis conforme o protocolo espacial.

Não reprovar uma região integral apenas porque uma região de detalhe funciona melhor na montagem.

Para GIFs, diferenciar reprodução animada, quadro estático e sequência editorial de estados. Não inferir mudanças de valores ou ações inexistentes.

## 5. Plano de montagem por vídeo

Produzir `editorial/montagens/NN-XXX_Montagem.json` com o ID correspondente ao roteiro, sem `V` no nome do arquivo, salvo contrato vigente diferente.

O plano deve registrar:
- `schema_version`, `video_id`, formato previsto (por padrão 1080×1920, 9:16) e estado (`PROPOSTO`, `PENDENTE_REVISAO` ou `APROVADO`, este último somente por homologação humana).
- Fontes: caminhos, revisões e referências verificáveis.
- Modalidade de áudio: gravação humana, referência sintética ou indefinida.
- Segmentos com ID estável, cena/take, vínculo com fala, início e duração em milissegundos **estimados ou medidos**, arquivo, ID exato da região, função visual e justificativa.
- Para GIFs, quadros/intervalos e modo de apresentação.
- Transições (corte seco por padrão), preservação da proporção, fundo neutro quando necessário.
- Pendências, decisões e dependências para renderização.

Exemplo **ilustrativo**, não um esquema definitivo nem seleção real:

```json
{
  "schema_version": "draft-1",
  "video_id": "V02-003",
  "status": "PROPOSTO",
  "formato": {"largura": 1080, "altura": 1920},
  "fontes": {
    "roteiro": "editorial/roteiros/02-003_Roteiro_Individual.docx",
    "mapa": "02_Sistemas_de_Numeracao/02_Mapa_Espacial.json"
  },
  "segmentos": [
    {
      "id": "S01",
      "cena_roteiro": "C01",
      "fala_id": "F01",
      "inicio_ms_estimado": 0,
      "duracao_ms_estimada": 5000,
      "arquivo": "bit.png",
      "regiao_id": "ideia_principal",
      "funcao_visual": "Introdução",
      "transicao": "corte_seco"
    }
  ]
}
```

Os IDs são fictícios. Adaptar aos campos e IDs reais do mapa e do roteiro. O contrato técnico futuro estabilizará o esquema e sua validação automática.

## 6. Tempo, narração e SRT

O tempo indicado no roteiro é estimativa editorial. Antes de haver áudio, registrar tempos provisórios. Após haver áudio de referência ou definitivo, medir sua duração real e ajustar a montagem.

Não acelerar falas ou suprimir explicações apenas para alcançar duração arbitrária. Se houver conflito, propor prolongamento, redistribuição ou revisão editorial.

A gravação humana pode ser definitiva; a voz sintética pode ser usada como referência quando autorizada e disponível.

**O SRT final deriva do áudio efetivamente utilizado, não somente das estimativas do roteiro.** Deve preservar termos técnicos, números e sinais; conter intervalos válidos e não sobrepostos. SRT gerado sem áudio é provisório e deve ser identificado como tal. Alteração de áudio exige nova sincronização das legendas afetadas.

Não embutir legendas no vídeo por padrão. Limites quantitativos de legenda e tolerâncias serão definidos no contrato técnico.

## 7. Incompatibilidades e retroalimentação

Diante de divergência entre fala, catálogo, mapa e original:
1. Identificar segmento e evidência.
2. Classificar segundo `curadoria/protocolo_retroalimentacao.md`.
3. Determinar se afeta o conteúdo **efetivamente usado**.
4. Preservar segmentos e regiões válidos.
5. Encaminhar à camada responsável e respeitar a autorização vigente.

Ressalvas visuais previstas e pendências fora da montagem não bloqueiam automaticamente. Erro conceitual exibido, texto indispensável encoberto, ausência de sustentação visual essencial ou necessidade de reescrita não autorizada bloqueiam o segmento afetado. Marcar `PENDENTE_REVISAO` e prosseguir nos segmentos independentes quando possível.

## 8. Validação do plano

Antes da entrega, verificar:
- Cobertura das falas e preservação da ordem pedagógica.
- Existência dos arquivos e IDs exatos de regiões.
- Correspondência entre falas, regiões e estados dos GIFs.
- Ausência de durações negativas, sobreposições ou lacunas não intencionais.
- Preservação visual e distinção entre ressalvas aceitáveis e impedimentos.
- Identificação de tempos estimados versus medidos.
- Rastreabilidade das fontes, inspeções realizadas e pendências.
- Ausência de alegação de aprovação humana ou renderização não executada.

A validação do plano não substitui a inspeção do MP4, do áudio ou do SRT.

## 9. Entrega, Git e aprovação

Entregar o JSON e um resumo das escolhas, dependências e pendências. Não sobrescrever plano existente sem autorização. Preservar IDs estáveis e documentar alterações.

Quando a implementação estiver autorizada, executar validações, commit, push e abertura de PR conforme `AGENTS.md`. **Nunca realizar merge automaticamente.** A homologação do plano e a aprovação do vídeo renderizado são decisões distintas.

## 10. Contratos complementares

Este protocolo responde **o que mostrar, quando e por quê**.

`curadoria/contrato_entrega_video.md` deverá definir ferramentas, renderização, MP4, áudio, SRT, manifesto, validações técnicas e armazenamento de binários.

`curadoria/protocolo_revisao_audiovisual.md` deverá definir inspeção, correção dirigida e homologação da execução renderizada.

O `AGENTS.md` deverá apontar sucintamente para os contratos, sem duplicá-los.

## 11. Critério de sucesso

A montagem está pronta para revisão quando há plano reproduzível, fontes verificadas, sequência coerente com o roteiro, tempos claramente estimados ou sincronizados e pendências delimitadas.

**Síntese:** o roteiro determina o conteúdo; o mapa oferece regiões; a montagem organiza a experiência temporal; a renderização produz os artefatos; a revisão humana decide sua aprovação.
