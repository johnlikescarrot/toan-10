#import "style.typ": *

= Phụ lục đối chiếu ma trận và nguồn

== 6.1. Bảng bao phủ từng câu và từng ý

Bảng này dùng để kiểm tra hai chiều: *mỗi yêu cầu trong bảng đặc tả có một vị trí đề ôn*, và *mỗi câu trong đề ôn đều có đáp án/lời giải*. Các mức độ viết tắt: NB — nhận biết; TH — thông hiểu; VD — vận dụng; VDC — vận dụng cao.

#table(
  columns: (0.75fr, 0.7fr, 0.55fr, 3.45fr, 1.1fr),
  table.header(
    [#th[Vị trí]], [#th[Đơn vị]], [#th[Mức]], [#th[Yêu cầu được bao phủ]], [#th[Đáp án/kết quả]],
  ),
  [C1], [1.1], [NB], [Nhận biết mệnh đề; phân biệt mệnh đề chứa biến, câu cầu khiến, câu hỏi], [C],
  [C2], [1.1], [NB], [Ý nghĩa và phủ định mệnh đề có $exists,forall$], [A],
  [C3], [1.2], [NB], [Chuyển từ tính chất đặc trưng sang liệt kê phần tử], [D],
  [C4], [1.3], [NB], [Biểu đồ Ven của giao hai tập hợp], [B],
  [C5], [2.1], [NB], [Nhận biết BPT bậc nhất hai ẩn], [B],
  [C6], [2.2], [NB], [Nhận biết nghiệm của hệ BPT bậc nhất hai ẩn], [A],
  [C7], [3.1], [NB], [Giá trị lượng giác của góc $120°$; quan hệ góc bù], [C],
  [C8], [3.1], [TH], [Tính $cos alpha$ từ $sin alpha$, xét dấu góc tù], [A],
  [C9], [3.2], [NB], [Nhận biết công thức định lí côsin], [D],
  [C10], [3.2], [TH], [Dùng định lí côsin tính cạnh], [C · $sqrt(39)$],
  [C11], [4.1], [NB], [Độ dài, hai vectơ bằng nhau, vectơ-không], [D],
  [C12], [4.1], [TH], [Chứng minh/nhận biết hai vectơ bằng nhau trong hình bình hành], [B],
  [ĐS1a], [1.2], [NB], [Dùng đúng $in$ và $subset$], [Đ],
  [ĐS1b], [1.2], [TH], [Biểu diễn $(1;4]$ trên trục số], [Đ],
  [ĐS1c], [1.3], [TH], [Giao và hợp của hai tập hữu hạn], [Đ],
  [ĐS1d], [1.3], [VD], [Hiệu của hai tập hợp], [S · ${1;2}$],
  [ĐS2a], [2.1], [NB], [Kiểm tra một cặp số là nghiệm], [Đ],
  [ĐS2b], [2.1], [TH], [Xác định phía nửa mặt phẳng nghiệm bằng điểm $O$], [S · chứa $O$],
  [ĐS2c], [2.1], [TH], [Mô tả đường bờ và điều kiện lấy bờ], [Đ],
  [ĐS2d], [2.1], [VD], [Chuyển điều kiện khối lượng thực tế về BPT], [Đ],
  [TLN1], [1.2], [TH], [Tính số tập con của tập có $5$ phần tử], [$32$],
  [TLN2], [1.3], [VD], [Bài toán thực tế bằng phép toán tập hợp], [$35$],
  [TLN3], [3.1], [VD], [Tính biểu thức khi biết một giá trị lượng giác], [$2$],
  [TLN4], [3.2], [TH], [Dùng công thức diện tích với góc $150°$], [$12$],
  [TL1], [1.3], [TH], [Giao, hợp, hiệu, phần bù], [Có lời giải],
  [TL2], [3.2], [VD], [Bài toán khoảng cách thực tế bằng định lí côsin], [$70$ m],
  [TL3], [2.2], [VDC], [Miền nghiệm của hệ và phương án tối ưu], [$130$ triệu tại $(30;20)$],
)

#answer-strip([
  *Kết quả kiểm tra số lượng:* 12/12 câu chọn phương án · 2/2 câu đúng–sai với 8/8 ý · 4/4 câu trả lời ngắn · 3/3 câu tự luận · 27/27 dòng trong bảng đều có đáp án hoặc lời giải.
])

== 6.2. Nội dung bảng đặc tả nguồn đã phân tích

Phần dưới ghi lại đầy đủ yêu cầu theo từng đơn vị của tệp DOCX; dấu câu và kí hiệu toán được chuẩn hóa để dễ đọc. Tên “Câu …” trong phần này là *nhãn của bảng đặc tả nguồn*, không phải nguyên văn đề thi.

