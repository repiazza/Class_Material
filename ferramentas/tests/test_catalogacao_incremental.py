import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import struct
import subprocess
import tempfile
import unittest
import zipfile
import zlib
from docx import Document

SPEC=importlib.util.spec_from_file_location('incremental',Path(__file__).resolve().parents[1]/'catalogacao_incremental.py')
c=importlib.util.module_from_spec(SPEC);SPEC.loader.exec_module(c)


def png(rgb):
    def chunk(kind,data):return struct.pack('>I',len(data))+kind+data+struct.pack('>I',zlib.crc32(kind+data))
    return b'\x89PNG\r\n\x1a\n'+chunk(b'IHDR',struct.pack('>IIBBBBB',1,1,8,2,0,0,0))+chunk(b'IDAT',zlib.compress(b'\0'+bytes(rgb)))+chunk(b'IEND',b'')


@unittest.skipUnless(shutil.which('git'),'Git necessário à procedência da baseline')
class IncrementalTest(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name);self.module='01_Teste';self.folder=self.root/self.module;self.folder.mkdir()
        self.a=self.folder/'a.png';self.b=self.folder/'b.png';self.a.write_bytes(png((255,0,0)));self.b.write_bytes(png((0,255,0)))
        (self.root/'curadoria').mkdir()
        (self.root/c.NORMS[0]).write_text('| Palavra-chave canônica | Definição técnica consolidada |\n|---|---|\n| bit | Unidade binária. |\n| lógica booleana | Operações sobre valores lógicos. |\n',encoding='utf-8')
        (self.root/c.NORMS[1]).write_text('# Relações\n',encoding='utf-8')
        (self.root/'inventario.csv').write_text('modulo;arquivo\n01_Teste;a.png\n01_Teste;b.png\n01_Teste;01_Catalogo_Semantico.docx\n')
        self.canonical=self.folder/'01_Catalogo_Semantico.docx'
        self.make_catalog()
        self.git('init','-q');self.git('add','.');self.git('-c','user.name=Fixture','-c','user.email=fixture@example.invalid','commit','-qm','catalogado')
        self.reference=self.git('rev-parse','HEAD').decode().strip()
        self.initial=self.root/'baseline.docx'
        c.establish(self.root,self.module,self.canonical,self.root,self.reference,self.initial)

    def git(self,*args):
        return subprocess.run(['git','-C',str(self.root),*args],check=True,capture_output=True).stdout

    def make_catalog(self,table=False):
        d=Document();d.add_heading('01 — Teste',0);d.add_paragraph('2 arquivos: 2 PNG. Escopo preservado.')
        for i,name in enumerate(['a.png','b.png'],1):
            d.add_heading(f'{i:02d}. {name}',2)
            if table:
                t=d.add_table(rows=1,cols=1);t.cell(0,0).text='Conteúdo apresentado. Tabela preservada.'
            else:d.add_paragraph('Conteúdo apresentado. Imagem de fixture '+name)
            d.add_paragraph('Representação e exemplos. Um pixel sintético.')
            d.add_paragraph('Palavras-chave. bit')
        d.add_heading('Glossário de palavras-chave',1);d.add_paragraph('bit — Unidade binária.');d.add_paragraph('Arquivos: a.png, b.png');d.save(self.canonical)

    def packet(self,catalog,**items):
        p=c.plan(self.root,self.module,catalog)
        return {'catalogo_sha256':p['catalogo_sha256'],'fichas':{self.module+'/'+name:item for name,item in items.items()}}

    def item(self,name,old=None):
        result={'conteudo':'Imagem sintética de teste, sem interpretação do acervo.','representacao':'PNG de um pixel RGB.','palavras_chave':['bit'],'evidencia':'Fixture gerada por zlib; conteúdo conhecido do teste.','sha256_observado':c.sha((self.folder/name).read_bytes())}
        if old:result.update(anterior_sha256=old['sha256'],justificativa='Fixture alterou o pixel; revisão localizada.')
        return result

    def reads(self,result):return [x['arquivo'] for x in result['leituras'] if x['operacao']=='interpretacao_solicitada']

    def test_inclusao_png_preserva_demais_fichas_sem_interpretar(self):
        (self.folder/'novo.png').write_bytes(png((0,0,255)))
        before=c.Catalogo(self.initial);dest=self.root/'novo.docx';calls=[]
        def interpreter(identity,data,item,old):calls.append(identity);return item
        result=c.apply(self.root,self.module,self.initial,self.packet(self.initial,**{'novo.png':self.item('novo.png')}),dest,interpreter=interpreter)
        after=c.Catalogo(dest)
        self.assertEqual(calls,['01_Teste/novo.png']);self.assertEqual(self.reads(result),calls)
        self.assertEqual(len(after.records),3)
        for name in before.records:self.assertEqual(before.records[name]['sha256'],after.records[name]['sha256'])
        self.assertEqual(set(after.gloss['bit']['refs']),{'a.png','b.png','novo.png'})
        self.assertTrue(after.evidence())

    def test_modificacao_somente_ficha_alterada(self):
        old=c.Catalogo(self.initial);self.a.write_bytes(png((0,0,255)))
        dest=self.root/'modificado.docx'
        result=c.apply(self.root,self.module,self.initial,self.packet(self.initial,**{'a.png':self.item('a.png',old.records['a.png'])}),dest)
        new=c.Catalogo(dest)
        self.assertEqual(self.reads(result),['01_Teste/a.png'])
        self.assertEqual(old.records['b.png']['sha256'],new.records['b.png']['sha256'])
        self.assertNotEqual(old.records['a.png']['sha256'],new.records['a.png']['sha256'])

    def test_sem_mudancas_idempotente_bytes_e_mtime(self):
        before=(self.initial.read_bytes(),self.initial.stat().st_mtime_ns)
        result=c.apply(self.root,self.module,self.initial,self.packet(self.initial),self.initial)
        self.assertFalse(result['alterado']);self.assertEqual(self.reads(result),[])
        self.assertEqual(before,(self.initial.read_bytes(),self.initial.stat().st_mtime_ns))

    def test_renomeacao_git_conteudo_igual_sem_interpretacao(self):
        self.git('mv','01_Teste/a.png','01_Teste/renomeado.png')
        dest=self.root/'renomeado.docx'
        result=c.apply(self.root,self.module,self.initial,self.packet(self.initial),dest)
        self.assertEqual(len(result['renomeacoes']),1);self.assertEqual(self.reads(result),[])
        cat=c.Catalogo(dest);self.assertIn('renomeado.png',cat.records);self.assertNotIn('a.png',cat.records)
        self.assertEqual(set(cat.gloss['bit']['refs']),{'renomeado.png','b.png'})

    def test_renomeacao_historica_desde_referencia_comprovada(self):
        self.git('mv','01_Teste/a.png','01_Teste/renomeado.png')
        self.git('-c','user.name=Fixture','-c','user.email=fixture@example.invalid','commit','-qm','renomeado')
        (self.root/'outro.txt').write_text('commit independente')
        self.git('add','outro.txt');self.git('-c','user.name=Fixture','-c','user.email=fixture@example.invalid','commit','-qm','outra mudança')
        p=c.plan(self.root,self.module,self.initial)
        self.assertEqual(len(p['renomeacoes']),1)
        self.assertEqual(p['estados']['01_Teste/renomeado.png'],'renomeado_destino')

    def test_hash_igual_sozinho_nao_prova_renomeacao(self):
        self.a.rename(self.folder/'outro.png')
        p=c.plan(self.root,self.module,self.initial)
        self.assertFalse(p['renomeacoes']);self.assertEqual(p['estados']['01_Teste/a.png'],'ausente');self.assertEqual(p['estados']['01_Teste/outro.png'],'novo')

    def test_ausente_preserva_ficha_e_baseline_sem_perda(self):
        self.a.unlink();before=self.initial.read_bytes()
        result=c.apply(self.root,self.module,self.initial,self.packet(self.initial),self.initial)
        self.assertEqual(result['ausentes_pendentes'],['01_Teste/a.png'])
        self.assertEqual(before,self.initial.read_bytes());self.assertEqual(self.reads(result),[])
        self.assertIn('a.png',c.Catalogo(self.initial).records)

    def test_ausente_nao_bloqueia_novo_independente(self):
        self.a.unlink();(self.folder/'novo.png').write_bytes(png((0,0,255)))
        dest=self.root/'parcial.docx'
        result=c.apply(self.root,self.module,self.initial,self.packet(self.initial,**{'novo.png':self.item('novo.png')}),dest)
        self.assertEqual(result['ausentes_pendentes'],['01_Teste/a.png'])
        self.assertEqual(len(c.Catalogo(dest).records),3)

    def test_sem_baseline_bloqueia_antes_de_ler_originais(self):
        reader=c.Leituras()
        with self.assertRaisesRegex(c.Bloqueio,'BASELINE_AUSENTE'):c.plan(self.root,self.module,self.canonical,reader)
        self.assertEqual(reader.eventos,[])

    def test_catalogo_modificado_fora_da_baseline_bloqueia(self):
        bad=self.root/'alterado.docx'
        with zipfile.ZipFile(self.initial) as z,zipfile.ZipFile(bad,'w') as out:
            for name in z.namelist():
                data=z.read(name)
                if name=='word/document.xml':data=data.replace(b'2 arquivos:',b'3 arquivos:')
                out.writestr(name,data)
        with self.assertRaisesRegex(c.Bloqueio,'BASELINE_INCONSISTENTE'):c.plan(self.root,self.module,bad)

    def test_baseline_nao_e_hash_cego_da_arvore_atual(self):
        self.a.write_bytes(png((0,0,255)))
        output=self.root/'historica.docx'
        c.establish(self.root,self.module,self.canonical,self.root,self.reference,output)
        self.assertEqual(c.plan(self.root,self.module,output)['estados']['01_Teste/a.png'],'modificado')

    def test_referencia_de_catalogo_incorreta_recusada(self):
        changed=self.root/'outro.docx';d=Document(self.canonical);d.add_paragraph('alterado');d.save(changed)
        with self.assertRaisesRegex(c.Bloqueio,'difere da versão Git'):c.establish(self.root,self.module,changed,self.root,self.reference,self.root/'nao.docx')

    def test_inalterado_proibido_no_pacote_e_na_leitura_semantica(self):
        with self.assertRaisesRegex(c.Bloqueio,'inalterados proibidos'):c.apply(self.root,self.module,self.initial,self.packet(self.initial,**{'a.png':self.item('a.png')}),self.root/'erro.docx')
        with self.assertRaises(c.Bloqueio):c.Leituras().inspect(self.a,'01_Teste/a.png')

    def test_revisao_exige_confronto_da_ficha_anterior(self):
        self.a.write_bytes(png((0,0,255)))
        with self.assertRaisesRegex(c.Bloqueio,'ficha anterior'):c.apply(self.root,self.module,self.initial,self.packet(self.initial,**{'a.png':self.item('a.png')}),self.root/'erro.docx')

    def test_hash_observado_incompativel_e_recusado(self):
        (self.folder/'novo.png').write_bytes(png((0,0,255)));item=self.item('novo.png');item['sha256_observado']='0'*64
        with self.assertRaisesRegex(c.Bloqueio,'Material mudou'):c.apply(self.root,self.module,self.initial,self.packet(self.initial,**{'novo.png':item}),self.root/'erro.docx')

    def test_docx_tabelas_e_consumo_motor1_preservados(self):
        self.make_catalog(table=True);self.git('add','.');self.git('-c','user.name=Fixture','-c','user.email=fixture@example.invalid','commit','-qm','fichas com tabela')
        source=self.root/'tabelas-baseline.docx';c.establish(self.root,self.module,self.canonical,self.root,'HEAD',source)
        (self.folder/'novo.png').write_bytes(png((0,0,255)));dest=self.root/'tabelas-novo.docx'
        c.apply(self.root,self.module,source,self.packet(source,**{'novo.png':self.item('novo.png')}),dest)
        d=Document(dest);self.assertEqual(len(d.tables),2)
        self.assertTrue(all(t.cell(0,0).text=='Conteúdo apresentado. Tabela preservada.' for t in d.tables))
        self.assertTrue(any('novo.png'==p.text for p in d.paragraphs));c.Catalogo(dest).validate()

    def test_vocabulário_e_relacoes_mudam_sem_reinterpretar_originais(self):
        path=self.root/c.NORMS[1];path.write_text('# Relações\nUma revisão normativa.\n')
        p=c.plan(self.root,self.module,self.initial)
        self.assertEqual(p['normas_alteradas'],[c.NORMS[1]])
        result=c.apply(self.root,self.module,self.initial,self.packet(self.initial),self.initial)
        self.assertEqual(self.reads(result),[]);self.assertFalse(result['alterado'])

    def test_etiqueta_nova_fica_proposta_local(self):
        (self.folder/'novo.png').write_bytes(png((0,0,255)));item=self.item('novo.png');item['palavras_chave']=['termo local']
        packet=self.packet(self.initial,**{'novo.png':item});packet['termos_locais_propostos']={'termo local':'Definição da fixture.'}
        dest=self.root/'local.docx';result=c.apply(self.root,self.module,self.initial,packet,dest)
        self.assertEqual(result['propostas_terminologicas_pendentes'],['termo local'])
        self.assertIn('PENDENTE DE HOMOLOGAÇÃO',c.Catalogo(dest).gloss['termo local']['definition'])

    def test_nao_sobrescreve_catalogo_canonico_rastreado(self):
        with self.assertRaisesRegex(c.Bloqueio,'rastreada protegida'):c.establish(self.root,self.module,self.canonical,self.root,self.reference,self.canonical)

    def test_baseline_hashes_malformados_bloqueia_sem_leitura(self):
        bad=self.root/'baseline-invalida.docx'
        with zipfile.ZipFile(self.initial) as z,zipfile.ZipFile(bad,'w') as out:
            for name in z.namelist():
                payload=z.read(name)
                if name==c.PART:
                    node=c.ET.fromstring(payload);value=json.loads(node.text);value['materiais']['01_Teste/a.png']=False;node.text=json.dumps(value);payload=c.xml(node)
                out.writestr(name,payload)
        reader=c.Leituras()
        with self.assertRaisesRegex(c.Bloqueio,'BASELINE_INVALIDA'):c.plan(self.root,self.module,bad,reader)
        self.assertEqual(reader.eventos,[])

    def test_candidato_novo_dentro_do_acervo_recusado(self):
        with self.assertRaisesRegex(c.Bloqueio,'dentro do acervo'):c.establish(self.root,self.module,self.canonical,self.root,self.reference,self.folder/'experimental.docx')

    def test_reverso_inconsistente_bloqueia_leitura_controlada(self):
        bad=self.root/'reverso.docx';d=Document(self.canonical)
        next(p for p in d.paragraphs if p.text.startswith('Arquivos:')).text='Arquivos: a.png'
        d.save(bad)
        with self.assertRaisesRegex(c.Bloqueio,'inconsistente'):c.Catalogo(bad)


if __name__=='__main__':unittest.main()
