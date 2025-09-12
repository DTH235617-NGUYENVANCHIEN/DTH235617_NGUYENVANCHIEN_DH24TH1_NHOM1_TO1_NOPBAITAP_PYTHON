# Câu 8: Viết chương trình tính log_a(x)

import math

# Nhập x, a từ bàn phím
x = float(input("Nhập x (x > 0): "))
a = float(input("Nhập a (a > 0, a != 1): "))

if x > 0 and a > 0 and a != 1:
    loga_x = math.log(x) / math.log(a)
    print(f"log_{a}({x}) =", loga_x)
else:
    print("Giá trị nhập vào không hợp lệ (x > 0, a > 0, a != 1).")