'''
Mẫu ban đầu:
    done=False
    n,m=0,100
    while not done and n!=m:
        n=int(input())
        if n<0:
            done=True
        print("n=",n)
'''
n, m = 0, 100
while n != m:
    n = int(input())
    if n < 0:
        break
    print("n =", n)

'''Sử dụng break để thoát khỏi vòng lặp khi nhập số âm, thay cho biến done.
Vòng lặp kết thúc khi n = m hoặc khi nhập số âm.'''
