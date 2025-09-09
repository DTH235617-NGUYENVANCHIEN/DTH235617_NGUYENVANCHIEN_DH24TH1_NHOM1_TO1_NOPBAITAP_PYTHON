def test(i, j, k):
    if i < j:
        if j < k:
            i = j
        else:
            j = k
    else:
        if j > k:
            j = i
        else:
            i = k
    print("i =", i, ", j =", j, ", k =", k)

# (a) i = 3, j = 5, k = 7
test(3, 5, 7)   # i = 5 , j = 5 , k = 7

# (b) i = 3, j = 7, k = 5
test(3, 7, 5)   # i = 7 , j = 5 , k = 5

# (c) i = 5, j = 3, k = 7
test(5, 3, 7)   # i = 7 , j = 3 , k = 7

# (d) i = 5, j = 7, k = 3
test(5, 7, 3)   # i = 7 , j = 5 , k = 3

# (e) i = 7, j = 3, k = 5
test(7, 3, 5)   # i = 7 , j = 7 , k = 5

# (f) i = 7, j = 5, k = 3
test(7, 5, 3)   # i = 7 , j = 7 , k =