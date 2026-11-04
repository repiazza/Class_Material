#!/usr/bin/env python3
"""Reconcilia apenas inventario.csv e blocos explícitos do README (Python 3.10+)."""
from __future__ import annotations
import argparse
import csv
import io
import re
import subprocess
import sys
import textwrap
import zipfile
from collections import Counter
from pathlib import Path
from urllib.parse import quote, unquote, urlsplit
from xml.etree import ElementTree

CHAPTER = re.compile(r'^\d{2,}_.+')
MATERIAL = {'.png', '.jpg', '.jpeg', '.gif', '.md', '.c', '.h', '.zip'}
DERIVED_DIR = re.compile(r'^(?:evidencias(?:_|$)|derivados(?:_|$)|artefatos(?:_|$)|artifacts$|prototipos(?:_|$)|temporarios$|tmp$|__pycache__$)', re.I)
DERIVED_FILE = re.compile(r'(?:_Mapa_Espacial\.json$|_Autoauditoria_Mapa\.md$|^(?:renderizar|manifesto|autoauditoria|relatorio|validacao)[_-].*\.(?:py|json)$)', re.I)
BEGIN = '<!-- reconciliacao:inicio {} -->'
END = '<!-- reconciliacao:fim {} -->'
BLOCKS = ('arquitetura', 'organizacao', 'inventario', 'catalogos', 'exercicios')


def read(path: Path) -> str:
    return path.read_text(encoding='utf-8')


def material_text(path: Path, warnings: list[str]) -> str:
    try:
        return read(path)
    except (OSError, UnicodeError):
        warnings.append(f'{path.parent.name}/{path.name}: cabeçalho textual não lido como UTF-8; nome físico preservado, sem inferir título.')
        return ''


def link(label: str, path: str) -> str:
    return '[' + label.replace('|', '\\|').replace('[', '\\[').replace(']', '\\]') + '](' + quote(path, safe='/#._-') + ')'


def table_cell(value: str) -> str:
    return value.replace('|', '\\|').replace('\n', ' ').strip()


def inventory(root: Path) -> list[tuple[str, str]]:
    path = root / 'inventario.csv'
    if not path.exists():
        return []
    data = list(csv.reader(io.StringIO(read(path)), delimiter=';'))
    if not data or data[0] != ['modulo', 'arquivo'] or any(len(row) != 2 for row in data[1:]):
        raise ValueError('inventario.csv: esperado exclusivamente modulo;arquivo com duas colunas.')
    return [tuple(row) for row in data[1:]]


def scan(root: Path, previous: list[tuple[str, str]]):
    chapters = sorted((p for p in root.iterdir() if CHAPTER.fullmatch(p.name) and p.is_dir() and not p.is_symlink()), key=lambda p: p.name)
    rows, warnings = [], []
    old = set(previous)
    for chapter in chapters:
        canonical = chapter.name.split('_', 1)[0] + '_Catalogo_Semantico.docx'
        for path in sorted(chapter.rglob('*')):
            rel = path.relative_to(chapter)
            if any(part.startswith('.') or DERIVED_DIR.match(part) for part in rel.parts[:-1]):
                continue
            if path.is_symlink():
                warnings.append(f'{chapter.name}/{rel.as_posix()}: link simbólico fora da descoberta automática.')
                continue
            if not path.is_file() or path.name.startswith('.'):
                continue
            name = rel.as_posix()
            if DERIVED_FILE.search(path.name) or re.match(r'^(?:[0-9]{2}_)?(?:autoauditoria|relatorio|manifesto|validacao)(?:[_-].*)?\.(?:md|json)$', path.name, re.I) or path.suffix.lower() in {'.tmp', '.bak', '.pyc'} or path.name.endswith('~'):
                continue
            if path.name.startswith('renderizar') and path.suffix == '.py':
                continue
            if path.suffix.lower() == '.docx' and re.search(r'experimental|prototipo|rascunho', path.stem, re.I):
                continue
            if path.suffix.lower() in MATERIAL and path.name.lower() not in {'readme.md', 'agents.md'} or (path.parent == chapter and path.name == canonical):
                rows.append((chapter.name, name))
            else:
                # Um tipo desconhecido não elimina entrada histórica real e não cria nova classificação.
                if (chapter.name, name) in old:
                    rows.append((chapter.name, name))
                warnings.append(f'{chapter.name}/{name}: função ambígua; ' + ('entrada existente preservada.' if (chapter.name, name) in old else 'não incluído automaticamente.'))
    return chapters, sorted(set(rows)), sorted(set(warnings))


