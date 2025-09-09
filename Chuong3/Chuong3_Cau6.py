# Câu 6: Đọc số n (tối đa 2 chữ số) ra dạng chữ

chu_so = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]

n = int(input("Nhập số n (0-99): "))

if 0 <= n <= 9:
    print(chu_so[n])
elif 10 <= n <= 99:
    hang_chuc = n // 10
    hang_don_vi = n % 10
    if hang_chuc == 1:
        if hang_don_vi == 0:
            print("mười")
        elif hang_don_vi == 5:
            print("mười lăm")
        else:
            print("mười", chu_so[hang_don_vi])
    else:
        if hang_don_vi == 0:
            print(chu_so[hang_chuc], "mươi")
        elif hang_don_vi == 1:
            print(chu_so[hang_chuc], "mươi mốt")
        elif hang_don_vi == 5:
            print(chu_so[hang_chuc], "mươi lăm")
        else:
            print(chu_so[hang_chuc], "mươi", chu_so[hang_don_vi])
else:
    print("Vui lòng nhập số từ 0 đến 99.")