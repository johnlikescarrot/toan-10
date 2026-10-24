#!/usr/bin/env python3
"""Generate textbook-grade vector SVG illustrations & coordinate plots for Grade 10 Math (Kết nối tri thức)."""
import os

OUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src", "assets")
os.makedirs(OUT_DIR, exist_ok=True)

FONT = "Be Vietnam Pro, DejaVu Sans, sans-serif"

# ==============================================================================
# 1. Venn Diagrams & Counting Principle (Mục 1.3 - Câu 4 TN & Câu 2 TLN)
# ==============================================================================
venn_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 225" width="760" height="225" font-family="{FONT}">
  <rect x="0" y="0" width="760" height="225" rx="10" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.2"/>
  <text x="380" y="22" text-anchor="middle" font-size="12.5" font-weight="700" fill="#0F172A">4 PHÉP TOÁN TẬP HỢP TRÊN BIỂU ĐỒ VEN &amp; CÔNG THỨC ĐẾM THỰC TẾ (MỤC 1.3)</text>

  <!-- Card 1: Intersection A ∩ B -->
  <rect x="12" y="32" width="140" height="182" rx="8" fill="#FFFFFF" stroke="#93C5FD" stroke-width="1.2"/>
  <rect x="12" y="32" width="140" height="24" rx="8" fill="#DBEAFE"/>
  <text x="82" y="48" text-anchor="middle" font-size="10.5" font-weight="700" fill="#1E40AF">1. GIAO: A ∩ B</text>
  <circle cx="66" cy="102" r="28" fill="#EFF6FF" stroke="#2563EB" stroke-width="1.6"/>
  <circle cx="98" cy="102" r="28" fill="#EFF6FF" stroke="#0D9488" stroke-width="1.6"/>
  <!-- Lens intersection -->
  <path d="M 82 78.6 A 28 28 0 0 1 82 125.4 A 28 28 0 0 1 82 78.6 Z" fill="#3B82F6" fill-opacity="0.78" stroke="#1D4ED8" stroke-width="1.2"/>
  <text x="50" y="106" font-size="10" font-weight="700" fill="#1E40AF">A</text>
  <text x="108" y="106" font-size="10" font-weight="700" fill="#0F766E">B</text>
  <text x="82" y="148" text-anchor="middle" font-size="9.2" font-weight="700" fill="#0F172A">x ∈ A  VÀ  x ∈ B</text>
  <text x="82" y="164" text-anchor="middle" font-size="8.6" fill="#475569">Phần chung của A và B</text>
  <text x="82" y="182" text-anchor="middle" font-size="8.5" font-weight="600" fill="#1D4ED8">Từ khóa: “và”, “đồng thời”,</text>
  <text x="82" y="195" text-anchor="middle" font-size="8.5" font-weight="600" fill="#1D4ED8">“giỏi cả 2 môn”</text>

  <!-- Card 2: Union A ∪ B -->
  <rect x="162" y="32" width="140" height="182" rx="8" fill="#FFFFFF" stroke="#5EEAD4" stroke-width="1.2"/>
  <rect x="162" y="32" width="140" height="24" rx="8" fill="#CCFBF1"/>
  <text x="232" y="48" text-anchor="middle" font-size="10.5" font-weight="700" fill="#0F766E">2. HỢP: A ∪ B</text>
  <circle cx="216" cy="102" r="28" fill="#14B8A6" fill-opacity="0.65" stroke="#0F766E" stroke-width="1.6"/>
  <circle cx="248" cy="102" r="28" fill="#14B8A6" fill-opacity="0.65" stroke="#0F766E" stroke-width="1.6"/>
  <text x="200" y="106" font-size="10" font-weight="700" fill="#0F172A">A</text>
  <text x="258" y="106" font-size="10" font-weight="700" fill="#0F172A">B</text>
  <text x="232" y="148" text-anchor="middle" font-size="9.2" font-weight="700" fill="#0F172A">x ∈ A  HOẶC  x ∈ B</text>
  <text x="232" y="164" text-anchor="middle" font-size="8.6" fill="#475569">Gộp tất cả phần tử A, B</text>
  <text x="232" y="182" text-anchor="middle" font-size="8.5" font-weight="600" fill="#0F766E">Từ khóa: “hoặc”, “ít nhất</text>
  <text x="232" y="195" text-anchor="middle" font-size="8.5" font-weight="600" fill="#0F766E">một trong hai môn”</text>

  <!-- Card 3: Difference A \ B -->
  <rect x="312" y="32" width="140" height="182" rx="8" fill="#FFFFFF" stroke="#FCD34D" stroke-width="1.2"/>
  <rect x="312" y="32" width="140" height="24" rx="8" fill="#FEF3C7"/>
  <text x="382" y="48" text-anchor="middle" font-size="10.5" font-weight="700" fill="#92400E">3. HIỆU: A \\ B</text>
  <circle cx="366" cy="102" r="28" fill="#F59E0B" fill-opacity="0.72" stroke="#B45309" stroke-width="1.6"/>
  <circle cx="398" cy="102" r="28" fill="#FFFFFF" stroke="#64748B" stroke-width="1.6"/>
  <circle cx="366" cy="102" r="28" fill="none" stroke="#B45309" stroke-width="1.6"/>
  <text x="350" y="106" font-size="10" font-weight="700" fill="#78350F">A</text>
  <text x="408" y="106" font-size="10" font-weight="700" fill="#475569">B</text>
  <text x="382" y="148" text-anchor="middle" font-size="9.2" font-weight="700" fill="#0F172A">x ∈ A  NHƯNG  x ∉ B</text>
  <text x="382" y="164" text-anchor="middle" font-size="8.6" fill="#475569">Thuộc riêng A, bỏ phần B</text>
  <text x="382" y="182" text-anchor="middle" font-size="8.5" font-weight="600" fill="#B45309">Từ khóa: “chỉ thuộc A”,</text>
  <text x="382" y="195" text-anchor="middle" font-size="8.5" font-weight="600" fill="#B45309">“chỉ giỏi đúng môn A”</text>

  <!-- Card 4: Complement C_E A -->
  <rect x="462" y="32" width="136" height="182" rx="8" fill="#FFFFFF" stroke="#FCA5A5" stroke-width="1.2"/>
  <rect x="462" y="32" width="136" height="24" rx="8" fill="#FEE2E2"/>
  <text x="530" y="48" text-anchor="middle" font-size="10.5" font-weight="700" fill="#991B1B">4. PHẦN BÙ: C_E(A)</text>
  <ellipse cx="530" cy="102" rx="46" ry="30" fill="#EF4444" fill-opacity="0.55" stroke="#991B1B" stroke-width="1.6"/>
  <circle cx="530" cy="102" r="16" fill="#FFFFFF" stroke="#1E293B" stroke-width="1.5"/>
  <text x="530" y="106" text-anchor="middle" font-size="9.5" font-weight="700" fill="#0F172A">A</text>
  <text x="494" y="88" font-size="9.5" font-weight="700" fill="#7F1D1D">E</text>
  <text x="530" y="148" text-anchor="middle" font-size="9.2" font-weight="700" fill="#0F172A">C_E(A) = E \\ A (A ⊂ E)</text>
  <text x="530" y="164" text-anchor="middle" font-size="8.6" fill="#475569">Phần của E nằm ngoài A</text>
  <text x="530" y="182" text-anchor="middle" font-size="8.5" font-weight="600" fill="#DC2626">Trên trục số ℝ:</text>
  <text x="530" y="195" text-anchor="middle" font-size="8.5" font-weight="600" fill="#DC2626">C_ℝ(A) = ℝ \\ A</text>

  <!-- Card 5: Inclusion-Exclusion Formula -->
  <rect x="608" y="32" width="140" height="182" rx="8" fill="#1E293B" stroke="#334155" stroke-width="1.2"/>
  <text x="678" y="50" text-anchor="middle" font-size="10" font-weight="700" fill="#FACC15">CÔNG THỨC ĐẾM VEN</text>
  <line x1="618" y1="56" x2="738" y2="56" stroke="#475569" stroke-width="1"/>
  <text x="678" y="73" text-anchor="middle" font-size="8.8" font-weight="700" fill="#93C5FD">• Hai tập hợp A, B:</text>
  <text x="678" y="88" text-anchor="middle" font-size="8.8" font-weight="700" fill="#FFFFFF">n(A∪B) = n(A)+n(B)−n(A∩B)</text>
  <text x="678" y="105" text-anchor="middle" font-size="8.3" fill="#6EE7B7">Chỉ riêng A: n(A\\B)=n(A)−n(A∩B)</text>
  <text x="678" y="120" text-anchor="middle" font-size="8.3" fill="#FCD34D">Cả lớp E (có k em không</text>
  <text x="678" y="132" text-anchor="middle" font-size="8.3" fill="#FCD34D">tham gia môn nào):</text>
  <text x="678" y="146" text-anchor="middle" font-size="8.8" font-weight="700" fill="#FFFFFF">n(E) = n(A∪B) + k</text>
  <line x1="618" y1="154" x2="738" y2="154" stroke="#475569" stroke-width="1"/>
  <text x="678" y="169" text-anchor="middle" font-size="8.6" font-weight="700" fill="#FCA5A5">• Số tập con của A (n phần tử):</text>
  <text x="678" y="184" text-anchor="middle" font-size="9.2" font-weight="700" fill="#FACC15">Tổng số tập con = 2ⁿ</text>
  <text x="678" y="198" text-anchor="middle" font-size="8.2" fill="#E2E8F0">Khác ∅: 2ⁿ − 1 | Thực sự: 2ⁿ − 1</text>
