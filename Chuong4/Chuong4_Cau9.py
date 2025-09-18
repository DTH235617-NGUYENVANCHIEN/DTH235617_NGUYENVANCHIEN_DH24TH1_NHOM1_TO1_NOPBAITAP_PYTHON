import math

def nested_sqrt(n):
    result = 0
    for _ in range(n):
        result = math.sqrt(2 + result)
    return result

# Chương trình chính
n = int(input("Nhập n: "))
print(f"S({n}) = {nested_sqrt(n)}")