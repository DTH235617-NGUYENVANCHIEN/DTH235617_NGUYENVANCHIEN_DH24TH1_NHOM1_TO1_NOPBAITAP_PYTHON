#Tính giá trị biểu thức S:S(x,n)=x+(x^3)/3!+(x^5)/5!+....+x^2n+1/(2n+1)!
import math

def S(x, n):
    result = 0
    for k in range(n + 1):
        result += (x ** (2 * k + 1)) / math.factorial(2 * k + 1)
    return result

# Ví dụ: tính S(2, 3)
x = 2
n = 3
print(S(x, n))
