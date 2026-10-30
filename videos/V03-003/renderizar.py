"""Reproduz V03-003 com o WAV de referência existente, sem nova síntese.
Uso: python videos/V03-003/renderizar.py --audio /workspace/artifacts/V03-003/V03-003_Audio_Referencia.wav --saida /workspace/artifacts/V03-003/V03-003.mp4
Dependências: Python, Pillow e FFmpeg. Não modifica mapa, imagens ou roteiro.
"""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile
from PIL import Image


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def project(image, normalized_box):
    width, height = image.size
    box = tuple(round(v*d) for v,d in zip(normalized_box,(width,height,width,height)))
    crop = image.crop(box).convert('RGB')
    factor = min(1080/crop.width,1920/crop.height)
    size = (round(crop.width*factor),round(crop.height*factor))
    output = Image.new('RGB',(1080,1920),(22,22,22))
    output.paste(crop.resize(size,Image.Resampling.LANCZOS),((1080-size[0])//2,(1920-size[1])//2))
    return output


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--audio',type=Path,required=True)
    parser.add_argument('--saida',type=Path,required=True)
    args = parser.parse_args()
    if args.saida.exists():
        parser.error('Saída já existe; preservar o MP4 ou escolher outro destino.')
    root = Path(__file__).resolve().parents[2]
    plan = json.loads((root/'editorial/montagens/03-003_Montagem.json').read_text())
    if sha(args.audio) != plan['audio']['sha256']:
        raise ValueError('WAV diferente da referência medida; não reutilizar sincronismo.')
    for source in [plan['fontes']['roteiro'],plan['fontes']['mapa'],plan['fontes']['autoauditoria'],*plan['fontes']['originais']]:
        if sha(root/source['caminho']) != source['sha256']:
            raise ValueError('Fonte alterada: '+source['caminho'])
    spatial = json.loads((root/plan['fontes']['mapa']['caminho']).read_text())
    with tempfile.TemporaryDirectory(prefix='v03003-render-') as tmp:
        tmp = Path(tmp)
        concat = []
        last = None
        for take in plan['segmentos']:
            for shot in take['projecoes']:
                source = root/shot['arquivo']
                material = next(m for m in spatial['materiais'] if m['arquivo']==source.name)
                region = next(r for r in material['regioes'] if r['id']==shot['regiao_id'])
                if sha(source)!=material['sha256']:
                    raise ValueError('Original não corresponde ao mapa.')
                if region['bbox_normalizada']!=shot['bbox_normalizada']:
                    raise ValueError('Geometria do plano difere do mapa.')
                with Image.open(source) as image:
                    last = tmp/(shot['id']+'.png')
                    project(image,region['bbox_normalizada']).save(last,compress_level=1)
                concat.extend(["file '"+str(last)+"'",'duration '+str(shot['duracao_ms_medida']/1000)])
        if last is None:
            raise ValueError('Plano sem projeções.')
        concat.append("file '"+str(last)+"'")
        listing = tmp/'quadros.ffconcat'
        listing.write_text('\n'.join(concat)+'\n')
        args.saida.parent.mkdir(parents=True,exist_ok=True)
        subprocess.run(['ffmpeg','-hide_banner','-n','-f','concat','-safe','0','-i',str(listing),
                        '-i',str(args.audio),'-vf','fps=30,format=yuv420p','-c:v','libx264',
                        '-preset','fast','-tune','stillimage','-crf','20','-threads','2',
                        '-c:a','aac','-b:a','128k','-t',str(plan['duracao_total_ms_medida']/1000),
                        '-shortest','-movflags','+faststart',str(args.saida)],check=True)


if __name__=='__main__':
    main()
