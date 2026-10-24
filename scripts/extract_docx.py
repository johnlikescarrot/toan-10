"""Trích xuất đoạn văn, công thức OMML và ô bảng; không diễn giải ảnh WMF."""
from pathlib import Path
from zipfile import ZipFile
import xml.etree.ElementTree as ET
import hashlib

ROOT = Path(__file__).resolve().parents[1]
source = ROOT / 'MA TRẬN TOÁN 10 - GIỮA KÌ I.docx'
ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
      'm': 'http://schemas.openxmlformats.org/officeDocument/2006/math'}
def text(el):
    return ''.join(e.text or '' for e in el.iter() if e.tag in
                   {f'{{{ns["w"]}}}t', f'{{{ns["m"]}}}t'})
with ZipFile(source) as z:
    body = ET.fromstring(z.read('word/document.xml')).find('w:body', ns)
    lines = ['# Bản trích xuất DOCX', '', f'SHA-256: `{hashlib.sha256(source.read_bytes()).hexdigest()}`',
             '', 'Các ô gộp giữ thứ tự XML, không tự khôi phục bố cục bảng. '
             'Công thức OMML chỉ nối phần chữ, không giữ bố cục; 4 ảnh WMF không được OCR.', '']
    for el in body:
        if el.tag == f'{{{ns["w"]}}}p':
            lines.append(text(el))
        elif el.tag == f'{{{ns["w"]}}}tbl':
            lines.append('\n## Bảng\n')
            for row in el.findall('w:tr', ns):
                lines.append(' | '.join(' / '.join(text(p) for p in cell.findall('w:p', ns))
                                        for cell in row.findall('w:tc', ns)))
    lines += ['', '## Đối tượng nhúng', *[n for n in z.namelist() if '/media/' in n]]
(ROOT / 'kiem-chung/trich-xuat-docx.md').write_text('\n'.join(line.rstrip() for line in lines) + '\n', encoding='utf-8')
