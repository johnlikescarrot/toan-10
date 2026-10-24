# 2|Kiến thức trọng tâm
Mỗi mục dưới đây được trình bày theo cùng một khuôn: **định nghĩa – công thức → ví dụ mẫu có lời giải → lỗi thường gặp → hộp Chốt ý**. Hộp Chốt ý là phần tối thiểu em phải nhớ trước khi bước vào phòng thi.

## 2.1 Mệnh đề
### 2.1.1 Mệnh đề là gì?
**Mệnh đề** là một câu khẳng định mà tính đúng – sai của nó có thể xác định được. Mỗi mệnh đề chỉ có thể **đúng** hoặc **sai**, không thể vừa đúng vừa sai.

| Câu | Là mệnh đề? | Vì sao |
|---|---|---|
| “Số 2026 chia hết cho 2” | Có (đúng) | Là câu khẳng định, kiểm tra được |
| “7 là số nguyên tố” | Có (đúng) | Kiểm tra được |
| “2 + 3 = 6” | Có (sai) | Là khẳng định sai |
| “Hôm nay trời đẹp quá!” | Không | Câu cảm thán, không có tính đúng – sai |
| “Bạn có thích Toán không?” | Không | Câu hỏi |
| “Hãy nộp bài đúng giờ” | Không | Câu mệnh lệnh |
| “5x + 3 > 0” | Không (là **mệnh đề chứa biến**) | Chưa xác định được cho đến khi biết x |

**Mệnh đề chứa biến** là câu khẳng định có chứa một hay nhiều biến, mà với mỗi giá trị của biến ta được một mệnh đề. Ví dụ P(x): “x² > 4”. Khi đó P(3) là mệnh đề đúng, P(1) là mệnh đề sai.

!> **Phân biệt “mệnh đề chứa biến” và “mệnh đề”**
> Câu “x + 1 > 2” **không phải** mệnh đề vì chưa có tính đúng – sai xác định. Nhưng câu “∀x ∈ ℝ, x + 1 > 2” thì **là** mệnh đề (và là mệnh đề sai). Dấu hiệu nhận biết: có lượng từ ∀ hoặc ∃ ở đầu thì câu đó là mệnh đề.

### 2.1.2 Mệnh đề phủ định
Cho mệnh đề P. Mệnh đề **phủ định** của P, kí hiệu là ¬P hoặc “không phải P”, là mệnh đề **đúng khi P sai** và **sai khi P đúng**.

| Mệnh đề P | Mệnh đề phủ định ¬P |
|---|---|
| “5 là số nguyên tố” (đúng) | “5 không phải là số nguyên tố” (sai) |
| “π < 3” (sai) | “π ≥ 3” (đúng) |
| “Mọi học sinh lớp 10A đều biết bơi” | “Có một học sinh lớp 10A không biết bơi” |
| “Tồn tại số tự nhiên chia hết cho 5” | “Mọi số tự nhiên đều không chia hết cho 5” |

Nhận xét quan trọng: **phủ định không phải là “nói ngược lại”** mà là phá bỏ tính đúng của mệnh đề. Với mệnh đề so sánh, phủ định của “<” là “≥”, của “=” là “≠”, của “chia hết” là “không chia hết”.

### 2.1.3 Kéo theo, đảo, tương đương và điều kiện cần – đủ
Với hai mệnh đề P, Q ta có:

| Tên gọi | Kí hiệu | Cách đọc | Sai khi nào |
|---|---|---|---|
| Mệnh đề kéo theo | P ⇒ Q | “Nếu P thì Q”; “P suy ra Q” | **Chỉ sai khi P đúng và Q sai** |
| Mệnh đề đảo | Q ⇒ P | “Nếu Q thì P” | Không nhất thiết cùng đúng – sai với P ⇒ Q |
| Mệnh đề tương đương | P ⇔ Q | “P khi và chỉ khi Q” | Đúng khi P và Q **cùng đúng hoặc cùng sai** |

**Điều kiện cần – điều kiện đủ:** nếu P ⇒ Q là mệnh đề đúng thì
- **P là điều kiện đủ** để có Q (có P là đủ để suy ra Q);
- **Q là điều kiện cần** để có P (muốn có P thì buộc phải có Q).

**Điều kiện cần và đủ:** khi P ⇔ Q đúng, P là điều kiện cần và đủ của Q.

