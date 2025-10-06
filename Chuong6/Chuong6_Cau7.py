def cau7():
    N = int(input("Nhập số lượng phần tử N: "))
    while True:
        lst = []
        for i in range(N):
            x = int(input(f"Nhập số thứ {i+1}: "))
            lst.append(x)
        if all(lst[i] <= lst[i+1] for i in range(len(lst)-1)):
            break
        print("Dãy không tăng, nhập lại!")
    print("Dãy tăng vừa nhập:", lst)
    print("Các số trong dãy là:")
    for num in lst:
        print(num, end=' ')
    print()

cau7()