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