> **Ví dụ mẫu 1**
> Cho mệnh đề “Nếu một số tự nhiên chia hết cho 6 thì nó chia hết cho 3”. Hãy phát biểu mệnh đề đảo và cho biết mệnh đề đảo đúng hay sai; xác định điều kiện cần, điều kiện đủ.
>
> **Giải.** Mệnh đề đảo: “Nếu một số tự nhiên chia hết cho 3 thì nó chia hết cho 6”. Mệnh đề đảo **sai**, chẳng hạn số 9 chia hết cho 3 nhưng không chia hết cho 6. Mệnh đề ban đầu đúng, nên “chia hết cho 6” là **điều kiện đủ** để “chia hết cho 3”, còn “chia hết cho 3” là **điều kiện cần** để “chia hết cho 6”.

### 2.1.4 Hai lượng từ ∀ và ∃
| Kí hiệu | Đọc là | Ý nghĩa | Phủ định |
|---|---|---|---|
| ∀x ∈ X, P(x) | “Với mọi x thuộc X, P(x)” | Mọi phần tử của X đều thỏa P | ∃x ∈ X, ¬P(x) |
| ∃x ∈ X, P(x) | “Tồn tại x thuộc X để P(x)” | Có ít nhất một phần tử của X thỏa P | ∀x ∈ X, ¬P(x) |

**Quy tắc ghi nhớ:** phủ định thì **đổi lượng từ** (∀ ↔ ∃) và **phủ định phần thân** (P → ¬P).

> **Ví dụ mẫu 2**
> Phát biểu mệnh đề phủ định của: “∀x ∈ ℝ, x² + 1 > 0” và “∃n ∈ ℕ, n² = n”.
>
> **Giải.** Mệnh đề phủ định thứ nhất: “∃x ∈ ℝ, x² + 1 ≤ 0”. Mệnh đề phủ định thứ hai: “∀n ∈ ℕ, n² ≠ n”.

> **Ví dụ mẫu 3**
> Xét tính đúng – sai của mệnh đề “∃x ∈ ℚ, x² = 2”.
>
> **Giải.** Mệnh đề **sai**, vì căn bậc hai của 2 là số vô tỉ: không tồn tại số hữu tỉ nào bình phương bằng 2. Mệnh đề phủ định “∀x ∈ ℚ, x² ≠ 2” là mệnh đề đúng.

!> **Ba lỗi hay gặp ở phần mệnh đề**
> 1. Phủ định “∀x, x > 0” thành “∀x, x < 0” (sai – phải là “∃x, x ≤ 0”).
> 2. Cho rằng P ⇒ Q và Q ⇒ P luôn cùng đúng – sai. Thực tế chúng độc lập với nhau.
> 3. Nhầm điều kiện cần và điều kiện đủ. Mẹo: trong câu “Nếu P thì Q”, P đứng **trước** nên là điều kiện **đủ** (có P là đủ), Q đứng **sau** nên là điều kiện **cần**.

+> **Chốt ý 2.1**
> Mệnh đề chỉ đúng hoặc sai; phủ định đảo ngược giá trị đúng – sai; P ⇒ Q chỉ sai khi P đúng Q sai; phủ định của ∀ là ∃ và ngược lại, kèm phủ định phần thân; trong “Nếu P thì Q”: P là điều kiện đủ, Q là điều kiện cần.

## 2.2 Tập hợp
### 2.2.1 Cách xác định một tập hợp
Có hai cách thường dùng:

- **Liệt kê các phần tử:** A = {1; 2; 3; 4; 5}.
- **Chỉ ra tính chất đặc trưng:** A = {x ∈ ℕ | x < 6}, đọc là “tập hợp các số tự nhiên x sao cho x < 6”.

Kí hiệu: a ∈ A (a thuộc A), b ∉ A (b không thuộc A). Tập hợp **rỗng** kí hiệu ∅ là tập không có phần tử nào.

### 2.2.2 Tập con, tập hợp bằng nhau, số tập con
**Định nghĩa.** A là **tập con** của B (kí hiệu A ⊂ B) nếu mọi phần tử của A đều là phần tử của B. Hai tập hợp **bằng nhau** (A = B) khi A ⊂ B và B ⊂ A, tức là chúng có đúng cùng các phần tử.

Quy ước: ∅ ⊂ A với mọi tập A; A ⊂ A với mọi tập A.

**Công thức đếm số tập con.** Một tập hợp có **n phần tử** (n ≥ 0) thì có **2ⁿ tập con**, trong đó có **1 tập rỗng** và **1 tập chính nó**, nên có **2ⁿ − 1 tập con khác rỗng**.

| Số phần tử của A | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| Số tập con | 1 | 2 | 4 | 8 | 16 | 32 | 64 |

> **Ví dụ mẫu 4**
> Cho A = {1; 2; 3; 4}. Viết tất cả tập con của A có đúng hai phần tử và cho biết A có bao nhiêu tập con.
>
> **Giải.** Các tập con hai phần tử: {1; 2}, {1; 3}, {1; 4}, {2; 3}, {2; 4}, {3; 4} (6 tập). A có 4 phần tử nên có 2⁴ = 16 tập con.

