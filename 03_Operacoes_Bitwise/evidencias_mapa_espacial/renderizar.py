#!/usr/bin/env python3
"""Reproduz projeções e painéis do JSON; não modifica as fontes nem o mapa."""
from pathlib import Path
import argparse,json,hashlib,math
from PIL import Image,ImageDraw,ImageFont

def project(im,box):
    w,h=im.size
    bbox=tuple(round(v*s) for v,s in zip(box,(w,h,w,h)))
    crop=im.crop(bbox).convert('RGB')
    factor=min(1080/crop.width,1920/crop.height)
    size=(min(1080,round(crop.width*factor)),min(1920,round(crop.height*factor)))
    result=Image.new('RGB',(1080,1920),(22,22,22))
    result.paste(crop.resize(size,Image.Resampling.LANCZOS),((1080-size[0])//2,(1920-size[1])//2))
    return result,bbox

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--mapa',type=Path,default=Path(__file__).resolve().parents[1]/'03_Mapa_Espacial.json');ap.add_argument('--saida',type=Path,default=Path(__file__).resolve().parent);args=ap.parse_args()
    m=json.loads(args.mapa.read_text());base=Path(__file__).resolve().parents[1];out=args.saida;out.mkdir(parents=True,exist_ok=True)
    font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',15)
    index=[];panels=[]
    for material in m['materiais']:
        path=base/material['arquivo'];assert hashlib.sha256(path.read_bytes()).hexdigest()==material['sha256'],path
        src=Image.open(path);assert list(src.size)==material['dimensoes_px']
        entries=[]
        # Todas as regiões em todos os quadros: inclusive estados que não aparecem na montagem de um vídeo.
        for frame in range(getattr(src,'n_frames',1)):
            src.seek(frame);im=src.convert('RGB')
            for region in material['regioes']:
                result,bbox=project(im,region['bbox_normalizada'])
                name=f"{path.stem}_{material['tipo']}__{region['id']}__f{frame:02}.png"
                result.save(out/name,optimize=True)
                entry={'arquivo':material['arquivo'],'regiao':region['id'],'quadro':frame,'bbox_px':bbox,'projecao':name,'sha256':hashlib.sha256((out/name).read_bytes()).hexdigest()}
                entries.append(entry);index.append(entry)
        for start in range(0,len(entries),4):
            block=entries[start:start+4];sheet=Image.new('RGB',(1080,2040),'#d0d6df');draw=ImageDraw.Draw(sheet)
            for j,entry in enumerate(block):
                x=j%2*540;y=j//2*1020
                draw.text((x+8,y+3),material['arquivo'],fill='black',font=font)
                draw.text((x+8,y+24),entry['regiao']+' | f'+str(entry['quadro']),fill='black',font=font)
                with Image.open(out/entry['projecao']) as im:sheet.paste(im.resize((540,960),Image.Resampling.LANCZOS),(x,y+55))
            name=f"painel_{path.stem}_{start//4+1:02}.jpg";sheet.save(out/name,quality=90)
            panels.append({'arquivo':material['arquivo'],'painel':name,'projecoes':[e['projecao'] for e in block]})
    (out/'indice_projecoes.json').write_text(json.dumps({'algoritmo':'round(normalizado*dimensão), bbox exclusiva, RGB, Lanczos, fit integral 1080x1920, fundo RGB(22,22,22)','projecoes':index,'paineis':panels},ensure_ascii=False,indent=2)+'\n')
    print('Projeções:',len(index),'Painéis:',len(panels))
if __name__=='__main__':main()
