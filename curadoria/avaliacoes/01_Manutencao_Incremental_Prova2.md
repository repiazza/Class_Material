# Manutenção incremental do capítulo 01 — Prova 2

Registro de execução autorizada sobre a base `78a59ee44152e45e21bedcada24c67ec5f19435f`.
Este laudo é evidência histórica, não norma operacional nem homologação pedagógica.

## Referência controlada e delta

- Catálogo original SHA-256: `236c6306881fd1633f6c7b1a416d94314b3347a05a593c2028b20bd17678af20`.
- Referência Git: `7e755aeebc44fafefdb5a1b4995e19da1a3d5009`; o mecanismo verificou correspondência binária do catálogo e leu os materiais daquele snapshot, sem adotar os hashes correntes como referência antiga.
- Baseline estabelecida em candidato externo, com zero interpretações; procedência e hashes ficam em `customXml/catalogacao_baseline.xml` do DOCX publicado.
- Planejamento: 14 materiais inalterados, dois novos; zero modificados, ausentes ou renomeados; vocabulário e relações sem mudança desde a referência.
- Aplicação instrumentada: exatamente dois eventos `interpretacao_solicitada`, exclusivamente para as novas imagens; hash binário dos demais não foi tratado como interpretação.

## Fichas novas e inspeção efetiva

Os dois PNGs RGB de 1536×1024 foram abertos e inspecionados visualmente no diagnóstico que precedeu esta execução, com identidade confirmada por SHA-256 no planejamento e na aplicação. A inspeção não foi inferida dos nomes ou hashes.

| Material | SHA-256 do original | Conteúdo verificado |
|---|---|---|
| `fluxograma_decisao.png` | `0dc8a433cf6681be56b9761b388ae028c8244e41a1e2f3b8d03de7c9533ef367` | Ramos de chuva/guarda-chuva, permissões e expressão R = ¬P ∨ Q. Equivalência conferida nas quatro combinações; mantém o modelo simplificado. |
| `precedencia_logica.png` | `f262875d5d02e35c5e2ea013ced4b8ed3c3f7da8ba9f9364fa475a263efd8e11` | Regras (P ∨ Q) ∧ R e P ∨ (Q ∧ R); caso 1,0,0 com saídas 0 e 1. Agrupamento não foi confundido com ordem temporal de execução; R é entrada local, não a saída do exemplo da chuva. |

## Preservação das fichas

Comparação pelo digest dos blocos XML reconhecidos por `Catalogo`, antes e depois: **14/14 idênticos**. Nenhuma ficha anterior reinterpretada ou reescrita. A verificação do mecanismo e uma comparação independente confirmaram o resultado.

| Material anterior | SHA-256 do bloco XML antes e depois | Resultado |
|---|---|---|
| `logica_booleana.png` | `bac00122fdfd18d8772611d33e4c6707ffd4db20fffe643777eb297764d67a9e` | idêntico |
| `logica_booleana2.png` | `74fd0a239b15ed6c887316e2778b34e50a7738b55bf50c9e9adf3012cce2ebe3` | idêntico |
| `logica_booleana3.png` | `f3a0fc6f0eb1c70b499cf11e0d55e942b87846a9af67d469dcdc8f8899207ce0` | idêntico |
| `not_p.gif` | `113a62a924085001721fd153e7573d69360adb6ad980c0f532ece8ebea90e72d` | idêntico |
| `p_and_q.gif` | `04b05ca62d34fca9d4f654353db34922084c5cc8f8656df71a2b0e4ee968dba6` | idêntico |
| `p_or_q.gif` | `1618da13dac827abd07d690fd977e6afedc6609886941060949db095e5205f28` | idêntico |
| `p_xor_q.gif` | `d9e4807aa211f4115643484c5b85c79edde27d8f96e04e98f260a8029d36a81b` | idêntico |
| `problema_condicoes.png` | `bc97567da824cbbbe335aba4bbb3815a95b81ab37093c86ad5922deb63c263c4` | idêntico |
| `problemas_condicoes2.png` | `6fafff9e7c8e963d6d074181cce81b648b8fcda211916a0b47118fb778882895` | idêntico |
| `problemas_condicoes3.png` | `dfe52dc0f266d5569a786804d73d6a068da616d8da869c316c01ba7a20a424c8` | idêntico |
| `problemas_condicoes4.png` | `a8d0cedb32f7c0b5970dd9f093d4431ed742c97ede8e46b8c70a86986e47f16d` | idêntico |
| `problemas_condicoes5.png` | `9b964aa222e8fb7c8a26fa7b153cdbc83163493d922506fc28ad48c8f0710b81` | idêntico |
| `exercicio.md` | `71435ca25eb4d01f4739c9741784c6512e14fe785d32be337ce7c04dd73815be` | idêntico |
| `gabarito.md` | `ba0f62a0cfc6af6d1d59efb02a4ebffacd9192def6eb589c8241815741a8f17d` | idêntico |