!> **Cẩn thận với tập rỗng**
> ∅ **khác** {∅}. Tập ∅ không có phần tử nào; tập {∅} có đúng một phần tử là tập rỗng. Khi liệt kê tập con, đừng quên tập rỗng và chính tập đã cho.

### 2.2.3 Các tập số và các khoảng – đoạn – nửa khoảng
| Kí hiệu | Tên gọi | Mô tả trên trục số |
|---|---|---|
| ℕ = {0; 1; 2; …} | Tập số tự nhiên | – |
| ℕ* = {1; 2; 3; …} | Tập số tự nhiên khác 0 | – |
| ℤ | Tập số nguyên | – |
| ℚ | Tập số hữu tỉ | – |
| ℝ | Tập số thực | Toàn bộ trục số |
| (a; b) | Khoảng | Không lấy hai đầu mút |
| [a; b] | Đoạn | Lấy cả hai đầu mút |
| (a; b] | Nửa khoảng | Không lấy a, lấy b |
| [a; b) | Nửa khoảng | Lấy a, không lấy b |
| (−∞; a); (−∞; a] | Nửa khoảng (nửa đường thẳng) | Không lấy a / lấy a |
| (a; +∞); [a; +∞) | Nửa khoảng (nửa đường thẳng) | Không lấy a / lấy a |
| (−∞; +∞) | Khoảng | Chính là ℝ |

!> **Quy tắc dấu ngoặc**
> **Ngoặc tròn ( )** = **không** lấy đầu mút. **Ngoặc vuông [ ]** = **có** lấy đầu mút. Ở hai đầu ±∞ luôn dùng ngoặc tròn, vì ∞ không phải là số.

> **Ví dụ mẫu 5**
> Viết các tập sau dưới dạng khoảng, đoạn, nửa khoảng: A = {x ∈ ℝ | −2 ≤ x < 3}; B = {x ∈ ℝ | x > 5}; C = {x ∈ ℝ | x ≤ −1}.
>
> **Giải.** A = [−2; 3); B = (5; +∞); C = (−∞; −1].

### 2.2.4 Giao, hợp, hiệu, phần bù
Cho hai tập hợp A và B:

| Phép toán | Kí hiệu | Định nghĩa | Cách nhớ |
|---|---|---|---|
| Giao | A ∩ B | Các phần tử **thuộc cả A và B** | “Và” – phần chung |
| Hợp | A ∪ B | Các phần tử **thuộc A hoặc thuộc B** | “Hoặc” – gộp lại |
| Hiệu | A \ B | Các phần tử **thuộc A nhưng không thuộc B** | “A bỏ đi phần của B” |
| Phần bù | B ∖ A (khi A ⊂ B) | Các phần tử thuộc B mà không thuộc A | “Phần còn lại của B sau khi bỏ A” |

[[vennrow]]

Ba hệ thức cần nhớ khi làm bài đếm (dạng biểu đồ Ven):
- |A ∪ B| = |A| + |B| − |A ∩ B| (hai tập).
- Với ba tập: |A ∪ B ∪ C| = |A| + |B| + |C| − |A ∩ B| − |B ∩ C| − |C ∩ A| + |A ∩ B ∩ C|.
- Nếu A và B rời nhau (A ∩ B = ∅) thì |A ∪ B| = |A| + |B|.

> **Ví dụ mẫu 6**
> Cho A = [−1; 4] và B = (2; 6). Tìm A ∩ B, A ∪ B, A \ B, B \ A.
>
> **Giải.** Biểu diễn hai tập trên trục số rồi “chồng” lên nhau: A ∩ B = (2; 4]; A ∪ B = [−1; 6); A \ B = [−1; 2]; B \ A = (4; 6).

> **Ví dụ mẫu 7**
> Lớp 10A có 40 học sinh, trong đó 22 em tham gia câu lạc bộ Toán, 18 em tham gia câu lạc bộ Tin, 8 em tham gia cả hai. Hỏi có bao nhiêu em không tham gia câu lạc bộ nào?
>
> **Giải.** Số em tham gia ít nhất một câu lạc bộ là 22 + 18 − 8 = 32. Vậy số em không tham gia câu lạc bộ nào là 40 − 32 = **8 em**.

!> **Sai lầm khi hợp các khoảng**
> Khi lấy hợp, nhiều bạn viết A ∪ B = (−∞; 6) dù A có đầu mút −1. Hãy vẽ trục số: hợp là **tất cả** các điểm bị tô bởi ít nhất một tập, nên kết quả phải bắt đầu từ đầu mút nhỏ nhất.

