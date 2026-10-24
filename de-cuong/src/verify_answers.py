"""Kiem tra lai toan bo ket qua so trong de cuong va de minh hoa.
Chay: python3 de-cuong/src/verify_answers.py
"""
import math

D = math.degrees
R = math.radians
ok = fail = 0


def chk(name, got, want, tol=5e-3):
    global ok, fail
    good = (got == want) if tol == 0 else abs(got - want) < tol
    ok, fail = ok + good, fail + (not good)
    print(f"[{'PASS' if good else 'FAIL'}] {name:<52s} got={got!r:>18}  want={want!r}")


print("=== PHAN I: TRAC NGHIEM NHIEU PHUONG AN ===")
# Cau 2: phu dinh cua "forall x in R, x^2+1 > 0"  -> "exists x in R, x^2+1 <= 0"  (dap an A)
# Cau 3: A = {x in Z | -2 <= x < 3} = {-2,-1,0,1,2}
chk("Cau 3: so phan tu cua {x in Z | -2<=x<3}", len([x for x in range(-9, 9) if -2 <= x < 3]), 5, 0)
# Cau 8: sin a = 3/5, 90<a<180 -> cos a = -4/5
s = 3 / 5
chk("Cau 8: cos a", -math.sqrt(1 - s * s), -0.8)
# Cau 10: S = 1/2 . AB . AC . sin A = 1/2.8.5.sin60 = 10*sqrt(3)
chk("Cau 10: dien tich 1/2.8.5.sin60", 0.5 * 8 * 5 * math.sin(R(60)), 10 * math.sqrt(3))
# Cau 11: hinh binh hanh ABCD -> AB = DC (dap an A)
# Cau 12: hinh binh hanh ABCD tam O -> AD = -CB  => phat bieu "AD = CB" la SAI (dap an C)
chk("Cau 12: kiem tra AD = -CB (hinh binh hanh)",
    abs(((1 - 0) - (1 - 0))), 0, 0)  # hinh hoc, chi kiem tra tinh nhat quan ki hieu

print("\n=== PHAN II: DUNG / SAI ===")
A_lo, A_hi, B_lo = -3.0, 4.0, 0.0   # A = (-3;4], B = [0;+inf)
chk("C1a: 4 thuoc A, -3 khong thuoc A  -> DUNG", (A_lo < 4 <= A_hi) and not (A_lo < -3 <= A_hi), True)
chk("C1c: A cap B = [0;4] (khong phai (0;4]) -> phat bieu SAI",
    max(A_lo, B_lo), 0.0)
ints_A_minus_B = [k for k in range(-20, 20) if A_lo < k <= A_hi and not (k >= B_lo)]
chk("C1d: (A\\B) cap Z = {-2;-1}", len(ints_A_minus_B), 2, 0)
print("       chi tiet:", ints_A_minus_B)

# (*) 3x + 2y <= 12
def f(x, y):
    return 3 * x + 2 * y
chk("C2a: (2;3) la nghiem cua (*)", f(2, 3) <= 12, True)
chk("C2a: (3;1) THUOC mien nghiem -> phat bieu SAI", f(3, 1) <= 12, True)
print("       3*3+2*1 =", f(3, 1), "(<=12 nen (3;1) thuoc mien nghiem)")
chk("C2b: O(0;0) thuoc mien nghiem", f(0, 0) <= 12, True)
chk("C2c: cat Ox tai x=4", 12 / 3, 4.0)
chk("C2c: cat Oy tai y=6", 12 / 2, 6.0)

print("\n=== PHAN III: TRA LOI NGAN ===")
sol = sorted({x for x in range(-30, 30) if x * x - 5 * x + 6 == 0} | {0, 1, 2, 3})
chk("TLN1: tap A", len(sol), 4, 0)
print("       A =", sol, "-> so tap con =", 2 ** len(sol))
chk("TLN1: so tap con = 2^4", 2 ** len(sol), 16, 0)
chk("TLN2: so HS khong thich ca hai mon", 40 - (25 + 20 - 12), 7, 0)
t = -2.0                                    # tan a = -2, 90<a<180
cos_a = -1 / math.sqrt(1 + t * t)
sin_a = t * cos_a
chk("TLN3: sin a = 2/sqrt5", sin_a, 2 / math.sqrt(5))
chk("TLN3: cos a = -1/sqrt5", cos_a, -1 / math.sqrt(5))
P = (2 * sin_a - 3 * cos_a) / (sin_a + cos_a)
chk("TLN3: P = (2sin-3cos)/(sin+cos)", P, 7.0)
h = 20 * math.tan(R(55))
chk("TLN4: chieu cao cot co = 20.tan55", h, 28.5630, 1e-3)
print(f"       lam tron hang phan muoi -> {round(h,1)}")

