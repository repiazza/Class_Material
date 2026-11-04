#!/usr/bin/env python3
"""Planejamento por hashes e aplicação localizada em DOCX candidato (sem visão automática)."""
from __future__ import annotations
import argparse
from collections import Counter
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import zipfile
from lxml import etree as ET

sys.path.insert(0, str(Path(__file__).resolve().parent))
import reconciliar_documentacao as fisico

W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
PART = 'customXml/catalogacao_baseline.xml'
NS = 'urn:class-material:catalogacao-incremental:1'
FILE = re.compile(r'^(?:(\d+)[.)]\s+)?(?:Arquivo:\s*)?(.+\.(?:png|jpe?g|gif|md|c|h|zip))$', re.I)
NORMS = ('curadoria/vocabulario_controlado.md', 'curadoria/relacionamentos_conceituais.md')


class Bloqueio(ValueError):
    pass


def sha(data):
    return hashlib.sha256(data).hexdigest()


def text(node):
    return ''.join(t.text or '' for t in node.iter(W+'t')).strip()


def xml(node):
    return ET.tostring(node, encoding='utf-8', xml_declaration=True)


def digest(nodes):
    return sha(b''.join(xml(n) for n in nodes))


def split_terms(value):
    return [x.strip() for x in re.split(r'\s*·\s*|\s*;\s*|\s*,\s*', value) if x.strip()]