+> **Chốt ý 2.2**
> Tập n phần tử có 2ⁿ tập con; ngoặc tròn không lấy đầu mút, ngoặc vuông có lấy; giao là phần chung, hợp là gộp, hiệu A \ B là “A bỏ B”; với bài toán đếm dùng |A ∪ B| = |A| + |B| − |A ∩ B|.

## 2.3 Bất phương trình và hệ bất phương trình bậc nhất hai ẩn
### 2.3.1 Khái niệm
**Bất phương trình bậc nhất hai ẩn x, y** có dạng tổng quát ax + by ≤ c (hoặc ax + by ≥ c, ax + by < c, ax + by > c), trong đó a, b, c là các số thực đã biết và **a² + b² ≠ 0** (a, b không đồng thời bằng 0).

Cặp số (x₀; y₀) là **một nghiệm** của bất phương trình nếu thay vào ta được một bất đẳng thức đúng. Tập hợp tất cả các điểm trong mặt phẳng tọa độ có tọa độ là nghiệm được gọi là **miền nghiệm**.

| Là bất phương trình bậc nhất hai ẩn? | Lý do |
|---|---|
| 2x + 3y ≤ 5 | Có (a = 2, b = 3) |
| x − y > 0 | Có |
| x² + y < 1 | Không (chứa x²) |
| xy − 1 ≥ 0 | Không (chứa tích xy) |
| 1/x + y < 3 | Không (x ở mẫu) |

### 2.3.2 Cách biểu diễn miền nghiệm
**Bốn bước bắt buộc:**

1. Vẽ đường thẳng d: ax + by = c (đường thẳng này gọi là **đường biên**).
2. Lấy một điểm M₀(x₀; y₀) **không thuộc d** – thường chọn gốc tọa độ O(0; 0) cho nhanh.
3. Thay M₀ vào bất phương trình: nếu được bất đẳng thức đúng thì **miền nghiệm là nửa mặt phẳng bờ d chứa M₀**; nếu sai thì lấy nửa mặt phẳng còn lại.
4. Kết luận: nếu bất phương trình có dấu ≤ hoặc ≥ thì **lấy cả đường biên**; nếu có dấu < hoặc > thì **không lấy đường biên** (vẽ nét đứt).

> **Ví dụ mẫu 8**
> Biểu diễn miền nghiệm của bất phương trình 2x + y − 4 ≤ 0.
>
> **Giải.** Vẽ đường thẳng d: 2x + y = 4 qua hai điểm (0; 4) và (2; 0). Thay O(0; 0): 2·0 + 0 − 4 = −4 ≤ 0, đúng. Vậy miền nghiệm là **nửa mặt phẳng bờ d chứa gốc tọa độ O, kể cả đường thẳng d**.

!> **Hai lỗi kinh điển**
> 1. Chọn điểm thử **nằm trên** đường biên (thay vào được 0 ≤ 0, luôn đúng) rồi kết luận sai. Điểm thử phải **không thuộc** đường biên.
> 2. Quên rằng dấu ≤, ≥ thì lấy cả bờ. Trong bài thi, nếu đề nói “kể cả bờ” mà em vẽ nét đứt là mất điểm trình bày.

### 2.3.3 Hệ bất phương trình bậc nhất hai ẩn
Hệ gồm hai hay nhiều bất phương trình bậc nhất hai ẩn; nghiệm của hệ là cặp số thỏa **tất cả** các bất phương trình trong hệ. Về hình học, **miền nghiệm của hệ là phần giao các miền nghiệm** của từng bất phương trình – thường là một **đa giác** (có thể không bị chặn).

Quy trình: biểu diễn từng miền nghiệm, lấy phần chung, xác định các **đỉnh** của đa giác (giao điểm của các đường biên).

> **Ví dụ mẫu 9**
> Biểu diễn miền nghiệm của hệ: 2x + y ≤ 100; x + 2y ≤ 80; x ≥ 0; y ≥ 0.
>
> **Giải.** Bốn đường biên lần lượt là d₁: 2x + y = 100 (qua (0; 100) và (50; 0)), d₂: x + 2y = 80 (qua (0; 40) và (80; 0)), trục Oy (x = 0) và trục Ox (y = 0). Miền nghiệm là tứ giác OABC với O(0; 0), A(50; 0), B(40; 20) – giao điểm của d₁ và d₂ – và C(0; 40).

[[lpfig|Hình 1. Miền nghiệm của hệ 2x + y ≤ 100; x + 2y ≤ 80; x ≥ 0; y ≥ 0 là tứ giác OABC.]]