def docx_title(path: Path) -> str:
    try:
        with zipfile.ZipFile(path) as z:
            body = ElementTree.fromstring(z.read('word/document.xml'))
        ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
        for par in body.findall('.//w:body/w:p', ns):
            text = ''.join(x.text or '' for x in par.findall('.//w:t', ns)).strip()
            if text:
                return text
    except (OSError, KeyError, zipfile.BadZipFile, ElementTree.ParseError):
        pass
    return ''


def chapter_title(chapter: Path, warnings: list[str]) -> str:
    number = chapter.name.split('_', 1)[0]
    catalog = chapter / f'{number}_Catalogo_Semantico.docx'
    titles = [docx_title(catalog)] if catalog.exists() else []
    for p in sorted(chapter.glob('exercicio*.md')):
        titles.extend(re.findall(r'^#\s+(.+)$', material_text(p, warnings), re.M)[:1])
    for title in titles:
        match = re.match(r'^' + re.escape(number) + r'\s*[—–-]\s*(.+)', title)
        if match:
            return match[1].strip()
    return chapter.name.split('_', 1)[1].replace('_', ' ')


def metadata(text: str, key: str) -> str:
    match = re.search(r'(?mi)^\s*>?\s*\*\*' + re.escape(key) + r':\*\*\s*(.+)', text)
    return match[1].strip().rstrip('\\').strip() if match else 'Não declarado no cabeçalho; consultar a fonte.'


def wrapped(text: str) -> str:
    return '<br/>'.join(textwrap.wrap(text, width=19, break_long_words=False, break_on_hyphens=False))


