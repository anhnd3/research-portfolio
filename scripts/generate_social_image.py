"""Generate a 1200x630 OG preview for the current public research article."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

WIDTH, HEIGHT = 1200, 630
ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets" / "research-reranking-og.png"
OUTPUT.parent.mkdir(parents=True, exist_ok=True)

img = Image.new("RGB", (WIDTH, HEIGHT))
pixels = img.load()
for y in range(HEIGHT):
    for x in range(WIDTH):
        t = x / WIDTH * 0.7 + y / HEIGHT * 0.3
        pixels[x, y] = (int(12 + 10*t), int(26 + 42*t), int(49 + 60*t))
draw = ImageDraw.Draw(img)
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REGULAR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
def font(size, bold=False):
    return ImageFont.truetype(FONT_BOLD if bold else FONT_REGULAR, size)

draw.rounded_rectangle((65, 56, 397, 103), radius=22, fill="#1d436c")
draw.text((88, 67), "AIDEN  /  RESEARCH", fill="#cce5fc", font=font(20, True))
draw.rounded_rectangle((1035, 58, 1135, 100), radius=20, fill="#305f8c")
draw.text((1057, 68), "v1.2", fill="#e7f4ff", font=font(20, True))
draw.text((66, 160), "Compact Models for", fill="#ffffff", font=font(62, True))
draw.text((66, 247), "Domain-Specific", fill="#ffffff", font=font(66, True))
draw.text((66, 331), "Reranking", fill="#ffffff", font=font(66, True))
draw.rounded_rectangle((66, 442, 830, 447), radius=2, fill="#3ec4c2")
draw.text((66, 468), "Architectures  |  Learning Objectives  |  Decision Readouts", fill="#d3e1f0", font=font(21))
draw.text((66, 548), "594 QUERIES     5 CONFIGURATIONS     MULTI-LABEL EVALUATION", fill="#a5c9e9", font=font(18, True))
points = [(910,377),(958,333),(1006,356),(1054,292),(1102,264)]
for i,(x,y) in enumerate(points):
    draw.ellipse((x-8,y-8,x+8,y+8), fill="#51cfcb")
    if i:
        px,py=points[i-1]
        draw.line((px,py,x,y), fill="#64c1cc", width=4)
for x,height in [(916,69),(964,123),(1012,102),(1060,163),(1108,188)]:
    draw.rounded_rectangle((x,479-height,x+14,479), radius=5, fill="#234e76")
img.save(OUTPUT, "PNG", optimize=True)
print(f"Social image: {OUTPUT} ({OUTPUT.stat().st_size} bytes)")

# GDEM reproduction social preview — forest green, low/high spectral graph motif.
OUTPUT_GDEM = ROOT/"assets"/"research-gdem-og.png"
im2=Image.new("RGB",(WIDTH,HEIGHT))
px=im2.load()
for y in range(HEIGHT):
    for x in range(WIDTH):
        v=0.55*x/WIDTH+0.45*y/HEIGHT
        px[x,y]=(int(16+16*v),int(31+29*v),int(23+23*v))
pen=ImageDraw.Draw(im2)
pen.rounded_rectangle((65,56,355,103),radius=21,fill="#315644")
pen.text((86,67),"AIDEN / RESEARCH",fill="#e4f4d5",font=font(20,True))
pen.text((65,171),"Graph Distillation",fill="#fbf9f0",font=font(62,True))
pen.text((65,251),"with Eigenbasis",fill="#d8edab",font=font(59,True))
pen.text((65,333),"Matching",fill="#d8edab",font=font(64,True))
pen.rounded_rectangle((65,439,755,444),radius=2,fill="#a0c399")
pen.text((65,466),"Reproduction  |  Graph Fourier  |  Cross-GNN Transfer",fill="#d0decf",font=font(20))
pen.text((65,552),"17 CONFIGURATIONS   /   6 DATASETS   /   DEC 2025",fill="#b9d49e",font=font(18,True))
nodes=[(931,177),(1008,150),(1088,211),(934,280),(1018,277),(1103,305),(962,390),(1036,395),(1117,416)]
edges=[(0,1),(1,2),(0,3),(0,4),(1,4),(2,4),(2,5),(3,4),(4,5),(3,6),(3,7),(4,7),(5,7),(5,8),(6,7),(7,8)]
for i,j in edges:
    pen.line((*nodes[i],*nodes[j]),fill="#62826f",width=4)
for k,(x,y) in enumerate(nodes):
    c="#d8edae" if k<3 else "#9fc5bc" if k<6 else "#d7b98f"
    pen.ellipse((x-10,y-10,x+10,y+10),fill=c,outline="#fffdf2",width=2)
im2.save(OUTPUT_GDEM,"PNG",optimize=True)
print(f"Social image: {OUTPUT_GDEM} ({OUTPUT_GDEM.stat().st_size} bytes)")


# UFCE thesis retrospective social preview — verified target-class transition.
OUTPUT_UFCE = ROOT/"assets"/"research-ufce-og.png"
im3=Image.new("RGB",(WIDTH,HEIGHT))
upx=im3.load()
for y in range(HEIGHT):
    for x in range(WIDTH):
        v=0.48*x/WIDTH+0.52*y/HEIGHT
        upx[x,y]=(int(15+16*v),int(33+30*v),int(25+25*v))
p=ImageDraw.Draw(im3)
p.rounded_rectangle((65,56,366,103),radius=21,fill="#355d45")
p.text((86,67),"AIDEN / RESEARCH",fill="#eef5d8",font=font(20,True))
p.text((65,161),"UFCE Revisited",fill="#f9f7eb",font=font(66,True))
p.text((65,249),"Validity Before",fill="#d8edac",font=font(62,True))
p.text((65,332),"Recommendation",fill="#d8edac",font=font(61,True))
p.rounded_rectangle((65,439,815,444),radius=2,fill="#a9c79b")
p.text((65,465),"Counterfactual Validity  |  User Feedback  |  Handoff",fill="#d3e4d1",font=font(19))
p.text((65,551),"THESIS DEFENDED SEP 2026   /   5 DATASETS",fill="#c9dba9",font=font(19,True))
# Conceptual candidates: the accepted state is reached only after verification.
for i,(x,y) in enumerate([(966,177),(1088,177),(966,290),(1088,290)]):
    fill=("#e9b982","#e9b982","#e9b982","#b9e798")[i]
    p.ellipse((x-18,y-18,x+18,y+18),fill=fill,outline="#f5f6ec",width=2)
    p.line((x+19,y,x+43,y),fill="#b8d1b8",width=3)
p.rounded_rectangle((917,375,1144,433),radius=12,fill="#224d35",outline="#719978",width=2)
p.text((942,389),"f(x') = target",fill="#d8edac",font=font(20,True))
im3.save(OUTPUT_UFCE,"PNG",optimize=True)
print(f"Social image: {OUTPUT_UFCE} ({OUTPUT_UFCE.stat().st_size} bytes)")


# Vision Transformer / FER-2013 retrospective social preview — accuracy versus model size.
OUTPUT_VIT = ROOT/"assets"/"research-vit-og.png"
im4=Image.new("RGB",(WIDTH,HEIGHT))
vpx=im4.load()
for y in range(HEIGHT):
    for x in range(WIDTH):
        v=0.6*x/WIDTH+0.4*y/HEIGHT
        vpx[x,y]=(int(21+14*v),int(34+22*v),int(29+20*v))
q=ImageDraw.Draw(im4)
q.rounded_rectangle((65,56,355,103),radius=21,fill="#3a5a4a")
q.text((86,67),"AIDEN / RESEARCH",fill="#eef5d8",font=font(20,True))
q.text((65,161),"Vision Transformers",fill="#f9f7eb",font=font(60,True))
q.text((65,247),"for Facial Expression",fill="#d8edac",font=font(54,True))
q.text((65,323),"Recognition",fill="#d8edac",font=font(60,True))
q.rounded_rectangle((65,439,780,444),radius=2,fill="#a9c79b")
q.text((65,465),"FER-2013  |  Accuracy  |  Model Size  |  Latency",fill="#d3e4d1",font=font(20))
q.text((65,551),"3 ARCHITECTURES   /   RESEARCH 2025",fill="#c9dba9",font=font(19,True))
# Bars: parameter count (millions), small hybrid versus two large transformers.
for x,params,label,fill in [(930,6.22,"6.2M","#d8edac"),(1010,88.96,"89M","#7f9f8a"),(1090,85.80,"86M","#7f9f8a")]:
    h=int(20+params*2.6)
    q.rounded_rectangle((x,470-h,x+46,470),radius=6,fill=fill)
    q.text((x,482),label,fill="#e8efe3",font=font(16,True))
im4.save(OUTPUT_VIT,"PNG",optimize=True)
print(f"Social image: {OUTPUT_VIT} ({OUTPUT_VIT.stat().st_size} bytes)")