</svg>
"""

# ==============================================================================
# 2. Number Line Intervals & Operations (Mục 1.2 & 1.3 - Câu 1 ĐS & Câu 1 TL)
# ==============================================================================
number_line_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 220" width="760" height="220" font-family="{FONT}">
  <defs>
    <marker id="arrAxis" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="#0F172A"/>
    </marker>
  </defs>
  <rect x="0" y="0" width="760" height="220" rx="10" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.2"/>
  <text x="380" y="22" text-anchor="middle" font-size="12.5" font-weight="700" fill="#0F172A">MINH HỌA PHÉP TOÁN TẬP HỢP TRÊN TRỤC SỐ: A = [−3; 4) VÀ B = (1; 6] (CÂU 1 TỰ LUẬN)</text>

  <!-- Set A = [-3; 4) -->
  <text x="18" y="56" font-size="10.5" font-weight="700" fill="#1D4ED8">Tập A = [−3; 4):</text>
  <line x1="145" y1="52" x2="725" y2="52" stroke="#94A3B8" stroke-width="1.5" marker-end="url(#arrAxis)"/>
  <!-- Hatched outside -->
  <line x1="145" y1="52" x2="250" y2="52" stroke="#CBD5E1" stroke-width="6"/>
  <line x1="510" y1="52" x2="715" y2="52" stroke="#CBD5E1" stroke-width="6"/>
  <!-- Active segment [-3; 4) -->
  <line x1="250" y1="52" x2="510" y2="52" stroke="#2563EB" stroke-width="4.5"/>
  <text x="250" y="56" text-anchor="middle" font-size="14" font-weight="800" fill="#1D4ED8">[</text>
  <text x="510" y="56" text-anchor="middle" font-size="14" font-weight="800" fill="#1D4ED8">)</text>
  <text x="250" y="40" text-anchor="middle" font-size="9.5" font-weight="700" fill="#1D4ED8">−3</text>
  <text x="510" y="40" text-anchor="middle" font-size="9.5" font-weight="700" fill="#1D4ED8">4</text>
  <text x="155" y="40" font-size="9" fill="#64748B">−∞</text>
  <text x="710" y="40" font-size="9" fill="#64748B">+∞</text>

  <!-- Set B = (1; 6] -->
  <text x="18" y="96" font-size="10.5" font-weight="700" fill="#0F766E">Tập B = (1; 6]:</text>
  <line x1="145" y1="92" x2="725" y2="92" stroke="#94A3B8" stroke-width="1.5" marker-end="url(#arrAxis)"/>
  <line x1="145" y1="92" x2="398" y2="92" stroke="#CBD5E1" stroke-width="6"/>
  <line x1="585" y1="92" x2="715" y2="92" stroke="#CBD5E1" stroke-width="6"/>
  <line x1="398" y1="92" x2="585" y2="92" stroke="#0D9488" stroke-width="4.5"/>
  <text x="398" y="96" text-anchor="middle" font-size="14" font-weight="800" fill="#0F766E">(</text>
  <text x="585" y="96" text-anchor="middle" font-size="14" font-weight="800" fill="#0F766E">]</text>
  <text x="398" y="80" text-anchor="middle" font-size="9.5" font-weight="700" fill="#0F766E">1</text>
  <text x="585" y="80" text-anchor="middle" font-size="9.5" font-weight="700" fill="#0F766E">6</text>

  <!-- Guide dashed vertical lines -->
  <line x1="250" y1="52" x2="250" y2="175" stroke="#94A3B8" stroke-width="1" stroke-dasharray="3,3"/>
  <line x1="398" y1="92" x2="398" y2="175" stroke="#94A3B8" stroke-width="1" stroke-dasharray="3,3"/>
  <line x1="510" y1="52" x2="510" y2="175" stroke="#94A3B8" stroke-width="1" stroke-dasharray="3,3"/>
  <line x1="585" y1="92" x2="585" y2="175" stroke="#94A3B8" stroke-width="1" stroke-dasharray="3,3"/>

  <!-- Intersection A ∩ B = (1; 4) -->
  <text x="18" y="136" font-size="10.5" font-weight="700" fill="#DC2626">Giao A ∩ B = (1; 4):</text>
  <line x1="145" y1="132" x2="725" y2="132" stroke="#94A3B8" stroke-width="1.5" marker-end="url(#arrAxis)"/>
  <line x1="398" y1="132" x2="510" y2="132" stroke="#DC2626" stroke-width="5"/>
  <text x="398" y="136" text-anchor="middle" font-size="14" font-weight="800" fill="#DC2626">(</text>
  <text x="510" y="136" text-anchor="middle" font-size="14" font-weight="800" fill="#DC2626">)</text>
  <text x="454" y="122" text-anchor="middle" font-size="9" font-weight="700" fill="#DC2626">Phần thuộc CẢ 2 trục</text>

  <!-- Summary results bottom bar -->
  <rect x="14" y="156" width="732" height="52" rx="7" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.1"/>
  <text x="28" y="175" font-size="9.8" font-weight="700" fill="#1E40AF">• Hợp: A ∪ B = [−3; 6]</text>
  <text x="195" y="175" font-size="9.8" font-weight="700" fill="#B45309">• Hiệu: A \\ B = [−3; 1]  (Vì 1 ∉ B nên 1 CÒN LẠI trong A \\ B → ngoặc vuông [−3; 1]!)</text>
  <text x="28" y="196" font-size="9.2" font-weight="700" fill="#0F766E">• Hiệu: B \\ A = [4; 6]  (Vì 4 ∉ A nên 4 còn lại trong B \\ A)</text>
  <text x="342" y="196" font-size="9.0" font-weight="700" fill="#DC2626">• Phần bù: C_ℝ(A) = ℝ \\ A = (−∞; −3) ∪ [4; +∞)  (Đổi [ ↔ ( tại biên!)</text>
</svg>
"""

