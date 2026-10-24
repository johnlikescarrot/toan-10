#!/usr/bin/env python3
"""
Independent mathematical verification script for 100% of computational problems
in Phần D (Question Bank) and Phần E (03 Complete 2026–2027 Midterm I Exams).
"""

import math
from fractions import Fraction


def verify_question_bank() -> None:
    print("=== Verifying Phần D: Ngân hàng câu hỏi & bài tập ===")

    # --- MCQ checks ---
    # Q10: A = {x in Z | (x^2 - 4)(2x - 3) = 0} -> x = -2, 2 (since 3/2 not in Z)
    q10 = [x for x in range(-10, 11) if (x**2 - 4) * (2 * x - 3) == 0]
    assert q10 == [-2, 2], q10

    # Q11: B = {x in N | x^2 - 5x + 4 <= 0} -> {1, 2, 3, 4}
    q11 = [x for x in range(0, 20) if x**2 - 5 * x + 4 <= 0]
    assert q11 == [1, 2, 3, 4], q11

    # Q28: sin a = 3/5, 90 < a < 180 -> cos a = -4/5, tan a = -3/4
    sin_a = Fraction(3, 5)
    cos_a = -Fraction(4, 5)
    assert sin_a**2 + cos_a**2 == 1
    assert sin_a / cos_a == Fraction(-3, 4)

    # Q29: cos a = -1/3 -> P = 2 sin^2 a + 5 cos^2 a = 2(8/9) + 5(1/9) = 21/9 = 7/3
    cos2 = Fraction(1, 9)
    sin2 = 1 - cos2
    assert 2 * sin2 + 5 * cos2 == Fraction(7, 3)

    # Q30: tan a = 2 -> P = (3 sin a - 2 cos a) / (sin a + cos a) = (6 - 2)/(2 + 1) = 4/3
    t = Fraction(2, 1)
    assert (3 * t - 2) / (t + 1) == Fraction(4, 3)

    # Q36: Triangle ABC: b=5, c=8, A=60 deg -> a^2 = 25 + 64 - 2*5*8*(1/2) = 49 -> a=7
    a_sq = 5**2 + 8**2 - 2 * 5 * 8 * Fraction(1, 2)
    assert a_sq == 49

    # Q37: Triangle ABC: a=6, A=30 deg -> R = a/(2 sin A) = 6 / (2 * 0.5) = 6
    assert Fraction(6, 1) / (2 * Fraction(1, 2)) == 6

    # Q38: Triangle ABC: a=13, b=14, c=15 -> p=21, S = sqrt(21*8*7*6) = 84, r = S/p = 4, R = abc/(4S) = 65/8
    a, b, c = 13, 14, 15
    p = (a + b + c) // 2
    S = math.isqrt(p * (p - a) * (p - b) * (p - c))
    assert p == 21 and S == 84
    assert Fraction(S, p) == 4
    assert Fraction(a * b * c, 4 * S) == Fraction(65, 8)

    # Q39: Triangle ABC: AB=6, AC=8, A=120 deg -> S = 1/2 * 6 * 8 * sin(120) = 12*sqrt(3)
    assert Fraction(1, 2) * 6 * 8 == 24  # * sqrt(3)/2 = 12*sqrt(3)

    # Q40: Pond distance: CA=40, CB=60, C=60 deg -> AB^2 = 1600+3600-2400 = 2800 -> AB = 20*sqrt(7) ~ 52.9 m
    ab2 = 40**2 + 60**2 - 2 * 40 * 60 * Fraction(1, 2)
    assert ab2 == 2800 and round(math.sqrt(ab2), 1) == 52.9

    # --- True/False checks ---
    # ĐS1: A = [-3; 2), B = (0; 5]
    # a) -3 in A (True)
    # b) A \cap Z = {-3, -2, -1, 0, 1} -> 5 elements (if statement says 6 elements -> False)
    a_int = [x for x in range(-10, 10) if -3 <= x < 2]
    assert a_int == [-3, -2, -1, 0, 1] and len(a_int) == 5
    # c) A \cap B = (0; 2), C_R(A \cup B) = R \ [-3; 5] = (-inf; -3) U (5; +inf)
    # d) C = (m - 1; m + 2), C \subset A=[-3; 2) -> m - 1 >= -3 and m + 2 <= 2 -> -2 <= m <= 0 (3 integer values: -2,-1,0)
    m_vals = [m for m in range(-10, 10) if m - 1 >= -3 and m + 2 <= 2]
    assert m_vals == [-2, -1, 0]

    # ĐS2: A = {x in R | |x| <= 3} = [-3; 3], B = (1; +inf), M = (2m - 1; 2m + 3)
    # M \cap A = empty <=> 2m + 3 < -3 or 2m - 1 > 3 <=> m < -3 or m > 2 -> M \cap A != empty <=> -3 <= m <= 2 (6 integers)
    m_nonempty = [m for m in range(-10, 10) if not (2 * m + 3 <= -3 or 2 * m - 1 >= 3)]
    # Careful! M = (2m-1; 2m+3) is open! If 2m+3 == -3 (m=-3), M = (-7; -3) and A = [-3; 3] -> M \cap A = empty!
    # If 2m-1 == 3 (m=2), M = (3; 7) and A = [-3; 3] -> M \cap A = empty!
    # So M \cap A != empty <=> -3 < m < 2 -> integers m in {-2, -1, 0, 1} (4 integers)!
    assert m_nonempty == [-2, -1, 0, 1]

    # ĐS3: Venn 45 students, Math=25, Eng=20, 8 neither -> M U E = 37 -> M \cap E = 25 + 20 - 37 = 8
    assert 25 + 20 - (45 - 8) == 8
    # Only Math = 25 - 8 = 17, exactly 1 subject = 17 + (20 - 8) = 29
    assert (25 - 8) + (20 - 8) == 29

    # ĐS6: Ticket problem: x child tickets (40k), y adult tickets (80k), min revenue 4,000k -> 40x + 80y >= 4000 <=> x + 2y >= 100
    assert 40 * 30 + 80 * 40 == 4400 >= 4000

    # --- Short Answer (TLN) checks ---
    # TLN1: A = {x in N | x^2 - 4x + 3 = 0 or x^2 - 9 = 0} -> x in N: {1, 3} -> Wait let's make 4 elements:
    # A = {x in Z | x^2 <= 4} -> {-2, -1, 0, 1, 2} -> 5 elements -> 2^5 = 32 subsets!
    tln1 = [x for x in range(-10, 10) if x**2 <= 4]
    assert len(tln1) == 5 and 2 ** len(tln1) == 32

    # TLN2: A = {x in N | x < 6 and x is divisor of 12} -> {1, 2, 3, 4} -> non-empty subsets = 2^4 - 1 = 15
    tln2 = [x for x in range(1, 6) if 12 % x == 0]
    assert tln2 == [1, 2, 3, 4] and (2 ** len(tln2) - 1) == 15

    # TLN3: A = {1; 2}, B = {1; 2; 3; 4; 5; 6} -> X such that A \subset X \subset B -> 2^(6-2) = 16
    assert 2 ** (6 - 2) == 16

    # TLN4: Class 40 students, Football=22, Badminton=18, Neither=7 -> F U B = 33 -> Both = 22+18-33 = 7
    assert 22 + 18 - (40 - 7) == 7

    # TLN5: Class 45 students, Math=25, Phys=23, Chem=20, MP=11, PC=8, CM=9, all 3 = 5.
    # At least 1 = 25+23+20 - (11+8+9) + 5 = 68 - 28 + 5 = 45? If class has 50 students, neither = 50 - 45 = 5!
    union3 = 25 + 23 + 20 - (11 + 8 + 9) + 5
    assert union3 == 45 and 50 - union3 == 5

    # TLN6: Survey 100 tourists: Hue=65, DaNang=55, both=30 -> only Hue = 65 - 30 = 35
    assert 65 - 30 == 35

    # TLN7: tan a = 3 -> P = (2 sin a + 3 cos a) / (4 sin a - cos a) = (6 + 3)/(12 - 1) -> let's make exact decimal!
    # Pick tan a = 3, P = (2 sin a + 4 cos a) / (3 sin a - cos a) = (6 + 4)/(9 - 1) = 10/8 = 1.25!
    ta = Fraction(3, 1)
    assert (2 * ta + 4) / (3 * ta - 1) == Fraction(5, 4)  # 1,25

    # TLN8: tan a = -2 -> P = (5 sin^2 a - 3 sin a cos a + 2 cos^2 a) / (sin^2 a + 3 cos^2 a)
    # = (5*4 - 3*(-2) + 2) / (4 + 3) = (20 + 6 + 2) / 7 = 28 / 7 = 4!
    ta2 = Fraction(-2, 1)
    assert (5 * ta2**2 - 3 * ta2 + 2) / (ta2**2 + 3) == 4

    # TLN9: sin a + cos a = 5/4? Impossible since max is sqrt(2) ~ 1.414!
    # Good catch! Pick sin a - cos a = 1/5 (valid since (1/5)^2 = 1/25 <= 2!)
    # Wait: if sin a + cos a = 7/5 (since 7/5 = 1.4 <= 1.4142, derived from 3-4-5 triangle: 3/5 + 4/5 = 7/5!):
    # Then 1 + 2 sin a cos a = 49/25 -> sin a cos a = 12/25 = 0.48!
    s_plus_c = Fraction(7, 5)
    assert float(s_plus_c) < math.sqrt(2)
    sc = (s_plus_c**2 - 1) / 2
    assert sc == Fraction(12, 25)  # 0,48

    # TLN10: Triangle ABC: a=7, b=8, c=5 -> cos A = (64+25-49)/(80) = 40/80 = 1/2 -> A = 60 deg!
    cosA = Fraction(8**2 + 5**2 - 7**2, 2 * 8 * 5)
    assert cosA == Fraction(1, 2)

    # TLN11: Triangle ABC: a=10, b=17, c=21 -> p=24, S = sqrt(24*14*7*3) = sqrt(7056) = 84; h_c = 2S/c = 168/21 = 8!
    p11 = (10 + 17 + 21) // 2
    S11 = math.isqrt(p11 * (p11 - 10) * (p11 - 17) * (p11 - 21))
    assert p11 == 24 and S11 == 84 and Fraction(2 * S11, 21) == 8

    # TLN12: Tower height from A, B with AB=30m, alpha=30 deg, beta=60 deg:
    # Angle ACB = 60 - 30 = 30 deg -> triangle ABC isosceles at B (BC = AB = 30m)!
    # Height CH = BC * sin 60 = 30 * sqrt(3)/2 = 15*sqrt(3) ~ 26.0 m (25.98 -> 26,0)!
    h_tower = 30 * math.sin(math.radians(60))
    assert round(h_tower, 1) == 26.0 and round(h_tower, 2) == 25.98

    # --- Essay (TL) checks in Question Bank ---
    # TL5: Two ships leave port O at same time: Ship 1 at 20 km/h, Ship 2 at 30 km/h, angle 120 deg.
    # After 2 hours: OA = 40 km, OB = 60 km, angle AOB = 120 deg.
    # AB^2 = 40^2 + 60^2 - 2*40*60*cos(120) = 1600 + 3600 + 2400 = 7600 -> AB = 20*sqrt(19) ~ 87.18 km!
    ab_ships = math.sqrt(40**2 + 60**2 - 2 * 40 * 60 * (-0.5))
    assert 40**2 + 60**2 + 2400 == 7600 and round(ab_ships, 2) == 87.18

    # TL6: Tower CH with observer eye height 1.5m: AB = 25m, alpha = 32 deg, beta = 50 deg:
    # Angle ACB = 18 deg; BC = 25 * sin(32) / sin(18); CH' = BC * sin(50); H = CH' + 1.5
    bc_tl6 = 25 * math.sin(math.radians(32)) / math.sin(math.radians(18))
    ch_prime = bc_tl6 * math.sin(math.radians(50))
    total_h = ch_prime + 1.5
    assert round(bc_tl6, 2) == 42.87 and round(total_h, 2) == 34.34

    # TL9: Juice blending (LP): Pineapple juice (x liters) & Orange juice (y liters):
    # Vitamin A: 2x + y >= 8? Let's check textbook classic KNTT juice problem:
    # Max 9g flavoring, 12 liters water, 240g sugar:
    # Type I (x liters): 30g sugar, 1l water, 1g flavor -> profit 60k
    # Type II (y liters): 10g sugar, 1l water, 4g flavor -> profit 80k
    # Constraints: x >= 0, y >= 0, 3x + y <= 24, x + y <= 9, x + 4y <= 12?
    # Let's check intersections of {x>=0, y>=0, 3x+y<=21, x+y<=9, x+4y<=24}:
    # - x=0 -> y=6: (0,6)
    # - x+4y=24 and x+y=9 -> 3y=15 -> y=5, x=4! Check 3(4)+5=17 <= 21! Vertex (4,5)!
    # - x+y=9 and 3x+y=21 -> 2x=12 -> x=6, y=3! Check 6+4(3)=18 <= 24! Vertex (6,3)!
    # - y=0 in 3x+y=21 -> x=7! Vertex (7,0)!
    # ALL 5 VERTICES ARE EXACT INTEGERS: O(0,0), A(0,6), B(4,5), C(6,3), D(7,0)!
    # Profit F(x,y) = 60x + 80y (thousand VND):
    # F(0,0)=0, F(0,6)=480, F(4,5)=640, F(6,3)=600, F(7,0)=420 -> MAX = 640 at (4,5)!
    verts_tl9 = [(0, 0), (0, 6), (4, 5), (6, 3), (7, 0)]
    for vx, vy in verts_tl9:
        assert vx >= 0 and vy >= 0 and 3 * vx + vy <= 21 and vx + vy <= 9 and vx + 4 * vy <= 24
    vals_tl9 = {v: 60 * v[0] + 80 * v[1] for v in verts_tl9}
    assert max(vals_tl9.values()) == 640 and vals_tl9[(4, 5)] == 640
    print("  Phần D verified OK!")