class Catalogo:
    def __init__(self, path):
        self.path = Path(path) if isinstance(path,(str,Path)) else None
        try:
            with zipfile.ZipFile(path) as z:
                if z.testzip():
                    raise Bloqueio('DOCX com CRC inválido.')
                self.infos = z.infolist()
                self.parts = {i.filename:z.read(i) for i in self.infos}
            self.tree = ET.fromstring(self.parts['word/document.xml'])
            self.body = self.tree.find(W+'body')
            if self.body is None:raise Bloqueio('Documento sem corpo WordprocessingML.')
            self.nodes = list(self.body)
        except (OSError, zipfile.BadZipFile, KeyError, ET.ParseError) as exc:
            raise Bloqueio('DOCX ilegível ou formato não suportado: '+str(exc)) from exc
        self.records = {}
        heads=[]
        for i,node in enumerate(self.nodes):
            if node.tag != W+'p':
                continue
            value=text(node)
            if value.startswith('Glossário'):
                self.gloss_start=i
                break
            match=FILE.fullmatch(value)
            if match and (match[1] or value.startswith("Arquivo: ") or not re.search(r"[.:]\s",value)):
                heads.append((i,match[2]))
        else:
            raise Bloqueio('Glossário identificável ausente; não reconstruir catálogo.')
        if not heads:
            raise Bloqueio('Fichas identificáveis ausentes; requer adaptação controlada.')
        self.prefix=self.nodes[:heads[0][0]]
        for pos,(start,name) in enumerate(heads):
            end=heads[pos+1][0] if pos+1<len(heads) else self.gloss_start
            if name in self.records:
                raise Bloqueio('Ficha duplicada: '+name)
            block=self.nodes[start:end]
            keywords=[]
            for n in block:
                for p in ([n] if n.tag==W+'p' else list(n.iter(W+'p'))):
                    m=re.match(r'^Palavras-chave[.:]\s*(.+)',text(p))
                    if m:
                        keywords.extend(split_terms(m[1]))
            if not keywords or len(keywords)!=len(set(keywords)):
                raise Bloqueio('Etiquetas ausentes/duplicadas na ficha '+name)
            self.records[name]={'nodes':block,'terms':keywords,'sha256':digest(block)}
        used=set(t for r in self.records.values() for t in r['terms'])
        self.gloss={};self.gloss_prefix=[];self.tail=[]
        pending=None;block=[];definition='';started=False
        # Os formatos existentes incluem termo separado, termo — definição e termo. definição.
        for node in self.nodes[self.gloss_start+1:]:
            value=text(node)
            candidate=next((t for t in sorted(used,key=lambda t:-len(t)) if value==t or value.startswith(t+' — ') or value.startswith(t+'. ')),None)
            if candidate:
                if pending:
                    raise Bloqueio('Entrada de glossário sem índice: '+pending)
                pending=candidate;block=[node];definition=value[len(candidate):].lstrip(' —.');started=True
                continue
            if pending:
                block.append(node)
                ref=re.match(r'^(?:Materiais|Arquivos|Arquivos associados):\s*(.*)',value)
                if ref:
                    if pending in self.gloss:
                        raise Bloqueio('Termo duplicado no glossário: '+pending)
                    self.gloss[pending]={'nodes':block,'definition':definition,'refs':split_terms(ref[1])}
                    pending=None;block=[]
                elif value:
                    definition=(definition+' '+value).strip()
            elif not started:
                self.gloss_prefix.append(node)
            else:
                self.tail.append(node)
        if pending or set(self.gloss)!=used:
            raise Bloqueio('Glossário incompleto ou estrutura não reconhecida.')
        self.validate()

    def validate(self):
        rev={t:[] for t in self.gloss}
        for name,r in self.records.items():
            for term in r['terms']:
                if term not in rev:
                    raise Bloqueio('Etiqueta sem definição: '+term)
                rev[term].append(name)
        for term,entry in self.gloss.items():
            if not entry['definition'] or len(entry['refs'])!=len(set(entry['refs'])) or set(entry['refs'])!=set(rev[term]):
                raise Bloqueio('Glossário/reverso inconsistente: '+term)
        return rev

    def fingerprint(self):
        return {n:sha(v) for n,v in self.parts.items() if n not in {PART,'[Content_Types].xml','_rels/.rels'}}

    def evidence(self):
        if PART not in self.parts:
            raise Bloqueio('BASELINE_AUSENTE: estabelecer referência controlada, sem reconstrução integral.')
        try:
            root=ET.fromstring(self.parts[PART]);data=json.loads(root.text)
        except (ET.ParseError,ValueError,TypeError) as exc:
            raise Bloqueio('BASELINE_INVALIDA: '+str(exc)) from exc
        if not isinstance(data,dict) or not isinstance(data.get('modulo'),str) or not isinstance(data.get('materiais'),dict) or not isinstance(data.get('origem'),dict) or not isinstance(data.get('normas'),dict):
            raise Bloqueio('BASELINE_INVALIDA: campos obrigatórios ausentes ou malformados.')
        if set(data['normas'])!=set(NORMS) or any(v is not None and (not isinstance(v,str) or not re.fullmatch(r'[a-f0-9]{64}',v)) for v in data['normas'].values()):
            raise Bloqueio('BASELINE_INVALIDA: referências normativas.')
        if data.get('schema')!=1 or data.get('partes_catalogo')!=self.fingerprint():
            raise Bloqueio('BASELINE_INCONSISTENTE: o pacote catalogado mudou fora da referência.')
        if set(data.get('materiais',{}))!=set(data['modulo']+'/'+name for name in self.records):
            raise Bloqueio('BASELINE_INCONSISTENTE: fichas e identidades divergem.')
        if not data.get('origem',{}).get('catalogo_sha256') or not data['origem'].get('referencia_commit'):
            raise Bloqueio('BASELINE_SEM_PROCEDENCIA.')
        if any(not isinstance(h,str) or not re.fullmatch(r'[a-f0-9]{64}',h) for h in data['materiais'].values()):
            raise Bloqueio('BASELINE_INVALIDA: hashes materiais.')
        return data


class Leituras:
    """Separa hash binário de solicitação de interpretação; não certifica visão/ASR."""
    def __init__(self):
        self.eventos=[]
        self.permitidos=set()

    def hash(self,path,identity):
        self.eventos.append({'operacao':'hash_binario','arquivo':identity})
        return sha(Path(path).read_bytes())

    def inspect(self,path,identity):
        if identity not in self.permitidos:
            raise Bloqueio('Interpretação de material inalterado proibida: '+identity)
        self.eventos.append({'operacao':'interpretacao_solicitada','arquivo':identity})
        return Path(path).read_bytes()