# ==============================================================================
# 3. Linear Inequality & System of Inequalities in 2 Variables (Mục 2.1 & 2.2)
# ==============================================================================
ineq_plane_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 240" width="760" height="240" font-family="{FONT}">
  <defs>
    <marker id="arrAx" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="#0F172A"/>
    </marker>
    <pattern id="hatchRed" width="8" height="8" patternTransform="rotate(45 0 0)" patternUnits="userSpaceOnUse">
      <line x1="0" y1="0" x2="0" y2="8" stroke="#FCA5A5" stroke-width="2"/>
    </pattern>
  </defs>
  <rect x="0" y="0" width="760" height="240" rx="10" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.2"/>

  <!-- Left Panel: Single BPT 2x + y <= 4 -->
  <rect x="12" y="12" width="360" height="216" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
  <text x="192" y="30" text-anchor="middle" font-size="11" font-weight="700" fill="#0F172A">A. Miền nghiệm BPT: 2x + y ≤ 4 (Mục 2.1)</text>

  <!-- Shaded discarded half-plane (2x + y > 4) -->
  <polygon points="105,42 290,42 290,205 225,205" fill="url(#hatchRed)"/>
  <!-- Feasible half-plane (2x + y <= 4) -->
  <polygon points="40,42 105,42 225,205 40,205" fill="#DBEAFE" fill-opacity="0.45"/>

  <!-- Axes: O at (125, 165), scale: 1 unit = 30px -->
  <!-- Line 2x + y = 4 passes through (0,4)->(125, 45) and (2,0)->(185, 165) -->
  <line x1="40" y1="165" x2="295" y2="165" stroke="#0F172A" stroke-width="1.5" marker-end="url(#arrAx)"/>
  <line x1="125" y1="210" x2="125" y2="40" stroke="#0F172A" stroke-width="1.5" marker-end="url(#arrAx)"/>
  <!-- Boundary line d: 2x + y = 4 through (105, 5) clipped to (125,45) and (185,165) -> slope dy/dx = 120/60 = 2 -->
  <line x1="120" y1="35" x2="205" y2="205" stroke="#1D4ED8" stroke-width="2.5"/>

  <circle cx="125" cy="165" r="3.5" fill="#DC2626"/>
  <circle cx="125" cy="45" r="3.5" fill="#1D4ED8"/>
  <circle cx="185" cy="165" r="3.5" fill="#1D4ED8"/>
  <text x="86" y="179" font-size="9.5" font-weight="700" fill="#DC2626">O(0;0)</text>
  <text x="84" y="48" font-size="9.5" font-weight="700" fill="#1D4ED8">B(0;4)</text>
  <text x="186" y="180" font-size="9.5" font-weight="700" fill="#1D4ED8">A(2;0)</text>
  <text x="285" y="179" font-size="10" font-weight="700" fill="#0F172A">x</text>
  <text x="112" y="46" font-size="10" font-weight="700" fill="#0F172A">y</text>

  <text x="78" y="120" text-anchor="middle" font-size="9.5" font-weight="700" fill="#1E40AF">MIỀN NGHIỆM</text>
  <text x="78" y="133" text-anchor="middle" font-size="8.5" fill="#1E40AF">(Không bị gạch,</text>
  <text x="78" y="145" text-anchor="middle" font-size="8.5" fill="#1E40AF">chứa O, kể cả bờ d)</text>

  <rect x="210" y="52" width="152" height="100" rx="6" fill="#F8FAFC" stroke="#93C5FD" stroke-width="1"/>
  <text x="286" y="68" text-anchor="middle" font-size="9.2" font-weight="700" fill="#1E40AF">Quy trình 3 bước chuẩn:</text>
  <text x="218" y="84" font-size="8.5" fill="#0F172A">B1: Vẽ bờ d: 2x + y = 4</text>
  <text x="218" y="96" font-size="8.5" fill="#475569">qua A(2;0) và B(0;4).</text>
  <text x="218" y="111" font-size="8.5" fill="#0F172A">B2: Thử O(0;0): 2·0+0 = 0 ≤ 4</text>
  <text x="218" y="123" font-size="8.5" font-weight="700" fill="#0F766E">→ ĐÚNG (chứa gốc O).</text>
  <text x="218" y="138" font-size="8.5" fill="#DC2626">B3: Gạch bỏ nửa không chứa O.</text>

  <!-- Right Panel: Reading BPT from Graph & Boundary Rules -->
  <rect x="386" y="12" width="362" height="216" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
  <text x="567" y="30" text-anchor="middle" font-size="11" font-weight="700" fill="#0F172A">B. Mẹo Đọc Nhanh Phương Trình Đường Bờ &amp; Dấu BPT</text>

  <rect x="400" y="42" width="334" height="54" rx="6" fill="#EFF6FF" stroke="#93C5FD" stroke-width="1"/>
  <text x="410" y="59" font-size="9.5" font-weight="700" fill="#1E40AF">1. Công thức đoạn chắn (cực nhanh cho Trắc nghiệm &amp; Đúng/Sai):</text>
  <text x="410" y="75" font-size="9" fill="#0F172A">Đường thẳng d cắt Ox tại A(a; 0) và cắt Oy tại B(0; b) (a, b ≠ 0) có PT:</text>
  <text x="567" y="90" text-anchor="middle" font-size="10" font-weight="700" fill="#DC2626">x / a  +  y / b  =  1</text>

  <rect x="400" y="104" width="334" height="54" rx="6" fill="#F0FDFA" stroke="#5EEAD4" stroke-width="1"/>
  <text x="410" y="121" font-size="9.5" font-weight="700" fill="#0F766E">2. Phân biệt KỂ CẢ BỜ vs KHÔNG KỂ BỜ:</text>
  <text x="410" y="137" font-size="9" fill="#0F172A">• BPT có dấu  ≤  hoặc  ≥  ↔  Tính cả đường bờ d (vẽ nét liền).</text>
  <text x="410" y="151" font-size="9" fill="#0F172A">• BPT có dấu  &lt;  hoặc  &gt;  ↔  Không tính đường bờ d (vẽ nét đứt).</text>

  <rect x="400" y="166" width="334" height="52" rx="6" fill="#FFFBEB" stroke="#FCD34D" stroke-width="1"/>
  <text x="410" y="183" font-size="9.5" font-weight="700" fill="#B45309">3. Cảnh báo khi đường bờ d ĐI QUA GỐC O(0; 0) (c = 0):</text>
  <text x="410" y="198" font-size="9" fill="#0F172A">Khi ax + by ≤ 0 (đi qua O), KHÔNG thử O(0;0)! Hãy lấy điểm</text>
  <text x="410" y="211" font-size="9" font-weight="700" fill="#92400E">M(1; 0) hoặc N(0; 1) không nằm trên d để thử dấu!</text>
