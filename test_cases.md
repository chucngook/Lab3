# Test Cases - Black Box Testing

## Bài 1: Tính chu vi hình chữ nhật

### Input

* chiều dài
* chiều rộng

### Expected Output

* Chu vi hình chữ nhật hoặc thông báo lỗi

### Valid Test Cases

| STT | Input   | Expected Output |
| --- | ------- | --------------- |
| 1   | (5, 3)  | 16              |
| 2   | (10, 2) | 24              |

### Invalid Test Cases

| STT | Input   | Expected Output |
| --- | ------- | --------------- |
| 1   | (0, 5)  | Lỗi             |
| 2   | (-2, 4) | Lỗi             |

---

## Bài 2: Tính diện tích hình chữ nhật

### Input

* chiều dài
* chiều rộng

### Expected Output

* Diện tích hình chữ nhật hoặc thông báo lỗi

### Valid Test Cases

| STT | Input  | Expected Output |
| --- | ------ | --------------- |
| 1   | (5, 3) | 15              |
| 2   | (7, 4) | 28              |

### Invalid Test Cases

| STT | Input   | Expected Output |
| --- | ------- | --------------- |
| 1   | (0, 3)  | Lỗi             |
| 2   | (-1, 6) | Lỗi             |

---

## Bài 3: Giải phương trình bậc 2

### Input

* a, b, c

### Expected Output

* 2 nghiệm phân biệt
* nghiệm kép
* vô nghiệm
* hoặc thông báo lỗi

### Valid Test Cases

| STT | Input      | Expected Output    |
| --- | ---------- | ------------------ |
| 1   | (1, -3, 2) | 2 nghiệm phân biệt |
| 2   | (1, 2, 1)  | nghiệm kép         |

### Invalid Test Cases

| STT | Input     | Expected Output |
| --- | --------- | --------------- |
| 1   | (0, 2, 1) | Lỗi             |
| 2   | (1, 2, 5) | Vô nghiệm       |

---

## Bài 4: Tính số ngày của một tháng

### Input

* tháng
* năm

### Expected Output

* số ngày trong tháng hoặc thông báo lỗi

### Valid Test Cases

| STT | Input     | Expected Output |
| --- | --------- | --------------- |
| 1   | (2, 2024) | 29              |
| 2   | (4, 2025) | 30              |

### Invalid Test Cases

| STT | Input      | Expected Output |
| --- | ---------- | --------------- |
| 1   | (0, 2024)  | Lỗi             |
| 2   | (13, 2024) | Lỗi             |

---

## Bài 5: Kiểm tra số nguyên tố

### Input

* số nguyên n

### Expected Output

* True / False hoặc thông báo kết luận

### Valid Test Cases

| STT | Input | Expected Output |
| --- | ----- | --------------- |
| 1   | (7)   | True            |
| 2   | (13)  | True            |

### Invalid Test Cases

| STT | Input | Expected Output |
| --- | ----- | --------------- |
| 1   | (1)   | False           |
| 2   | (-7)  | False           |

---

## Bài 6: Tính tổng S = 1 - 2 + 3 - 4 + ... + n

### Input

* số nguyên n

### Expected Output

* Giá trị tổng hoặc thông báo lỗi

### Valid Test Cases

| STT | Input | Expected Output |
| --- | ----- | --------------- |
| 1   | (5)   | 3               |
| 2   | (4)   | -2              |

### Invalid Test Cases

| STT | Input | Expected Output |
| --- | ----- | --------------- |
| 1   | (0)   | Lỗi             |
| 2   | (-3)  | Lỗi             |

---

## Bài 7: Tìm UCLN của a và b

### Input

* a
* b

### Expected Output

* UCLN hoặc thông báo lỗi

### Valid Test Cases

| STT | Input    | Expected Output |
| --- | -------- | --------------- |
| 1   | (12, 18) | 6               |
| 2   | (25, 15) | 5               |

### Invalid Test Cases

| STT | Input  | Expected Output |
| --- | ------ | --------------- |
| 1   | (0, 0) | Lỗi             |

---

## Bài 8: Tính tổng S = 1! + 2! + 3! + ... + n!

### Input

* số nguyên n

### Expected Output

* Tổng giai thừa hoặc thông báo lỗi

### Valid Test Cases

| STT | Input | Expected Output |
| --- | ----- | --------------- |
| 1   | (3)   | 9               |
| 2   | (4)   | 33              |

### Invalid Test Cases

| STT | Input | Expected Output |
| --- | ----- | --------------- |
| 1   | (0)   | Lỗi             |
| 2   | (-2)  | Lỗi             |

---

## Ghi chú kiểm thử

Bài thực hành áp dụng các kỹ thuật kiểm thử hộp đen gồm:

* Phân lớp tương đương (Equivalence Partitioning)
* Phân tích giá trị biên (Boundary Value Analysis)
* Dữ liệu hợp lệ và dữ liệu không hợp lệ
* Kiểm tra ngoại lệ và xử lý lỗi

Các test case được chia thành:

* Issue #1: dữ liệu hợp lệ
* Issue #2: dữ liệu không hợp lệ, giá trị biên và ngoại lệ