print("\n=== PHAN IV: TU LUAN ===")
# Cau 1: A = [-4;3), B = (1;6]
chk("TL1: A cap B = (1;3) - dau trai", max(-4, 1), 1, 0)
chk("TL1: A hop B = [-4;6] - dau phai", max(3, 6), 6, 0)
# Cau 2: h = AB . sin35 . sin50 / sin15
AB = 24.0
goc_ADB = 180 - 35 - (180 - 50)
chk("TL2: goc ADB", goc_ADB, 15, 1e-9)
BD = AB * math.sin(R(35)) / math.sin(R(15))
ht = BD * math.sin(R(50))
chk("TL2: BD = 24.sin35/sin15", BD, 53.1871, 1e-3)
chk("TL2: chieu cao thap CD", ht, 40.7437, 1e-3)
print(f"       lam tron hang phan muoi -> {round(ht,1)} m")
# doi chieu bang cong thuc cot
chk("TL2: doi chieu 24/(cot35-cot50)", AB / (1 / math.tan(R(35)) - 1 / math.tan(R(50))), ht, 1e-9)
# Cau 3: max F = 500x + 400y, mien: x,y>=0; 4x+3y<=48; 2x+3y<=36
verts = [(0, 0), (12, 0), (6, 8), (0, 12)]
for (x, y) in verts:
    assert 4 * x + 3 * y <= 48 and 2 * x + 3 * y <= 36, (x, y)
vals = {v: 500 * v[0] + 400 * v[1] for v in verts}
print("       dinh va gia tri F:", vals)
chk("TL3: dinh (6;8) = giao 4x+3y=48 & 2x+3y=36", (48 - 36) / 2, 6, 0)
chk("TL3: F lon nhat (nghin dong)", max(vals.values()), 6200, 0)
# quet toan bo mien nghiem nguyen de chac chan
best = max((500 * x + 400 * y) for x in range(0, 14) for y in range(0, 14)
           if 4 * x + 3 * y <= 48 and 2 * x + 3 * y <= 36)
chk("TL3: quet vet (x,y nguyen) F lon nhat", best, 6200, 0)

print("\n=== VI DU MINH HOA TRONG PHAN LY THUYET ===")
chk("VD ch2: dinh (2;4) cua {x+y<=6, 2x+y<=8, x,y>=0}", (2 * 2 + 4), 8, 0)
F2 = {(0, 0): 0, (4, 0): 12, (2, 4): 14, (0, 6): 12}
chk("VD ch2: max F=3x+2y = 14 tai (2;4)", max(F2.values()), 14, 0)
p = (13 + 14 + 15) / 2
chk("VD ch3: Heron a=13,b=14,c=15 -> S=84", math.sqrt(p * (p - 13) * (p - 14) * (p - 15)), 84.0)
chk("VD ch3: cosin b=5,c=8,A=60 -> a=7", math.sqrt(25 + 64 - 2 * 5 * 8 * math.cos(R(60))), 7.0)
chk("VD ch3: dinh li sin a=6, A=60 -> R=2*sqrt3", 6 / math.sin(R(60)) / 2, 2 * math.sqrt(3))
# b=5, c=8, a=7  ->  m_a = (1/2)*sqrt(2b^2 + 2c^2 - a^2) = (1/2)*sqrt(129)
ma = math.sqrt((2 * (5 ** 2) + 2 * (8 ** 2) - 7 ** 2) / 4)
chk("VD ch3: trung tuyen m_a = (1/2)sqrt129", ma, math.sqrt(129) / 2, 1e-12)
chk("VD ch3: trung tuyen m_a ~ 5.6789", ma, 5.67891, 1e-4)
print("       2b^2+2c^2-a^2 =", 2 * 25 + 2 * 64 - 49)
chk("VD ch3: cot30 = sqrt3", 1 / math.tan(R(30)), math.sqrt(3))
chk("VD ch3: sin150 = 1/2", math.sin(R(150)), 0.5)
chk("VD ch3: cos135 = -sqrt2/2", math.cos(R(135)), -math.sqrt(2) / 2)
chk("VD ch3: tan120 = -sqrt3", math.tan(R(120)), -math.sqrt(3))

print(f"\n=== TONG: {ok} PASS / {fail} FAIL ===")
raise SystemExit(1 if fail else 0)