def architecture(root: Path) -> str:
    # Dependências dos contratos conhecidos; existência só demonstra presença, nunca homologação.
    stages = {
        'A': ('Acervo original', 'inventario.csv'),
        'K': ('Catalogação semântica', 'curadoria/protocolo_catalogacao_semantica.md'),
        'B': ('Fundamentação semântica', 'curadoria/vocabulario_controlado.md'),
        'C': ('Descoberta e dossiê editorial', 'curadoria/protocolo_roteirizacao.md'),
        'I': ('Consolidação de identidades e decisões', 'curadoria/protocolo_consolidacao_editorial.md'),
        'J': ('Seleção humana de candidato e dossiê', 'AGENTS.md'),
        'E': ('Roteiro individual', 'curadoria/protocolo_roteiro_individual.md'),
        'F': ('Mapa espacial reutilizável', 'curadoria/protocolo_mapeamento_espacial.md'),
        'G': ('Plano de montagem', 'curadoria/protocolo_montagem_audiovisual.md'),
        'H': ('Geração audiovisual de referência', 'curadoria/contrato_entrega_video.md'),
        'U': ('Interpretação humana: áudio externo', 'videos/motor3/README.md'),
        'T': ('Finalização experimental: Motor 3', 'videos/motor3/__main__.py'),
        'V': ('Revisão audiovisual e homologação humana', 'curadoria/protocolo_revisao_audiovisual.md'),
        'R': ('Retroalimentação de inconsistências', 'curadoria/protocolo_retroalimentacao.md'),
        'Q': ('Reconciliação documental: índice e README', 'ferramentas/reconciliar_documentacao.py'),
    }
    present = {key: value for key, value in stages.items() if (root / value[1]).is_file()}
    lines = ['## Visão geral da arquitetura', '',
             'O fluxo distingue contratos documentais, artefatos existentes e execução experimental. As setas indicam dependências; não são aprovações nem uma sequência automática de produção. Clique nas etapas para consultar suas fontes.', '',
             '```mermaid', '%%{init: {"htmlLabels": false, "markdownAutoWrap": false, "flowchart": {"htmlLabels": false, "wrappingWidth": 240}}}%%', 'flowchart TD']
    for key, (title, path) in present.items():
        lines.append(f'    {key}["{wrapped(title)}"]')
    for left, right in [('A','K'),('K','B'),('B','C'),('C','I'),('C','J'),('I','J'),('J','E'),('A','F'),('E','G'),('F','G'),('G','H'),('G','T'),('U','T'),('H','V'),('T','V'),('V','R'),('A','Q')]:
        if left in present and right in present:
            arrow = '-.->' if (left,right) in {('I','J'),('A','Q')} else '-->'
            lines.append(f'    {left} {arrow} {right}')
    for key, (_, path) in present.items():
        lines.append(f'    click {key} "./{path}" "Consultar fonte"')
    lines.extend(['```', '', '### Contratos presentes e seus estados declarados', '',
                  'A existência de um protocolo não comprova implementação, demonstração ou homologação. Os estados abaixo são transcritos dos cabeçalhos das fontes, sem reinterpretar sua aprovação.', '',
                  '| Contrato | Versão declarada | Estado declarado na fonte |', '|---|---|---|'])
    for path in sorted((root/'curadoria').glob('*.md')):
        if not path.name.startswith(('protocolo_', 'contrato_')):
            continue
        text = read(path)
        title = re.search(r'^#\s+(.+)', text, re.M)
        lines.append(f'| {link(title[1] if title else path.stem, path.relative_to(root).as_posix())} | {table_cell(metadata(text,"Versão"))} | {table_cell(metadata(text,"Estado"))} |')
    lines += ['', '### Artefatos observáveis', '', '| Componente | Evidência física atual |', '|---|---|']
    for label, folder, pattern in [('Dossiês canônicos','editorial/dossies','[0-9][0-9]_Dossie_Editorial.docx'),('Registros de consolidação','editorial/consolidacoes','[0-9][0-9]_Consolidacao_Editorial.md'),('Roteiros individuais','editorial/roteiros','*_Roteiro_Individual.docx'),('Planos de montagem','editorial/montagens','*_Montagem.json')]:
        path=root/folder
        if path.is_dir():
            count = len(list(path.glob(pattern)))
            lines.append(f'| {label} | {count} '+('arquivo' if count == 1 else 'arquivos')+f' em {link(folder,folder+"/")}; presença não implica aprovação. |')
    maps=sorted(root.glob('[0-9][0-9]_*/[0-9][0-9]_Mapa_Espacial.json'))
    lines.append(f'| Mapas espaciais | {len(maps)} mapas canônicos presentes; seleção e tempos pertencem à montagem. |')
    motor_readme=root/'videos/motor3/README.md'
    if motor_readme.is_file():
        lines += ['', '### Finalização e interpretação humana', '',
                  f'O núcleo tem implementação presente em {link("videos/motor3", "videos/motor3/")}. Áudio externo é uma entrada para finalização; a rotina documental não produz nem presume uma gravação humana. Capacidades e limitações são declarações do {link("laudo do Motor 3", "videos/motor3/RELATORIO.md")} e do README do componente, não certificações desta reconciliação.', '']
        text=read(motor_readme)
        state=re.search(r'^## Estado demonstrado\s*\n(.*?)(?=^## |\Z)',text,re.S|re.M)
        if state:
            lines += [line for line in state[1].strip().splitlines() if line.startswith('|')]
        else:
            lines += ['Estado demonstrado não localizado; consultar a fonte. Não se presume demonstração.']
    lines += ['', 'A produção segue o '+link('contrato de entrega','curadoria/contrato_entrega_video.md')+'. MP4 e áudios permanecem fora do Git, no workspace; arquivos de projeto, legendas e relatórios são versionáveis. Entrega técnica não equivale à homologação editorial.', '',
              'A '+link('retroalimentação','curadoria/protocolo_retroalimentacao.md')+' encaminha inconsistências à camada responsável e preserva derivados válidos. Correções pedagógicas e alterações de fontes dependem de autorização específica. Esta reconciliação não implementa propagação automática de mudanças por hashes nem correção de imagens.', '',
              '### Reconciliação documental', '',
              'Execute `python ferramentas/reconciliar_documentacao.py` após alterações elegíveis. O modo `--check` verifica divergências sem escrever; o CI utiliza esse modo. Somente `inventario.csv` e os blocos gerados deste README são atualizados. Ambiguidades são informadas; não homologam materiais nem bloqueiam entradas independentes.', '',
              'Regras, limites e testes: '+link('instruções de execução','ferramentas/README.md')+'. O responsável humano continua decidindo sobre a integração das PRs, as escolhas editoriais e as correções pedagógicas; não há merge automático.']
    return '\n'.join(lines)


