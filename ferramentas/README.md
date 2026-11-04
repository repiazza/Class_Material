# Reconciliação documental

Da raiz, com Python 3.10 ou superior, sem dependências externas:

```bash
python ferramentas/reconciliar_documentacao.py
python ferramentas/reconciliar_documentacao.py --check
python -B -m unittest discover -s ferramentas/tests -v
```

`--root /caminho/do/checkout` permite usar outra árvore ou fixtures. A execução normal escreve somente `inventario.csv` e os cinco blocos `reconciliacao:inicio/fim` do README; fora dos blocos, o texto é preservado. Não escreve documentos iguais, nem incorpora timestamps. O comando apenas informa adições, remoções e ambiguidades na saída; não cria outro inventário ou cadastro de estado.

O modo `--check` não escreve: retorna 0 se os documentos coincidem com a reconciliação e não há links locais inválidos, 1 se há divergência ou link inválido e 2 em erro de leitura/contrato/marcadores. Ambiguidades são avisos, sem bloquear arquivos independentes. Links inválidos de trechos não gerados são preservados, informados e fazem a verificação falhar; não se inventa um destino. O CSV inválido ou marcadores ausentes/duplicados interrompem antes de escrever.

## Elegibilidade física

- Capítulos: diretórios reais `NN_...` na raiz; pastas internas podem organizar materiais. Nomes e caminhos relativos são preservados exatamente, com ordenação lexical estável, sem depender de locale.
- Materiais: PNG, JPG/JPEG, GIF, Markdown, C, headers e ZIP, nas áreas de materiais. O catálogo canônico é exclusivamente `NN_Catalogo_Semantico.docx` na raiz do capítulo. Presença não implica homologação semântica. ZIP não é descompactado.
- Exclusões por função/localização: pastas de evidências, derivados, artefatos, protótipos e temporários; ocultos; mapas JSON; relatórios/manifestos/autoauditorias/validações técnicas nomeados como tais; renderizadores; catálogos experimentais e rascunhos. A extensão de mídia dentro de evidências não a torna original.
- Formatos ou funções não reconhecidos são sinalizados. Entradas históricas reais de tipo desconhecido são preservadas, sem fazer o mesmo com entradas reconhecidamente técnicas; novos desconhecidos ficam fora até esclarecimento. Links simbólicos não são promovidos a materiais.

Renomear um material é observado como remoção do caminho antigo e adição do novo; a rotina não afirma identidade por similaridade de nomes. Quando o Git está disponível, relata também renomeações `R` da área preparada ou do último commit que correspondam às remoções/adições observadas. Sem essa evidência, não inventa a correspondência. Git é opcional; a reconciliação física funciona sem ele. Os caminhos exatos, que são a identidade operacional atual, são reconciliados nas duas direções. Não há UUID, hashes de identidade ou metadados paralelos. Os avisos podem exigir esclarecer o papel de um arquivo; não exigem aprovação para entradas independentes.

## README e arquitetura

A navegação usa a árvore física, títulos documentais (primeiro título do catálogo ou cabeçalho numerado do exercício), papéis verificáveis e disponibilidade de arquivos. A leitura do título DOCX utiliza somente ZIP/XML da biblioteca padrão, sem interpretar os registros semânticos. Se não houver título documental, a identificação usa o nome do diretório. Exercícios e respostas são listados por papel no capítulo; não há pareamento inferido por números. Etapas A/B, alternativas e implementações permanecem identificáveis pelos nomes e cabeçalhos documentais.

O fluxo Mermaid tem rótulos quebrados em linhas de até aproximadamente 19 caracteres, sem cortar palavras; usa `htmlLabels: false` para evitar caixas HTML com texto truncado. Nós possuem links às fontes reais. A renderização depende também da versão do Mermaid usada pelo visualizador.

Os estados são transcritos dos cabeçalhos dos contratos presentes em `curadoria/protocolo_*.md` e `contrato_*.md`; contagens de artefatos vêm de caminhos canônicos. A tabela de capacidades demonstradas do Motor 3 vem do README do próprio componente, identificada como declaração da fonte, não certificação automática. Uma mudança contratual atualiza esses indicadores e não promove PROPOSTO, FUTURO ou EXPERIMENTAL a IMPLEMENTADO. Presença de código é descrita somente como presença de implementação.

As dependências do fluxo conhecido estão no próprio mecanismo. Um contrato novo aparece automaticamente na tabela de fontes; isso não permite inferir sua posição no fluxo ou aprovar uma capacidade. Mudanças de responsabilidade que não sejam expressas pelos indicadores estruturados exigem análise documental pelo agente e ajuste fundamentado da representação, dentro da autorização de manutenção de README/inventário. Não há interpretação semântica geral de prosa, registro de estados paralelo ou criação automática de decisões humanas.

As seções históricas e editoriais fora dos limites permanecem manuais. Não coloque contagens ou afirmações de estado atual nessas seções. A reconciliação não modifica contratos, catálogos, fontes didáticas, vocabulário, relações ou decisões do checklist.

## Integração

Execute após alterações de acervo, catálogos, contratos ou componentes, antes do commit/PR do escopo autorizado. Não depende da geração de catálogo para funcionar. `.github/workflows/reconciliacao-documental.yml` executa testes e `--check` em PRs e pushes na `main`, sem escrita, commits ou merge. A configuração de proteção de branch é administrada no GitHub: o workflow fornece um check, mas não configura sozinho sua obrigatoriedade.

Resultado da primeira execução e evidências: [relatório](RELATORIO_RECONCILIACAO.md).
