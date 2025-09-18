def oscillate(start, stop):
    for i in range(start, stop + 1):
        yield i
        if i != 0:
            yield -i

# Chạy thử
for n in oscillate(-3, 5):
    print(n, end=' ')