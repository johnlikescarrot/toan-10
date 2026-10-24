"""Hình SVG tự vẽ, có nhãn tiếng Việt; không cần tải tài nguyên bên ngoài."""
from pathlib import Path
from math import sin, cos, pi
OUT = Path(__file__).resolve().parents[1] / 'tai-lieu/hinh'
OUT.mkdir(exist_ok=True)
def svg(name, width, height, body):
    defs = '<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8" fill="#174b61"/></marker></defs>'
    (OUT / name).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">{defs}<g font-family="DejaVu Sans" font-size="16" fill="#123e55">{body}</g></svg>')
def line(x1,y1,x2,y2,arrow=False,color='#174b61',dash=False):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="2"'+(' marker-end="url(#arrow)"' if arrow else '')+(' stroke-dasharray="5 4"' if dash else '')+'/>'
def text(x,y,s):return f'<text x="{x}" y="{y}">{s}</text>'
def dot(x,y,closed=True):return f'<circle cx="{x}" cy="{y}" r="4" fill="'+('#174b61' if closed else 'white')+'" stroke="#174b61" stroke-width="2"/>'
# Four disjoint regions with the counts from T4.
svg('ven.svg',640,180, '<rect x="10" y="5" width="620" height="170" rx="7" fill="#f7fafb" stroke="#8196a0"/>'
    '<circle cx="260" cy="90" r="70" fill="#c9e8eb" stroke="#166976"/>'
    '<circle cx="360" cy="90" r="70" fill="#ffe1b2" fill-opacity="0.7" stroke="#997128"/>'
    +text(25,30,'U: 45 học sinh')+text(205,24,'Bóng đá')+text(365,24,'Cầu lông')
    +text(220,96,'17')+text(305,96,'8')+text(385,96,'12')+text(465,140,'8: không môn nào'))
# Number line, T2.
b=''
for y,label,l,r,lc,rc in [(40,'A',125,365,True,False),(90,'B',269,461,False,True),(140,'A ∩ B',269,365,False,False)]:
    b+=text(10,y+5,label)+line(90,y,555,y,True)+f'<line x1="{l}" y1="{y}" x2="{r}" y2="{y}" stroke="#16888d" stroke-width="7"/>'+dot(l,y,lc)+dot(r,y,rc)
    for x,n in [(125,'−2'),(269,'1'),(365,'3'),(461,'5')]:b+=text(x-7,y+24,n)
svg('truc-so.svg',640,180,b)
# Parallelogram and arrow directions.
points={'A':(100,140),'B':(330,140),'C':(410,35),'D':(180,35)}
b=''
for a,c in [('A','B'),('B','C'),('D','C'),('A','D')]:b+=line(*points[a],*points[c],True)
for n,(x,y) in points.items():b+=text(x-15,y+22 if y>100 else y-10,n)
b+=text(465,70,'AB và DC:')+text(465,95,'cùng hướng,')+text(465,120,'cùng độ dài.')
svg('vecto.svg',640,180,b)
# Linear feasible polygon for H1/H2: coordinate map in units 30.
x0,y0=100,255
pt=lambda x,y:(x0+30*x,y0-30*y)
b='<polygon points="'+ ' '.join(f'{x},{y}' for x,y in [pt(0,0),pt(4,0),pt(2,4),pt(0,6)])+'" fill="#bfe5e8" stroke="#166976" stroke-width="2"/>'
b+=line(*pt(-0.5,0),*pt(7.3,0),True)+line(*pt(0,-0.4),*pt(0,7.5),True)
b+=line(*pt(-.4,6.4),*pt(6.7,-.7))+line(*pt(.5,7),*pt(4.3,-.6))
for x,y,n,dx,dy in [(0,0,'O(0;0)',-65,25),(4,0,'A(4;0)',-10,25),(2,4,'B(2;4)',10,5),(0,6,'C(0;6)',-80,-10)]:
    a,c=pt(x,y);b+=dot(a,c)+text(a+dx,c+dy,n)
b+=text(320,280,'x')+text(85,22,'y')+text(355,65,'Miền tô: thỏa cả hệ')+text(355,100,'x ≥ 0; y ≥ 0')+text(355,130,'x + y ≤ 6')+text(355,160,'2x + y ≤ 8')+text(355,205,'Các cạnh đều được lấy.')
svg('mien-nghiem.svg',640,300,b)
# Triangle IV.2: A=(90,175), B=(300,175), C=(255.62,9.38), scaling 3.5 pixels/m.
A=(90,190);B=(300,190);C=(255.621778,24.378222)
b=line(*A,*B)+line(*A,*C)+line(*B,*C)
b+=text(65,212,'A')+text(303,212,'B')+text(255,18,'C')+text(165,215,'60 m')+text(130,176,'45°')+text(250,176,'75°')
b+=text(370,70,'∠C = 60°')+text(370,108,'AC đối diện góc B.')+text(370,146,'AB đối diện góc C.')
svg('tam-giac.svg',640,230,b)
print('Đã vẽ 5 hình SVG.')
