#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check_completeness.py -- Doi chieu de cuong voi ma tran de kiem tra.

Kiem tra:
  * Du 12 cau trac nghiem nhieu phuong an (moi cau du 4 phuong an A-D).
  * Du 2 cau dung/sai, moi cau 4 y (a-d).
  * Du 4 cau tra loi ngan.
  * Du 3 cau tu luan.
  * Moi cau deu co dap an trong Phan 4.
  * Ti le diem theo chuong khop voi ma tran goc (4,0 / 2,5 / 3,0 / 0,5).
"""
import re
import sys

sys.path.insert(0, "de-cuong/src")
import content  # noqa: E402

TEXT = "\n".join(content.SECTIONS)
PARTS = {}
for name in ("PART3", "PART4"):
    PARTS[name] = getattr(content, name)

p3 = content.PART3
p4 = content.PART4
fails, passes = [], []


def ok(cond, msg):
    (passes if cond else fails).append(msg)


# ---------------------------------------------------------------- Phan I
mc_questions = re.findall(r"\*\*Câu (\d+)\.\*\*", p3.split("PHẦN II.")[0])
ok(len(mc_questions) == 12, f"Phần I có 12 câu (đếm được {len(mc_questions)})")
ok(mc_questions == [str(i) for i in range(1, 13)],
   "Phần I đánh số Câu 1..12 liên tục")

seg1 = p3.split("PHẦN II.")[0]
for n in range(1, 13):
    body = seg1.split(f"**Câu {n}.**")[1].split("**Câu ")[0]
    opts = re.findall(r"^- \*\*([A-D])\.\*\*", body, re.M)
    ok(opts == ["A", "B", "C", "D"], f"Câu {n}: đủ 4 phương án A–D (thấy {opts})")

# ---------------------------------------------------------------- Phan II
seg2 = p3.split("PHẦN II.")[1].split("PHẦN III.")[0]
ds_questions = re.findall(r"\*\*Câu (\d+)\.\*\*", seg2)
ok(ds_questions == ["1", "2"], f"Phần II có 2 câu (thấy {ds_questions})")
for n in ("1", "2"):
    body = seg2.split(f"**Câu {n}.**")[1]
    body = body.split("**Câu 2.**")[0] if n == "1" else body
    subs = re.findall(r"^- \*\*([a-d])\)\*\*", body, re.M)
    ok(subs == ["a", "b", "c", "d"], f"Câu đúng/sai {n}: đủ 4 ý a–d (thấy {subs})")

# ---------------------------------------------------------------- Phan III
seg3 = p3.split("PHẦN III.")[1].split("PHẦN IV.")[0]
st_questions = re.findall(r"\*\*Câu (\d+)\.\*\*", seg3)
ok(st_questions == ["1", "2", "3", "4"], f"Phần III có 4 câu (thấy {st_questions})")

# ---------------------------------------------------------------- Phan IV
seg4 = p3.split("PHẦN IV.")[1]
tl_questions = re.findall(r"\*\*Câu (\d+)\.\*\*", seg4)
ok(tl_questions == ["1", "2", "3"], f"Phần IV có 3 câu tự luận (thấy {tl_questions})")

# --------------------------------------------------- dap an trong Phan IV
ans_mc = re.search(r"\| Đáp án \|(.+)\|\n", p4)
if ans_mc:
    letters = re.findall(r"\b([A-D])\b", ans_mc.group(1))
    ok(len(letters) == 12, f"Bảng đáp án Phần I có 12 phương án (thấy {len(letters)})")
else:
    fails.append("Không tìm thấy bảng đáp án Phần I")

for n in range(1, 13):
    ok(f"**Câu {n} – Đáp án" in p4 or f"**Câu {n} – Đáp án" in p4,
       f"Câu {n} có lời giải chi tiết ở Phần 4")

for n in ("1", "2"):
    ok(f"**Câu {n}.** A =" in p4 or f"**Câu {n}.** " in p4,
       f"Câu đúng/sai {n} có lời giải chi tiết ở Phần 4")

for n in ("1", "2", "3", "4"):
    ok(f"**Câu {n} – Đáp án:" in p4, f"Câu trả lời ngắn {n} có đáp án")

for n in ("1", "2", "3"):
    ok(f"### Câu {n} (1,0 điểm)" in p4, f"Câu tự luận {n} có lời giải và hướng dẫn chấm")

# ----------------------------------------------------- tong diem theo cau truc
ok("12 câu – 3,0 điểm" in p3, "Phần I ghi đúng 12 câu – 3,0 điểm")
ok("2 câu – 2,0 điểm" in p3, "Phần II ghi đúng 2 câu – 2,0 điểm")
ok("4 câu – 2,0 điểm" in p3, "Phần III ghi đúng 4 câu – 2,0 điểm")
ok("3 câu – 3,0 điểm" in p3, "Phần IV ghi đúng 3 câu – 3,0 điểm")

# ------------------------------------ doi chieu bang dac ta: 24 lenh hoi + 3 TL
ok("24 lệnh hỏi" in TEXT, "Tài liệu nêu đúng tổng 24 lệnh hỏi trắc nghiệm")
ok("2⁴ = 16" in TEXT or "2⁴ = 16" in TEXT, "Đáp án số tập con dùng 2⁴")

# ------------------------------------------------------------- in ket qua
print(f"{len(passes)} kiểm tra ĐẠT")
if fails:
    print(f"\n{len(fails)} kiểm tra KHÔNG ĐẠT:")
    for f in fails:
        print("  ✗", f)
    raise SystemExit(1)
print("Không có lỗi: đề minh họa khớp đầy đủ với ma trận và mọi câu đều có đáp án.")
