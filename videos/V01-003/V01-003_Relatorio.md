# Produção audiovisual piloto V01-003 — retomada da PR #15

**Resultado: PENDENTE_REVISAO. Modalidade produzida: REFERENCIA.** MP4, voz sintética real e SRT foram gerados. A produção não está entregue externamente: uploads recusados com HTTP 401; escuta perceptiva e sincronismo fino permanecem não verificados. Não é uma prévia silenciosa nem homologação humana.

## Fontes e continuidade

Preservado o commit inicial 05f67b2. A branch audiovisual/piloto-v01-003 recebeu origin/main edba16d por merge 1be0466, sem rebase, force-push ou reescrita. Mapa 01 efetivamente usado: commit c5711ef6a37b378dc607a4b7d8b25cef1facb015, integrado pela PR #16. SHA-256 do mapa: `abc56bc3a40bee936edcbd6f209a6a66313468a2c8fa986b578a90703f855806`. Roteiro individual 1.0 PROPOSTO, dossiê de origem, mapa e originais mantidos byte a byte; autorização expressa da retomada permite o piloto experimental. O roteiro continua sendo a autoridade das falas; o dossiê não foi usado para regenerá-las.

Foram reutilizados os cinco takes S01–S05 e suas falas literais. Os 70 segundos iniciais permanecem no plano como estimativa histórica; a duração final medida é **77,224 segundos**. Não se acelerou a voz para caber em 70 segundos. Não se regenerou o mapa ou se reabriu auditoria geral.

## Montagem executada

| Take | Intervalo medido (s) | Material e regiões homologadas |
|---|---|---|
| S01 / Take 01 | 0.000–11.718 | problema_condicoes.png: `problema` |
| S02 / Take 02 | 11.718–28.016 | problemas_condicoes2.png: `proposicao_p`, `proposicao_q`, `proposicao_r` |
| S03 / Take 03 | 28.016–44.428 | problemas_condicoes3.png: `significado_and`, `conclusao` |
| S04 / Take 04 | 44.428–61.138 | problemas_condicoes5.png: `construcao_expressao`, `tabela_final` |
| S05 / Take 05 | 61.138–77.224 | problemas_condicoes5.png: `cenario_10`, `conclusao` |

O plano registra 16 projeções/trechos de voz dentro desses cinco takes. Todos são PNGs estáticos, com cortes secos e fundo neutro; nenhum GIF ou movimento foi presumido. As regiões são resolvidas por IDs reais; as caixas não mudam. Pequenas margens e fragmentos previstos do mapa foram preservados. A condição simplificada chuva/guarda-chuva continua sendo limite pedagógico do roteiro, não garantia física. O r da conjunção intermediária não é a decisão final: o aviso de conclusão da imagem 3 foi preservado ao fazer esse contraste.

## Voz e SRT reais

FFmpeg/ffprobe 7.1.5, Python e Pillow disponíveis. Embora não houvesse sintetizador instalado, o endpoint Google Translate TTS foi testado com sucesso: `client=tw-ob`, `tl=pt-BR`, respostas HTTP 200 com áudio MPEG. Não houve instalação, contratação ou troca de palavras; textos foram enviados ao serviço externo autorizado para síntese de referência. O serviço não expõe versão/identificador estável de voz: preservou-se o WAV resultante com hash, para que reproduzir o vídeo não dependa de nova síntese.

Cada frase/cláusula foi sintetizada, decodificada para PCM mono 48 kHz e medida; foram inseridos 250 ms de pausa técnica ao final de cada bloco. O SRT tem 16 entradas UTF-8, obtidas dos intervalos reais dos blocos e com quebra de linha textual, sem sobreposição. Não se trata de alinhamento palavra a palavra, nem SRT de futura gravação humana. A sincronização por blocos não comprova pronúncia ou sincronismo perceptivo fino. Legendas externas, sem queima no MP4.

## Inspeção, correção dirigida e limites

- MP4 1080×1920, H.264/yuv420p, 30 fps; AAC mono 48 kHz. Duração ffprobe: 77,224 s. Decodificação completa de áudio/vídeo concluída sem erros.
- Os 16 trechos têm sinal de voz não silencioso, sem amostras PCM saturadas. Áudio AAC extraído do MP4 correlaciona com o WAV PCM em 0,999911, evidência de integridade da codificação, não de qualidade linguística.
- Foram extraídos e visualmente inspecionados 16 quadros representativos dos trechos, cobrindo todos os takes. Comparação numérica com as projeções de origem e em ambos os lados dos 15 limites (30 verificações, ±100 ms) confirmou as imagens esperadas; nenhuma troca indevida, corte ou distorção foi identificada. Quantização do tempo da imagem decorre da taxa de quadros; o plano preserva tempos medidos do áudio.
- **V01-003-REV-002 / AV-M, corrigida:** a primeira exportação mostrava o painel conjunto P/Q/R pequeno durante a nomeação. Só esse trecho foi dividido em três cláusulas literais e recebeu os cartões individuais homologados; demais áudios foram reutilizados. SRT e cronologia posteriores foram atualizados, a saída completa foi novamente decodificada e os quadros/fronteiras reinspecionados.
- **V01-003-REV-004, pendente:** não houve escuta perceptiva nem reprodução audiovisual humana contínua nesta interface. Quadros estáticos e métricas não demonstram pronúncia, cadência ou sincronismo percebido. Conferir especialmente P/E/Q, OU e os pontos de troca visual. Não se afirma ter assistido ou ouvido integralmente o resultado.