</svg>
"""

# ==============================================================================
# 4. Linear Programming Polygon (Mục 2.2 - Câu 3 Tự luận VDC)
# ==============================================================================
lp_poly_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 235" width="760" height="235" font-family="{FONT}">
  <defs>
    <marker id="arrLP" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="#0F172A"/>
    </marker>
  </defs>
  <rect x="0" y="0" width="760" height="235" rx="10" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.2"/>
  <text x="380" y="22" text-anchor="middle" font-size="12.5" font-weight="700" fill="#0F172A">MÔ HÌNH BÀI TOÁN TỐI ƯU HỆ BPT BẬC NHẤT HAI ẨN (CÂU 3 TỰ LUẬN VDC — 1,0 ĐIỂM)</text>

  <!-- Left Coordinate Plot: O(60, 195), scale: 1 unit = 18px -->
  <!-- System: x >= 0, y >= 0, x + 2y <= 8, 3x + y <= 9 -->
  <!-- Vertices: O(0,0)->(60,195); A(3,0)->(114,195); B(2,3)->(96,141); C(0,4)->(60,123) -->
  <!-- Wait let's make scale larger: 1 unit = 32px! O(65, 198):
       C(0,4) -> (65, 70)
       B(2,3) -> (129, 102)
       A(3,0) -> (161, 198) -->
  <rect x="14" y="32" width="320" height="190" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
  <!-- Feasible Polygon OABC -->
  <polygon points="65,198 161,198 129,102 65,70" fill="#CCFBF1" stroke="#0D9488" stroke-width="2"/>
  <!-- Line d1: x + 2y = 8 through (0,4)->(65,70) and (8,0)->(321,198) -->
  <line x1="50" y1="62.5" x2="290" y2="182.5" stroke="#2563EB" stroke-width="1.8"/>
  <!-- Line d2: 3x + y = 9 through (1,6)->(97,6)->clip at (110,45) and (3,0)->(161,198) -->
  <line x1="110" y1="45" x2="166" y2="213" stroke="#DC2626" stroke-width="1.8"/>

  <!-- Axes -->
  <line x1="35" y1="198" x2="310" y2="198" stroke="#0F172A" stroke-width="1.6" marker-end="url(#arrLP)"/>
  <line x1="65" y1="215" x2="65" y2="38" stroke="#0F172A" stroke-width="1.6" marker-end="url(#arrLP)"/>

  <!-- Dashed coords for B(2; 3) -->
  <line x1="129" y1="102" x2="129" y2="198" stroke="#64748B" stroke-width="1" stroke-dasharray="3,3"/>
  <line x1="65" y1="102" x2="129" y2="102" stroke="#64748B" stroke-width="1" stroke-dasharray="3,3"/>

  <!-- Vertices dots -->
  <circle cx="65" cy="198" r="4" fill="#0F172A"/>
  <circle cx="161" cy="198" r="4" fill="#DC2626"/>
  <circle cx="129" cy="102" r="4.5" fill="#B91C1C"/>
  <circle cx="65" cy="70" r="4" fill="#2563EB"/>

  <text x="48" y="212" font-size="9.5" font-weight="700" fill="#0F172A">O(0;0)</text>
  <text x="155" y="213" font-size="9.5" font-weight="700" fill="#DC2626">A(3;0)</text>
  <text x="136" y="100" font-size="10" font-weight="700" fill="#B91C1C">B(2;3) ★ Đỉnh tối ưu</text>
  <text x="28" y="74" font-size="9.5" font-weight="700" fill="#2563EB">C(0;4)</text>
  <text x="125" y="212" font-size="8.8" fill="#475569">2</text>
  <text x="52" y="105" font-size="8.8" fill="#475569">3</text>
  <text x="86" y="155" font-size="9.5" font-weight="700" fill="#0F766E">Miền</text>
  <text x="86" y="168" font-size="9.5" font-weight="700" fill="#0F766E">OABC</text>
  <text x="225" y="142" font-size="8.8" font-weight="600" fill="#2563EB">d₁: x + 2y = 8</text>
  <text x="152" y="65" font-size="8.8" font-weight="600" fill="#DC2626">d₂: 3x + y = 9</text>

  <!-- Right Panel: 4-Step Method to Get Full 1.0 Point -->
  <rect x="348" y="32" width="398" height="190" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
  <text x="547" y="50" text-anchor="middle" font-size="11" font-weight="700" fill="#1E40AF">QUY TRÌNH 4 BƯỚC ĂN TRỌN 1,0 ĐIỂM CÂU 3 TỰ LUẬN</text>
  <line x1="360" y1="57" x2="734" y2="57" stroke="#E2E8F0" stroke-width="1"/>

  <text x="360" y="75" font-size="9.3" font-weight="700" fill="#0F172A">• Bước 1 (0,25 đ) — Gọi ẩn &amp; Lập hệ BPT + Hàm mục tiêu:</text>
  <text x="368" y="90" font-size="8.8" fill="#334155">Gọi x, y (x ≥ 0, y ≥ 0) là số lượng cần tìm. Từ định mức nguyên liệu/thời gian</text>
  <text x="368" y="102" font-size="8.8" fill="#334155">lập hệ BPT bậc nhất hai ẩn và biểu thức lợi nhuận/chi phí F(x; y) = ax + by.</text>

  <text x="360" y="121" font-size="9.3" font-weight="700" fill="#0F766E">• Bước 2 (0,25 đ) — Biểu diễn miền nghiệm &amp; Tìm tọa độ các đỉnh:</text>
  <text x="368" y="136" font-size="8.8" fill="#334155">Vẽ các đường thẳng bờ trên Oxy. Miền nghiệm là miền đa giác lồi OABC.</text>
  <text x="368" y="148" font-size="8.8" fill="#334155">Giải hệ PT giao điểm các đường bờ để tìm tọa độ các đỉnh: O(0;0), A(3;0), B(2;3), C(0;4).</text>

  <text x="360" y="167" font-size="9.3" font-weight="700" fill="#B45309">• Bước 3 (0,25 đ) — Tính giá trị F(x; y) tại từng đỉnh đa giác:</text>
  <text x="368" y="182" font-size="8.8" fill="#334155">VD với F(x; y) = 4x + 3y: F(O) = 0; F(A) = 12; F(B) = 4·2 + 3·3 = 17; F(C) = 12.</text>

  <text x="360" y="201" font-size="9.3" font-weight="700" fill="#DC2626">• Bước 4 (0,25 đ) — So sánh &amp; Kết luận thực tế:</text>
  <text x="368" y="215" font-size="8.8" font-weight="700" fill="#991B1B">Giá trị lớn nhất F_max = 17 đạt tại đỉnh B(2; 3) (kiểm tra x, y nguyên nếu đề yêu cầu).</text>
</svg>
"""

