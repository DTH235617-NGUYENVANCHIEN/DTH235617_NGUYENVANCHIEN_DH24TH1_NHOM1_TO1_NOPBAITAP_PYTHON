def cau8():
    n = int(input("Nhập số lượng phần tử n: "))
    lst = []
    for i in range(n):
        x = float(input(f"Nhập số thực thứ {i+1}: "))
        lst.append(x)
    lst.sort(reverse=True)
    print("Dãy sau khi sắp xếp giảm dần:")
    for num in lst:
        print(num, end=' ')
    print()

cau8()