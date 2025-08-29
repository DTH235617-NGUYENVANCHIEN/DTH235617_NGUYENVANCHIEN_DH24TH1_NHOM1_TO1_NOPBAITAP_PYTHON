x = 10
y = 3
ncc = 4
number_of_closed_cases = 5

x += 1        # (a)
x /= 2        # (b)
x -= 1        # (c)
x += y        # (d)
x -= (y + 7)  # (e)
x *= 2        # (f)
number_of_closed_cases += 2 * ncc  # (g)

print("x =", x)
print("number_of_closed_cases =", number_of_closed_cases)