# ==============================================================================
# 5. Unit Semicircle & Trig Identities (Mục 3.1 - Câu 7, 8 TN & Câu 3 TLN)
# ==============================================================================
trig_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 230" width="760" height="230" font-family="{FONT}">
  <defs>
    <marker id="arrTr" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="#0F172A"/>
    </marker>
  </defs>
  <rect x="0" y="0" width="760" height="230" rx="10" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.2"/>
  <text x="380" y="22" text-anchor="middle" font-size="12.5" font-weight="700" fill="#0F172A">NỬA ĐƯỜNG TRÒN ĐƠN VỊ (0° → 180°) &amp; DẤU GIÁ TRỊ LƯỢNG GIÁC (MỤC 3.1)</text>

  <!-- Left Panel: Semicircle centered at O(195, 175), radius R = 115 -->
  <rect x="12" y="32" width="366" height="186" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
  <!-- Axes -->
  <line x1="45" y1="175" x2="345" y2="175" stroke="#0F172A" stroke-width="1.5" marker-end="url(#arrTr)"/>
  <line x1="195" y1="202" x2="195" y2="42" stroke="#0F172A" stroke-width="1.5" marker-end="url(#arrTr)"/>
  <!-- Semicircle R=115 from (80, 175) to (310, 175) -->
  <path d="M 80 175 A 115 115 0 0 1 310 175" fill="#EFF6FF" fill-opacity="0.45" stroke="#1D4ED8" stroke-width="2.2"/>

  <!-- Point M at 50 deg: x = 195 + 115*cos(50)=269, y = 175 - 115*sin(50)=87 -->
  <!-- Point M' at 130 deg: x = 195 - 74 = 121, y = 87 -->
  <line x1="195" y1="175" x2="269" y2="87" stroke="#DC2626" stroke-width="2.2"/>
  <line x1="195" y1="175" x2="121" y2="87" stroke="#0D9488" stroke-width="2.2" stroke-dasharray="4,3"/>
  <line x1="121" y1="87" x2="269" y2="87" stroke="#64748B" stroke-width="1.2" stroke-dasharray="3,3"/>
  <line x1="269" y1="87" x2="269" y2="175" stroke="#DC2626" stroke-width="1.2" stroke-dasharray="3,3"/>
  <line x1="121" y1="87" x2="121" y2="175" stroke="#0D9488" stroke-width="1.2" stroke-dasharray="3,3"/>

  <!-- Angle arc alpha -->
  <path d="M 225 175 A 30 30 0 0 0 214 152" fill="none" stroke="#DC2626" stroke-width="1.6"/>
  <text x="232" y="164" font-size="10" font-weight="700" fill="#DC2626">α</text>
  <text x="152" y="148" font-size="9" font-weight="700" fill="#0F766E">180°−α</text>

  <circle cx="269" cy="87" r="4" fill="#DC2626"/>
  <circle cx="121" cy="87" r="4" fill="#0D9488"/>
  <text x="275" y="83" font-size="9.5" font-weight="700" fill="#DC2626">M(x₀; y₀)</text>
  <text x="58" y="83" font-size="9.5" font-weight="700" fill="#0F766E">M'(−x₀; y₀)</text>
  <text x="200" y="83" font-size="9" font-weight="700" fill="#1E40AF">y₀ = sin α &gt; 0</text>
  <text x="248" y="190" font-size="8.8" font-weight="700" fill="#DC2626">x₀ = cos α</text>
  <text x="112" y="190" font-size="8.8" font-weight="700" fill="#0F766E">−cos α</text>
  <text x="312" y="190" font-size="9" font-weight="700" fill="#0F172A">A(1;0) [0°]</text>
  <text x="24" y="168" font-size="8.6" font-weight="700" fill="#0F172A">A'(−1;0) [180°]</text>
  <text x="202" y="55" font-size="9" font-weight="700" fill="#0F172A">B(0;1) [90°]</text>
  <text x="186" y="190" font-size="9.5" font-weight="700" fill="#0F172A">O</text>

  <!-- Right Panel: Sign Table & Supplementary/Complementary Rules -->
  <rect x="390" y="32" width="358" height="186" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
  <text x="569" y="50" text-anchor="middle" font-size="11" font-weight="700" fill="#0F172A">BẢNG XÉT DẤU (CÂU 8 TN) &amp; HAI GÓC BÙ NHAU / PHỤ NHAU</text>

  <!-- Sign mini-table -->
  <rect x="404" y="58" width="330" height="62" rx="5" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1"/>
  <line x1="404" y1="78" x2="734" y2="78" stroke="#CBD5E1" stroke-width="1"/>
  <line x1="404" y1="99" x2="734" y2="99" stroke="#CBD5E1" stroke-width="1"/>
  <line x1="534" y1="58" x2="534" y2="120" stroke="#CBD5E1" stroke-width="1"/>
  <line x1="584" y1="58" x2="584" y2="120" stroke="#CBD5E1" stroke-width="1"/>
  <line x1="634" y1="58" x2="634" y2="120" stroke="#CBD5E1" stroke-width="1"/>
  <line x1="684" y1="58" x2="684" y2="120" stroke="#CBD5E1" stroke-width="1"/>

  <text x="469" y="72" text-anchor="middle" font-size="9" font-weight="700" fill="#0F172A">Loại góc α</text>
  <text x="559" y="72" text-anchor="middle" font-size="9" font-weight="700" fill="#1E40AF">sin α</text>
  <text x="609" y="72" text-anchor="middle" font-size="9" font-weight="700" fill="#1E40AF">cos α</text>
  <text x="659" y="72" text-anchor="middle" font-size="9" font-weight="700" fill="#1E40AF">tan α</text>
  <text x="709" y="72" text-anchor="middle" font-size="9" font-weight="700" fill="#1E40AF">cot α</text>

  <text x="469" y="92" text-anchor="middle" font-size="8.8" font-weight="600" fill="#0F766E">Góc nhọn (0° &lt; α &lt; 90°)</text>
  <text x="559" y="92" text-anchor="middle" font-size="10" font-weight="800" fill="#0F766E">+</text>
  <text x="609" y="92" text-anchor="middle" font-size="10" font-weight="800" fill="#0F766E">+</text>
  <text x="659" y="92" text-anchor="middle" font-size="10" font-weight="800" fill="#0F766E">+</text>
  <text x="709" y="92" text-anchor="middle" font-size="10" font-weight="800" fill="#0F766E">+</text>

  <text x="469" y="113" text-anchor="middle" font-size="8.8" font-weight="600" fill="#DC2626">Góc tù (90° &lt; α &lt; 180°)</text>
  <text x="559" y="113" text-anchor="middle" font-size="10" font-weight="800" fill="#0F766E">+</text>
  <text x="609" y="113" text-anchor="middle" font-size="10" font-weight="800" fill="#DC2626">−</text>
  <text x="659" y="113" text-anchor="middle" font-size="10" font-weight="800" fill="#DC2626">−</text>
  <text x="709" y="113" text-anchor="middle" font-size="10" font-weight="800" fill="#DC2626">−</text>

  <!-- Supplementary & Complementary boxes -->
  <rect x="404" y="128" width="160" height="80" rx="6" fill="#FEF2F2" stroke="#FCA5A5" stroke-width="1"/>
  <text x="484" y="143" text-anchor="middle" font-size="9.2" font-weight="700" fill="#991B1B">HAI GÓC BÙ NHAU (180° − α)</text>
  <text x="484" y="157" text-anchor="middle" font-size="8.6" font-weight="700" fill="#0F766E">sin(180° − α) = +sin α</text>
  <text x="484" y="171" text-anchor="middle" font-size="8.6" font-weight="700" fill="#DC2626">cos(180° − α) = −cos α</text>
  <text x="484" y="185" text-anchor="middle" font-size="8.6" fill="#DC2626">tan(180° − α) = −tan α</text>
  <text x="484" y="199" text-anchor="middle" font-size="8.6" fill="#DC2626">cot(180° − α) = −cot α</text>

  <rect x="574" y="128" width="160" height="80" rx="6" fill="#EFF6FF" stroke="#93C5FD" stroke-width="1"/>
  <text x="654" y="143" text-anchor="middle" font-size="9.2" font-weight="700" fill="#1E40AF">HAI GÓC PHỤ NHAU (90° − α)</text>
  <text x="654" y="157" text-anchor="middle" font-size="8.6" font-weight="700" fill="#1D4ED8">sin(90° − α) = cos α</text>
  <text x="654" y="171" text-anchor="middle" font-size="8.6" font-weight="700" fill="#1D4ED8">cos(90° − α) = sin α</text>
  <text x="654" y="185" text-anchor="middle" font-size="8.6" fill="#1D4ED8">tan(90° − α) = cot α</text>
  <text x="654" y="199" text-anchor="middle" font-size="8.6" fill="#1D4ED8">cot(90° − α) = tan α</text>