### 2.3.4 Bài toán tối ưu (vận dụng cao – chính là Câu 21)
Bài toán: tìm giá trị lớn nhất (hoặc nhỏ nhất) của biểu thức F = ax + by trên miền nghiệm của một hệ bất phương trình, với x, y là các đại lượng thực tế (số sản phẩm, số giờ, số hecta…).

**Ba bước giải:**

1. **Lập mô hình:** gọi x, y là các đại lượng cần tìm, viết hệ bất phương trình (nhớ thêm x ≥ 0, y ≥ 0) và biểu thức mục tiêu F.
2. **Xác định miền nghiệm và các đỉnh** của đa giác.
3. **Tính F tại từng đỉnh** rồi so sánh. Với bài toán quy hoạch tuyến tính, F đạt giá trị lớn nhất/nhỏ nhất tại một trong các đỉnh (nếu miền nghiệm là đa giác).

> **Ví dụ mẫu 10**
> Một xưởng may mỗi ngày có 100 m vải và 80 giờ công. Một bộ đồ loại A cần 2 m vải và 1 giờ công, lãi 800 nghìn đồng; một bộ loại B cần 1 m vải và 2 giờ công, lãi 500 nghìn đồng. Hỏi mỗi ngày nên may bao nhiêu bộ mỗi loại để lãi lớn nhất?
>
> **Giải.** Gọi x, y là số bộ loại A, B (x ≥ 0, y ≥ 0, nguyên). Ràng buộc: 2x + y ≤ 100 (vải) và x + 2y ≤ 80 (giờ công). Lãi F = 800x + 500y (nghìn đồng). Miền nghiệm là tứ giác O(0; 0), A(50; 0), B(40; 20), C(0; 40). Tính: F(O) = 0; F(A) = 40 000; F(B) = 32 000 + 10 000 = **42 000**; F(C) = 20 000. Vậy lãi lớn nhất là **42 triệu đồng**, đạt khi may **40 bộ loại A và 20 bộ loại B**.

!> **Bẫy của bài toán tối ưu**
> Đề bài hỏi “lãi lớn nhất” nhưng nhiều bạn chỉ đưa ra cặp (x; y). Phải **kết luận bằng số tiền kèm đơn vị** và nêu rõ số lượng từng loại. Ngoài ra, nếu x, y là số sản phẩm thì cần kiểm tra nghiệm tìm được có **nguyên và không âm** hay không.

+> **Chốt ý 2.3**
> Vẽ biên → thử một điểm không thuộc biên → chọn nửa mặt phẳng; dấu ≤, ≥ thì lấy bờ; miền nghiệm của hệ là **phần giao**; bài toán tối ưu: lập hệ + hàm mục tiêu, tính F tại **các đỉnh**, kết luận có đơn vị.

## 2.4 Giá trị lượng giác của một góc từ 0° đến 180°
### 2.4.1 Định nghĩa
Trong mặt phẳng tọa độ, lấy **nửa đường tròn đơn vị** (tâm O, bán kính 1, nằm phía trên trục hoành). Với góc α (0° ≤ α ≤ 180°), lấy điểm M trên nửa đường tròn sao cho góc xOM = α và gọi M(x₀; y₀). Khi đó:

- sin α = y₀
- cos α = x₀
- tan α = y₀/x₀ (xác định khi x₀ ≠ 0, tức α ≠ 90°)
- cot α = x₀/y₀ (xác định khi y₀ ≠ 0, tức α ≠ 0° và α ≠ 180°)

Hệ quả trực tiếp: với mọi α ta luôn có **−1 ≤ sin α ≤ 1**, **−1 ≤ cos α ≤ 1**, và **sin α ≥ 0** (vì M nằm phía trên trục hoành).

### 2.4.2 Dấu của các giá trị lượng giác và quan hệ bù nhau
| Góc α | sin | cos | tan | cot |
|---|---|---|---|---|
| 0° < α < 90° (nhọn) | + | + | + | + |
| α = 90° | 1 | 0 | không xác định | 0 |
| 90° < α < 180° (tù) | + | − | − | − |

**Hai góc bù nhau** (α và 180° − α) có:
- sin(180° − α) = sin α
- cos(180° − α) = − cos α
- tan(180° − α) = − tan α
- cot(180° − α) = − cot α

Cách nhớ: **“sin bù” – chỉ sin giữ nguyên dấu, ba giá trị còn lại đổi dấu.**

> **Ví dụ mẫu 11**
> Tính sin 150°, cos 135°, tan 120°.
>
> **Giải.** sin 150° = sin 30° = 1/2. cos 135° = −cos 45° = −√2/2. tan 120° = −tan 60° = −√3.