=== Đơn vị 1.1 · Mệnh đề

- *Nhận biết — Câu 1:* biết thế nào là mệnh đề, mệnh đề phủ định, mệnh đề chứa biến.
- *Nhận biết — Câu 2:* biết ý nghĩa kí hiệu phổ biến ($forall$) và kí hiệu tồn tại ($exists$).

Phần mục tiêu chung của tệp còn nêu mệnh đề kéo theo, mệnh đề đảo, tương đương, điều kiện cần–đủ và phủ định mệnh đề có lượng từ; các nội dung này đã được đưa vào Chuyên đề 1 để tránh hổng kiến thức.

=== Đơn vị 1.2 · Tập hợp

- *Nhận biết — Câu 3:* cho tập hợp bằng cách liệt kê hoặc chỉ ra tính chất đặc trưng của các phần tử.
- *Nhận biết — Câu 1a (ĐS):* sử dụng đúng các kí hiệu $in, subset$; sử dụng đúng $(a;b)$, $[a;b]$, $(a;b]$, $[a;b)$, $(-oo;a)$, $(-oo;a]$, $(a;+oo)$, $[a;+oo)$, $(-oo;+oo)$.
- *Thông hiểu — Câu 1b:* biểu diễn các khoảng, đoạn trên trục số; lấy ví dụ về tập hợp, tập con, hai tập bằng nhau.
- *Thông hiểu — Câu 1 (TLN):* tìm số tập hợp con của một tập hợp.

=== Đơn vị 1.3 · Các phép toán trên tập hợp

- *Nhận biết — Câu 4:* dùng biểu đồ Ven để biểu diễn giao và hợp của hai tập hợp.
- *Thông hiểu — Câu 1c và Câu 1 (TL):* thực hiện giao, hợp, phần bù của một tập con.
- *Vận dụng — Câu 1d:* thực hiện các phép toán giao, hợp, phần bù của một tập con.
- *Vận dụng — Câu 2 (TLN):* bài toán thực tế về các phép toán tập hợp.

=== Đơn vị 2.1 · Bất phương trình bậc nhất hai ẩn

- *Nhận biết — Câu 5:* nhận biết BPT bậc nhất hai ẩn.
- *Nhận biết — Câu 2a:* nhận biết nghiệm và miền nghiệm trên mặt phẳng tọa độ.
- *Thông hiểu — Câu 2b, 2c:* mô tả miền nghiệm trên mặt phẳng tọa độ.
- *Vận dụng — Câu 2d:* chuyển điều kiện của bài toán thực tế về dạng BPT bậc nhất hai ẩn.

=== Đơn vị 2.2 · Hệ bất phương trình bậc nhất hai ẩn

- *Nhận biết — Câu 6:* nhận biết hệ BPT bậc nhất hai ẩn; nhận biết nghiệm và miền nghiệm trên mặt phẳng tọa độ.
- *Vận dụng cao — Câu 3 (TL):* mô tả miền nghiệm của hệ trên mặt phẳng tọa độ; tìm giá trị tối ưu trong bài toán chọn phương án.

=== Đơn vị 3.1 · Giá trị lượng giác của một góc từ $0°$ đến $180°$

- *Nhận biết — Câu 7:* nhận biết giá trị lượng giác của một góc từ $0°$ đến $180°$; nhận biết hệ thức liên hệ giữa giá trị lượng giác của các góc phụ nhau, bù nhau; tính giá trị đúng hoặc gần đúng bằng máy tính cầm tay.
- *Thông hiểu — Câu 8:* tính giá trị lượng giác của một góc khi biết một trong bốn giá trị lượng giác của nó.
- *Vận dụng — Câu 3 (TLN):* cho biết một giá trị lượng giác, tính giá trị của một biểu thức.

=== Đơn vị 3.2 · Hệ thức lượng trong tam giác

- *Nhận biết — Câu 9:* nhận biết định lí côsin, định lí sin, công thức tính diện tích tam giác.
- *Thông hiểu — Câu 10 (TN) và Câu 4 (TLN):* sử dụng các hệ thức lượng để tính cạnh, góc chưa biết và diện tích; ứng dụng trong bài toán thực tiễn đơn giản.
- *Vận dụng — Câu 2 (TL):* mô tả cách giải tam giác và vận dụng vào bài toán thực tiễn, ví dụ xác định khoảng cách khi gặp vật cản hoặc chiều cao khi không đo trực tiếp được.

=== Đơn vị 4.1 · Khái niệm vectơ

