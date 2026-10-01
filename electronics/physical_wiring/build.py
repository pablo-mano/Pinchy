"""Build the photo-based Pinchy wiring sheet from documented pin/net anchors.

Photographs remain unmodified; nested SVG viewports crop/rotate their presentation.
The drawing is a proposed interconnect, not an electrically validated assembly.
"""
from pathlib import Path
from html import escape
import base64, csv, io, json
from PIL import Image

HERE = Path(__file__).resolve().parent
OUT = HERE.parent
W, H = 2400, 1710
C = dict(gnd='#354656', v3='#c62839', bclk='#1269bc', ws='#09826f',
         mic='#804cb7', din='#c76313', power='#ac7510', spkp='#bb3571', spkn='#715e42')
INK, MUTED, BORDER = '#172b3a', '#546674', '#ccd6dd'
s = []
def put(x): s.append(x)
def text(x,y,t,size=23,color=INK,weight=400,anchor='start',extra=''):
    put(f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" font-weight="{weight}" text-anchor="{anchor}" {extra}>{escape(t)}</text>')
def lines(x,y,ts,size=22,color=MUTED,step=30):
    for i,t in enumerate(ts): text(x,y+i*step,t,size,color)
def rect(x,y,w,h,fill='white',stroke=BORDER,r=16,dash=''):
    put(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="2" stroke-dasharray="{dash}"/>')
def group(net): put(f'<g class="net" data-net="{net}"><title>{escape(NETS[net]["description"])}</title>')
def end(): put('</g>')
def line(points,col,width=5,dash=False,halo=True):
    pts=' '.join(f'{x:.1f},{y:.1f}' for x,y in points)
    if halo: put(f'<polyline points="{pts}" fill="none" stroke="white" stroke-width="{width+5}" stroke-linejoin="round" stroke-linecap="round"/>')
    put(f'<polyline points="{pts}" fill="none" stroke="{col}" stroke-width="{width}" stroke-linejoin="round" stroke-linecap="round"'+(' stroke-dasharray="12 9"' if dash else '')+'/>')
def dot(x,y,col,r=6):
    put(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{col}" stroke="white" stroke-width="2"/>')
def label(x,y,t,col):
    text(x,y,t,21,col,600,extra='paint-order="stroke" stroke="white" stroke-width="7" stroke-linejoin="round"')
def photo(name,x,y,w,h,crop=None,rotate=False):
    p=HERE/'assets'/name
    im=Image.open(p)
    # Convert unsupported WebP storage only; pixel geometry is retained.
    if p.suffix=='.webp':
        b=io.BytesIO(); im.save(b,format='PNG'); data=b.getvalue(); mime='image/png'
    else: data=p.read_bytes(); mime='image/jpeg'
    uri='data:'+mime+';base64,'+base64.b64encode(data).decode()
    iw,ih=im.size
    cx,cy,cw,ch=crop or (0,0,iw,ih)
    if rotate:
        put(f'<svg x="{x}" y="{y}" width="{w}" height="{h}" viewBox="0 0 {ch} {cw}"><g transform="translate(0 {cw}) rotate(-90)">')
        put(f'<svg width="{cw}" height="{ch}" viewBox="{cx} {cy} {cw} {ch}">')
    else: put(f'<svg x="{x}" y="{y}" width="{w}" height="{h}" viewBox="{cx} {cy} {cw} {ch}">')
    put(f'<image width="{iw}" height="{ih}" href="{uri}"/>')
    put('</svg>')
    if rotate: put('</g></svg>')

NETS = {
 'v3':dict(label='3V3 · mikrofon',description='J9.6 3V3 → mikrofon 3V. Zasilanie mikrofonu 3,3 V.',endpoints=['J9.6','MIC.3V']),
 'gnd':dict(label='GND · wspólna masa',description='J9.5 → MIC.GND; MIC.SEL → MIC.GND. J9.1 → AMP.GND. Masa BAT− jest wspólna przez płytkę.',endpoints=['J9.5','MIC.GND','MIC.SEL','J9.1','AMP.GND']),
 'bclk':dict(label='BCLK · GPIO19',description='J9.3 D−/GPIO19 → MIC.BCLK oraz AMP.BCLK. Kropka oznacza rozgałęzienie.',endpoints=['J9.3','MIC.BCLK','AMP.BCLK']),
 'ws':dict(label='WS / LRCLK · GPIO20',description='J9.4 D+/GPIO20 → MIC.LRCL oraz AMP.LRC. Jeden wspólny zegar ramki.',endpoints=['J9.4','MIC.LRCL','AMP.LRC']),
 'mic':dict(label='DOUT · GPIO44 + 100 kΩ',description='MIC.DOUT → J9.10 RXD/GPIO44. RPD1 100 kΩ łączy DOUT z GND, równolegle do linii danych.',endpoints=['MIC.DOUT','J9.10','RPD1.1']),
 'din':dict(label='DIN · GPIO43',description='J9.9 TXD/GPIO43 → AMP.DIN. Dane dźwięku z ESP32 do wzmacniacza.',endpoints=['J9.9','AMP.DIN']),
 'power':dict(label='Zasilanie · do weryfikacji',description='BAT+ → J1.1; BAT− → J1.2 po wymianie wtyku i dostosowaniu ładowania. Sieć VCC Waveshare → AMP.VCC dopiero po wskazaniu punktu na PCB i pomiarach.',endpoints=['BAT.+','J1.1','BAT.-','J1.2','WAVE.VCC_UNVERIFIED','AMP.VCC']),
 'spkp':dict(label='SPK+ · głośnik',description='AMP.SPK+ → czerwony przewód głośnika. Wyjście mostkowe, nie masa.',endpoints=['AMP.SPK+','SPK.+']),
 'spkn':dict(label='SPK− · głośnik',description='AMP.SPK− → czarny przewód głośnika. Nie łączyć z GND.',endpoints=['AMP.SPK-','SPK.-']),
}

put(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="title desc">')
put('<title id="title">Pinchy — rzeczywiste moduły, piny i połączenia</title><desc id="desc">Diagram fotograficzny dla Waveshare ESP32-S3-Touch-LCD-2.1B, SPH0645, DFRobot DFR0954, głośnika 8 omów 1 W i akumulatora Akyga AKY0107. Linie przerywane wymagają weryfikacji przed podłączeniem. Pełna tabela tekstowa znajduje się pod diagramem.</desc>')
put('<style>text{font-family:Arial,"DejaVu Sans",sans-serif}.net{transition:opacity .15s}.net.dim{opacity:.10}.net:hover{filter:drop-shadow(0 0 2px #708090)}</style>')
put(f'<rect width="{W}" height="{H}" fill="#f4f7fa"/>')
text(56,68,'PINCHY / rzeczywiste elementy i połączenia',42,weight=700)
text(58,112,'SPH0645  •  DFRobot DFR0954  •  Akyga LP503759 / 1350 mAh  •  projekt do testu na stole',24,MUTED)
text(2338,67,'01.10.2026 / v1',22,MUTED,anchor='end')

# Main hardware and the explicitly schematic expansion of its tiny connector.
rect(35,157,650,704)
text(62,200,'Waveshare ESP32-S3-Touch-LCD-2.1B',26,weight=700)
text(62,232,'Tył płytki; fotografia referencyjna wspólnej PCB 2.1/2.1B',19,MUTED)
photo('waveshare-rear.jpg',75,255,560,560,(140,140,520,520))
text(70,837,'Orientuj po BAT, USB i microSD — nie po kolorach wiązki.',19,MUTED)
def wp(x,y): return (75+(x-140)*560/520,255+(y-140)*560/520)
rect(724,213,280,596)
text(744,248,'J9 · SH1.0 · 12 pin',25,weight=700)
text(744,276,'Rozwinięcie numerów ze schematu',17,MUTED)
J={}
pin_defs={12:('GPIO0',None),11:('NC / GND*',None),10:('RXD / GPIO44','mic'),9:('TXD / GPIO43','din'),8:('SDA / GPIO15',None),7:('SCL / GPIO7',None),6:('3V3','v3'),5:('GND','gnd'),4:('D+ / GPIO20','ws'),3:('D− / GPIO19','bclk'),2:('VBUS / 5V',None),1:('GND','gnd')}
for i,pin in enumerate(range(12,0,-1)):
    y=310+41*i; J[pin]=(994,y)
    name,net=pin_defs[pin]
    col=C[net] if net else '#87949f'
    text(745,y+7,str(pin).zfill(2),21,col,600)
    text(789,y+7,name,20,col)
    dot(994,y,col,5)
    if net is None: line([(998,y),(1013,y)],col,2,halo=False)
line([wp(260,250),(668,325),(712,325)],MUTED,2,True,False)
text(70,904,'J1 · BAT',25,weight=700)
rect(64,925,414,152)
text(83,960,'Złącze akumulatora MX1.25 2-pin',23,weight=600)
text(84,1005,'1  BAT+',23,C['v3'],600);dot(464,998,C['v3'])
text(84,1048,'2  GND / BAT−',23,C['gnd'],600);dot(464,1042,C['gnd'])
line([wp(255,355),(52,485),(52,986),(64,986)],MUTED,2,True,False)
text(84,1097,'Numery pinów — nie widok strony wtyku.',19,MUTED)

# Microphone: actual sound-port face, pads in their real top-to-bottom order.
text(1560,195,'Adafruit SPH0645 · #3421',28,weight=700)
text(1560,225,'Strona z otworem akustycznym',21,MUTED)
photo('microphone-pins.jpg',1585,251,310,386,(88,180,285,355))
mic_x=1585+(155-88)*310/285
MIC={name:(mic_x,251+(y-180)*386/355) for name,y in [('SEL',230),('LRCL',280),('DOUT',331),('BCLK',382),('GND',432),('3V',483)]}
for name,(x,y) in MIC.items():
    net={'SEL':'gnd','LRCL':'ws','DOUT':'mic','BCLK':'bclk','GND':'gnd','3V':'v3'}[name]
    dot(x,y,C[net],5)

# DFR0954 manufacturer rendering, rotated to make the real pad labels upright.
text(1450,803,'DFRobot DFR0954 · MAX98357A',28,weight=700)
text(1450,833,'Wariant wzmacniacza z listy zakupowej',21,MUTED)
photo('dfr0954-pinout.webp',1450,867,370,409,(400,40,1110,1005),rotate=True)
scale=370/1005
def ap(x,y):return (1450+(y-40)*scale,867+(1510-x)*scale)
AMP={name:ap(x,118) for name,x in [('VCC',567),('GND',721),('LRC',875),('BCLK',1032),('DIN',1186),('SPK+',1340)]}
AMP['SPK-']=ap(1340,962)
for name,(x,y) in AMP.items():dot(x,y,C[{'VCC':'power','GND':'gnd','LRC':'ws','BCLK':'bclk','DIN':'din','SPK+':'spkp','SPK-':'spkn'}[name]],5)
text(1450,1315,'GAIN i SD: pozostaw niepodłączone. NC: nie używaj.',21,MUTED)
text(1450,1346,'Drugie VCC i GND to te same sieci — użyj jednej pary.',20,MUTED)

# Data paths. Clocks branch deliberately; crossings have a white bridge and no dot.
for net,mp,trunk,amp_name in [('ws','LRCL',1180,'LRC'),('bclk','BCLK',1128,'BCLK')]:
    jp=4 if net=='ws' else 3; start=J[jp]; target=MIC[mp]; out=AMP[amp_name]
    group(net)
    line([start,(trunk,start[1]),(trunk,target[1]),target],C[net])
    line([(trunk,start[1]),(trunk,out[1]),out],C[net])
    dot(trunk,start[1],C[net]);label(1200,out[1]-12,'WS / LRCLK' if net=='ws' else 'BCLK',C[net]);end()
group('v3');line([J[6],(1330,J[6][1]),(1330,MIC['3V'][1]),MIC['3V']],C['v3']);end()
group('mic');line([J[10],(1268,J[10][1]),(1268,MIC['DOUT'][1]),MIC['DOUT']],C['mic']);end()
group('din');line([J[9],(1080,J[9][1]),(1080,AMP['DIN'][1]),AMP['DIN']],C['din']);label(1200,AMP['DIN'][1]-12,'DIN',C['din']);end()
group('gnd')
line([J[5],(1380,J[5][1]),(1380,MIC['GND'][1]),MIC['GND']],C['gnd'])
line([J[1],(1038,J[1][1]),(1038,AMP['GND'][1]),AMP['GND']],C['gnd'])
line([MIC['SEL'],(1565,MIC['SEL'][1]),(1565,MIC['GND'][1]),MIC['GND']],C['gnd'],3)
dot(1565,MIC['GND'][1],C['gnd']);label(1200,AMP['GND'][1]-12,'GND',C['gnd']);end()

# The 100k pull-down is in parallel, never inserted in series with DOUT.
rx=1494; y1=MIC['DOUT'][1]; y2=MIC['GND'][1]
group('mic');line([(rx,y1),(rx,y1+24)],C['mic'],4);dot(rx,y1,C['mic'])
rect(rx-13,y1+24,26,y2-y1-47,'#ead7a9','#8f7548',8)
for off,col in [(31,'#744727'),(42,'#272424'),(53,'#efbb19')]:
    put(f'<rect x="{rx-13}" y="{y1+off}" width="26" height="6" fill="{col}"/>')
put(f'<rect x="{rx-13}" y="{y2-33}" width="26" height="5" fill="#ad9640"/>')
line([(rx,y2-23),(rx,y2)],C['gnd'],4);dot(rx,y2,C['gnd'])
text(1465,y1+28,'100 kΩ',22,C['mic'],600,anchor='end');end()
rect(1940,261,405,336)
text(1965,303,'RPD1 · 100 kΩ',27,C['mic'],700)
lines(1965,342,['DOUT ↔ GND','Dwie końcówki do dwóch sieci.','Rezystor nie przerywa DOUT.','Można dolutować przy padach','mikrofonu i zaizolować nóżki.'],22,step=34)
text(1965,552,'SEL ↔ GND: kanał lewy.',22,C['gnd'],600)
text(1585,675,'Nie zasłaniaj otworu „PORT”.',21,MUTED)

# Speaker terminal anchors correspond to its two supplied lead ends.
text(1940,803,'Głośnik · 8 Ω / 1 W',28,weight=700)
text(1940,833,'Kamami 560816 · przewody fabryczne',21,MUTED)
photo('speaker.jpg',2020,873,320,283,(215,230,365,323))
sp_neg=(2020+(233-215)*320/365,873+(248-230)*283/323)
sp_pos=(2020+(249-215)*320/365,873+(257-230)*283/323)
group('spkp');line([AMP['SPK+'],(1410,AMP['SPK+'][1]),(1410,858),(1987,858),(1987,sp_pos[1]),sp_pos],C['spkp'],4);label(1848,881,'SPK+',C['spkp']);end()
group('spkn');line([AMP['SPK-'],(1905,AMP['SPK-'][1]),(1905,sp_neg[1]),sp_neg],C['spkn'],4);label(1848,965,'SPK−',C['spkn']);end()
text(1940,1203,'SPK− nie jest masą.',25,C['spkp'],700)
text(1940,1238,'Żadnego przewodu głośnika do GND.',21,MUTED)
text(1940,1272,'Zacznij od małej głośności (1 W).',21,MUTED)

# Battery photo and the unverified power connections are visually distinct.
text(65,1136,'Twoja Akyga · LP503759 / 1350 mAh',27,weight=700)
photo('aky0107.jpg',68,1150,500,350,(0,140,800,560))
text(70,1517,'3,7 V · 1350 mAh · PCM · fabrycznie JST 2,54 mm',22,MUTED)
rect(661,1100,343,256,'#fffaf0','#d7ba75')
text(682,1138,'Po wymianie wtyku',25,C['power'],700)
text(682,1177,'MX1.25 2-pin do J1',23,C['power'])
text(682,1220,'BAT+ → J1.1',23,C['v3'],600)
text(682,1264,'BAT− → J1.2',23,C['gnd'],600)
text(682,1312,'Polaryzację sprawdź miernikiem.',19,MUTED)
group('power')
line([(661,1212),(640,1212),(640,998),(464,998)],C['v3'],4,True)
line([(661,1256),(620,1256),(620,1042),(464,1042)],C['gnd'],4,True)
end()
line([(530,1445),(640,1445),(640,1333),(661,1333)],MUTED,2,True,False)
text(658,1400,'Fabryczny JST 2,54 mm',20,MUTED)
text(658,1428,'do wymiany na MX1.25.',20,MUTED)
rect(724,856,280,212,'#fffaf0','#d7ba75')
text(744,893,'VCC Waveshare',25,C['power'],700)
lines(744,929,['Sieć przy U5 VIN / C14.','Punkt lutowania na PCB','jeszcze do identyfikacji.','To nie pin 3V3.'],20,step=29)
group('power');line([(994,1043),(1005,1043),(1005,AMP['VCC'][1]),AMP['VCC']],C['power'],5,True)
label(1100,AMP['VCC'][1]+35,'AMP.VCC · 3,3–5 V',C['power']);end()

# Concise material limitations, kept part of the exported sheet.
rect(1050,1390,1295,206,'#fff7e8','#d7ba75')
text(1075,1430,'Linie przerywane: sprawdzić przed podłączeniem',26,C['power'],700)
lines(1075,1470,['Akumulator: maks. ładowanie 1,35 A; standardowo 270 mA, szybko 675 mA.',
                'Schemat Waveshare: R7 = 82 kΩ → nastawa ok. 2 A. Wymaga dostosowania i pomiaru.',
                'Wzmacniacz: potwierdź VCC, zakres 3,3–5 V i wydajność zasilania, także przy baterii.'],22,step=34)
rect(42,1552,962,112,'#edf3f7','#ccd6dd')
text(64,1585,'Tryb audio: USB–UART odłączony.',23,weight=700)
lines(64,1617,['GPIO19/20 zajmuje I²S. Zasilanie przez native USB tylko z D+ i D−',
               'oddzielnie odizolowanymi. Firmware musi zwolnić GPIO43/44 i USB.'],20,step=28)
text(1075,1640,'● połączenie / odgałęzienie     Skrzyżowanie bez kropki nie łączy przewodów.',21,MUTED)
text(60,1690,'* J9.11: dokumentacja tekstowa NC, starszy schemat GND — pozostaw niepodłączony. Rozwinięcie J9 nie przedstawia strony wtyczki.',18,MUTED)
put('</svg>')
svg='\n'.join(s)
svg_path=OUT/'03_physical_connections.svg';svg_path.write_text(svg)

rows=[('3V3','J9.6 / 3V3','MIC 3V','3,3 V'),('GND','J9.5 / GND','MIC GND','Wspólna masa'),('SEL','MIC SEL','MIC GND','Kanał lewy'),('BCLK','J9.3 / D− / GPIO19','MIC BCLK + AMP BCLK','Rozgałęzienie'),('WS','J9.4 / D+ / GPIO20','MIC LRCL + AMP LRC','Rozgałęzienie'),('MIC DATA','MIC DOUT','J9.10 / RXD / GPIO44','Dane z mikrofonu'),('RPD1','MIC DOUT','100 kΩ → GND','Dodatkowy rezystor; połączenie równoległe'),('AMP DATA','J9.9 / TXD / GPIO43','AMP DIN','Dane do wzmacniacza'),('AMP GND','J9.1 / GND','AMP GND','Powrót zasilania wzmacniacza'),('AMP VCC','Waveshare VCC / U5 VIN / C14','AMP VCC','Warunkowe: punkt fizyczny i zakres 3,3–5 V do sprawdzenia'),('SPK+','AMP SPK+','Czerwony przewód głośnika','8 Ω / 1 W'),('SPK−','AMP SPK−','Czarny przewód głośnika','Nie łączyć z GND'),('BAT+','Akyga BAT+','J1.1 BAT','Warunkowe: wtyk i ładowanie do dostosowania'),('BAT−','Akyga BAT−','J1.2 GND','Potwierdź polaryzację miernikiem')]
with (OUT/'03_physical_connections.csv').open('w') as f:
    writer=csv.writer(f, lineterminator="\n");writer.writerow(['signal','from','to','note']);writer.writerows(rows)
manifest={'date':'2026-10-01','status':'proposed_unmeasured','battery_confirmed_by_user':'Akyga AKY0107 LP503759 3.7V 1350mAh','amplifier_assumption':'DFRobot DFR0954, procurement-list variant; not separately confirmed by user','microphone':'Adafruit SPH0645 #3421','nets':NETS,'j9':{str(p):n for p,(n,_) in pin_defs.items()},'mic_photo_anchors':MIC,'amp_photo_anchors':AMP,'limitations':['VCC solder point has not been identified on physical PCB.','Battery charge current must be adapted and measured before USB charging.','Diagram requires bench validation of I2S/UART mux and GPIO assignment.','J9 pin numbers are logical, not connector face or wire-colour instructions.']}
(HERE/'connections.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
options='<option value="all">Wszystkie połączenia</option>'+''.join(f'<option value="{k}">{escape(v["label"])}</option>' for k,v in NETS.items())
table=''.join('<tr>'+''.join('<td>'+escape(v)+'</td>' for v in row)+'</tr>' for row in rows)
html='''<!doctype html><html lang="pl"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Pinchy — elementy i połączenia</title>
<style>*{box-sizing:border-box}body{margin:0;background:#e9eef3;color:#172b3a;font:16px/1.5 system-ui,sans-serif}header{position:sticky;top:0;z-index:5;background:#fff;padding:15px 24px;border-bottom:1px solid #cbd6df}h1{font-size:20px;margin:0 24px 0 0;display:inline-block}nav{display:flex;align-items:center;gap:12px;flex-wrap:wrap}select,button,a.download{font:inherit;border:1px solid #b4c3cd;border-radius:7px;background:white;color:#172b3a;padding:7px 12px;text-decoration:none}button{cursor:pointer}#description{margin:9px 0 0;color:#465b6a;min-height:24px}#viewport{overflow:auto;padding:18px}#drawing{width:100%;min-width:980px;margin:auto;background:white;box-shadow:0 8px 32px #233e5014}#drawing svg{width:100%;height:auto;display:block}section{max-width:1400px;margin:28px auto;padding:24px;background:#fff;border-radius:12px}h2{font-size:22px;margin-top:0}table{border-collapse:collapse;width:100%}th,td{padding:10px 12px;text-align:left;border-bottom:1px solid #e0e7ec}th{background:#f1f5f8}a{color:#1269bc}.sources li{margin:8px 0}.note{color:#73501c;background:#fff6e7;padding:14px 18px;border-radius:8px}svg .net{cursor:pointer}@media print{header,section{display:none}#viewport{padding:0;overflow:visible}#drawing{min-width:0;width:100%!important;box-shadow:none}@page{size:A3 landscape;margin:6mm}}</style>
<header><nav><h1>Pinchy · diagram połączeń</h1><label>Podświetl: <select id="net">OPTIONS</select></label><button id="fit">Dopasuj</button><button id="zoom">Powiększ 150%</button><a class="download" href="03_physical_connections.pdf">PDF do druku</a><a class="download" href="03_physical_connections.svg" download>SVG</a></nav><p id="description">Wybierz sygnał, aby prześledzić przewód i jego rozgałęzienia. Kliknięcie przewodu także go podświetla.</p></header>
<main><div id="viewport"><div id="drawing">DIAGRAM</div></div><section><h2>Połączenia pin po pinie</h2><p class="note">Bateria potwierdzona przez użytkownika: Akyga AKY0107 / LP503759. Wzmacniacz przyjęty z listy zakupowej: DFRobot DFR0954. Diagram przedstawia połączenia do sprawdzenia na stole; nie jest potwierdzeniem działania prototypu. Fotografie pokazują orientację modułów, a rozwinięcia J9 i J1 pokazują numery funkcjonalne ze schematu. Przewody wtyków trzeba zidentyfikować miernikiem.</p><table><thead><tr><th>Sygnał</th><th>Od</th><th>Do</th><th>Uwagi</th></tr></thead><tbody>ROWS</tbody></table></section><section class="sources"><h2>Źródła i orientacja części</h2><ul><li><a href="https://docs.waveshare.com/ESP32-S3-Touch-LCD-2.1">Waveshare — wspólna dokumentacja 2.1 i 2.1B</a>, <a href="https://files.waveshare.com/wiki/ESP32-S3-Touch-LCD-2.1/ESP32-S3-Touch-LCD-2.1_schematic_diagram.pdf">schemat J9, J1 i zasilania</a>. Zdjęcie tylnej PCB pochodzi z karty 2.1; producent publikuje wspólny schemat elektryczny. Przed lutowaniem sprawdź rewizję swojej płytki.</li><li><a href="https://learn.adafruit.com/adafruit-i2s-mems-microphone-breakout/pinouts">Adafruit #3421 — pinout</a>, <a href="https://cdn-shop.adafruit.com/product-files/3421/i2S%20Datasheet.PDF#page=7">Knowles — rezystor 100 kΩ na DATA</a>. Fotografia mikrofonu pokazuje stronę z otworem i opisami pinów.</li><li><a href="https://wiki.dfrobot.com/dfr0954/">DFRobot DFR0954 — wygląd PCB, piny i zasilanie 3,3–5 V</a>. Widok producenta obrócony o 90°; nie odbity lustrzanie. VCC z Waveshare wymaga pomiaru także przy rozładowanej baterii; nie zatwierdzono pracy w całym zakresie baterii.</li><li><a href="https://www.tme.eu/Document/d09d785c980e096e8a2305b0492fc05e/AKY0107.pdf">Karta Akyga AKY0107</a>: 1C = 1,35 A maksymalnego prądu ładowania i rozładowania. Ładowanie standardowe 0,2C; szybkie 0,5C. To nie są pomiary prądu Waveshare.</li><li><a href="https://kamami.pl/akumulatory/1202750-akumulator-litowo-polimerowy-akyga-aky0107-lp503759-li-po-3-7v-1350mah-pcm-jst-2-54-2-pin-150mm-5906574243544.html">Kamami — zdjęcie Akygi</a>, <a href="https://kamami.pl/glosniki/560816-glosnik-z-przewodami-8-1w-5906623455089.html">Kamami — zdjęcie głośnika 560816</a>.</li></ul><p>Kolory linii służą do śledzenia sygnałów, nie opisują fabrycznych kolorów przewodów J9. Zdjęcia i render modułu należą do producentów / sprzedawcy; diagram nie zmienia ich licencji. Elementy nie są narysowane w jednej skali.</p></section></main>
<script>const nets=NETJSON;const chooser=document.getElementById('net');const desc=document.getElementById('description');function show(k){chooser.value=k;document.querySelectorAll('svg .net').forEach(g=>g.classList.toggle('dim',k!=='all'&&g.dataset.net!==k));desc.textContent=k==='all'?'Wybierz sygnał, aby prześledzić przewód i jego rozgałęzienia. Kliknięcie przewodu także go podświetla.':nets[k].description}chooser.addEventListener('change',()=>show(chooser.value));document.querySelectorAll('svg .net').forEach(g=>g.addEventListener('click',()=>show(g.dataset.net)));document.getElementById('fit').onclick=()=>document.getElementById('drawing').style.width='100%';document.getElementById('zoom').onclick=()=>document.getElementById('drawing').style.width='150%';</script></html>'''
html=html.replace('OPTIONS',options).replace('DIAGRAM',svg).replace('ROWS',table).replace('NETJSON',json.dumps(NETS,ensure_ascii=False))
(OUT/'03_physical_connections.html').write_text(html)
print('Built SVG, HTML, CSV and connection manifest.')