### 2.4.3 Bảng giá trị lượng giác của các góc đặc biệt
| α | sin α | cos α | tan α | cot α |
|---|---|---|---|---|
| 0° | 0 | 1 | 0 | không xác định |
| 30° | 1/2 | √3/2 | √3/3 | √3 |
| 45° | √2/2 | √2/2 | 1 | 1 |
| 60° | √3/2 | 1/2 | √3 | √3/3 |
| 90° | 1 | 0 | không xác định | 0 |
| 120° | √3/2 | −1/2 | −√3 | −√3/3 |
| 135° | √2/2 | −√2/2 | −1 | −1 |
| 150° | 1/2 | −√3/2 | −√3/3 | −√3 |
| 180° | 0 | −1 | 0 | không xác định |

+> **Mẹo nhớ bảng**
> Với sin của 0°, 30°, 45°, 60°, 90°: viết √0/2, √1/2, √2/2, √3/2, √4/2 rồi rút gọn. cos là dãy ngược lại. Từ 90° đến 180° lấy đối xứng qua góc bù và đổi dấu cos, tan, cot.

### 2.4.4 Biết một giá trị lượng giác, tìm các giá trị còn lại
Ba hệ thức nền tảng (dùng liên tục trong đề thi):

- **sin²α + cos²α = 1** (đúng với mọi α)
- **tan α = sin α / cos α**, **cot α = cos α / sin α**, **tan α · cot α = 1**
- **1 + tan²α = 1/cos²α** và **1 + cot²α = 1/sin²α**

**Quy trình:** tính giá trị tuyệt đối bằng hệ thức → **xác định dấu** dựa vào khoảng của α (nhọn hay tù) → kết luận.

> **Ví dụ mẫu 12**
> Cho sin α = 3/5 với 90° < α < 180°. Tính cos α, tan α, cot α.
>
> **Giải.** cos²α = 1 − sin²α = 1 − 9/25 = 16/25, suy ra |cos α| = 4/5. Vì 90° < α < 180° nên cos α < 0, do đó cos α = −4/5. Từ đó tan α = (3/5)/(−4/5) = −3/4 và cot α = −4/3.

> **Ví dụ mẫu 13**
> Cho tan α = −2 với 90° < α < 180°. Tính giá trị của biểu thức P = (sin α + 3cos α)/(2sin α − cos α).
>
> **Giải.** Chia cả tử và mẫu cho cos α (cos α ≠ 0): P = (tan α + 3)/(2tan α − 1) = (−2 + 3)/(2·(−2) − 1) = 1/(−5) = **−1/5**.

!> **Lỗi làm mất điểm nhiều nhất ở dạng này**
> Bỏ qua dữ kiện khoảng của α và chọn dấu “+”. Chỉ cần α là góc tù thì **cos, tan, cot đều âm**. Hãy viết dấu ra nháp trước khi thay số.

### 2.4.5 Dùng máy tính cầm tay (CASIO fx-580VN X)
| Cần tìm | Thao tác |
|---|---|
| sin, cos, tan của góc | Nhập số đo góc rồi bấm sin/cos/tan (chú ý chế độ **D** – độ) |
| Góc khi biết sin | SHIFT + sin, nhập giá trị, bấm = (kết quả trong khoảng 0° – 180° với sin) |
| Góc khi biết cos | SHIFT + cos (máy cho góc 0° – 180°) |
| Góc khi biết tan | SHIFT + tan |

!> **Kiểm tra chế độ máy**
> Trước giờ thi, bấm SHIFT + MENU (SETUP) để chắc chắn máy đang ở **Deg** (độ), không phải Rad. Nếu ở Rad, sin 30 sẽ cho kết quả hoàn toàn khác.

+> **Chốt ý 2.4**
> sin luôn không âm với α ∈ [0°; 180°]; góc tù thì cos, tan, cot âm; hai góc bù nhau chỉ sin giữ nguyên; sin²α + cos²α = 1; biết một giá trị phải **xét dấu theo khoảng của α** trước khi kết luận.

## 2.5 Hệ thức lượng trong tam giác
Kí hiệu quy ước: tam giác ABC có BC = a, CA = b, AB = c; R là bán kính đường tròn ngoại tiếp; r là bán kính đường tròn nội tiếp; p = (a + b + c)/2 là nửa chu vi; S là diện tích.

### 2.5.1 Định lí côsin
Trong tam giác ABC:

- **a² = b² + c² − 2bc·cos A**
- b² = c² + a² − 2ca·cos B
- c² = a² + b² − 2ab·cos C

**Hệ quả (dùng để tính góc khi biết ba cạnh):**

- cos A = (b² + c² − a²)/(2bc)
- cos B = (c² + a² − b²)/(2ca)
- cos C = (a² + b² − c²)/(2ab)

