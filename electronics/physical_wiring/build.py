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
 'v3':dict(label='3V3 · microphone',description='J9.6 3V3 → MIC 3V. Microphone supply: 3.3 V.',endpoints=['J9.6','MIC.3V']),
 'gnd':dict(label='GND · common ground',description='J9.5 → MIC.GND; MIC.SEL → MIC.GND. J9.1 → AMP.GND. BAT− shares ground through the board.',endpoints=['J9.5','MIC.GND','MIC.SEL','J9.1','AMP.GND']),
 'bclk':dict(label='BCLK · GPIO19',description='J9.3 D−/GPIO19 → MIC.BCLK and AMP.BCLK. A dot marks the shared clock branch.',endpoints=['J9.3','MIC.BCLK','AMP.BCLK']),
 'ws':dict(label='WS / LRCLK · GPIO20',description='J9.4 D+/GPIO20 → MIC.LRCL and AMP.LRC. Both modules share the word clock.',endpoints=['J9.4','MIC.LRCL','AMP.LRC']),
 'mic':dict(label='DOUT · GPIO44 + 100 kΩ',description='MIC.DOUT → J9.10 RXD/GPIO44. RPD1 is a 100 kΩ pull-down between DOUT and GND, not a series resistor.',endpoints=['MIC.DOUT','J9.10','RPD1.1']),
 'din':dict(label='DIN · GPIO43',description='J9.9 TXD/GPIO43 → AMP.DIN. Audio data travels from the ESP32 to the amplifier.',endpoints=['J9.9','AMP.DIN']),
 'power':dict(label='Power · verify first',description='BAT+ → J1.1; BAT− → J1.2 after replacing the connector and adjusting charging. Connect Waveshare VCC to AMP.VCC only after locating and measuring the supply point.',endpoints=['BAT.+','J1.1','BAT.-','J1.2','WAVE.VCC_UNVERIFIED','AMP.VCC']),
 'spkp':dict(label='SPK+ · speaker',description='AMP.SPK+ → the red speaker lead. This is a bridge output, not ground.',endpoints=['AMP.SPK+','SPK.+']),
 'spkn':dict(label='SPK− · speaker',description='AMP.SPK− → the black speaker lead. Do not connect it to GND.',endpoints=['AMP.SPK-','SPK.-']),
}

