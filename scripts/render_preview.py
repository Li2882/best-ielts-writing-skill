"""Render an original typographic social preview (requires Pillow)."""
import argparse
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser()
parser.add_argument('--font',type=Path,default=Path('C:/Windows/Fonts/segoeui.ttf'))
parser.add_argument('--bold-font',type=Path,default=Path('C:/Windows/Fonts/segoeuib.ttf'))
args=parser.parse_args()
if not args.font.is_file() or not args.bold_font.is_file():
    raise SystemExit('Supply available fonts using --font and --bold-font.')
image=Image.new('RGB',(1280,640),'#0f172a')
draw=ImageDraw.Draw(image)
def text(x,y,value,size,color='#f8fafc',bold=False):
    font=ImageFont.truetype(str(args.bold_font if bold else args.font),size)
    box=draw.textbbox((x,y),value,font=font)
    if box[2]>1230 or box[3]>625:raise ValueError(f'Text would clip: {value}')
    draw.text((x,y),value,fill=color,font=font)
draw.rounded_rectangle((64,70,136,78),radius=4,fill='#2dd4bf')
text(64,119,'TASK 1 + TASK 2  /  AI SKILL',22,'#94a3b8')
text(60,177,'IELTS Writing Coach',72,bold=True)
text(64,275,'Understand your score. Know what to improve.',29,'#cbd5e1')
text(64,348,'Band estimates · Evidence · Diagnosis · Revisions',23,'#2dd4bf')
draw.line((64,425,1216,425),fill='#334155',width=1)
text(64,441,'0.482',48,bold=True)
text(64,508,'OVERALL-BAND MAE',20,'#94a3b8')
text(405,441,'82.1%',48,bold=True)
text(405,508,'WITHIN ±0.5 BAND',20,'#94a3b8')
text(830,454,'28-essay development evaluation',21,'#cbd5e1')
text(830,494,'Unofficial · GPT-6 Astra / High',18,'#94a3b8')
text(64,571,'OPEN WORKFLOW. TRACEABLE FEEDBACK.',17,'#64748b')
target=ROOT/'assets/social-preview.png'
image.save(target,optimize=True)
if target.stat().st_size>=1_000_000:raise ValueError('Social preview exceeds 1 MB.')
print(f'{target}: 1280x640, {target.stat().st_size} bytes')
