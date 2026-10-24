"""Kiểm tra độc lập các phép tính trọng yếu; không thay thế rà soát sư phạm."""
from pathlib import Path
import re
import unittest
from itertools import combinations
from sympy import (S, Interval, FiniteSet, Union, Rational as Q, sqrt, sin, cos,
                   tan, pi, simplify, symbols, solve)

ROOT = Path(__file__).resolve().parents[1]
x, y = symbols('x y')
def area(a,b,c):
    p = Q(a+b+c,2)
    return sqrt(p*(p-a)*(p-b)*(p-c))
def vertices(constraints):
    """constraints: (a,b,c) biểu thị ax+by <= c, gồm cả không âm."""
    found = set()
    for (a,b,c),(d,e,f) in combinations(constraints,2):
        if a*e-b*d == 0:
            continue
        sol = solve([a*x+b*y-c,d*x+e*y-f],(x,y))
        pt = (sol[x],sol[y])
        if all(A*pt[0]+B*pt[1]<=C for A,B,C in constraints):
            found.add(pt)
    return found

class MathChecks(unittest.TestCase):
    def eq(self,a,b): self.assertEqual(simplify(a-b),0)
    def test_logic(self):
        for P in (False,True):
            for T in (False,True):
                self.assertEqual(not(P and not T), (not P) or T)
                self.assertEqual(P==T,((not P) or T) and ((not T) or P))
        self.assertLess(Q(1,2)**2,Q(1,2)) # B04
        self.assertEqual(3%3,0); self.assertNotEqual(3%6,0) # B03
    def test_set_intervals_examples_and_exam(self):
        A=Interval(-2,3,right_open=True);B=Interval(1,5,left_open=True)
        self.assertEqual(A&B,Interval.open(1,3))
        self.assertEqual(A|B,Interval(-2,5))
        self.assertEqual(A-B,Interval(-2,1))
        self.assertEqual(B-A,Interval(3,5))
        self.assertEqual(S.Reals-A,Union(Interval.open(-S.Infinity,-2),Interval(3,S.Infinity)))
        A=Interval(-3,2,right_open=True);B=Interval(0,5)
        self.assertEqual(A&B,Interval(0,2,right_open=True))
        self.assertEqual(A|B,Interval(-3,5))
        self.assertEqual(S.Reals-A,Union(Interval.open(-S.Infinity,-3),Interval(2,S.Infinity)))
    def test_set_practice(self):
        self.assertEqual([n for n in range(-5,5) if -3<=n<2],[-3,-2,-1,0,1])
        self.assertEqual(2**5,32);self.assertEqual(2**5-2,30)
        A=Interval(-S.Infinity,2);B=Interval.open(-1,5)
        self.assertEqual(A&B,Interval(-1,2,left_open=True))
        self.assertEqual(A|B,Interval.open(-S.Infinity,5))
        self.assertEqual(A-B,Interval(-S.Infinity,-1))
        self.assertEqual(B-A,Interval.open(2,5))
        U=FiniteSet(1,2,3,4,5,6);A=FiniteSet(1,2,4);B=FiniteSet(2,3,4)
        self.assertEqual(A&B,FiniteSet(2,4));self.assertEqual(A|B,FiniteSet(1,2,3,4))
        self.assertEqual(U-A,FiniteSet(3,5,6))
        self.assertEqual(22+18-7,33); self.assertEqual(40-33,7)
        self.assertEqual(30+28-50,8);self.assertEqual(30-8,22)
        both=20+17-(36-5);self.assertEqual(both,6);self.assertEqual(36-5-both,25)
        both=Q(24+19-31,2);self.assertEqual(both,6);self.assertEqual(24+19-both,37)
    def test_linear_regions(self):
        cons=[(-1,0,0),(0,-1,0),(1,1,6),(2,1,8)]
        self.assertEqual(vertices(cons),{(0,0),(4,0),(2,4),(0,6)})
        self.assertEqual(max(3*a+2*b for a,b in vertices(cons)),14)
        cons=[(-1,0,0),(0,-1,0),(1,1,5),(1,0,3)]
        self.assertEqual(vertices(cons),{(0,0),(3,0),(3,2),(0,5)})
        self.assertEqual(max(2*a+b for a,b in vertices(cons)),8)
    def test_optimization_practice(self):
        cons=[(-1,0,0),(0,-1,0),(2,1,8),(1,2,10)]
        self.assertEqual(vertices(cons),{(0,0),(4,0),(2,4),(0,5)})
        best=max((300*a+400*b,a,b) for a in range(9) for b in range(11)
                 if 2*a+b<=8 and a+2*b<=10)
        self.assertEqual(best,(2200,2,4))
    def test_optimization_exam(self):
        cons=[(-1,0,0),(0,-1,0),(2,1,12),(1,2,12)]
        self.assertEqual(vertices(cons),{(0,0),(6,0),(4,4),(0,6)})
        self.assertEqual(max(500*a+400*b for a,b in vertices(cons)),3600)
        best=max((500*a+400*b,a,b) for a in range(13) for b in range(13)
                 if 2*a+b<=12 and a+2*b<=12)
        self.assertEqual(best,(3600,4,4))
    def test_trigonometry(self):
        self.eq(sin(150*pi/180),Q(1,2));self.eq(cos(120*pi/180),-Q(1,2))
        self.eq(tan(135*pi/180),-1)
        self.eq(sqrt(1-Q(5,13)**2),Q(12,13))
        self.eq(Q(12,13)/(-Q(5,13)),-Q(12,5))
        self.eq((Q(4,5)+2*(-Q(3,5)))/(2*Q(4,5)-(-Q(3,5))),-Q(2,11))
        self.eq((3*2-1)/Q(2+1),Q(5,3))
        # L1: -10; exam III.3 deliberately uses fresh data and gives 11.
        self.eq((2*Q(3,5)+Q(4,5))/(Q(3,5)-Q(4,5)),-10)
        self.eq((2*Q(4,5)+Q(3,5))/(Q(4,5)-Q(3,5)),11)
    def test_triangles(self):
        self.eq(sqrt(5**2+8**2-2*5*8*cos(pi/3)),7)
        self.eq(5*8*sin(pi/3)/2,10*sqrt(3))
        self.eq(7/(2*sin(pi/3)),7*sqrt(3)/3)
        self.eq(area(13,14,15),84);self.eq(Q(84,21),4)
        self.eq(Q(13*14*15,4*84),Q(65,8))
        self.eq(sqrt(6**2+8**2-2*6*8*cos(pi/3)),2*sqrt(13))
        self.eq(6*8*sin(pi/3)/2,12*sqrt(3))
        self.eq(10*sin(pi/4)/sin(pi/6),10*sqrt(2))
        self.eq(area(5,5,6),12);self.eq(Q(12,8),Q(3,2))
        self.eq(Q(5*5*6,4*12),Q(25,8));self.eq(area(10,10,12),48)
        self.assertEqual(round(float(80*sin(pi/3)/sin(75*pi/180)),1),71.7)
        self.assertEqual(round(float(40*tan(35*pi/180)+Q(3,2)),1),29.5)
        ac=100*sin(75*pi/180)/sin(pi/3)
        self.assertEqual(round(float(ac),1),111.5)
        self.assertEqual(round(float(ac*sin(pi/4)),1),78.9)
        self.assertEqual(round(float(60*sin(75*pi/180)/sin(pi/3)),1),66.9)
    def test_exam_answers_and_points(self):
        self.assertEqual(2**5-1,31);self.assertEqual(25+21-(42-6),10)
        self.eq(sqrt(3**2+4**2-2*3*4*cos(pi/3)),sqrt(13))
        self.assertTrue(2*2+3<=8)
        self.assertTrue(all(2*a+b==8 for a,b in [(4,0),(0,8)]))
        f={0:0,1:Q(1,10),2:Q(1,4),3:Q(1,2),4:1}
        self.eq(12*Q(1,4)+2*f[4]+4*Q(1,2)+3,10)
        self.eq(10*Q(1,4)+f[3]+f[4]+3*Q(1,2)+Q(9,4),Q(31,4))
    def test_document_structure(self):
        src=(ROOT/'tai-lieu/de-cuong.typ').read_text()
        exam=src.split('= 13. Đề minh họa 90 phút',1)[1].split('= 14. Đáp án',1)[0]
        for section,total in [('I',12),('II',2),('III',4),('IV',3)]:
            matches=re.findall(r'\*'+section+r'\.(\d+)(?:\.\*| ·)',exam)
            self.assertEqual([int(n) for n in matches],list(range(1,total+1)))
        self.assertEqual(len(re.findall(r'\*[abcd]\)\*',exam)),8)
        for i in range(1,29):
            tag=f'B{i:02d}'
            self.assertRegex(src,rf'\*{tag} ·') # bài tập
            self.assertIn(f'*{tag}.*',src) # lời giải
        self.assertNotIn('s q r t',src)
        self.assertIn('không chứa đề thi hoặc đáp án gốc',src)

if __name__=='__main__': unittest.main(verbosity=2)