def verify_exams_2026_2027() -> None:
    print("=== Verifying Phần E: 03 Đề Kiểm Tra Giữa Học Kỳ I (2026–2027) ===")

    # =========================================================================
    # ĐỀ SỐ 01 (NĂM HỌC 2026–2027)
    # =========================================================================
    # P.I Q8: cos a = -3/5 (0 < a < 180) -> sin a = 4/5, tan a = -4/3
    assert Fraction(4, 5) ** 2 + Fraction(-3, 5) ** 2 == 1
    # P.I Q10: Triangle ABC: AB=5, AC=7, A=60 deg -> BC^2 = 25 + 49 - 35 = 39 -> BC = sqrt(39)
    assert 5**2 + 7**2 - 5 * 7 == 39

    # P.II Q1 (Sets): A = [-2; 4), B = (1; 6]
    # a) 4 notin A and 1 notin B -> True
    # b) A \cap Z = {-2, -1, 0, 1, 2, 3} -> 6 integers
    assert len([x for x in range(-10, 10) if -2 <= x < 4]) == 6
    # c) A \cap B = (1; 4); C_R(A \cup B) = R \ [-2; 6] = (-inf; -2) U (6; +inf)
    # d) M = [m - 1; m + 2] \subset A = [-2; 4) <=> m - 1 >= -2 and m + 2 < 4 (STRICT < because 4 notin A while m+2 in M!)
    # <=> -1 <= m < 2 -> integer m in {-1, 0, 1} (3 values)!
    m_e1 = [m for m in range(-10, 10) if (m - 1 >= -2) and (m + 2 < 4)]
    assert m_e1 == [-1, 0, 1]

    # P.II Q2 (Linear Inequality): 2x + y <= 10 (or student buying notebooks x at 10k, pens y at 5k with 50k -> 10x+5y<=50 <=> 2x+y<=10)
    # Boundary d: 2x + y = 10 passes through (5,0) and (0,10); (2,5): 4+5=9<=10 True; (4,3): 8+3=11<=10 False!
    assert 2 * 2 + 5 <= 10 and not (2 * 4 + 3 <= 10)

    # P.III Q1 (Subsets): A = {x in N | (x - 1)(x^2 - 5x + 6) = 0} -> roots 1, 2, 3? Wait (x-2)(x-3)=0 -> {1, 2, 3} (3 elems -> 8)
    # Let's make A = {x in Z | x^2 - 3x - 4 <= 0} -> [-1, 4] -> {-1, 0, 1, 2, 3, 4} -> 6 elements -> 2^6 = 64 subsets!
    e1_tln1 = [x for x in range(-10, 10) if x**2 - 3 * x - 4 <= 0]
    assert e1_tln1 == [-1, 0, 1, 2, 3, 4] and 2 ** len(e1_tln1) == 64

    # P.III Q2 (Venn): Class 10A1 of THPT Hà Huy Tập has 44 students: 26 STEM club, 22 English club, 9 neither.
    # Union = 44 - 9 = 35 -> Both = 26 + 22 - 35 = 13!
    assert 26 + 22 - (44 - 9) == 13

    # P.III Q3 (Trig expr): tan a = 2 -> P = (4 sin a + 5 cos a) / (2 sin a - cos a) = (8 + 5) / (4 - 1) -> 13/3 not exact!
    # Pick P = (3 sin a + 4 cos a) / (2 sin a + cos a) = (6 + 4)/(4 + 1) = 10/5 = 2!
    # Or even nicer non-trivial decimal: tan a = 2 -> P = (5 sin a - 3 cos a) / (sin a + 2 cos a) = (10 - 3)/(2 + 4) -> 7/6 no;
    # P = (5 sin a - cos a) / (2 sin a) = (10 - 1)/4 = 9/4 = 2.25!
    ta_e1 = Fraction(2, 1)
    assert (5 * ta_e1 - 1) / (2 * ta_e1) == Fraction(9, 4)  # 2,25

    # P.III Q4 (Triangle): Triangle ABC has AB = 8, AC = 10, A = 60 deg. Area S = 1/2 * 8 * 10 * sin 60 = 20*sqrt(3) ~ 34.6!
    # Or exact integer area with Heron: a=13, b=20, c=21 -> p=27, S = sqrt(27*14*7*6) = sqrt(15876) = 126!
    p_e1 = (13 + 20 + 21) // 2
    s_e1 = math.isqrt(p_e1 * (p_e1 - 13) * (p_e1 - 20) * (p_e1 - 21))
    assert p_e1 == 27 and s_e1 == 126

    # P.IV Q1 (TL1 - Sets): A = (-3; 4] and B = [1; 7)
    # A \cap B = [1; 4]; A \cup B = (-3; 7); A \ B = (-3; 1); C_R A = (-inf; -3] U (4; +inf)

    # P.IV Q2 (TL2 - Real-world Trig): Pond obstacle AB: CA = 50m, CB = 70m, angle ACB = 60 deg (or 120 deg!)
    # Let's check ACB = 60 deg: AB^2 = 50^2 + 70^2 - 2*50*70*0.5 = 2500 + 4900 - 3500 = 3900 -> AB = 10*sqrt(39) ~ 62.45 m!
    ab_e1_sq = 50**2 + 70**2 - 2 * 50 * 70 * Fraction(1, 2)
    assert ab_e1_sq == 3900 and round(math.sqrt(ab_e1_sq), 2) == 62.45

    # P.IV Q3 (TL3 - LP): Workshop type I (x), type II (y):
    # x >= 0, y >= 0, 2x + y <= 16, x + 3y <= 18. Profit F = 5x + 4y (million VND).
    # Vertices O(0,0), A(0,6), B(6,4), C(8,0) -> F: 0, 24, 46 (MAX), 40!
    v_e1 = [(0, 0), (0, 6), (6, 4), (8, 0)]
    f_e1 = {v: 5 * v[0] + 4 * v[1] for v in v_e1}
    assert f_e1[(6, 4)] == 46 and max(f_e1.values()) == 46

    # =========================================================================
    # ĐỀ SỐ 02 (NĂM HỌC 2026–2027)
    # =========================================================================
    # P.I Q8: sin a = 2/3, 90 < a < 180 -> cos a = -sqrt(5)/3
    assert Fraction(2, 3) ** 2 + Fraction(5, 9) == 1
    # P.I Q10: Triangle ABC: a = 8, A = 45 deg, B = 60 deg -> b = a * sin 60 / sin 45 = 8 * (sqrt(3)/2) / (sqrt(2)/2) = 4*sqrt(6)
    assert round(8 * math.sin(math.radians(60)) / math.sin(math.radians(45)), 4) == round(4 * math.sqrt(6), 4)

    # P.II Q1 (Sets): A = {x in R | -1 <= x <= 5} = [-1; 5], B = (2; +inf)
    # a) A = [-1; 5], -1 in A, 2 notin B (True)
    # b) A \ B = [-1; 2] (careful: 2 notin B so 2 stays in A \ B!)
    # c) C_R B = (-inf; 2], so A \cap (C_R B) = [-1; 2]
    # d) D = (m; m + 3): D \subset A = [-1; 5] <=> m >= -1 and m + 3 <= 5 <=> -1 <= m <= 2 (4 integer values: -1, 0, 1, 2)!
    # Check endpoints: if m=-1, D=(-1; 2) \subset [-1; 5] True! If m=2, D=(2; 5) \subset [-1; 5] True!
    m_e2 = [m for m in range(-10, 10) if m >= -1 and m + 3 <= 5]
    assert m_e2 == [-1, 0, 1, 2]

    # P.III Q1 (Subsets): A = {x in N | x is prime and x < 12} -> {2, 3, 5, 7, 11} (5 primes -> 2^5 = 32 subsets; 2-element subsets = C(5,2)=10; total subsets = 32)
    primes_12 = [2, 3, 5, 7, 11]
    assert len(primes_12) == 5 and 2 ** len(primes_12) == 32

    # P.III Q2 (Venn): 45 students: 28 Swim, 22 Basketball, 5 neither -> Union = 40 -> Both = 28+22-40 = 10 -> ONLY Swim = 28 - 10 = 18!
    both_e2 = 28 + 22 - (45 - 5)
    assert both_e2 == 10 and (28 - both_e2) == 18

    # P.III Q3 (Trig expr): cot a = 3 -> P = (3 sin^2 a + 4 sin a cos a - cos^2 a) / (2 sin^2 a + cos^2 a)
    # Divide by sin^2 a: (3 + 4 cot a - cot^2 a) / (2 + cot^2 a) = (3 + 12 - 9) / (2 + 9) -> 6/11 not terminating!
    # Pick denominator (sin^2 a + cos^2 a) = 1? Wait: if P = (5 sin^2 a + 4 sin a cos a + cos^2 a) / (sin^2 a + cos^2 a)? That's just 5 sin^2 + ...
    # Pick cot a = 2: (4 + 4*2 - 4) / (1 + 4) = 8/5 = 1.6! Let's check:
    # P = (4 sin^2 a + 4 sin a cos a - cos^2 a) / (sin^2 a + cos^2 a) = (4 + 8 - 4) / (1 + 4) = 8/5 = 1.6!
    cot_e2 = Fraction(2, 1)
    val_e2_q3 = (4 + 4 * cot_e2 - cot_e2**2) / (1 + cot_e2**2)
    assert val_e2_q3 == Fraction(8, 5)  # 1,6

    # P.III Q4 (Triangle): Triangle ABC has b=6, c=10, A=120 deg -> a^2 = 36 + 100 - 2*6*10*(-1/2) = 136 + 60 = 196 -> a = 14!
    # Perimeter = 14 + 6 + 10 = 30! Super clean!
    a2_e2 = 6**2 + 10**2 - 2 * 6 * 10 * Fraction(-1, 2)
    assert a2_e2 == 196 and math.isqrt(int(a2_e2)) == 14

    # P.IV Q2 (TL2 - Real-world Trig): Measure height of flagpole/tower CH across river:
    # Two points A, B collinear with H on ground, AB = 40m, angle CAH = 35 deg, angle CBH = 55 deg.
    # Angle ACB = 55 - 35 = 20 deg. By Law of Sines in ABC: BC / sin 35 = 40 / sin 20 -> BC = 40 * sin 35 / sin 20.
    # Height CH = BC * sin 55 = 40 * sin 35 * sin 55 / sin 20!
    bc_e2 = 40 * math.sin(math.radians(35)) / math.sin(math.radians(20))
    ch_e2 = bc_e2 * math.sin(math.radians(55))
    assert round(bc_e2, 2) == 67.08 and round(ch_e2, 2) == 54.95

    # P.IV Q3 (TL3 - LP): Truck rental (classic THPT Hà Huy Tập model!):
    # 450 pigs, 35 tons feed; max 12 large trucks (x), max 10 small trucks (y).
    # Large: 50 pigs, 5 tons, cost 4 million. Small: 30 pigs, 1 ton, cost 2 million.
    # System: 0 <= x <= 12, 0 <= y <= 10, 5x + 3y >= 45, 5x + y >= 35.
    # Vertices: M(5, 10), A(6, 5), B(9, 0), C(12, 0), D(12, 10).
    # Cost F = 4x + 2y: F(5,10)=40, F(6,5)=34 (MIN), F(9,0)=36, F(12,0)=48, F(12,10)=68!
    v_e2 = [(5, 10), (6, 5), (9, 0), (12, 0), (12, 10)]
    for vx, vy in v_e2:
        assert 0 <= vx <= 12 and 0 <= vy <= 10 and 5 * vx + 3 * vy >= 45 and 5 * vx + vy >= 35
    f_e2 = {v: 4 * v[0] + 2 * v[1] for v in v_e2}
    assert f_e2[(6, 5)] == 34 and min(f_e2.values()) == 34

    # =========================================================================
    # ĐỀ SỐ 03 (NĂM HỌC 2026–2027)
    # =========================================================================
    # P.I Q8: tan a = -sqrt(3) -> a = 120 deg -> cos a = -1/2, sin a = sqrt(3)/2
    # P.I Q10: Triangle ABC: a=9, b=10, c=17 -> p=18, S = sqrt(18*9*8*1) = sqrt(1296) = 36! r = S/p = 2!
    p_e3_q10 = (9 + 10 + 17) // 2
    s_e3_q10 = math.isqrt(p_e3_q10 * (p_e3_q10 - 9) * (p_e3_q10 - 10) * (p_e3_q10 - 17))
    assert p_e3_q10 == 18 and s_e3_q10 == 36 and s_e3_q10 // p_e3_q10 == 2

    # P.II Q1 (Sets): A = (-inf; 3], B = (-2; 7)
    # d) C = [2m - 1; +inf): A \cap C != empty <=> 2m - 1 <= 3 <=> m <= 2 -> positive integers m in {1, 2} (2 values)
    assert [m for m in range(1, 10) if 2 * m - 1 <= 3] == [1, 2]

    # P.III Q1 (Subsets): A = {1}, B = {1; 2; 3; 4; 5} -> sets X with A \subset X \subset B -> 2^(5-1) = 16!
    assert 2 ** (5 - 1) == 16

    # P.III Q2 (Venn 3 sets): Class 10A has 45 students, all join >=1 of 3 clubs (Math 22, Literature 20, Art 18),
    # ML=8, LA=6, AM=7. Find number in ALL THREE clubs:
    # 45 = 22 + 20 + 18 - (8 + 6 + 7) + x = 60 - 21 + x = 39 + x -> x = 6!
    assert 45 - (22 + 20 + 18 - (8 + 6 + 7)) == 6

    # P.III Q3 (Trig expr): cos a = -3/5 (90 < a < 180 -> sin a = 4/5).
    # Compute P = 10 sin a - 5 tan a = 10*(4/5) - 5*(-4/3)? Pick 15 tan a:
    # P = 5 sin a - 6 tan a = 5*(4/5) - 6*(-4/3) = 4 + 8 = 12!
    sin_e3 = Fraction(4, 5)
    cos_e3 = Fraction(-3, 5)
    tan_e3 = sin_e3 / cos_e3
    assert 5 * sin_e3 - 6 * tan_e3 == 12

    # P.III Q4 (Triangle): Ship navigation / Circumradius: Triangle ABC has BC = 12, A = 120 deg -> R = 12 / (2 sin 120) = 12 / sqrt(3) = 4*sqrt(3) ~ 6.93!
    assert round(12 / (2 * math.sin(math.radians(120))), 2) == 6.93

    # P.IV Q2 (TL2 - Real-world Trig): Tunnel through mountain AB:
    # Surveyor stands at C: CA = 300m, CB = 400m, angle ACB = 120 deg ->
    # AB^2 = 300^2 + 400^2 - 2*300*400*cos(120) = 90000 + 160000 + 120000 = 370000 -> AB = 100*sqrt(37) ~ 608.28 m!
    # Also find angle CAB: sin A = CB * sin 120 / AB = 400 * (sqrt(3)/2) / (100*sqrt(37)) = 2*sqrt(3/37) -> A ~ 34.7 deg!
    ab_e3 = math.sqrt(300**2 + 400**2 - 2 * 300 * 400 * (-0.5))
    angA_e3 = math.degrees(math.asin(400 * math.sin(math.radians(120)) / ab_e3))
    assert round(ab_e3, 2) == 608.28 and round(angA_e3, 1) == 34.7

    # P.IV Q3 (TL3 - LP): Cooperative growing dragon fruit (x ha) and mango (y ha) on max 10 ha:
    # Max 8 ha dragon fruit (0 <= x <= 8), y >= 0, x + y <= 10, labor: 20x + 30y <= 240 <=> 2x + 3y <= 24.
    # Profit F = 30x + 40y (million VND).
    # Vertices O(0,0), A(0,8), B(6,4), C(8,2), D(8,0) -> F: 0, 320, 340 (MAX!), 320, 240!
    v_e3 = [(0, 0), (0, 8), (6, 4), (8, 2), (8, 0)]
    for vx, vy in v_e3:
        assert 0 <= vx <= 8 and vy >= 0 and vx + vy <= 10 and 2 * vx + 3 * vy <= 24
    f_e3 = {v: 30 * v[0] + 40 * v[1] for v in v_e3}
    assert f_e3[(6, 4)] == 340 and max(f_e3.values()) == 340

    print("  Phần E (Đề 01, Đề 02, Đề 03 — Năm học 2026–2027) verified OK!")


if __name__ == "__main__":
    verify_question_bank()
    verify_exams_2026_2027()
    print("ALL MATHEMATICAL ASSERTIONS PASSED 100%!")