> **Ví dụ mẫu 14**
> Tam giác ABC có AB = 5, AC = 8 và góc A = 60°. Tính BC.
>
> **Giải.** BC² = AB² + AC² − 2·AB·AC·cos A = 25 + 64 − 2·5·8·(1/2) = 89 − 40 = 49. Vậy BC = 7.

### 2.5.2 Định lí sin
Trong tam giác ABC:

**a/sin A = b/sin B = c/sin C = 2R**

Hệ quả: a = 2R·sin A; sin A = a/(2R). Định lí sin đặc biệt hữu ích khi biết **một cạnh và góc đối diện** hoặc **hai góc và một cạnh**.

> **Ví dụ mẫu 15**
> Tam giác ABC có BC = 8 và góc A = 45°. Tính bán kính R của đường tròn ngoại tiếp tam giác.
>
> **Giải.** Từ a/sin A = 2R suy ra R = a/(2sin A) = 8/(2·(√2/2)) = 8/√2 = **4√2**.

### 2.5.3 Các công thức tính diện tích tam giác
| Công thức | Diễn đạt | Dùng khi biết |
|---|---|---|
| S = (1/2)·a·h | Nửa cạnh nhân chiều cao tương ứng | Một cạnh và đường cao |
| S = (1/2)·ab·sin C | Nửa tích hai cạnh nhân sin góc xen giữa | Hai cạnh và góc xen giữa |
| S = abc/(4R) | Tích ba cạnh chia 4 lần bán kính ngoại tiếp | Ba cạnh và R |
| S = p·r | Nửa chu vi nhân bán kính nội tiếp | Nửa chu vi và r |
| S = √(p(p − a)(p − b)(p − c)) | Công thức Hê-rông | Biết ba cạnh |

> **Ví dụ mẫu 16**
> Tam giác ABC vuông tại A có AB = 6, AC = 8. Tính diện tích S, bán kính r của đường tròn nội tiếp và bán kính R của đường tròn ngoại tiếp.
>
> **Giải.** BC = √(36 + 64) = 10. Diện tích S = (1/2)·6·8 = 24. Nửa chu vi p = (6 + 8 + 10)/2 = 12, do đó r = S/p = 24/12 = **2**. Tam giác vuông tại A nên BC là đường kính đường tròn ngoại tiếp: R = BC/2 = **5**.

### 2.5.4 Giải tam giác và bài toán thực tế
**Giải tam giác** là tìm các yếu tố còn lại (cạnh, góc) khi đã biết một số yếu tố. Ba tình huống thường gặp:

| Đề cho | Công cụ nên dùng |
|---|---|
| Hai cạnh và góc xen giữa | Định lí côsin để tìm cạnh thứ ba, sau đó định lí sin hoặc côsin để tìm góc |
| Ba cạnh | Định lí côsin (hệ quả) để tìm góc |
| Một cạnh và hai góc | Định lí sin (tính góc còn lại nhờ tổng ba góc bằng 180°) |

**Quy trình giải bài toán thực tế (đo khoảng cách, đo chiều cao):**

1. Vẽ hình, đặt tên các điểm và **xác định tam giác** chứa đại lượng cần tìm.
2. Ghi ra các yếu tố đã biết: cạnh nào, góc nào (chú ý góc tạo bởi hai hướng nhìn).
3. Chọn công cụ: côsin, sin, hay công thức diện tích.
4. Tính toán, **làm tròn theo yêu cầu đề** và viết kết luận có đơn vị.

> **Ví dụ mẫu 17**
> Để đo khoảng cách từ bờ đến một hòn đảo, người ta chọn hai điểm A, B trên bờ với AB = 100 m. Từ A đo được góc tạo bởi AB và hướng tới đảo C là 75°; từ B đo được góc tạo bởi BA và hướng tới C là 60°. Tính khoảng cách AC.
>
> **Giải.** Trong tam giác ABC: góc A = 75°, góc B = 60°, suy ra góc C = 180° − 75° − 60° = 45°. Theo định lí sin: AC/sin B = AB/sin C, nên AC = 100·sin 60°/sin 45° = 100·(√3/2)/(√2/2) = 50√6 ≈ **122,5 m**.

!> **Ba lỗi cần tránh**
> 1. Dùng định lí côsin với góc **không xen giữa** hai cạnh đã biết.
> 2. Nhầm cạnh đối diện với góc: a đối diện A, b đối diện B, c đối diện C.
> 3. Trong bài thực tế, quên rằng góc đo được thường là góc **tạo bởi hai hướng**, không phải góc trong tam giác – phải vẽ hình để xác định đúng.

+> **Chốt ý 2.5**
> Côsin: a² = b² + c² − 2bc cos A. Sin: a/sin A = 2R. Diện tích: S = (1/2)ab sin C = abc/(4R) = pr = √(p(p−a)(p−b)(p−c)). Bài thực tế: vẽ tam giác, xác định đúng góc xen giữa, chọn công cụ, kết luận có đơn vị.

