"""Reproduz os painéis a partir do mapa final e dos originais, sem alterar o mapa."""
from pathlib import Path
import hashlib,json
from PIL import Image,ImageDraw,ImageFont
ROOT=Path(__file__).resolve().parents[2]
CHAPTER=ROOT/'04_Argumentos_CommandLine'
DEST=Path(__file__).resolve().parent

def project(im,b):
 c=im.crop(b).convert('RGB');s=min(1080/c.width,1920/c.height);sz=(round(c.width*s),round(c.height*s));o=Image.new('RGB',(1080,1920),(15,20,30));o.paste(c.resize(sz,Image.Resampling.LANCZOS),((1080-sz[0])//2,(1920-sz[1])//2));return o

def main():
 m=json.loads((CHAPTER/'04_Mapa_Espacial.json').read_text());tiles=[]
 for mat in m['materiais']:
  source=CHAPTER/mat['arquivo'];assert hashlib.sha256(source.read_bytes()).hexdigest()==mat['sha256']
  im=Image.open(source);im.seek(im.n_frames-1 if im.format=='GIF' else 0)
  for region in mat['regioes']:
   # Same JPEG stage as the inspected projections.
   import io
   buf=io.BytesIO();project(im,region['bbox_px']).save(buf,format='JPEG',quality=88);buf.seek(0)
   tiles.append((Image.open(buf).copy(),mat['arquivo']+' / '+region['id']))
 font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',14)
 for i in range(0,len(tiles),8):
  panel=Image.new('RGB',(2160,1980),'#ddd');d=ImageDraw.Draw(panel)
  for j,(im,label) in enumerate(tiles[i:i+8]):
   x=j%4*540;y=j//4*990;panel.paste(im.resize((540,960)),(x,y));d.text((x+3,y+963),label,fill='black',font=font)
  panel.save(DEST/f'painel-{i//8+1:02d}.jpg',quality=86)
if __name__=='__main__':main()