def generated(root: Path, chapters: list[Path], rows: list[tuple[str,str]], warnings: list[str]) -> dict[str,str]:
    titles = {p.name: chapter_title(p, warnings) for p in chapters}
    catalogs = {(p.name, p.name.split('_',1)[0]+'_Catalogo_Semantico.docx') for p in chapters}
    nc = len(set(rows) & catalogs)
    counts=Counter(module for module,_ in rows)
    organization=['## Organização', '', 'Diretórios de capítulos são descobertos na raiz. A identificação abaixo usa o título documental do capítulo, quando disponível, ou seu nome físico. Numeração não estabelece ordem obrigatória de estudo.', '', '| Diretório | Identificação do capítulo | Entradas no índice | Catálogo canônico |', '|---|---|---:|---|']
    for p in chapters:
        name=p.name.split('_',1)[0]+'_Catalogo_Semantico.docx'
        cat=link(name,p.name+'/'+name) if (p.name,name) in rows else 'Sem catálogo canônico'
        organization.append(f'| {link(p.name,p.name+"/")} | {table_cell(titles[p.name])} | {counts[p.name]} | {cat} |')
    index=['## Localização dos materiais','',f'O {link("inventario.csv","inventario.csv")} contém **{len(rows)} entradas** em **{len(chapters)} capítulos**: **{len(rows)-nc} materiais didáticos** e **{nc} catálogos canônicos**. O contrato é `modulo;arquivo`; combine `modulo/arquivo` para localizar o arquivo a partir da raiz. A ordenação é estável por capítulo e caminho relativo do arquivo, preservando grafia e caixa.', '',
           'São elegíveis materiais PNG, JPG/JPEG, GIF, Markdown, fontes C, headers e pacotes ZIP nas áreas de materiais dos capítulos, além de `NN_Catalogo_Semantico.docx` canônico. O ZIP é uma entrada física, sem promover membros internos. A existência física não depende de homologação semântica.', '',
           'Não entram mapas espaciais, evidências e derivados técnicos, protótipos, temporários, documentos editoriais ou de governança, arquivos internos do Git, este README ou o próprio índice. Elegibilidade considera localização e papel, além da extensão. Arquivos de função incerta são sinalizados; registros históricos reais de tipo desconhecido são preservados até esclarecimento.']
    cattext=['## Catálogos semânticos','',f'Há {nc} catálogos canônicos presentes para {len(chapters)} capítulos; consulte a disponibilidade na tabela. Catálogos experimentais externos ao checkout não são referências canônicas.', '',
             'O catálogo descreve conteúdos, representações, exemplos, palavras-chave, glossário e relações inversas aos materiais. Identifique cada material por capítulo e nome exato. O documento não substitui os originais nem comprova correção ou validação visual. A '+link('catalogação semântica','curadoria/protocolo_catalogacao_semantica.md')+' rege criação e revisão autorizadas; a reconciliação física não lê os registros para classificar ou homologar conteúdos.', '',
             'O '+link('vocabulário controlado','curadoria/vocabulario_controlado.md')+' preserva termos canônicos e distinções locais. O '+link('mapa conceitual','curadoria/relacionamentos_conceituais.md')+' é fonte auxiliar de relações e decisões humanas, sem impor sequência curricular. Esta rotina não altera esses documentos.']
    exercises=['## Exercícios e gabaritos','',
               'Os arquivos são agrupados por capítulo e papel documental, **sem presumir pareamento por numeração ou semelhança de nomes**. Rótulos entre parênteses reproduzem cabeçalhos dos próprios Markdown, quando presentes; códigos e pacotes são identificados pelo formato. Enunciados e gabaritos podem ter etapas, explicações ou alternativas de solução.', '',
               '| Módulo | Enunciados | Gabaritos e implementações | Pacotes de apoio |', '|---|---|---|---|']
    for p in chapters:
        groups=[[],[],[]]
        for module,name in rows:
            if module!=p.name:
                continue
            base=Path(name).name.casefold()
            target=0 if re.match(r'^exercicio(?:\d|[_\.]|$)',base) else 1 if re.match(r'^gabarito(?:\d|[_\.]|$)',base) else 2 if Path(name).suffix.lower()=='.zip' else None
            if target is None:
                continue
            item=link(name,p.name+'/'+name)
            if Path(name).suffix.lower()=='.md':
                headers=re.findall(r'^#{1,3}\s+(.+)$',material_text(p/name, warnings),re.M)
                role=next((h for h in headers if re.search(r'exerc[ií]cio|gabarito|etapa',h,re.I)),None)
                if role:item+=' ('+table_cell(role)+')'
            elif Path(name).suffix.lower() in {'.c','.h'}:
                item+=' (implementação C)' if name.lower().endswith('.c') else ' (header C)'
            groups[target].append(item)
        exercises.append('| '+p.name.split('_',1)[0]+' - '+table_cell(titles[p.name])+' | '+' | '.join('<br/>'.join(g) if g else 'Não identificado' for g in groups)+' |')
    exercises+=['','A tabela comprova localização e papel documental, não equivalência técnica entre soluções nem auditoria pedagógica. Um gabarito pode orientar várias partes; soluções alternativas não são redundantes por definição.']
    return dict(arquitetura=architecture(root),organizacao='\n'.join(organization),inventario='\n'.join(index),catalogos='\n'.join(cattext),exercicios='\n'.join(exercises))


