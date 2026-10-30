"""Produção local de referência. Requer Pillow, espeakng-loader e ffmpeg/ffprobe.
Executar na raiz: python videos/V04-004/renderizar.py
Binários e intermediários ficam fora do checkout. Não realiza upload.
"""
from pathlib import Path
import ctypes as ct
import hashlib,json,math,re,subprocess,wave
from PIL import Image
import espeakng_loader
ROOT=Path(__file__).resolve().parents[2]
WORK=Path('/workspace/artifacts/V04-004');WORK.mkdir(parents=True,exist_ok=True)
PROJECT=ROOT/'videos/V04-004';FPS=30;SR=22050


EXPECTED_SOURCES = {'editorial/dossies/04_Dossie_Editorial.docx': '3212b59adc0228c3b68632c40cbbd67e025bb832f75aa16cbb3172d433dc336e', 'editorial/roteiros/04-004_Roteiro_Individual.docx': 'a939a9390a023fad2d8e396518b97d62de29eaa341eda409586d42b823bb2958', '04_Argumentos_CommandLine/04_Mapa_Espacial.json': 'eb35a6f8b57571729e43f1a42adaddb4ded82e4796bc418e91a5e64765f2b7a7'}

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def run(args): subprocess.run(args,check=True,stdout=subprocess.DEVNULL)
def project(im,b):
 crop=im.crop(b).convert('RGB');scale=min(1080/crop.width,1920/crop.height);size=(round(crop.width*scale),round(crop.height*scale));out=Image.new('RGB',(1080,1920),(15,20,30));out.paste(crop.resize(size,Image.Resampling.LANCZOS),((1080-size[0])//2,(1920-size[1])//2));return out

def writewav(path,data):
 with wave.open(str(path),'wb') as w:w.setnchannels(1);w.setsampwidth(2);w.setframerate(SR);w.writeframes(data)
def stamp(sec):
 n=round(sec*1000);return f'{n//3600000:02d}:{n//60000%60:02d}:{n//1000%60:02d},{n%1000:03d}'
def main():
 for path,expected in EXPECTED_SOURCES.items():
  assert sha(ROOT/path)==expected, 'Fonte alterada: '+path
 lib=espeakng_loader.load_library();lib.espeak_Initialize.argtypes=[ct.c_int,ct.c_int,ct.c_char_p,ct.c_int];lib.espeak_Initialize.restype=ct.c_int
 assert lib.espeak_Initialize(2,0,espeakng_loader.get_data_path().encode(),0)==SR
 lib.espeak_SetVoiceByName.argtypes=[ct.c_char_p];assert lib.espeak_SetVoiceByName(b'pt-br')==0
 lib.espeak_SetParameter(1,155,0)
 chunks=[]
 @ct.CFUNCTYPE(ct.c_int,ct.POINTER(ct.c_short),ct.c_int,ct.c_void_p)
 def callback(data,n,events):
  if n>0: chunks.append(ct.string_at(data,n*2))
  return 0
 lib.espeak_SetSynthCallback(callback)
 lib.espeak_Synth.argtypes=[ct.c_void_p,ct.c_size_t,ct.c_uint,ct.c_int,ct.c_uint,ct.c_uint,ct.POINTER(ct.c_uint),ct.c_void_p]
 mapa=json.loads((ROOT/'04_Argumentos_CommandLine/04_Mapa_Espacial.json').read_text())
 chosen=[('argopt3.png','tres_fontes'),('env4.png','fluxo_precedencia'),('env4.png','exemplos_fontes'),('resumo2.png','estrutura'),('env4.png','fluxo_precedencia')]
 segments=json.loads((PROJECT/'falas.json').read_text());timeline=[];allpcm=b'';cues=[];offset=0;totalframes=0
 for seg,(fname,rid) in zip(segments,chosen):
  mat=next(m for m in mapa['materiais'] if m['arquivo']==fname);region=next(r for r in mat['regioes'] if r['id']==rid)
  src=ROOT/'04_Argumentos_CommandLine'/fname;assert sha(src)==mat['sha256'];im=project(Image.open(src),region['bbox_px']);frame=WORK/(seg['id']+'.png');im.save(frame)
  pcm=b'\0\0'*round(.18*SR);utterances=re.split(r'(?<=[.;:])\s+',seg['texto'])
  for utterance in utterances:
   chunks.clear();text=utterance.encode('utf-8')+b'\0';buf=ct.create_string_buffer(text);uid=ct.c_uint()
   assert lib.espeak_Synth(buf,len(text),0,1,0,1,ct.byref(uid),None)==0
   lib.espeak_Synchronize();audio=b''.join(chunks);assert len(audio)>SR
   start=offset+len(pcm)/(2*SR);pcm+=audio;end=offset+len(pcm)/(2*SR);cues.append((start,end,utterance));pcm+=b'\0\0'*round(.10*SR)
  frames=math.ceil((len(pcm)/(2*SR)+.35)*FPS);target=frames*SR//FPS;pcm+=b'\0\0'*(target-len(pcm)//2);assert len(pcm)//2==target
  # SR/FPS=735 exactly; every cut is aligned to both PCM samples and video frames.
  wav=WORK/(seg['id']+'_Referencia.wav');writewav(wav,pcm);allpcm+=pcm
  clip=WORK/(seg['id']+'.mp4');run(['ffmpeg','-y','-loglevel','error','-loop','1','-framerate',str(FPS),'-i',str(frame),'-frames:v',str(frames),'-c:v','libx264','-preset','fast','-crf','18','-pix_fmt','yuv420p','-threads','2',str(clip)])
  timeline.append({**seg,'arquivo':'04_Argumentos_CommandLine/'+fname,'regiao_id':rid,'bbox_px':region['bbox_px'],'modo_visual':'IMAGEM_ESTATICA','transicao':'CORTE_SECO','inicio_s':offset,'duracao_s':frames/FPS,'frame_inicial':totalframes,'quadros':frames,'fonte_sha256':sha(src)})
  offset+=frames/FPS;totalframes+=frames
 audio=WORK/'V04-004_Audio_Referencia.wav';writewav(audio,allpcm)
 concat=WORK/'clips.txt';concat.write_text(''.join("file '"+str(WORK/(s['id']+'.mp4'))+"'\n" for s in timeline))
 run(['ffmpeg','-y','-loglevel','error','-f','concat','-safe','0','-i',str(concat),'-i',str(audio),'-map','0:v:0','-map','1:a:0','-c:v','copy','-c:a','aac','-b:a','128k','-movflags','+faststart',str(WORK/'V04-004.mp4')])
 (PROJECT/'V04-004.srt').write_text('\n\n'.join(f'{i}\n{stamp(a)} --> {stamp(b)}\n{txt}' for i,(a,b,txt) in enumerate(cues,1))+'\n',encoding='utf-8')
 sources={str(p.relative_to(ROOT)):sha(p) for p in [ROOT/'editorial/dossies/04_Dossie_Editorial.docx',ROOT/'editorial/roteiros/04-004_Roteiro_Individual.docx',ROOT/'04_Argumentos_CommandLine/04_Mapa_Espacial.json']}
 plan={'schema_version':'1.0','video_id':'V04-004','estado':'PROPOSTO','execucao':'EXPERIMENTAL_AUTORIZADA; escolha única excepcional após salvar dossiê; sem homologação humana','tipo_entrega':'REFERENCIA','audio':'eSpeak NG pt-br, 155 palavras/minuto; sintético local, não definitivo','legendas':'PROVISORIO; intervalos medidos por amostras PCM de cada enunciado sintetizado, não estimados por palavras','perfil':{'largura':1080,'altura':1920,'fps':FPS,'fundo_rgb':[15,20,30],'escala':'conter, proporção preservada'},'fontes_sha256':sources,'segmentos':timeline,'duracao_s':offset,'ajustes_montagem':['C05 repete env4.png/fluxo_precedencia, fonte já presente no candidato, em vez do painel de resumo2.png que mostra a ordem inversa de atribuição. Seleção visual autorizada; falas e sequência inalteradas.','Tempos substituídos pela duração medida da síntese, com pausas e alinhamento a quadros.'],'pendencias':['Escuta contínua e revisão editorial humana; SRT de referência provisório.']}
 (ROOT/'editorial/montagens/04-004_Montagem.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps({'duracao_s':offset,'quadros':totalframes,'cues':len(cues),'mp4':str(WORK/'V04-004.mp4')}))
if __name__=='__main__':main()
