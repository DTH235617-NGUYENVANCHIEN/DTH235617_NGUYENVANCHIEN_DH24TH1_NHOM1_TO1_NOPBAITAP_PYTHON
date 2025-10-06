def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def cau9():
    n = int(input("Nhập số lượng phần tử: "))
    M = []
    for i in range(n):
        x = int(input(f"Nhập số thứ {i+1}: "))
        M.append(x)

    # Dòng 1: Số lẻ
    odd = [x for x in M if x % 2 != 0]
    print("Các số lẻ:", odd)
    print("Tổng cộng có", len(odd), "số lẻ.")

    # Dòng 2: Số chẵn
    even = [x for x in M if x % 2 == 0]
    print("Các số chẵn:", even)
    print("Tổng cộng có", len(even), "số chẵn.")

    # Dòng 3: Số nguyên tố
    primes = [x for x in M if is_prime(x)]
    print("Các số nguyên tố:", primes)

    # Dòng 4: Không phải số nguyên tố
    not_primes = [x for x in M if not is_prime(x)]
    print("Các số không phải là số nguyên tố:", not_primes)

cau9()