def update_blocks(text: str, blocks: dict[str,str]) -> str:
    for name, content in blocks.items():
        begin,end=BEGIN.format(name),END.format(name)
        if text.count(begin)!=1 or text.count(end)!=1 or text.index(begin)>text.index(end):
            raise ValueError(f'README: limites ausentes/duplicados/invertidos no bloco {name}. Nada foi escrito.')
        a=text.index(begin)+len(begin);b=text.index(end)
        text=text[:a]+'\n'+content.strip()+'\n'+text[b:]
    return text


def slug(text: str) -> str:
    text=re.sub(r'<[^>]+>|[`*]','',text).lower().strip()
    return ''.join(c for c in text if c.isalnum() or c in ' _-').replace(' ','-')


def local_links(root: Path, text: str) -> list[str]:
    errors=[]
    targets=re.findall(r'(?<!!)\[[^\]\n]*\]\(([^)\n]+)\)',text)
    targets+=re.findall(r'^\s*click\s+\w+\s+"([^"]+)"',text,re.M)
    targets+=re.findall(r'^\s*\[[^\]]+\]:\s+(\S+)',text,re.M)
    for target in targets:
        target=target.strip().strip('<>')
        parts=urlsplit(target)
        if parts.scheme or parts.netloc:
            continue
        path=root/unquote(parts.path or 'README.md')
        if not path.exists():
            errors.append('Link local inexistente: '+target);continue
        if parts.fragment and path.is_file() and path.suffix.lower()=='.md':
            content=text if path==root/'README.md' else read(path)
            anchors=[];seen=Counter()
            for title in re.findall(r'^#{1,6}\s+(.+)$',content,re.M):
                anchor=slug(title);anchors.append(anchor+('-'+str(seen[anchor]) if seen[anchor] else ''));seen[anchor]+=1
            if unquote(parts.fragment) not in anchors:
                errors.append('Âncora local inexistente: '+target)
    return sorted(set(errors))