def sources(root,module):
    chapters,rows,warnings=fisico.scan(root,fisico.inventory(root))
    if module not in {p.name for p in chapters}:
        raise Bloqueio('Capítulo inexistente.')
    catalog=module.split('_')[0]+'_Catalogo_Semantico.docx'
    return [name for mod,name in rows if mod==module and name!=catalog],warnings


def norms(root):
    return {name:sha((root/name).read_bytes()) if (root/name).is_file() else None for name in NORMS}


def vocabulary(root):
    path=root/NORMS[0]
    if not path.is_file():
        raise Bloqueio('Vocabulário mestre ausente.')
    result={}
    for line in path.read_text(encoding='utf-8').splitlines():
        if line.startswith('| '):
            cells=[x.strip().strip('`').replace(r'\|','|') for x in re.split(r'(?<!\\)\|',line.strip('|'))]
            if len(cells)>=2 and cells[0] not in {'Palavra-chave canônica','---'}:
                result[cells[0]]=cells[1]
    return result


def git(root,*args):
    proc=subprocess.run(['git','-C',str(root),*args],capture_output=True,check=False)
    if proc.returncode:
        raise Bloqueio('Referência Git não verificável: '+proc.stderr.decode(errors='replace').strip())
    return proc.stdout


def candidate(path,source):
    path=Path(path).resolve()
    # Uma saída candidata nunca substitui arquivo rastreado, mesmo com nome canônico.
    parent=path.parent
    if parent.exists():
        proc=subprocess.run(['git','-C',str(parent),'ls-files','--error-unmatch','--',path.name],capture_output=True,check=False)
        if proc.returncode==0:
            raise Bloqueio('Saída rastreada protegida; use candidato fora do Git.')
    if path==Path(source).resolve() and path.name.endswith('_Catalogo_Semantico.docx'):
        # Permitido apenas no-op; escrita efetiva passa por save() com comparação.
        return path
    return path


