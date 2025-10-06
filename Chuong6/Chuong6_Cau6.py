def cau6():
    N = int(input("Nhập số lượng phần tử N: "))
    lst = []
    while len(lst) < N:
        x = int(input(f"Nhập số thứ {len(lst)+1}: "))
        if x not in lst:
            lst.append(x)
        else:
            print("Số đã tồn tại, nhập lại!")
    print("List vừa nhập:", lst)

# Gọi hàm để chạy chương trình
cau6()