</svg>
"""

# ==============================================================================
# 6. Triangle Relations & Practical Surveying (Mục 3.2 - Câu 9, 10 TN, Câu 4 TLN & Câu 2 TL)
# ==============================================================================
triangle_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 230" width="760" height="230" font-family="{FONT}">
  <rect x="0" y="0" width="760" height="230" rx="10" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.2"/>
  <text x="380" y="22" text-anchor="middle" font-size="12.5" font-weight="700" fill="#0F172A">HỆ THỨC LƯỢNG TRONG TAM GIÁC &amp; 2 BÀI TOÁN ĐO ĐẠC THỰC TẾ (CÂU 2 TỰ LUẬN)</text>

  <!-- Panel 1: Standard Triangle ABC -->
  <rect x="12" y="32" width="240" height="186" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
  <text x="132" y="49" text-anchor="middle" font-size="10.2" font-weight="700" fill="#1E40AF">1. Tam giác ABC &amp; Các kí hiệu chuẩn</text>
  <!-- Triangle A(115, 65), B(35, 165), C(220, 165) -->
  <polygon points="115,65 35,165 220,165" fill="#EFF6FF" fill-opacity="0.55" stroke="#1D4ED8" stroke-width="2"/>
  <!-- Altitude AH at x=115, y=165; Median AM to M(127.5, 165) -->
  <line x1="115" y1="65" x2="115" y2="165" stroke="#DC2626" stroke-width="1.5" stroke-dasharray="3,3"/>
  <line x1="115" y1="65" x2="132" y2="165" stroke="#0D9488" stroke-width="1.6"/>
  <rect x="115" y="157" width="8" height="8" fill="none" stroke="#DC2626" stroke-width="1"/>

  <text x="115" y="59" text-anchor="middle" font-size="10" font-weight="700" fill="#0F172A">A</text>
  <text x="23" y="170" font-size="10" font-weight="700" fill="#0F172A">B</text>
  <text x="226" y="170" font-size="10" font-weight="700" fill="#0F172A">C</text>
  <text x="112" y="178" font-size="9" font-weight="700" fill="#DC2626">H</text>
  <text x="132" y="178" font-size="9" font-weight="700" fill="#0F766E">M</text>
  <text x="64" y="112" font-size="9.5" font-weight="700" fill="#1D4ED8">c</text>
  <text x="176" y="112" font-size="9.5" font-weight="700" fill="#1D4ED8">b</text>
  <text x="180" y="178" font-size="9.5" font-weight="700" fill="#1D4ED8">a = BC</text>
  <text x="98" y="122" font-size="8.8" font-weight="700" fill="#DC2626">h_a</text>
  <text x="135" y="122" font-size="8.8" font-weight="700" fill="#0F766E">m_a</text>

  <text x="132" y="195" text-anchor="middle" font-size="8.6" font-weight="700" fill="#0F172A">a² = b² + c² − 2bc·cos A (ĐL Côsin)</text>
  <text x="132" y="209" text-anchor="middle" font-size="8.6" font-weight="700" fill="#DC2626">a/sin A = b/sin B = c/sin C = 2R</text>

  <!-- Panel 2: Distance across a lake (Law of Cosines) -->
  <rect x="262" y="32" width="240" height="186" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
  <text x="382" y="49" text-anchor="middle" font-size="10.2" font-weight="700" fill="#0F766E">2. Đo khoảng cách AB qua hồ nước</text>
  <!-- Lake blob between A(315, 76) and B(465, 86) -->
  <ellipse cx="392" cy="88" rx="58" ry="24" fill="#BAE6FD" stroke="#0284C7" stroke-width="1.3"/>
  <text x="392" y="92" text-anchor="middle" font-size="8.8" font-weight="700" fill="#0369A1">Hồ nước / Vật cản</text>
  <!-- Point C(365, 168) on shore -->
  <line x1="365" y1="168" x2="315" y2="76" stroke="#0F766E" stroke-width="2"/>
  <line x1="365" y1="168" x2="465" y2="86" stroke="#0F766E" stroke-width="2"/>
  <line x1="315" y1="76" x2="465" y2="86" stroke="#DC2626" stroke-width="2.2" stroke-dasharray="5,3"/>
  <circle cx="315" cy="76" r="4" fill="#DC2626"/>
  <circle cx="465" cy="86" r="4" fill="#DC2626"/>
  <circle cx="365" cy="168" r="4" fill="#0F172A"/>
  <text x="298" y="75" font-size="9.5" font-weight="700" fill="#DC2626">A</text>
  <text x="473" y="88" font-size="9.5" font-weight="700" fill="#DC2626">B</text>
  <text x="365" y="182" text-anchor="middle" font-size="9.5" font-weight="700" fill="#0F172A">C (Điểm ngắm)</text>
  <text x="322" y="132" font-size="8.8" font-weight="700" fill="#0F766E">b = CA</text>
  <text x="426" y="138" font-size="8.8" font-weight="700" fill="#0F766E">a = CB</text>
  <text x="372" y="148" font-size="9" font-weight="700" fill="#B45309">γ</text>
  <text x="382" y="196" text-anchor="middle" font-size="8.5" fill="#334155">Đo CA = b, CB = a và góc ACB = γ:</text>
  <text x="382" y="210" text-anchor="middle" font-size="8.8" font-weight="700" fill="#DC2626">AB = √(a² + b² − 2ab·cos γ)</text>

  <!-- Panel 3: Measuring Tower Height from 2 points -->
  <rect x="512" y="32" width="236" height="186" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
  <text x="630" y="49" text-anchor="middle" font-size="10.2" font-weight="700" fill="#B45309">3. Đo chiều cao tháp CH từ 2 điểm A, B</text>
  <!-- Ground line from A(530, 165) -> B(605, 165) -> H(695, 165), top C(695, 65) -->
  <line x1="524" y1="165" x2="725" y2="165" stroke="#475569" stroke-width="1.8"/>
  <!-- Tower CH -->
  <line x1="695" y1="165" x2="695" y2="65" stroke="#DC2626" stroke-width="3.2"/>
  <rect x="687" y="157" width="8" height="8" fill="none" stroke="#0F172A" stroke-width="1"/>
  <!-- Sight lines CA and CB -->
  <line x1="535" y1="165" x2="695" y2="65" stroke="#2563EB" stroke-width="1.6"/>
  <line x1="610" y1="165" x2="695" y2="65" stroke="#0D9488" stroke-width="1.8"/>

  <circle cx="535" cy="165" r="3.5" fill="#2563EB"/>
  <circle cx="610" cy="165" r="3.5" fill="#0D9488"/>
  <circle cx="695" cy="65" r="4" fill="#DC2626"/>
  <text x="535" y="179" text-anchor="middle" font-size="9.5" font-weight="700" fill="#2563EB">A</text>
  <text x="610" y="179" text-anchor="middle" font-size="9.5" font-weight="700" fill="#0F766E">B</text>
  <text x="695" y="179" text-anchor="middle" font-size="9.5" font-weight="700" fill="#0F172A">H</text>
  <text x="695" y="59" text-anchor="middle" font-size="9.5" font-weight="700" fill="#DC2626">C (Đỉnh)</text>
  <text x="562" y="161" font-size="8.8" font-weight="700" fill="#2563EB">α</text>
  <text x="632" y="161" font-size="8.8" font-weight="700" fill="#0F766E">β</text>
  <text x="572" y="178" text-anchor="middle" font-size="8.5" font-weight="700" fill="#B45309">d = AB</text>
  <text x="712" y="118" font-size="9.5" font-weight="700" fill="#DC2626">h</text>

  <text x="630" y="195" text-anchor="middle" font-size="8.4" fill="#334155">ĐL Sin trong ΔABC: BC = d·sin α / sin(β−α)</text>
  <text x="630" y="209" text-anchor="middle" font-size="8.6" font-weight="700" fill="#DC2626">h = CH = BC·sin β = d·sin α·sin β / sin(β−α)</text>
</svg>
"""

