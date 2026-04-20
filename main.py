import math


# 1. Tính chu vi hình chữ nhật

def tinh_chu_vi_hcn(chieu_dai, chieu_rong):
    if chieu_dai <= 0 or chieu_rong <= 0:
        return "Lỗi: Chiều dài và chiều rộng phải lớn hơn 0"
    return 2 * (chieu_dai + chieu_rong)


# 2. Tính diện tích hình chữ nhật

def tinh_dien_tich_hcn(chieu_dai, chieu_rong):
    if chieu_dai <= 0 or chieu_rong <= 0:
        return "Lỗi: Chiều dài và chiều rộng phải lớn hơn 0"
    return chieu_dai * chieu_rong


# 3. Giải phương trình bậc 2: ax^2 + bx + c = 0

def giai_phuong_trinh_bac_2(a, b, c):
    if a == 0:
        return "Lỗi: a phải khác 0 để là phương trình bậc 2"

    delta = b ** 2 - 4 * a * c

    if delta < 0:
        return "Phương trình vô nghiệm"
    elif delta == 0:
        x = -b / (2 * a)
        return f"Phương trình có nghiệm kép x = {x}"
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return f"Phương trình có 2 nghiệm phân biệt x1 = {x1}, x2 = {x2}"


# 4. Tính số ngày của một tháng

def la_nam_nhuan(nam):
    return (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0)


def tinh_so_ngay_trong_thang(thang, nam):
    if thang < 1 or thang > 12:
        return "Lỗi: Tháng phải từ 1 đến 12"

    if thang in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif thang in [4, 6, 9, 11]:
        return 30
    else:
        return 29 if la_nam_nhuan(nam) else 28


# 5. Kiểm tra số nguyên tố

def kiem_tra_so_nguyen_to(n):
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


# 6. Tính tổng S = 1 - 2 + 3 - 4 + ... + n

def tinh_tong_dan_dau(n):
    if n <= 0:
        return "Lỗi: n phải lớn hơn 0"

    tong = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            tong -= i
        else:
            tong += i

    return tong


# 7. Tìm UCLN của a và b

def tim_ucln(a, b):
    if a == 0 and b == 0:
        return "Lỗi: a và b không thể đồng thời bằng 0"

    a = abs(a)
    b = abs(b)

    while b != 0:
        a, b = b, a % b

    return a


# 8. Tính tổng S = 1! + 2! + 3! + ... + n!

def giai_thua(n):
    if n < 0:
        return "Lỗi: n không được âm"

    ket_qua = 1
    for i in range(1, n + 1):
        ket_qua *= i

    return ket_qua


def tinh_tong_giai_thua(n):
    if n <= 0:
        return "Lỗi: n phải lớn hơn 0"

    tong = 0
    for i in range(1, n + 1):
        tong += giai_thua(i)

    return tong


# =============================
# ISSUE #1: TEST CASE DỮ LIỆU HỢP LỆ
# =============================

# =============================
# ISSUE #2: TEST CASE DỮ LIỆU KHÔNG HỢP LỆ + BIÊN + NGOẠI LỆ
# =============================

invalid_test_cases = {
    "Bài 1 - Chu vi HCN": [
        {"input": (0, 5), "expected": "Lỗi"},
        {"input": (-2, 4), "expected": "Lỗi"}
    ],

    "Bài 2 - Diện tích HCN": [
        {"input": (0, 3), "expected": "Lỗi"},
        {"input": (-1, 6), "expected": "Lỗi"}
    ],

    "Bài 3 - PT bậc 2": [
        {"input": (0, 2, 1), "expected": "Lỗi"},
        {"input": (1, 2, 5), "expected": "vô nghiệm"}
    ],

    "Bài 4 - Số ngày trong tháng": [
        {"input": (0, 2024), "expected": "Lỗi"},
        {"input": (13, 2024), "expected": "Lỗi"}
    ],

    "Bài 5 - Số nguyên tố": [
        {"input": (1,), "expected": False},
        {"input": (-7,), "expected": False}
    ],

    "Bài 6 - Tổng luân phiên": [
        {"input": (0,), "expected": "Lỗi"},
        {"input": (-3,), "expected": "Lỗi"}
    ],

    "Bài 7 - UCLN": [
        {"input": (0, 0), "expected": "Lỗi"}
    ],

    "Bài 8 - Tổng giai thừa": [
        {"input": (0,), "expected": "Lỗi"},
        {"input": (-2,), "expected": "Lỗi"}
    ]
}


