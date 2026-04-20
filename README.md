# Bài thực hành kiểm thử hộp đen (Black Box Testing)

## 1. Mô tả bài tập

Bài thực hành xây dựng chương trình Python gồm 8 bài toán cơ bản và áp dụng kỹ thuật kiểm thử hộp đen để thiết kế test case, kiểm tra dữ liệu hợp lệ, dữ liệu không hợp lệ, giá trị biên và các trường hợp ngoại lệ.

Chương trình có menu lựa chọn gồm 8 chức năng:

1. Tính chu vi hình chữ nhật
2. Tính diện tích hình chữ nhật
3. Giải phương trình bậc 2
4. Tính số ngày của một tháng
5. Kiểm tra số nguyên tố
6. Tính tổng S = 1 - 2 + 3 - 4 + ... + n
7. Tìm UCLN của a và b
8. Tính tổng S = 1! + 2! + 3! + ... + n!

---

## 2. Mục tiêu kiểm thử

Mục tiêu của bài thực hành là:

* Kiểm tra chương trình xử lý đúng với dữ liệu hợp lệ
* Kiểm tra chương trình xử lý lỗi với dữ liệu không hợp lệ
* Kiểm tra các giá trị biên của đầu vào
* Đảm bảo chương trình hoạt động ổn định và đúng yêu cầu đề bài

---

## 3. Kỹ thuật kiểm thử hộp đen đã áp dụng

### 3.1 Phân lớp tương đương (Equivalence Partitioning)

Chia dữ liệu đầu vào thành các nhóm:

### Hợp lệ

Ví dụ:

* Tháng từ 1 đến 12
* Chiều dài > 0
* a ≠ 0 trong phương trình bậc 2
* n > 0 với các bài tính tổng

### Không hợp lệ

Ví dụ:

* Tháng < 1 hoặc > 12
* Chiều dài ≤ 0
* a = 0
* n ≤ 0
* a = 0 và b = 0 trong bài UCLN

---

### 3.2 Phân tích giá trị biên (Boundary Value Analysis)

Kiểm tra các giá trị tại biên:

Ví dụ bài tính số ngày trong tháng:

* 0
* 1
* 2
* 11
* 12
* 13

Ví dụ bài kiểm tra n:

* -1
* 0
* 1
* 2

---

## 4. Ví dụ test case

### Bài 1: Tính chu vi hình chữ nhật

| Input              | Expected Output |
| ------------------ | --------------- |
| dài = 5, rộng = 3  | 16              |
| dài = 0, rộng = 3  | Báo lỗi         |
| dài = -2, rộng = 4 | Báo lỗi         |

---

### Bài 3: Giải phương trình bậc 2

| Input          | Expected Output    |
| -------------- | ------------------ |
| a=1, b=-3, c=2 | 2 nghiệm phân biệt |
| a=1, b=2, c=1  | nghiệm kép         |
| a=0, b=2, c=1  | Báo lỗi            |

---

### Bài 4: Tính số ngày trong tháng

| Input              | Expected Output |
| ------------------ | --------------- |
| tháng=2, năm=2024  | 29              |
| tháng=4, năm=2025  | 30              |
| tháng=13, năm=2024 | Báo lỗi         |

---

## 5. Kết quả kiểm thử

Chương trình đã được chạy thử với:

* Dữ liệu hợp lệ
* Dữ liệu không hợp lệ
* Giá trị biên
* Trường hợp ngoại lệ

Kết quả được lưu trong thư mục:

```text
test_results/
```

Bao gồm ảnh chụp màn hình quá trình chạy chương trình và kết quả kiểm thử thực tế.

---

## 6. GitHub Issues

### Issue #1

Thiết kế test case cho dữ liệu hợp lệ của 8 bài toán.

### Issue #2

Thiết kế test case cho dữ liệu không hợp lệ, giá trị biên và các trường hợp ngoại lệ.

Sau khi hoàn thành từng issue, thực hiện commit với nội dung:

```bash
git commit -m "Resolve issue #1: valid test cases"
git commit -m "Resolve issue #2: invalid and boundary test cases"
```

---

## 7. Kết luận

Qua bài thực hành này, em đã áp dụng kiểm thử hộp đen để phân tích đầu vào, thiết kế test case và kiểm tra chương trình một cách hệ thống.

Bài tập giúp hiểu rõ hơn về:

* kiểm thử phần mềm
* dữ liệu hợp lệ và không hợp lệ
* giá trị biên
* cách sử dụng GitHub trong quy trình phát triển phần mềm

Đây là nền tảng quan trọng cho việc kiểm thử phần mềm trong thực tế.