put(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="title desc">')
put('<title id="title">Pinchy — physical modules, pins and connections</title><desc id="desc">Photo wiring diagram for Waveshare ESP32-S3-Touch-LCD-2.1B, SPH0645, DFRobot DFR0954, an 8 ohm 1 W speaker and Akyga AKY0107 battery. Dashed power connections require verification. A text connection table follows the drawing.</desc>')
put('<style>text{font-family:Arial,"DejaVu Sans",sans-serif}.net{transition:opacity .15s}.net.dim{opacity:.10}.net:hover{filter:drop-shadow(0 0 2px #708090)}</style>')
put(f'<rect width="{W}" height="{H}" fill="#f4f7fa"/>')
text(56,68,'PINCHY / physical parts and connections',42,weight=700)
text(58,112,'SPH0645  •  DFRobot DFR0954  •  Akyga LP503759 / 1350 mAh  •  bench-test proposal',24,MUTED)
text(2338,67,'01 OCT 2026 / v2',22,MUTED,anchor='end')

# Main hardware and the explicitly schematic expansion of its tiny connector.
rect(35,157,650,704)
text(62,200,'Waveshare ESP32-S3-Touch-LCD-2.1B',26,weight=700)
text(62,232,'Rear PCB; reference photo for the shared 2.1/2.1B design',19,MUTED)
photo('waveshare-rear.jpg',75,255,560,560,(140,140,520,520))
text(70,837,'Orient by BAT, USB and microSD; verify harness polarity.',19,MUTED)
def wp(x,y): return (75+(x-140)*560/520,255+(y-140)*560/520)
rect(724,213,280,596)
text(744,248,'J9 · SH1.0 · 12 pin',25,weight=700)
text(744,276,'Pin numbers from the schematic',17,MUTED)
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
text(83,960,'MX1.25 2-pin battery connector',23,weight=600)
text(84,1005,'1  BAT+',23,C['v3'],600);dot(464,998,C['v3'])
text(84,1048,'2  GND / BAT−',23,C['gnd'],600);dot(464,1042,C['gnd'])
line([wp(255,355),(52,485),(52,986),(64,986)],MUTED,2,True,False)
text(84,1097,'Pin numbers, not a connector-face view.',19,MUTED)

# Microphone: actual sound-port face, pads in their real top-to-bottom order.
text(1560,195,'Adafruit SPH0645 · #3421',28,weight=700)
text(1560,225,'Sound-port side of the microphone',21,MUTED)
photo('microphone-pins.jpg',1585,251,310,386,(88,180,285,355))
mic_x=1585+(155-88)*310/285
MIC={name:(mic_x,251+(y-180)*386/355) for name,y in [('SEL',230),('LRCL',280),('DOUT',331),('BCLK',382),('GND',432),('3V',483)]}
for name,(x,y) in MIC.items():
    net={'SEL':'gnd','LRCL':'ws','DOUT':'mic','BCLK':'bclk','GND':'gnd','3V':'v3'}[name]
    dot(x,y,C[net],5)

# DFR0954 manufacturer rendering, rotated to make the real pad labels upright.
text(1450,803,'DFRobot DFR0954 · MAX98357A',28,weight=700)
text(1450,833,'Amplifier variant from the shopping list',21,MUTED)
photo('dfr0954-pinout.webp',1450,867,370,409,(400,40,1110,1005),rotate=True)
scale=370/1005
def ap(x,y):return (1450+(y-40)*scale,867+(1510-x)*scale)
AMP={name:ap(x,118) for name,x in [('VCC',567),('GND',721),('LRC',875),('BCLK',1032),('DIN',1186),('SPK+',1340)]}
AMP['SPK-']=ap(1340,962)
for name,(x,y) in AMP.items():dot(x,y,C[{'VCC':'power','GND':'gnd','LRC':'ws','BCLK':'bclk','DIN':'din','SPK+':'spkp','SPK-':'spkn'}[name]],5)
text(1450,1315,'Leave GAIN and SD open. Do not use NC.',21,MUTED)
text(1450,1346,'Duplicate VCC / GND pads: use one pair.',20,MUTED)

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
lines(1965,342,['DOUT ↔ GND','One lead to each of these nets.','Keep the DOUT wire continuous.','Solder near the microphone pads','and insulate the resistor leads.'],22,step=34)
text(1965,552,'SEL ↔ GND: left channel.',22,C['gnd'],600)
text(1585,675,'Keep the “PORT” opening clear.',21,MUTED)

# Speaker terminal anchors correspond to its two supplied lead ends.
text(1940,803,'Speaker · 8 Ω / 1 W',28,weight=700)
text(1940,833,'Kamami 560816 · factory leads',21,MUTED)
photo('speaker.jpg',2020,873,320,283,(215,230,365,323))
sp_neg=(2020+(233-215)*320/365,873+(248-230)*283/323)
sp_pos=(2020+(249-215)*320/365,873+(257-230)*283/323)
group('spkp');line([AMP['SPK+'],(1410,AMP['SPK+'][1]),(1410,858),(1987,858),(1987,sp_pos[1]),sp_pos],C['spkp'],4);label(1848,881,'SPK+',C['spkp']);end()
group('spkn');line([AMP['SPK-'],(1905,AMP['SPK-'][1]),(1905,sp_neg[1]),sp_neg],C['spkn'],4);label(1848,965,'SPK−',C['spkn']);end()
text(1940,1203,'SPK− is not ground.',25,C['spkp'],700)
text(1940,1238,'Neither speaker lead connects to GND.',21,MUTED)
text(1940,1272,'Start at low volume (1 W speaker).',21,MUTED)

# Battery photo and the unverified power connections are visually distinct.
text(65,1136,'Akyga · LP503759 / 1350 mAh',27,weight=700)
photo('aky0107.jpg',68,1150,500,350,(0,140,800,560))
text(70,1517,'3.7 V · 1350 mAh · PCM · factory JST 2.54 mm',22,MUTED)
rect(661,1100,343,256,'#fffaf0','#d7ba75')
text(682,1138,'Replace the plug first',25,C['power'],700)
text(682,1177,'MX1.25 2-pin to J1',23,C['power'])
text(682,1220,'BAT+ → J1.1',23,C['v3'],600)
text(682,1264,'BAT− → J1.2',23,C['gnd'],600)
text(682,1312,'Check polarity with a meter.',19,MUTED)
group('power')
line([(661,1212),(640,1212),(640,998),(464,998)],C['v3'],4,True)
line([(661,1256),(620,1256),(620,1042),(464,1042)],C['gnd'],4,True)
end()
line([(530,1445),(640,1445),(640,1333),(661,1333)],MUTED,2,True,False)
text(658,1400,'Factory JST 2.54 mm plug',20,MUTED)
text(658,1428,'replace with MX1.25.',20,MUTED)
rect(724,856,280,212,'#fffaf0','#d7ba75')
text(744,893,'Waveshare VCC',25,C['power'],700)
lines(744,929,['Net at U5 VIN / C14.','Physical solder point','still to be identified.','This is not the 3V3 pin.'],20,step=29)
group('power');line([(994,1043),(1005,1043),(1005,AMP['VCC'][1]),AMP['VCC']],C['power'],5,True)
label(1100,AMP['VCC'][1]+35,'AMP.VCC · 3.3–5 V',C['power']);end()

# Concise material limitations, kept part of the exported sheet.
rect(1050,1390,1295,206,'#fff7e8','#d7ba75')
text(1075,1430,'Dashed power connections: verify before connecting',26,C['power'],700)
lines(1075,1470,['Battery: max. charge 1.35 A; standard charge 270 mA, fast charge 675 mA.',
                'Waveshare schematic: R7 = 82 kΩ → approx. 2 A setting. Adjust and measure first.',
                'Amplifier: verify VCC, its 3.3–5 V range and current capacity, including on battery.'],22,step=34)
rect(42,1552,962,112,'#edf3f7','#ccd6dd')
text(64,1585,'Audio mode: disconnect USB–UART.',23,weight=700)
lines(64,1617,['I²S uses GPIO19/20. Native USB power requires D+ and D−',
               'individually isolated. Firmware must release GPIO43/44 and USB.'],20,step=28)
text(1075,1640,'● junction / branch     Crossing wires without a dot are not connected.',21,MUTED)
text(60,1690,'* J9.11: docs say NC, older schematic says GND — leave open. The J9 expansion does not show the connector face.',18,MUTED)
put('</svg>')
svg='\n'.join(s)
svg_path=OUT/'03_physical_connections.svg';svg_path.write_text(svg)

rows=[('3V3','J9.6 / 3V3','MIC 3V','3.3 V'),('GND','J9.5 / GND','MIC GND','Common ground'),('SEL','MIC SEL','MIC GND','Left channel'),('BCLK','J9.3 / D− / GPIO19','MIC BCLK + AMP BCLK','Shared branch'),('WS','J9.4 / D+ / GPIO20','MIC LRCL + AMP LRC','Shared branch'),('MIC DATA','MIC DOUT','J9.10 / RXD / GPIO44','Microphone data'),('RPD1','MIC DOUT','100 kΩ → GND','Additional parallel pull-down resistor'),('AMP DATA','J9.9 / TXD / GPIO43','AMP DIN','Amplifier audio data'),('AMP GND','J9.1 / GND','AMP GND','Amplifier power return'),('AMP VCC','Waveshare VCC / U5 VIN / C14','AMP VCC','Conditional: verify physical tap and 3.3–5 V range'),('SPK+','AMP SPK+','Red speaker lead','8 Ω / 1 W'),('SPK−','AMP SPK−','Black speaker lead','Do not connect to GND'),('BAT+','Akyga BAT+','J1.1 BAT','Conditional: adapt the connector and charge current'),('BAT−','Akyga BAT−','J1.2 GND','Verify polarity with a meter')]
with (OUT/'03_physical_connections.csv').open('w') as f:
    writer=csv.writer(f, lineterminator="\n");writer.writerow(['signal','from','to','note']);writer.writerows(rows)
manifest={'date':'2026-10-01','status':'proposed_unmeasured','battery_confirmed_by_user':'Akyga AKY0107 LP503759 3.7V 1350mAh','amplifier_assumption':'DFRobot DFR0954, procurement-list variant; not separately confirmed by user','microphone':'Adafruit SPH0645 #3421','nets':NETS,'j9':{str(p):n for p,(n,_) in pin_defs.items()},'mic_photo_anchors':MIC,'amp_photo_anchors':AMP,'limitations':['VCC solder point has not been identified on physical PCB.','Battery charge current must be adapted and measured before USB charging.','Diagram requires bench validation of I2S/UART mux and GPIO assignment.','J9 pin numbers are logical, not connector face or wire-colour instructions.']}
(HERE/'connections.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
# The interactive page is separate from the printable SVG layout.
table=''.join('<tr>'+''.join('<td>'+escape(v)+'</td>' for v in row)+'</tr>' for row in rows)
buttons=''.join(f'<button class="signal-row" data-signal="{k}" aria-pressed="false"><span class="signal-swatch" style="--signal:{C[k]}" aria-hidden="true"></span><span>{escape(v["label"])}<small>{escape(" · ".join(v["endpoints"][:3]))}</small></span><span class="signal-arrow" aria-hidden="true">↗</span></button>' for k,v in NETS.items())
html=(HERE/'page.html').read_text()
explorer_url='../site/index.html' if (OUT.parent/'site').is_dir() else '../../publish/Pinchy/site/index.html'
for token,value in {'DIAGRAM':svg,'ROWS':table,'NETBUTTONS':buttons,'NETJSON':json.dumps(NETS,ensure_ascii=False),'EXPLORER_URL':explorer_url}.items():
    html=html.replace('{{'+token+'}}',value)
(OUT/'03_physical_connections.html').write_text(html)
site=OUT.parent/'site/wiring'
if site.parent.is_dir():
    site.mkdir(exist_ok=True)
    (site/'index.html').write_text(html.replace('href="../site/index.html"','href="../index.html"'))
    (site/'03_physical_connections.svg').write_text(svg)
print('Built English SVG, HTML, CSV and connection manifest.')
