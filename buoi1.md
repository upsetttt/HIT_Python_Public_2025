Bài 1: Python là ngôn ngữ thông dịch hay biên dịch? Tại sao?
Python là ngôn ngữ thông dịch.

✅ Giải thích:
Python không biên dịch trực tiếp mã nguồn sang mã máy như ngôn ngữ C, C++, Java,... mà mã nguồn .py được dịch sang mã bytecode (file .pyc) và sau đó được thực thi bởi một trình thông dịch (interpreter) – cụ thể là Python Virtual Machine (PVM).

🔁 Quy trình hoạt động:
Viết mã nguồn Python (.py)

Python dịch sang bytecode (trung gian, không phải mã máy)

Trình thông dịch Python (PVM) thực thi bytecode

🔍 Ví dụ:
python
Copy
Edit
print("Hello, world!")
Lệnh trên không được biên dịch thành mã máy ngay mà được chạy trực tiếp bởi trình thông dịch.

✅ Kết luận:
Python là ngôn ngữ thông dịch, vì nó không cần biên dịch toàn bộ mã nguồn trước khi chạy và nó phụ thuộc vào trình thông dịch để thực thi từng dòng lệnh.


Bài 2: Tìm hiểu trước kiến thức buổi 2
1. Các kiểu dữ liệu trong Python
Kiểu dữ liệu	Mô tả	Ví dụ
int	Số nguyên	5, -10
float	Số thực (dấu phẩy động)	3.14, -2.7
str	Chuỗi ký tự	"Hello", 'Python'
bool	Giá trị đúng/sai	True, False
list	Danh sách các phần tử	[1, 2, 3], ['a', 'b']
tuple	Bộ giá trị không thay đổi	(1, 2), ('x', 'y')
dict	Từ điển (key-value)	{'name': 'Alice', 'age': 25}
set	Tập hợp không trùng lặp	{1, 2, 3}

2. Các toán tử trong Python
✅ Toán tử số học:
Toán tử	Ý nghĩa	Ví dụ
+	Cộng	3 + 2 → 5
-	Trừ	5 - 3 → 2
*	Nhân	4 * 2 → 8
/	Chia thực	5 / 2 → 2.5
//	Chia lấy nguyên	5 // 2 → 2
%	Chia lấy dư	5 % 2 → 1
**	Lũy thừa	2 ** 3 → 8

✅ Toán tử so sánh:
Toán tử	Ý nghĩa
==	Bằng
!=	Khác
>	Lớn hơn
<	Nhỏ hơn
>=	Lớn hơn hoặc bằng
<=	Nhỏ hơn hoặc bằng

✅ Toán tử logic:
Toán tử	Ý nghĩa	Ví dụ
and	Và	True and False → False
or	Hoặc	True or False → True
not	Phủ định	not True → False

3. Mệnh đề điều kiện và vòng lặp
✅ Mệnh đề điều kiện (if, elif, else)
python
Copy
Edit
a = 10
if a > 0:
    print("Số dương")
elif a == 0:
    print("Số không")
else:
    print("Số âm")
✅ Vòng lặp for
python
Copy
Edit
for i in range(5):
    print(i)
✅ Vòng lặp while
python
Copy
Edit
i = 0
while i < 5:
    print(i)
    i += 1
4. Kiểu dữ liệu True, False (kiểu bool)
True và False là 2 giá trị của kiểu dữ liệu boolean

Thường dùng trong điều kiện, logic:

python
Copy
Edit
a = 5
b = 3
print(a > b)  # True
Một số giá trị được xem là False trong Python:

None

0 (số 0)

"" (chuỗi rỗng)

[], {}, () (cấu trúc rỗng)

Nếu bạn muốn, mình có thể làm 1 file PDF hoặc bài tập ôn luyện theo từng phần.