def git_renames(root: Path, added: set, removed: set) -> list[tuple[str, str]]:
    """Correlaciona somente R documentado pelo Git, sem inferir identidade por nome/hash."""
    if not added or not removed:
        return []
    plus={module+'/'+name for module,name in added}
    minus={module+'/'+name for module,name in removed}
    result=set()
    for revisions in (['--cached','HEAD'], ['HEAD^','HEAD']):
        try:
            proc=subprocess.run(['git','-C',str(root),'diff','--name-status','-z','--find-renames',*revisions],capture_output=True,timeout=10,check=False)
        except (OSError,subprocess.TimeoutExpired):
            continue
        if proc.returncode:
            continue
        fields=iter(proc.stdout.decode('utf-8').split('\0'))
        for status in fields:
            if not status:
                continue
            old=next(fields,'')
            if status.startswith(('R','C')):
                new=next(fields,'')
                if status.startswith('R') and old in minus and new in plus:
                    result.add((old,new))
    return sorted(result)


def reconcile(root: Path, check: bool=False) -> dict:
    if any((root/name).is_symlink() for name in ('README.md', 'inventario.csv')):
        raise ValueError('README/inventário não podem redirecionar escrita por link simbólico.')
    previous=inventory(root)
    chapters,rows,warnings=scan(root,previous)
    text=read(root/'README.md')
    result_text=update_blocks(text,generated(root,chapters,rows,warnings))
    problems=local_links(root,result_text)
    if problems:
        # Links ambíguos fora dos blocos são preservados; alterações independentes são seguras.
        warnings+=problems
    stream=io.StringIO(newline='');writer=csv.writer(stream,delimiter=';',lineterminator='\n');writer.writerow(['modulo','arquivo']);writer.writerows(rows)
    outputs={'inventario.csv':stream.getvalue(),'README.md':result_text}
    changed=[name for name,content in outputs.items() if not (root/name).exists() or read(root/name)!=content]
    if not check:
        for name in changed:(root/name).write_text(outputs[name],encoding='utf-8',newline='')
    added,removed=set(rows)-set(previous),set(previous)-set(rows)
    return dict(capítulos=len(chapters),entradas=len(rows),adicionados=sorted(added),removidos=sorted(removed),renomeacoes_git=git_renames(root,added,removed),documentos_desatualizados=changed,avisos=sorted(set(warnings)),links_invalidos=problems)


def main(argv=None) -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1])
    parser.add_argument('--check',action='store_true',help='Não escreve; retorna 1 se houver divergência ou link inválido.')
    args=parser.parse_args(argv)
    try:result=reconcile(args.root.resolve(),args.check)
    except (OSError,ValueError,UnicodeError) as exc:
        print('ERRO: '+str(exc),file=sys.stderr);return 2
    print(f"{result['capítulos']} capítulos; {result['entradas']} entradas; +{len(result['adicionados'])}/-{len(result['removidos'])}.")
    for key in ('adicionados','removidos'):
        for module,name in result[key]:print(f'{key}: {module}/{name}')
    for old,new in result['renomeacoes_git']:print(f'Renomeação registrada pelo Git: {old} -> {new}')
    for name in result['documentos_desatualizados']:print(('Desatualizado: ' if args.check else 'Atualizado: ')+name)
    for warning in result['avisos']:print('AVISO: '+warning)
    return int(bool(result['links_invalidos'] or args.check and result['documentos_desatualizados']))


if __name__=='__main__':
    raise SystemExit(main())