## 2.6 Vectơ
### 2.6.1 Khái niệm vectơ
**Vectơ** là một đoạn thẳng có hướng. Vectơ có điểm đầu A và điểm cuối B được kí hiệu là \v{AB}. Vectơ còn được kí hiệu bằng một chữ cái thường: \v{a}, \v{b}, \v{x}…

- **Độ dài của vectơ** \v{AB} là độ dài đoạn thẳng AB, kí hiệu |\v{AB}| = AB.
- **Giá của vectơ** là đường thẳng đi qua điểm đầu và điểm cuối của vectơ đó.
- Vectơ **không** (kí hiệu \v{0}) là vectơ có điểm đầu và điểm cuối trùng nhau; |\v{0}| = 0.

### 2.6.2 Phương, hướng, hai vectơ bằng nhau
| Khái niệm | Định nghĩa |
|---|---|
| Hai vectơ **cùng phương** | Có giá song song hoặc trùng nhau |
| Hai vectơ **cùng hướng** | Cùng phương **và** cùng chiều (mũi tên chỉ về một phía) |
| Hai vectơ **ngược hướng** | Cùng phương nhưng ngược chiều |
| Hai vectơ **bằng nhau** | Cùng hướng **và** cùng độ dài |
| Hai vectơ **đối nhau** | Cùng độ dài nhưng ngược hướng |

Từ định nghĩa suy ra ngay: **hai vectơ bằng nhau thì cùng phương** (vì cùng hướng), nhưng **hai vectơ cùng phương chưa chắc cùng hướng** – chúng có thể ngược hướng.

!> **Vectơ – không: trường hợp đặc biệt**
> Vectơ \v{0} được coi là **cùng phương và cùng hướng với mọi vectơ**. Vì vậy, đừng nói “\v{0} không cùng phương với \v{AB}” – điều đó sai. Tuy nhiên \v{0} chỉ bằng chính nó.

> **Ví dụ mẫu 18**
> Cho hình bình hành ABCD. Trong các khẳng định sau, khẳng định nào đúng?
> a) \v{AB} = \v{CD}; b) \v{AB} = \v{DC}; c) \v{AD} = \v{BC}; d) \v{AC} = \v{BD}.
>
> **Giải.** Trong hình bình hành ABCD, cạnh AB song song và bằng cạnh DC, hai vectơ \v{AB} và \v{DC} cùng hướng và cùng độ dài nên **\v{AB} = \v{DC}** – khẳng định b) đúng. \v{AB} và \v{CD} ngược hướng nên a) sai. \v{AD} và \v{BC} cùng hướng và cùng độ dài nên c) đúng. \v{AC} và \v{BD} không cùng phương nên d) sai. Vậy b) và c) đúng.

> **Ví dụ mẫu 19**
> Cho hình vuông ABCD tâm O, cạnh a. Tính |\v{AC}| và chỉ ra một cặp vectơ đối nhau.
>
> **Giải.** Đường chéo hình vuông cạnh a bằng a√2, nên |\v{AC}| = a√2. Hai vectơ \v{AO} và \v{OC} có cùng độ dài (bằng a√2/2) nhưng ngược hướng, nên chúng là hai vectơ đối nhau.

### 2.6.3 Ba quy tắc dựng tổng, hiệu (kiến thức nối tiếp sau giữa kì)
Phần này **chưa có trong đề giữa kì I** theo ma trận, nhưng nắm trước sẽ giúp em học chương sau nhẹ hơn nhiều:

| Quy tắc | Hệ thức | Cách nhớ |
|---|---|---|
| Ba điểm (cộng) | \v{AB} + \v{BC} = \v{AC} | “Đi từ A đến C qua B” |
| Hình bình hành | \v{AB} + \v{AD} = \v{AC} | Đường chéo hình bình hành |
| Ba điểm (trừ) | \v{AB} − \v{AC} = \v{CB} | “Cuối trừ đầu” |
| Trung điểm | I là trung điểm AB ⇔ \v{IA} + \v{IB} = \v{0} | Hai vectơ đối nhau |
| Trọng tâm | G là trọng tâm tam giác ABC ⇔ \v{GA} + \v{GB} + \v{GC} = \v{0} | Tổng ba vectơ bằng \v{0} |

+> **Chốt ý 2.6**
> Vectơ = đoạn thẳng có hướng; giá là đường thẳng chứa nó; cùng phương chưa chắc cùng hướng; bằng nhau = cùng hướng + cùng độ dài; \v{0} cùng phương, cùng hướng với mọi vectơ và có độ dài 0.