Evidências: [antes da correção do take 02](evidencias/take02-antes.jpg); [métricas](evidencias/validacao.json). Painéis extraídos do MP4 final:

- [Inspeção final 01](evidencias/inspecao-final-01.jpg)
- [Inspeção final 02](evidencias/inspecao-final-02.jpg)
- [Inspeção final 03](evidencias/inspecao-final-03.jpg)
- [Inspeção final 04](evidencias/inspecao-final-04.jpg)
- [Inspeção final 05](evidencias/inspecao-final-05.jpg)
- [Inspeção final 06](evidencias/inspecao-final-06.jpg)

## Artefatos preservados e acesso

**O MP4 ainda não é acessível externamente.** Os caminhos abaixo identificam arquivos reais do ambiente; não são links de entrega ao usuário.

| Artefato | Caminho local preservado | Bytes | SHA-256 |
|---|---|---|
| V01-003.mp4 | `/workspace/artifacts/V01-003/V01-003.mp4` | 3884176 | `f464acd110d627f8d7e71f5a3d8cfeb6cb95500e447f9030833d35e6eebd9378` |
| V01-003_Audio_Referencia.wav | `/workspace/artifacts/V01-003/V01-003_Audio_Referencia.wav` | 7413548 | `1a215ae1505a3bdbc5d84668ca8d5d2d7fe94fe1314b695cedd5b3f542ba1d8b` |
| V01-003.srt | `/workspace/artifacts/V01-003/V01-003.srt` | 1300 | `0aa83917f1fc2cab411f22ea1e8d0e2d9b493ff1c712c1b0fbb3f68937e32c83` |

**V01-003-REV-003 / entrega bloqueada:** foram realmente testados criação e upload em release em rascunho do próprio GitHub, sem publicação. Metadados da release 428215524 foram criados, mas `gh release upload` retornou HTTP 401 Bad credentials em uploads.github.com; POST direto autenticado ao endpoint oficial também retornou HTTP 401. A consulta confirmou zero anexos. O rascunho vazio foi removido, sem criar tag publicada ou release pública. As credenciais disponíveis permitiram operações do repositório, mas não o upload nesse host. Nenhum segredo foi registrado.

A descoberta das ferramentas conectadas não encontrou upload de arquivos ou serviço de hospedagem de artefatos; download_file serve somente para entrada. Não foram usados serviços públicos aleatórios, links locais como se fossem acessíveis, nem MP4/WAV no Git. Para concluir, é necessário um canal de entrega suportado com autorização de upload funcional. Não se considera a distribuição concluída. Os binários ficam fora do repositório e sua persistência depende da retenção do workspace.

Versionados: plano atualizado, SRT da referência, manifesto, relatório, script de renderização e evidências pequenas. O script [renderizar.py](renderizar.py) recebe o WAV preservado e reconstitui o MP4 com hashes de entrada verificados; não instala ferramentas ou sintetiza outra voz. Comando: `python videos/V01-003/renderizar.py --audio /workspace/artifacts/V01-003/V01-003_Audio_Referencia.wav --saida /tmp/V01-003.mp4`. A disponibilidade externa do WAV tem o mesmo bloqueio do MP4.

## Validações e encerramento

Falas e IDs dos cinco takes preservados, soma dos intervalos medidos 77.224 ms, cobertura contínua; IDs de região e hashes resolvidos no mapa integrado; SRT cronológico, sem sobreposição, texto recomposto igual às falas, dentro do tempo do MP4; hashes dos artefatos calculados. Não se modificaram originais, mapa, catálogo, roteiro ou dossiê.

A ocorrência espacial V01-003-REV-001 está resolvida pela integração da PR #16. A execução continua sendo da PR #15, com o histórico anterior preservado. Correção técnica própria concluída; acesso ao vídeo e revisão auditiva permanecem pendentes. Não há GERADO_OK, nova PR para o piloto, merge automático ou publicação em plataforma audiovisual.

Teste de reprodução: o script versionado gerou um segundo MP4 com SHA-256 idêntico ao original (`f464acd110d627f8d7e71f5a3d8cfeb6cb95500e447f9030833d35e6eebd9378`), confirmando reprodução byte a byte neste ambiente.
