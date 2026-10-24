"""Kiểm tra PDF đã build; tùy chọn --render tạo ảnh rà soát không đưa vào Git."""
from pathlib import Path
import hashlib
import json
import sys
import fitz

ROOT=Path(__file__).resolve().parents[1]
path=ROOT/'tai-lieu/De-cuong-Toan-10-Giua-HKI-2026-2027.pdf'
doc=fitz.open(path)
issues=[]
texts=[]
fonts=set()
links=0
for n,page in enumerate(doc,1):
    text=page.get_text()
    texts.append(text)
    if not text.strip():issues.append(f'Trang {n}: không có văn bản')
    if '\ufffd' in text or '\x00' in text:issues.append(f'Trang {n}: kí tự thay thế/null')
    for word in page.get_text('words'):
        x0,y0,x1,y1=word[:4]
        if x0 < -0.5 or y0 < -0.5 or x1>page.rect.width+0.5 or y1>page.rect.height+0.5:
            issues.append(f'Trang {n}: chữ vượt mép giấy: {word[4]}')
    for font in page.get_fonts():
        fonts.add(font[3])
        if not doc.extract_font(font[0])[3]:issues.append(f'Trang {n}: font chưa nhúng: {font[3]}')
    links+=len(page.get_links())
    if '--render' in sys.argv:
        out=ROOT/'kiem-chung/render'
        out.mkdir(exist_ok=True)
        page.get_pixmap(matrix=fitz.Matrix(1.25,1.25)).save(str(out/f'trang-{n:02d}.png'))
all_text=' '.join(' '.join(texts).split())
for phrase in ['TỰ BIÊN SOẠN THEO MA TRẬN','28 bài tự biên soạn','không chứa đề thi hoặc đáp án gốc',
               '3,6 triệu đồng','66,9 m','Hình minh họa','Nguồn tham khảo']:
    if phrase not in all_text:issues.append(f'Thiếu đoạn văn bản: {phrase}')
if len(doc)!=28:issues.append(f'Số trang thay đổi: {len(doc)} (cần rà soát lại phân trang)')
if links<20:issues.append('Thiếu liên kết mục lục/nguồn')
report={
    'file':str(path.relative_to(ROOT)), 'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
    'pages':len(doc), 'size_bytes':path.stat().st_size, 'text_characters':sum(map(len,texts)),
    'all_pages_have_selectable_text':all(bool(t.strip()) for t in texts),
    'fonts':sorted(fonts), 'links':links, 'issues':issues,
    'scope':'Kiểm tra kỹ thuật và giới hạn trang, không tự chứng nhận mọi câu chữ/công thức hoặc nhãn SVG đều đúng.'
}
(ROOT/'kiem-chung/bao-cao-pdf.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,ensure_ascii=False,indent=2))
if issues:raise SystemExit(1)
