import importlib.util
from pathlib import Path
import tempfile
import subprocess
import shutil
import unittest
import zipfile

SOURCE=Path(__file__).resolve().parents[1]/'reconciliar_documentacao.py'
spec=importlib.util.spec_from_file_location('reconciliacao',SOURCE)
m=importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


class ReconciliacaoTest(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name)
        self.put('README.md','# Acervo\n\nIntrodução editorial preservada.\n\n'+ '\n\n'.join(m.BEGIN.format(x)+'\nantigo\n'+m.END.format(x) for x in m.BLOCKS)+'\n\n## Histórico humano\nDecisão inalterada.\n')
        self.put('inventario.csv','modulo;arquivo\n')
        self.put('AGENTS.md','# Regras\n')
        for name in ['catalogacao_semantica','roteirizacao','consolidacao_editorial','roteiro_individual','mapeamento_espacial','montagem_audiovisual','revisao_audiovisual','retroalimentacao']:
            self.put(f'curadoria/protocolo_{name}.md',f'# Protocolo {name}\n\n**Versão:** 0.1\n**Estado:** PROPOSTO\n')
        for file in ['curadoria/contrato_entrega_video.md','curadoria/vocabulario_controlado.md','curadoria/relacionamentos_conceituais.md','ferramentas/README.md']:
            self.put(file,'# Referência\n')
        self.put('ferramentas/reconciliar_documentacao.py','# presença do comando\n')
        self.put('01_Teste/exercicio.md','# 01 — Primeiro teste\n## Exercício — Duas partes\n')
        self.put('01_Teste/gabarito_a.md','# Gabarito — Parte A\n')
        self.put('01_Teste/gabarito_b.md','# Gabarito — Parte B\n')
        self.put('01_Teste/original.png','imagem simulada: só existência física, não validação visual')

    def put(self,name,data):
        p=self.root/name;p.parent.mkdir(parents=True,exist_ok=True)
        p.write_bytes(data if isinstance(data,bytes) else data.encode())
        return p

    def run_sync(self,check=False):
        return m.reconcile(self.root,check)

    def rows(self):
        return set(m.inventory(self.root))

    def test_inclusao_png_unicode_e_caixa(self):
        self.run_sync();self.put('01_Teste/Memória NOVA.PNG',b'x')
        result=self.run_sync()
        self.assertIn(('01_Teste','Memória NOVA.PNG'),result['adicionados'])
        self.assertIn('Memória NOVA.PNG',m.read(self.root/'inventario.csv'))
        self.assertEqual(m.local_links(self.root,m.read(self.root/'README.md')),[])

    def test_novo_capitulo_sem_catalogo(self):
        self.put('14_Novo_Capitulo/novo.png',b'x');self.run_sync()
        text=m.read(self.root/'README.md')
        self.assertIn('14_Novo_Capitulo/',text)
        self.assertIn('Sem catálogo canônico',text)
        self.assertIn('14 - Novo Capitulo',text)

    def test_remocao_e_renomeacao(self):
        self.run_sync()
        (self.root/'01_Teste/original.png').rename(self.root/'01_Teste/renomeado.png')
        change=self.run_sync()
        self.assertIn(('01_Teste','original.png'),change['removidos'])
        self.assertIn(('01_Teste','renomeado.png'),change['adicionados'])
        (self.root/'01_Teste/renomeado.png').unlink()
        self.assertIn(('01_Teste','renomeado.png'),self.run_sync()['removidos'])

    @unittest.skipUnless(shutil.which('git'),'Git opcional não disponível')
    def test_renomeacao_registrada_pelo_git(self):
        self.run_sync()
        def git(*args):
            subprocess.run(['git','-C',str(self.root),*args],check=True,capture_output=True)
        git('init','-q')
        git('add','.')
        git('-c','user.name=Fixture','-c','user.email=fixture@example.invalid','commit','-qm','fixture')
        git('mv','01_Teste/original.png','01_Teste/renomeado.png')
        result=self.run_sync()
        self.assertEqual(result['renomeacoes_git'],[('01_Teste/original.png','01_Teste/renomeado.png')])

    def test_catalogo_canonico_e_titulo_xml(self):
        self.run_sync()
        p=self.root/'01_Teste/01_Catalogo_Semantico.docx'
        with zipfile.ZipFile(p,'w') as z:
            z.writestr('word/document.xml','<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:body><w:p><w:r><w:t>01 — Título documentado</w:t></w:r></w:p></w:body></w:document>')
        self.run_sync()
        self.assertIn(('01_Teste',p.name),self.rows())
        self.assertIn('01 - Título documentado',m.read(self.root/'README.md'))

    def test_derivados_excluidos_por_papel_e_localizacao(self):
        for file in ['01_Teste/01_Mapa_Espacial.json','01_Teste/01_Autoauditoria_Mapa.md','01_Teste/evidencias_mapa_espacial/painel.png','01_Teste/evidencias_mapa_espacial/nota.md','01_Teste/derivados/copia.PNG','01_Teste/relatorio.md','01_Teste/renderizar.py','01_Teste/01_Catalogo_Semantico_Experimental.docx','01_Teste/arquivo.tmp']:
            self.put(file,'artefato técnico')
        result=self.run_sync()
        self.assertEqual(len(self.rows()),4)
        self.assertFalse(result['avisos'])

    def test_zip_e_headers_em_subdiretorio(self):
        self.put('01_Teste/include/calc.h','#define CALC 1\n')
        p=self.root/'01_Teste/apoio.zip'
        with zipfile.ZipFile(p,'w') as z:z.writestr('src/oculto.c','int x;')
        self.run_sync()
        self.assertIn(('01_Teste','apoio.zip'),self.rows())
        self.assertIn(('01_Teste','include/calc.h'),self.rows())
        self.assertFalse(any('oculto.c' in x[1] for x in self.rows()))

    def test_exercicios_gabaritos_sem_pareamento_inventado(self):
        self.put('01_Teste/gabarito_a_b_makefile_possivel.md','# Gabarito — Alternativa para B\n')
        self.run_sync();text=m.read(self.root/'README.md')
        self.assertIn('Parte A',text);self.assertIn('Parte B',text);self.assertIn('Alternativa para B',text)
        self.assertIn('sem presumir pareamento',text)
        self.assertIn('01 - Primeiro teste',text)

    def test_links_invalidos_inclusive_ancora_e_mermaid(self):
        self.run_sync();p=self.root/'README.md'
        p.write_text(m.read(p)+'\n[Erro](ausente.md)\n[Âncora](README.md#nao-existe)\n')
        self.assertEqual(len(self.run_sync(True)['links_invalidos']),2)
        self.assertEqual(m.local_links(self.root,'click X "./sumiu.md"'),['Link local inexistente: ./sumiu.md'])
        self.assertIn('[Erro](ausente.md)',m.read(p))
        self.assertEqual(m.main(['--root',str(self.root),'--check']),1)

    def test_idempotencia_e_ausencia_de_escrita(self):
        self.run_sync()
        files=[self.root/'README.md',self.root/'inventario.csv']
        before=[(p.read_bytes(),p.stat().st_mtime_ns) for p in files]
        result=self.run_sync()
        self.assertEqual(result['documentos_desatualizados'],[])
        self.assertEqual(before,[(p.read_bytes(),p.stat().st_mtime_ns) for p in files])
        self.assertEqual(self.run_sync(True)['documentos_desatualizados'],[])

    def test_check_nao_escreve_documentos_desatualizados(self):
        before=(self.root/'README.md').read_bytes()
        self.assertTrue(self.run_sync(True)['documentos_desatualizados'])
        self.assertEqual(before,(self.root/'README.md').read_bytes())

    def test_preserva_texto_manual_e_fontes(self):
        before={p.relative_to(self.root):p.read_bytes() for p in self.root.rglob('*') if p.is_file() and p.name not in ['README.md','inventario.csv']}
        self.run_sync()
        text=m.read(self.root/'README.md')
        self.assertTrue(text.startswith('# Acervo\n\nIntrodução editorial preservada.'))
        self.assertTrue(text.endswith('## Histórico humano\nDecisão inalterada.\n'))
        self.assertEqual(before,{p:(self.root/p).read_bytes() for p in before})

    def test_mudanca_contratual_atualiza_estado_sem_promocao(self):
        self.run_sync()
        self.put('curadoria/protocolo_catalogacao_semantica.md','# Catalogação\n**Versão:** 0.2\n**Estado:** FUTURO — não implementado\n')
        self.run_sync();text=m.read(self.root/'README.md')
        self.assertIn('FUTURO — não implementado',text)
        self.assertIn('| 0.2 |',text)
        self.assertIn('não comprova implementação',text)
        self.put('curadoria/protocolo_novo.md','# Capacidade nova\n**Estado:** PROPOSTO\n')
        self.run_sync();self.assertIn('[Capacidade nova]',m.read(self.root/'README.md'))

    def test_atualiza_laudo_motor_sem_homologar_humano(self):
        self.put('videos/motor3/__main__.py','# código')
        self.put('videos/motor3/RELATORIO.md','# Laudo')
        self.put('videos/motor3/README.md','# Motor\n## Estado demonstrado\n\n| Capacidade | Resultado |\n|---|---|\n| Humano | Não demonstrado |\n\n## Outros\n')
        self.run_sync();text=m.read(self.root/'README.md')
        self.assertIn('| Humano | Não demonstrado |',text)
        self.assertIn('Finalização<br/>experimental: Motor<br/>3',text)
        self.assertIn('Áudio externo é uma entrada',text)

    def test_ambiguidades_preservam_independentes_e_historico(self):
        self.put('01_Teste/desconhecido.bin',b'x');self.put('01_Teste/historico.pdf',b'pdf')
        self.put('inventario.csv','modulo;arquivo\n01_Teste;historico.pdf\n01_Teste;nao-existe.png\n')
        result=self.run_sync()
        self.assertEqual(len(result['avisos']),2)
        self.assertIn(('01_Teste','historico.pdf'),self.rows())
        self.assertNotIn(('01_Teste','desconhecido.bin'),self.rows())
        self.assertIn(('01_Teste','original.png'),self.rows())
        self.assertIn(('01_Teste','nao-existe.png'),result['removidos'])

    def test_json_desconhecido_nao_e_confundido_com_mapa(self):
        self.put('01_Teste/dados.json','{"entrada": 1}')
        result=self.run_sync()
        self.assertTrue(any('dados.json' in x for x in result['avisos']))
        self.assertIn(('01_Teste','original.png'),self.rows())

    def test_symlinks_nao_redirecionam_inventario_ou_escrita(self):
        (self.root/'01_Teste/copia.png').symlink_to(self.root/'01_Teste/original.png')
        self.assertTrue(any('link simbólico' in x for x in self.run_sync()['avisos']))
        self.assertNotIn(('01_Teste','copia.png'),self.rows())
        p=self.root/'README.md';p.unlink();p.symlink_to(self.root/'01_Teste/exercicio.md')
        before=(self.root/'01_Teste/exercicio.md').read_bytes()
        with self.assertRaises(ValueError):self.run_sync()
        self.assertEqual(before,(self.root/'01_Teste/exercicio.md').read_bytes())

    def test_cabecalho_ilegivel_preserva_indexacao_independente(self):
        self.put('01_Teste/exercicio_extra.md',b'\xff\xfe')
        result=self.run_sync()
        self.assertTrue(any('cabeçalho textual' in x for x in result['avisos']))
        self.assertIn(('01_Teste','exercicio_extra.md'),self.rows())
        self.assertIn(('01_Teste','original.png'),self.rows())
        self.assertIn('[exercicio_extra.md]',m.read(self.root/'README.md'))

    def test_csv_duplicado_e_fora_de_ordem_reconciliado(self):
        self.put('inventario.csv','modulo;arquivo\n01_Teste;original.png\n01_Teste;gabarito_a.md\n01_Teste;original.png\n')
        self.run_sync();rows=m.inventory(self.root)
        self.assertEqual(rows,sorted(set(rows)))

    def test_csv_invalido_nao_escreve(self):
        self.put('inventario.csv','modulo;arquivo;extra\n')
        before=(self.root/'README.md').read_bytes()
        with self.assertRaises(ValueError):self.run_sync()
        self.assertEqual(before,(self.root/'README.md').read_bytes())

    def test_marcador_ausente_nao_escreve(self):
        p=self.root/'README.md';p.write_text(m.read(p).replace(m.END.format('catalogos'),''))
        before=(self.root/'inventario.csv').read_bytes()
        with self.assertRaises(ValueError):self.run_sync()
        self.assertEqual(before,(self.root/'inventario.csv').read_bytes())

    def test_historico_de_avaliacoes_nao_vira_norma(self):
        self.put('curadoria/avaliacoes/protocolo_historico.md','# Norma histórica de teste\n**Estado:** FUTURO\n')
        self.run_sync();text=m.read(self.root/'README.md')
        self.assertIn('[avaliações históricas](curadoria/avaliacoes/)',text)
        self.assertNotIn('[Norma histórica de teste]',text)
        self.assertIn('Não são protocolos vigentes',text)

    def test_labels_mermaid_sem_palavras_cortadas(self):
        label=m.wrapped('Consolidação de identidades e decisões')
        self.assertEqual(label.replace('<br/>',' '),'Consolidação de identidades e decisões')
        self.assertTrue(all(len(line)<=19 for line in label.split('<br/>')))
        self.run_sync();text=m.read(self.root/'README.md')
        self.assertIn('"htmlLabels": false',text)
        self.assertIn('click K "./curadoria/protocolo_catalogacao_semantica.md"',text)


if __name__=='__main__':unittest.main()