valid_test_cases = {
    "Bài 1 - Chu vi HCN": [
        {"input": (5, 3), "expected": 16},
        {"input": (10, 2), "expected": 24}
    ],

    "Bài 2 - Diện tích HCN": [
        {"input": (5, 3), "expected": 15},
        {"input": (7, 4), "expected": 28}
    ],

    "Bài 3 - PT bậc 2": [
        {"input": (1, -3, 2), "expected": "2 nghiệm phân biệt"},
        {"input": (1, 2, 1), "expected": "nghiệm kép"}
    ],

    "Bài 4 - Số ngày trong tháng": [
        {"input": (2, 2024), "expected": 29},
        {"input": (4, 2025), "expected": 30}
    ],

    "Bài 5 - Số nguyên tố": [
        {"input": (7,), "expected": True},
        {"input": (13,), "expected": True}
    ],

    "Bài 6 - Tổng luân phiên": [
        {"input": (5,), "expected": 3},
        {"input": (4,), "expected": -2}
    ],

    "Bài 7 - UCLN": [
        {"input": (12, 18), "expected": 6},
        {"input": (25, 15), "expected": 5}
    ],

    "Bài 8 - Tổng giai thừa": [
        {"input": (3,), "expected": 9},
        {"input": (4,), "expected": 33}
    ]
}


if __name__ == "__main__":
    while True:
        print("\n========== MENU 8 BÀI TOÁN ==========")
        print("1. Tính chu vi hình chữ nhật")
        print("2. Tính diện tích hình chữ nhật")
        print("3. Giải phương trình bậc 2")
        print("4. Tính số ngày trong tháng")
        print("5. Kiểm tra số nguyên tố")
        print("6. Tính tổng S = 1 - 2 + 3 - 4 + ... + n")
        print("7. Tìm UCLN của a và b")
        print("8. Tính tổng S = 1! + 2! + 3! + ... + n!")
        print("0. Thoát chương trình")

        lua_chon = input("Nhập lựa chọn của bạn: ")

        if lua_chon == "1":
            dai = float(input("Nhập chiều dài: "))
            rong = float(input("Nhập chiều rộng: "))
            print("Kết quả:", tinh_chu_vi_hcn(dai, rong))

        elif lua_chon == "2":
            dai = float(input("Nhập chiều dài: "))
            rong = float(input("Nhập chiều rộng: "))
            print("Kết quả:", tinh_dien_tich_hcn(dai, rong))

        elif lua_chon == "3":
            a = float(input("Nhập a: "))
            b = float(input("Nhập b: "))
            c = float(input("Nhập c: "))
            print("Kết quả:", giai_phuong_trinh_bac_2(a, b, c))

        elif lua_chon == "4":
            thang = int(input("Nhập tháng: "))
            nam = int(input("Nhập năm: "))
            print("Kết quả:", tinh_so_ngay_trong_thang(thang, nam))

        elif lua_chon == "5":
            n = int(input("Nhập số nguyên n: "))
            if kiem_tra_so_nguyen_to(n):
                print(f"{n} là số nguyên tố")
            else:
                print(f"{n} không phải là số nguyên tố")

        elif lua_chon == "6":
            n = int(input("Nhập n: "))
            print("Kết quả:", tinh_tong_dan_dau(n))

        elif lua_chon == "7":
            a = int(input("Nhập a: "))
            b = int(input("Nhập b: "))
            print("Kết quả:", tim_ucln(a, b))

        elif lua_chon == "8":
            n = int(input("Nhập n: "))
            print("Kết quả:", tinh_tong_giai_thua(n))

        elif lua_chon == "0":
            print("Thoát chương trình.")
            break

        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập từ 0 đến 8.")