# ==============================================================================
# 7. Vector Concepts & Regular Hexagon / Parallelogram (Mục 4.1 - Câu 11, 12 TN)
# ==============================================================================
vector_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 220" width="760" height="220" font-family="{FONT}">
  <defs>
    <marker id="arrVBlue" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="#2563EB"/>
    </marker>
    <marker id="arrVRed" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="#DC2626"/>
    </marker>
    <marker id="arrVTeal" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="#0D9488"/>
    </marker>
  </defs>
  <rect x="0" y="0" width="760" height="220" rx="10" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.2"/>
  <text x="380" y="22" text-anchor="middle" font-size="12.5" font-weight="700" fill="#0F172A">KHÁI NIỆM VECTƠ, HAI VECTƠ CÙNG PHƯƠNG &amp; HAI VECTƠ BẰNG NHAU (MỤC 4.1)</text>

  <!-- Panel 1: Collinear, Same/Opposite Direction -->
  <rect x="12" y="32" width="236" height="176" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
  <text x="130" y="49" text-anchor="middle" font-size="10.2" font-weight="700" fill="#1E40AF">1. Giá, Cùng phương &amp; Cùng hướng</text>
  <!-- Carrier lines -->
  <line x1="26" y1="78" x2="232" y2="78" stroke="#CBD5E1" stroke-width="1.2" stroke-dasharray="4,3"/>
  <line x1="48" y1="78" x2="148" y2="78" stroke="#2563EB" stroke-width="2.8" marker-end="url(#arrVBlue)"/>
  <text x="98" y="70" text-anchor="middle" font-size="9.5" font-weight="700" fill="#1D4ED8">Vectơ a (gốc A, ngọn B)</text>

  <line x1="26" y1="112" x2="232" y2="112" stroke="#CBD5E1" stroke-width="1.2" stroke-dasharray="4,3"/>
  <line x1="48" y1="112" x2="148" y2="112" stroke="#0D9488" stroke-width="2.8" marker-end="url(#arrVTeal)"/>
  <text x="98" y="104" text-anchor="middle" font-size="9.5" font-weight="700" fill="#0F766E">Vectơ b = a (cùng hướng &amp; |b|=|a|)</text>

  <line x1="26" y1="146" x2="232" y2="146" stroke="#CBD5E1" stroke-width="1.2" stroke-dasharray="4,3"/>
  <line x1="188" y1="146" x2="68" y2="146" stroke="#DC2626" stroke-width="2.8" marker-end="url(#arrVRed)"/>
  <text x="128" y="138" text-anchor="middle" font-size="9.5" font-weight="700" fill="#DC2626">Vectơ c ngược hướng với a, b</text>

  <rect x="22" y="164" width="216" height="36" rx="5" fill="#FEF3C7"/>
  <text x="130" y="178" text-anchor="middle" font-size="8.6" font-weight="700" fill="#92400E">★ Quy ước: Vectơ-không (0) cùng phương</text>
  <text x="130" y="192" text-anchor="middle" font-size="8.6" font-weight="700" fill="#92400E">và CÙNG HƯỚNG với mọi vectơ!</text>

  <!-- Panel 2: Parallelogram ABCD -->
  <rect x="258" y="32" width="236" height="176" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
  <text x="376" y="49" text-anchor="middle" font-size="10.2" font-weight="700" fill="#0F766E">2. Hình bình hành ABCD tâm O</text>
  <!-- A(300, 74), B(450, 74), C(420, 146), D(270, 146), O(360, 110) -->
  <polygon points="300,74 450,74 420,146 270,146" fill="#F0FDFA" stroke="#94A3B8" stroke-width="1.5"/>
  <line x1="300" y1="74" x2="420" y2="146" stroke="#CBD5E1" stroke-width="1.2" stroke-dasharray="3,3"/>
  <line x1="270" y1="146" x2="450" y2="74" stroke="#CBD5E1" stroke-width="1.2" stroke-dasharray="3,3"/>
  <!-- Vector AB and DC -->
  <line x1="300" y1="74" x2="447" y2="74" stroke="#2563EB" stroke-width="2.6" marker-end="url(#arrVBlue)"/>
  <line x1="270" y1="146" x2="417" y2="146" stroke="#2563EB" stroke-width="2.6" marker-end="url(#arrVBlue)"/>
  <circle cx="360" cy="110" r="3.5" fill="#DC2626"/>
  <text x="290" y="70" font-size="9.5" font-weight="700" fill="#0F172A">A</text>
  <text x="455" y="70" font-size="9.5" font-weight="700" fill="#0F172A">B</text>
  <text x="426" y="154" font-size="9.5" font-weight="700" fill="#0F172A">C</text>
  <text x="256" y="154" font-size="9.5" font-weight="700" fill="#0F172A">D</text>
  <text x="360" y="103" text-anchor="middle" font-size="9" font-weight="700" fill="#DC2626">O</text>

  <text x="376" y="170" text-anchor="middle" font-size="8.8" font-weight="700" fill="#1E40AF">• AB = DC (chú ý thứ tự đỉnh! AB ≠ CD)</text>
  <text x="376" y="184" text-anchor="middle" font-size="8.8" font-weight="700" fill="#0F766E">• AD = BC ;  BA = CD ;  AO = OC ;  DO = OB</text>
  <text x="376" y="198" text-anchor="middle" font-size="8.5" fill="#DC2626">• OA và OC đối nhau (cùng độ dài, ngược hướng)</text>

  <!-- Panel 3: Regular Hexagon ABCDEF center O -->
  <rect x="504" y="32" width="244" height="176" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
  <text x="626" y="49" text-anchor="middle" font-size="10.2" font-weight="700" fill="#B45309">3. Lục giác đều ABCDEF tâm O (Câu 12 TN)</text>
  <!-- Center O(626, 108), R=44:
       A(604, 70), B(648, 70), C(670, 108), D(648, 146), E(604, 146), F(582, 108) -->
  <polygon points="604,70 648,70 670,108 648,146 604,146 582,108" fill="#FFFBEB" stroke="#D97706" stroke-width="1.6"/>
  <line x1="604" y1="70" x2="648" y2="146" stroke="#CBD5E1" stroke-width="1" stroke-dasharray="3,2"/>
  <line x1="648" y1="70" x2="604" y2="146" stroke="#CBD5E1" stroke-width="1" stroke-dasharray="3,2"/>
  <line x1="582" y1="108" x2="670" y2="108" stroke="#CBD5E1" stroke-width="1" stroke-dasharray="3,2"/>
  <!-- Highlight equal vectors to AB: FO, OC, ED -->
  <line x1="604" y1="70" x2="645" y2="70" stroke="#DC2626" stroke-width="2.5" marker-end="url(#arrVRed)"/>
  <line x1="582" y1="108" x2="623" y2="108" stroke="#2563EB" stroke-width="2.2" marker-end="url(#arrVBlue)"/>
  <line x1="626" y1="108" x2="667" y2="108" stroke="#2563EB" stroke-width="2.2" marker-end="url(#arrVBlue)"/>
  <line x1="604" y1="146" x2="645" y2="146" stroke="#2563EB" stroke-width="2.2" marker-end="url(#arrVBlue)"/>
  <circle cx="626" cy="108" r="3" fill="#0F172A"/>
  <text x="595" y="66" font-size="8.8" font-weight="700" fill="#DC2626">A</text>
  <text x="651" y="66" font-size="8.8" font-weight="700" fill="#DC2626">B</text>
  <text x="675" y="111" font-size="8.8" font-weight="700" fill="#0F172A">C</text>
  <text x="652" y="156" font-size="8.8" font-weight="700" fill="#0F172A">D</text>
  <text x="594" y="156" font-size="8.8" font-weight="700" fill="#0F172A">E</text>
  <text x="570" y="111" font-size="8.8" font-weight="700" fill="#0F172A">F</text>
  <text x="626" y="102" text-anchor="middle" font-size="8.5" font-weight="700" fill="#0F172A">O</text>

  <text x="626" y="172" text-anchor="middle" font-size="8.6" font-weight="700" fill="#DC2626">• Có 3 vectơ bằng AB là: FO, OC, ED</text>
  <text x="626" y="186" text-anchor="middle" font-size="8.5" fill="#1E40AF">• Có 9 vectơ (≠ 0) cùng phương với AB:</text>
  <text x="626" y="199" text-anchor="middle" font-size="8.2" fill="#475569">BA, FO, OF, OC, CO, FC, CF, ED, DE</text>
</svg>
"""

# ==============================================================================
# 8. True/False Question Bank Graph (graph_ds_bpt1.svg)
# ==============================================================================
# Line d passes through A(3; 0) and B(0; 2) -> 2x + 3y = 6. Unshaded region contains O(0;0): 2x + 3y <= 6
graph_ds_bpt1_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 210" width="420" height="210" font-family="{FONT}">
  <defs>
    <marker id="arrDS" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="#0F172A"/>
    </marker>
    <pattern id="hatchDS" width="8" height="8" patternTransform="rotate(45 0 0)" patternUnits="userSpaceOnUse">
      <line x1="0" y1="0" x2="0" y2="8" stroke="#FCA5A5" stroke-width="2.2"/>
    </pattern>
  </defs>
  <rect x="0" y="0" width="420" height="210" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.2"/>
  <!-- Origin O(110, 155), scale 1 unit = 40px: A(3,0)->(230,155), B(0,2)->(110,75) -->
  <!-- Line d through (35, 25) and (305, 205) -->
  <!-- Discarded upper-right region (2x + 3y > 6) -->
  <polygon points="35,25 360,25 360,200 297.5,200" fill="url(#hatchDS)"/>
  <!-- Feasible lower-left region -->
  <polygon points="25,25 35,25 297.5,200 25,200" fill="#EFF6FF" fill-opacity="0.45"/>

  <line x1="25" y1="155" x2="365" y2="155" stroke="#0F172A" stroke-width="1.6" marker-end="url(#arrDS)"/>
  <line x1="110" y1="200" x2="110" y2="20" stroke="#0F172A" stroke-width="1.6" marker-end="url(#arrDS)"/>
  <line x1="35" y1="25" x2="297.5" y2="200" stroke="#1D4ED8" stroke-width="2.5"/>

  <circle cx="110" cy="155" r="3.5" fill="#0F172A"/>
  <circle cx="230" cy="155" r="4" fill="#DC2626"/>
  <circle cx="110" cy="75" r="4" fill="#DC2626"/>
  <circle cx="150" cy="115" r="3.5" fill="#0F766E"/>
  <line x1="150" y1="115" x2="150" y2="155" stroke="#0F766E" stroke-width="1" stroke-dasharray="3,3"/>
  <line x1="110" y1="115" x2="150" y2="115" stroke="#0F766E" stroke-width="1" stroke-dasharray="3,3"/>

  <text x="95" y="170" font-size="10" font-weight="700" fill="#0F172A">O</text>
  <text x="225" y="172" font-size="10" font-weight="700" fill="#DC2626">3</text>
  <text x="234" y="148" font-size="9.5" font-weight="700" fill="#DC2626">A(3;0)</text>
  <text x="98" y="83" font-size="9.5" font-weight="700" fill="#DC2626">2</text>
  <text x="58" y="72" font-size="9.5" font-weight="700" fill="#DC2626">B(0;2)</text>
  <text x="156" y="113" font-size="9" font-weight="700" fill="#0F766E">M(1;1)</text>
  <text x="355" y="170" font-size="10.5" font-weight="700" fill="#0F172A">x</text>
  <text x="95" y="28" font-size="10.5" font-weight="700" fill="#0F172A">y</text>
  <text x="245" y="65" font-size="9.5" font-weight="700" fill="#991B1B">Phần gạch bỏ</text>
  <text x="65" y="135" font-size="9.5" font-weight="700" fill="#1E40AF">Miền nghiệm</text>
  <text x="65" y="147" font-size="8.5" fill="#1E40AF">(kể cả bờ d)</text>
</svg>
"""