- *Nhận biết — Câu 11:* biết khái niệm và tính chất của vectơ, vectơ-không, độ dài, hai vectơ cùng phương, cùng hướng, bằng nhau; biết vectơ-không cùng phương và cùng hướng với mọi vectơ.
- *Thông hiểu — Câu 12:* hiểu khái niệm và đặc điểm của vectơ, vectơ-không, độ dài, hai vectơ cùng phương, hai vectơ bằng nhau; chứng minh hai vectơ bằng nhau trong trường hợp đơn giản.

== 6.3. Nguồn tham khảo và cách sử dụng nguồn

=== Nguồn trực tiếp

+ *MA TRẬN TOÁN 10 - GIỮA KÌ I.docx* — tệp do người dùng cung cấp; nguồn duy nhất dùng để xác định trường, năm học, thời gian, cấu trúc, điểm, mức độ và vị trí câu hỏi.
+ *Toán 10, tập 1, bộ _Kết nối tri thức với cuộc sống_*, Bài 1–7 — dùng để chuẩn hóa tên bài và phạm vi kiến thức.
+ *Chương trình Giáo dục phổ thông môn Toán* — Bộ GD&ĐT, ban hành kèm Thông tư 32/2018/TT-BGDĐT ngày 26/12/2018 — dùng để đối chiếu định hướng năng lực và yêu cầu môn học.

=== Nguồn trực tuyến dùng để đối chiếu thuật ngữ (truy cập 24/10/2026)

1. #link("https://toanmath.com/2022/01/sach-giao-khoa-toan-10-tap-1-ket-noi-tri-thuc-voi-cuoc-song.html")[Mục lục SGK Toán 10 tập 1 — TOANMATH] (toanmath.com).
2. #link("https://loigiaihay.com/ly-thuyet-tap-hop-va-cac-phep-toan-tren-tap-hop-a109830.html")[Tập hợp và các phép toán trên tập hợp — Lời giải hay] (loigiaihay.com).
3. #link("https://loigiaihay.com/ly-thuyet-bat-phuong-trinh-bac-nhat-hai-an-sgk-toan-10-ket-noi-tri-thuc-a109832.html")[Bất phương trình bậc nhất hai ẩn — Lời giải hay] (loigiaihay.com).
4. #link("https://hoc247.net/toan-10/bai-4-he-bat-phuong-trinh-bac-nhat-hai-an-l11739.html")[Hệ bất phương trình bậc nhất hai ẩn — Hoc247] (hoc247.net).
5. #link("https://vietjack.com/toan-10-kn/ly-thuyet-bai-5-gia-tri-luong-giac-cua-mot-goc-tu-0-den-180.jsp")[Giá trị lượng giác của góc từ $0°$ đến $180°$ — VietJack] (vietjack.com).
6. #link("https://loigiaihay.com/ly-thuyet-he-thuc-luong-trong-tam-giac-a109890.html")[Hệ thức lượng trong tam giác — Lời giải hay] (loigiaihay.com).
7. #link("https://vietjack.com/toan-10-kn/ly-thuyet-bai-7-cac-khai-niem-mo-dau.jsp")[Bài 7 · Các khái niệm mở đầu về vectơ — VietJack] (vietjack.com).

#note("NGUYÊN TẮC BIÊN SOẠN", [
  Các nguồn trực tuyến chỉ được dùng để đối chiếu cấu trúc, thuật ngữ và công thức phổ thông. Câu hỏi luyện nhanh, đề ôn, hình vẽ và lời giải trong tài liệu này được xây dựng mới theo ma trận; không có đề bên ngoài nào được trình bày như đề chính thức của trường.
])

== 6.4. Danh mục kiểm tra cuối cùng

#table(
  columns: (3.8fr, 1.2fr),
  table.header([#th[Hạng mục]], [#th[Trạng thái]]),
  [Đủ bốn chuyên đề và đúng phạm vi Bài 1–7], [Đã có],
  [Đủ lý thuyết, ví dụ, lỗi thường gặp, luyện nhanh có đáp án], [Đã có],
  [Đủ 12 câu chọn phương án], [12/12],
  [Đủ 2 câu đúng–sai, mỗi câu 4 ý], [8/8 ý],
  [Đủ 4 câu trả lời ngắn], [4/4],
  [Đủ 3 câu tự luận và thang điểm], [3/3],
  [Có bảng đối chiếu mức độ và nội dung từng câu], [27/27 dòng],
  [Ghi rõ giới hạn: nguồn không có đề/đáp án chính thức], [Đã ghi],
  [Có công thức ôn nhanh, hình minh họa, mục lục và số trang], [Đã có],
)