## Glossário, índices e métricas

- Cobertura: 14 → 16 fichas; total físico: dez PNG, quatro GIF e dois Markdown.
- Glossário: 19 → 21 termos; todas as definições anteriores preservadas.
- `precedência de operadores`: definição reutilizada do vocabulário mestre; associação documenta agrupamento, sem atribuir execução sequencial.
- `fluxograma`: definição fundamentada na nova imagem, explicitamente **PROPOSTA LOCAL — PENDENTE DE HOMOLOGAÇÃO**. Vocabulário mestre e RC não foram modificados.
- Vínculos reversos existentes atualizados: AND lógico, condição, expressão lógica, negação lógica, OR lógico, proposição lógica e tomada de decisão. Duas entradas novas incluídas; cada etiqueta possui uma definição e referências exatamente correspondentes às fichas.
- O relatório da ferramenta aponta coocorrências com 13 fichas antigas. São candidatas a análise documental, não novas relações pedagógicas ou motivo para alterar derivados.
- README: capítulo 01, 15 → 17 entradas; total geral, 280 → 282 (270 materiais e 12 catálogos). CSV preserva `modulo;arquivo`, acrescentando somente os dois caminhos.

## Validação e limites

- 45 testes dos mecanismos de reconciliação e catalogação incremental passaram: `python -B -m unittest discover -s ferramentas/tests -v`.
- DOCX abriu com `python-docx`: corpo de 135 parágrafos; zero tabelas no documento resultante. CRC do pacote válido; baseline consistente; 16 identidades únicas, todas existentes; glossário e índice reverso exatos.
- Compatibilidade de consumo documental validada por leitura do DOCX; nenhum motor editorial foi executado. Paginação não foi renderizada nesta manutenção; integridade estrutural não significa homologação pedagógica.
- Catálogo candidato validado e incorporado ao caminho canônico dentro da autorização. Candidatos, pacotes de fichas e logs completos permanecem em `/workspace/artifacts/catalogacao-cap01/`, sem cópias redundantes no Git.
- Reconciliação final `--check`: 13 capítulos, 282 entradas, zero adições/remoções pendentes, avisos ou links inválidos. Planejamento do catálogo publicado: 16 inalterados, zero interpretações. Comparação final: 987 arquivos protegidos com hashes preservados; somente os quatro arquivos do escopo modificados/criados.

## Preservação do V01-003

Dossiê, roteiro, mapa e regiões, montagem, SRT, renderizador, manifestos, relatórios, evidências e binários existentes foram preservados por comparação de hashes. Nenhuma revisão audiovisual, renderização, síntese ou encerramento de pendência histórica foi realizado.

O mapa continua referenciando o snapshot anterior do catálogo: suas 14 fichas foram preservadas, e as novas imagens não foram selecionadas na montagem. A publicação do catálogo não exige modificar o mapa ou os derivados válidos.

MP4 preservado: `f464acd110d627f8d7e71f5a3d8cfeb6cb95500e447f9030833d35e6eebd9378`.
WAV preservado: `1a215ae1505a3bdbc5d84668ca8d5d2d7fe94fe1314b695cedd5b3f542ba1d8b`.

Pendências: revisão humana da PR e das fichas novas; homologação da etiqueta local `fluxograma`. Nenhuma decisão editorial foi presumida.