def save(catalog,dest,evidence,document=None,validator=None):
    if Path(dest).suffix.lower()!='.docx':raise Bloqueio('Candidato deve ser DOCX.')
    dest=candidate(dest,catalog.path)
    parts=dict(catalog.parts)
    if document is not None:
        parts['word/document.xml']=document
    evidence=deepcopy(evidence)
    evidence['partes_catalogo']={n:sha(v) for n,v in parts.items() if n not in {PART,'[Content_Types].xml','_rels/.rels'}}
    element=ET.Element('{'+NS+'}baseline');element.text=json.dumps(evidence,ensure_ascii=False,sort_keys=True,separators=(',',':'))
    parts[PART]=xml(element)
    content_ns='http://schemas.openxmlformats.org/package/2006/content-types'
    types=ET.fromstring(parts['[Content_Types].xml'])
    if not any(n.get('PartName')=='/'+PART for n in types):
        ET.SubElement(types,'{'+content_ns+'}Override',PartName='/'+PART,ContentType='application/xml')
        parts['[Content_Types].xml']=xml(types)
    rel_ns='http://schemas.openxmlformats.org/package/2006/relationships'
    rels=ET.fromstring(parts['_rels/.rels'])
    if not any(n.get('Target')==PART for n in rels):
        rid='rIdCatalogacaoIncremental'
        if any(n.get('Id')==rid for n in rels):
            raise Bloqueio('Relacionamento OPC reservado já utilizado.')
        ET.SubElement(rels,'{'+rel_ns+'}Relationship',Id=rid,Type='http://schemas.openxmlformats.org/officeDocument/2006/relationships/customXml',Target=PART)
        parts['_rels/.rels']=xml(rels)
    if parts==catalog.parts:
        if dest!=catalog.path.resolve():
            payload=catalog.path.read_bytes()
            if not dest.exists() or dest.read_bytes()!=payload:
                dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(payload)
        return
    if dest==catalog.path.resolve() and dest.name.endswith('_Catalogo_Semantico.docx'):
        raise Bloqueio('Não sobrescrever a entrada; fornecer outro candidato.')
    dest.parent.mkdir(parents=True,exist_ok=True)
    # Validar candidato inteiramente em memória antes de qualquer publicação.
    import io
    out=io.BytesIO()
    with zipfile.ZipFile(out,'w') as z:
        known=set()
        for info in catalog.infos:
            z.writestr(info,parts[info.filename]);known.add(info.filename)
        for name in sorted(set(parts)-known):
            info=zipfile.ZipInfo(name,date_time=(1980,1,1,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;z.writestr(info,parts[name])
    payload=out.getvalue()
    preview=Catalogo(io.BytesIO(payload));preview.evidence()
    if validator:validator(preview)
    if not dest.exists() or dest.read_bytes()!=payload:
        dest.write_bytes(payload)


def output_guard(root,module,catalog_path,output):
    candidate(output,catalog_path)
    if Path(output).resolve().is_relative_to((Path(root)/module).resolve()):
        raise Bloqueio('Saída dentro do acervo proibida neste fluxo; use candidato externo.')


def establish(root,module,catalog_path,repo,reference,output):
    output_guard(root,module,catalog_path,output)
    cat=Catalogo(catalog_path)
    if PART in cat.parts:
        raise Bloqueio('Baseline já existe; não recalibrar silenciosamente.')
    revision=git(repo,'rev-parse',reference+'^{commit}').decode().strip()
    canonical=module+'/'+module.split('_')[0]+'_Catalogo_Semantico.docx'
    old=git(repo,'show',revision+':'+canonical)
    if old!=Path(catalog_path).read_bytes():
        raise Bloqueio('Catálogo fornecido difere da versão Git; baseline recusada.')
    materials={module+'/'+name:sha(git(repo,'show',revision+':'+module+'/'+name)) for name in cat.records}
    norm={}
    for name in NORMS:
        try:norm[name]=sha(git(repo,'show',revision+':'+name))
        except Bloqueio:norm[name]=None
    data={'schema':1,'modulo':module,'origem':{'referencia_commit':revision,'catalogo_sha256':sha(old),'metodo':'snapshot Git do catálogo e originais presentes na mesma revisão; não é homologação semântica'},'materiais':materials,'normas':norm}
    save(cat,output,data)
    Catalogo(output).evidence()
    return {'baseline':'ESTABELECIDA_EM_CANDIDATO','referencia_commit':revision,'fichas':len(cat.records),'interpretacoes':0}


def plan(root,module,catalog_path,reader=None):
    reader=reader or Leituras()
    cat=Catalogo(catalog_path);base=cat.evidence()
    if base['modulo']!=module:
        raise Bloqueio('Baseline de outro capítulo.')
    names,warnings=sources(root,module)
    now={module+'/'+name:reader.hash(root/module/name,module+'/'+name) for name in names}
    before=base['materiais'];states={}
    for key in sorted(set(now)|set(before)):
        states[key]='ausente' if key not in now else 'novo' if key not in before else 'inalterado' if now[key]==before[key] else 'modificado'
    added={tuple(k.split('/',1)) for k,s in states.items() if s=='novo'}
    removed={tuple(k.split('/',1)) for k,s in states.items() if s=='ausente'}
    renames=[]
    for old,new in fisico.git_renames(root,added,removed,reference=base['origem']['referencia_commit']):
        if before[old]==now[new]:
            renames.append({'origem':old,'destino':new,'evidencia':'Git R + SHA-256 idêntico'})
            states[old]='renomeado_origem';states[new]='renomeado_destino'
    current_norm=norms(root)
    return {'modulo':module,'catalogo_sha256':sha(Path(catalog_path).read_bytes()),'estados':states,'hashes_atuais':now,'renomeacoes':renames,'ausentes_pendentes':[k for k,s in states.items() if s=='ausente'],'normas_alteradas':[k for k in NORMS if base.get('normas',{}).get(k)!=current_norm[k]],'fichas_sha256':{k:v['sha256'] for k,v in cat.records.items()},'avisos':warnings,'leituras':reader.eventos}


def paragraph(value,template=None):
    if template is not None:
        p=deepcopy(template)
        for n in list(p):
            if n.tag!=W+'pPr':p.remove(n)
    else:p=ET.Element(W+'p')
    run=ET.SubElement(p,W+'r')
    if template is not None:
        first=next(template.iter(W+'rPr'),None)
        if first is not None:run.append(deepcopy(first))
    node=ET.SubElement(run,W+'t');node.text=value
    return p


def new_record(name,item,old=None,title_template=None):
    if not isinstance(item,dict):raise Bloqueio('Ficha deve ser objeto: '+name)
    required=('conteudo','representacao','palavras_chave','evidencia','sha256_observado')
    if any(not item.get(k) for k in required):
        raise Bloqueio('Ficha incompleta: '+name)
    if any(not isinstance(item[k],str) for k in ('conteudo','representacao','evidencia','sha256_observado')):
        raise Bloqueio('Campos textuais inválidos: '+name)
    terms=item['palavras_chave']
    if not isinstance(terms,list) or any(not isinstance(t,str) or not t.strip() for t in terms) or len(terms)!=len(set(terms)):
        raise Bloqueio('Etiquetas inválidas: '+name)
    if old and (item.get('anterior_sha256')!=old['sha256'] or not item.get('justificativa')):
        raise Bloqueio('Revisão requer ficha anterior exata e justificativa: '+name)
    header=paragraph(name,title_template)
    nodes=[header,paragraph('Conteúdo apresentado. '+item['conteudo']),paragraph('Representação e exemplos. '+item['representacao'])]
    if item.get('ressalvas'):nodes.append(paragraph('Ressalvas. '+item['ressalvas']))
    nodes.extend([paragraph('Referências visuais verificadas. '+item['evidencia']),paragraph('Palavras-chave. '+' · '.join(terms))])
    return {'nodes':nodes,'terms':terms,'sha256':digest(nodes)}


def apply(root,module,catalog_path,packet,output,reader=None,interpreter=None):
    output_guard(root,module,catalog_path,output)
    reader=reader or Leituras();p=plan(root,module,catalog_path,reader)
    if not isinstance(packet,dict) or not isinstance(packet.get('fichas'),dict):raise Bloqueio('Pacote deve conter fichas indexadas por identidade.')
    if packet.get('catalogo_sha256')!=p['catalogo_sha256']:
        raise Bloqueio('Pacote de interpretação não corresponde ao catálogo planejado.')
    changed={k for k,s in p['estados'].items() if s in {'novo','modificado'}}
    if set(packet.get('fichas',{}))!=changed:
        raise Bloqueio('Pacote deve cobrir exatamente novos/modificados; inalterados proibidos.')
    reader.permitidos=changed
    cat=Catalogo(catalog_path);base=cat.evidence();records=deepcopy(cat.records)
    definitions={k:v['definition'] for k,v in cat.gloss.items()}
    master=vocabulary(root)
    proposed=packet.get('termos_locais_propostos',{})
    if any(k in master for k in proposed):
        raise Bloqueio('Proposta local não pode redefinir etiqueta canônica.')
    for identity in sorted(changed):
        name=identity.split('/',1)[1]
        data=reader.inspect(root/identity,identity)
        item=interpreter(identity,data,packet['fichas'][identity],records.get(name)) if interpreter else packet['fichas'][identity]
        if sha(data)!=p['hashes_atuais'][identity] or item.get('sha256_observado')!=sha(data):
            raise Bloqueio('Material mudou entre planejamento e inspeção: '+identity)
        record=new_record(name,item,records.get(name),next(iter(records.values()))['nodes'][0])
        for term in record['terms']:
            if term not in definitions:
                if term in master:definitions[term]=master[term]
                elif term in proposed and proposed[term]:definitions[term]='PROPOSTA LOCAL — PENDENTE DE HOMOLOGAÇÃO. '+proposed[term]
                else:raise Bloqueio('Etiqueta sem definição fundamentada: '+term)
        records[name]=record
    for rename in p['renomeacoes']:
        old,new=rename['origem'].split('/',1)[1],rename['destino'].split('/',1)[1]
        replacement={}
        for name,r in records.items():
            if name==old:
                r['nodes'][0]=paragraph(text(r['nodes'][0]).replace(old,new),r['nodes'][0]);name=new
            # Referências textuais exatas, sem substituir conceitos ou partes de outros nomes.
            for node in r['nodes']:
                for t in node.iter(W+'t'):
                    if t.text:
                        t.text=re.sub(r'(?<![\w./-])'+re.escape(old)+r'(?![\w./-])',lambda _:new,t.text)
            replacement[name]=r
        records=replacement
    # Sem mudanças físicas resolúveis, manter bytes inclusive na presença de pendências.
    if not changed and not p['renomeacoes']:
        candidate(output,catalog_path)
        if Path(output).resolve()!=Path(catalog_path).resolve():
            payload=Path(catalog_path).read_bytes()
            if not Path(output).exists() or Path(output).read_bytes()!=payload:
                Path(output).parent.mkdir(parents=True,exist_ok=True);Path(output).write_bytes(payload)
        return {**p,'alterado':False,'leituras':reader.eventos,'interpretacoes':0,'impacto':[]}
    rev={}
    for name,r in records.items():
        for term in r['terms']:rev.setdefault(term,[]).append(name)
    gloss_nodes=[]
    term_order=[term for term in cat.gloss if term in rev]+sorted(set(rev)-set(cat.gloss),key=str.casefold)
    for term in term_order:
        if term in cat.gloss and set(cat.gloss[term]['refs'])==set(rev[term]):
            gloss_nodes.extend(deepcopy(cat.gloss[term]['nodes']))
        elif term in cat.gloss:
            entry=deepcopy(cat.gloss[term]['nodes'])
            for i,node in enumerate(entry):
                if re.match(r'^(?:Materiais|Arquivos|Arquivos associados):',text(node)):
                    prefix=text(node).split(':',1)[0]
                    entry[i]=paragraph(prefix+': '+'; '.join(rev[term]),node)
            gloss_nodes.extend(entry)
        else:
            gloss_nodes.extend([paragraph(term+' — '+definitions[term]),paragraph('Materiais: '+'; '.join(rev[term]))])
    body=deepcopy(cat.body)
    for node in list(body):body.remove(node)
    prefix=deepcopy(cat.prefix)
    # Só atualizar cobertura se suas métricas mudaram; renomeação simples preserva a introdução.
    coverage_changed=(len(records)!=len(cat.records) or set(rev)!=set(cat.gloss) or
                      Counter(Path(n).suffix.lower() for n in records)!=Counter(Path(n).suffix.lower() for n in cat.records))
    if coverage_changed:
        summary=f'{len(records)} arquivos catalogados · {len(rev)} palavras-chave únicas.'
        for node in prefix:
            value=text(node)
            if re.match(r'^\d+ (?:arquivos|materiais)',value):
                replacement=summary
                if '. ' in value:replacement+=' '+value.split('. ',1)[1]
            elif re.search(r'\| \d+ arquivos:',value):
                replacement=value.split('|',1)[0]+'| '+summary
            elif re.match(r'^Escopo: \d+ materiais',value):
                replacement='Escopo: '+summary+(' '+value.split('. ',1)[1] if '. ' in value else '')
            else:
                continue
            updated=paragraph(replacement,node)
            prefix[prefix.index(node)]=updated
    nodes=prefix+[n for r in records.values() for n in r['nodes']]+[deepcopy(cat.nodes[cat.gloss_start])]+deepcopy(cat.gloss_prefix)+gloss_nodes+deepcopy(cat.tail)
    for node in nodes:body.append(node)
    tree=deepcopy(cat.tree);tree.remove(tree.find(W+'body'));tree.append(body)
    for identity in changed:base['materiais'][identity]=p['hashes_atuais'][identity]
    for rename in p['renomeacoes']:
        del base['materiais'][rename['origem']];base['materiais'][rename['destino']]=p['hashes_atuais'][rename['destino']]
    # Validar a preservação antes de gravar: manter o contexto de namespaces do corpo.
    expected_tree=deepcopy(cat.tree)
    expected_body=expected_tree.find(W+'body')
    def validate_preservation(after):
        for name,r in cat.records.items():
            identity=module+'/'+name
            if p['estados'].get(identity)!='inalterado':continue
            expected=[expected_body[cat.nodes.index(node)] for node in r['nodes']]
            for rename in p['renomeacoes']:
                old,new=rename['origem'].split('/',1)[1],rename['destino'].split('/',1)[1]
                for node in expected:
                    for t in node.iter(W+'t'):
                        if t.text:t.text=re.sub(r'(?<![\w./-])'+re.escape(old)+r'(?![\w./-])',lambda _:new,t.text)
            if after.records[name]['sha256']!=digest(expected):
                raise Bloqueio('Preservação da ficha falhou: '+identity)
    save(cat,output,base,xml(tree),validator=validate_preservation)
    after=Catalogo(output);after.evidence()
    # Relação por etiquetas é candidato a impacto, nunca nova RC homologada.
    terms_changed=set(t for key in changed for t in records[key.split('/',1)[1]]['terms'])
    impact=[name for name,r in cat.records.items() if module+'/'+name not in changed and terms_changed.intersection(r['terms'])]
    return {**p,'alterado':True,'interpretacoes':len(changed),'leituras':reader.eventos,'impacto':impact,'impacto_natureza':'coocorrência documental para avaliação; não prova relação pedagógica','propostas_terminologicas_pendentes':list(proposed),'docx_integro':True,'glossario_reverso_exatos':True,'referencias_fisicas_validas':not bool(p['ausentes_pendentes']),'fichas':len(after.records)}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('operacao',choices=['baseline','planejar','aplicar'])
    parser.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1])
    parser.add_argument('--modulo',required=True)
    parser.add_argument('--catalogo',type=Path,required=True)
    parser.add_argument('--saida',type=Path)
    parser.add_argument('--referencia')
    parser.add_argument('--repositorio',type=Path)
    parser.add_argument('--fichas',type=Path)
    parser.add_argument('--relatorio',type=Path)
    args=parser.parse_args()
    try:
        if args.operacao=='baseline':
            if not args.saida or not args.referencia:raise Bloqueio('Baseline exige --saida e --referencia Git explícita.')
            result=establish(args.root,args.modulo,args.catalogo,args.repositorio or args.root,args.referencia,args.saida)
        elif args.operacao=='planejar':result=plan(args.root,args.modulo,args.catalogo)
        else:
            if not args.saida or not args.fichas:raise Bloqueio('Aplicação exige --saida e --fichas inspecionadas pelo agente.')
            result=apply(args.root,args.modulo,args.catalogo,json.loads(args.fichas.read_text(encoding='utf-8')),args.saida)
        payload=json.dumps(result,ensure_ascii=False,indent=2)
        if args.relatorio:
            candidate(args.relatorio,args.catalogo)
            args.relatorio.parent.mkdir(parents=True,exist_ok=True);args.relatorio.write_text(payload+'\n',encoding='utf-8')
        print(payload)
        return 0
    except (Bloqueio,OSError,ValueError) as exc:
        print('BLOQUEADO: '+str(exc),file=sys.stderr);return 2


if __name__=='__main__':raise SystemExit(main())
