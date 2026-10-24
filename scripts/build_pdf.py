"""Biên dịch PDF bằng Typst; không tải gói/font từ mạng khi build."""
from pathlib import Path
import typst
root = Path(__file__).resolve().parents[1]
output = root / 'tai-lieu/De-cuong-Toan-10-Giua-HKI-2026-2027.pdf'
typst.compile(str(root / 'tai-lieu/de-cuong.typ'), output=str(output), root=str(root))
print(output)