# ==============================================================================
# 9. Exam 01 Visual Illustration (exam1_geometry_bpt.svg)
# ==============================================================================
# Line d passes through A(4; 0) and B(0; 2) -> x + 2y = 4. Unshaded contains O(0;0): x + 2y <= 4
exam1_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 195" width="420" height="195" font-family="{FONT}">
  <defs>
    <marker id="arrE1" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="#0F172A"/>
    </marker>
    <pattern id="hatchE1" width="8" height="8" patternTransform="rotate(45 0 0)" patternUnits="userSpaceOnUse">
      <line x1="0" y1="0" x2="0" y2="8" stroke="#FCA5A5" stroke-width="2.2"/>
    </pattern>
  </defs>
  <rect x="0" y="0" width="420" height="195" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.2"/>
  <!-- Origin O(100, 145), scale 1 unit = 36px: A(4,0)->(244,145), B(0,2)->(100,73) -->
  <!-- Line through (20, 33) and (324, 185) -->
  <polygon points="20,33 370,33 370,185 324,185" fill="url(#hatchE1)"/>
  <polygon points="20,33 324,185 20,185" fill="#DBEAFE" fill-opacity="0.42"/>

  <line x1="20" y1="145" x2="375" y2="145" stroke="#0F172A" stroke-width="1.6" marker-end="url(#arrE1)"/>
  <line x1="100" y1="185" x2="100" y2="18" stroke="#0F172A" stroke-width="1.6" marker-end="url(#arrE1)"/>
  <line x1="20" y1="33" x2="324" y2="185" stroke="#1D4ED8" stroke-width="2.5"/>

  <circle cx="100" cy="145" r="3.5" fill="#0F172A"/>
  <circle cx="244" cy="145" r="4" fill="#DC2626"/>
  <circle cx="100" cy="73" r="4" fill="#DC2626"/>
  <text x="86" y="160" font-size="10" font-weight="700" fill="#0F172A">O</text>
  <text x="240" y="162" font-size="10" font-weight="700" fill="#DC2626">4</text>
  <text x="248" y="138" font-size="9.5" font-weight="700" fill="#DC2626">A(4;0)</text>
  <text x="88" y="81" font-size="9.5" font-weight="700" fill="#DC2626">2</text>
  <text x="48" y="70" font-size="9.5" font-weight="700" fill="#DC2626">B(0;2)</text>
  <text x="365" y="160" font-size="10.5" font-weight="700" fill="#0F172A">x</text>
  <text x="85" y="26" font-size="10.5" font-weight="700" fill="#0F172A">y</text>
  <text x="195" y="102" font-size="9.5" font-weight="700" fill="#1D4ED8">d: x + 2y = 4</text>
  <text x="58" y="125" font-size="9.2" font-weight="700" fill="#1E40AF">Miền nghiệm (không gạch)</text>
</svg>
"""

# ==============================================================================
# 10. Exam 02 Visual Illustration (exam2_geometry_bpt.svg)
# ==============================================================================
# Line d passes through A(2; 0) and B(0; 4) -> 2x + y = 4. Unshaded does NOT contain O(0;0): 2x + y >= 4
exam2_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 195" width="420" height="195" font-family="{FONT}">
  <defs>
    <marker id="arrE2" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="#0F172A"/>
    </marker>
    <pattern id="hatchE2" width="8" height="8" patternTransform="rotate(45 0 0)" patternUnits="userSpaceOnUse">
      <line x1="0" y1="0" x2="0" y2="8" stroke="#FCA5A5" stroke-width="2.2"/>
    </pattern>
  </defs>
  <rect x="0" y="0" width="420" height="195" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.2"/>
  <!-- Origin O(110, 155), scale: x unit = 40px, y unit = 28px: A(2,0)->(190,155), B(0,4)->(110,43) -->
  <!-- Line through (95, 22) and (211.4, 185) -->
  <!-- Discarded lower-left region containing O(0;0) -->
  <polygon points="20,22 95,22 211.4,185 20,185" fill="url(#hatchE2)"/>
  <!-- Feasible upper-right region (2x + y >= 4) -->
  <polygon points="95,22 370,22 370,185 211.4,185" fill="#F0FDFA" fill-opacity="0.55"/>

  <line x1="20" y1="155" x2="375" y2="155" stroke="#0F172A" stroke-width="1.6" marker-end="url(#arrE2)"/>
  <line x1="110" y1="185" x2="110" y2="16" stroke="#0F172A" stroke-width="1.6" marker-end="url(#arrE2)"/>
  <line x1="95" y1="22" x2="211.4" y2="185" stroke="#0D9488" stroke-width="2.5"/>

  <circle cx="110" cy="155" r="3.5" fill="#0F172A"/>
  <circle cx="190" cy="155" r="4" fill="#DC2626"/>
  <circle cx="110" cy="43" r="4" fill="#DC2626"/>
  <text x="95" y="170" font-size="10" font-weight="700" fill="#0F172A">O</text>
  <text x="186" y="172" font-size="10" font-weight="700" fill="#DC2626">2</text>
  <text x="196" y="148" font-size="9.5" font-weight="700" fill="#DC2626">A(2;0)</text>
  <text x="98" y="51" font-size="9.5" font-weight="700" fill="#DC2626">4</text>
  <text x="58" y="42" font-size="9.5" font-weight="700" fill="#DC2626">B(0;4)</text>
  <text x="365" y="170" font-size="10.5" font-weight="700" fill="#0F172A">x</text>
  <text x="95" y="24" font-size="10.5" font-weight="700" fill="#0F172A">y</text>
  <text x="175" y="92" font-size="9.5" font-weight="700" fill="#0F766E">d: 2x + y = 4</text>
  <text x="275" y="115" text-anchor="middle" font-size="9.5" font-weight="700" fill="#0F766E">Miền nghiệm</text>
  <text x="275" y="128" text-anchor="middle" font-size="8.5" fill="#0F766E">(không gạch, kể cả d)</text>
</svg>
"""

ASSETS = {
    "venn_operations.svg": venn_svg,
    "number_line_intervals.svg": number_line_svg,
    "linear_inequality_plane.svg": ineq_plane_svg,
    "linear_programming_poly.svg": lp_poly_svg,
    "unit_semicircle_trig.svg": trig_svg,
    "triangle_relations.svg": triangle_svg,
    "vector_concepts.svg": vector_svg,
    "graph_ds_bpt1.svg": graph_ds_bpt1_svg,
    "exam1_geometry_bpt.svg": exam1_svg,
    "exam2_geometry_bpt.svg": exam2_svg,
}

if __name__ == "__main__":
    for filename, content in ASSETS.items():
        path = os.path.join(OUT_DIR, filename)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content.strip() + "\n")
        print(f"Generated {path}")
