# Có bao nhiêu dấu * được in ra màn hình?

count = 0
for a in range(20, 100, 5):
    print('*', end='')
    count += 1
print()
print("Số dấu * được in ra là:", count)
"""# Kết quả: Có 16 dấu * được in ra
Giải thích:
- Lệnh `range(20, 100, 5)` tạo ra dãy số bắt đầu từ 20 đến 95, mỗi lần tăng 5.
- Các giá trị của a là: 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95 (tổng cộng 16 số).
- Mỗi lần lặp, chương trình in ra một dấu * và tăng biến đếm count lên 1.
- Sau vòng lặp, biến count có giá trị 16, tức là có 16 dấu * được in ra màn hình."""