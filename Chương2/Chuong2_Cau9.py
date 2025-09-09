i1 = 2
i2 = 5
i3 = -3
d1 = 2.0
d2 = 5.0
d3 = -0.5

print("a:", i1 + (i2 * i3))
print("b:", i1 * (i2 + i3))
print("c:", i1 / (i2 + i3))
print("d:", i1 // (i2 + i3))
print("e:", i1 / i2 + i3)
print("f:", i1 // i2 + i3)
print("g:", 3 + 4 + 5 / 3)
print("h:", 3 + 4 + 5 // 3)
print("i:", (3 + 4 + 5) / 3)
print("j:", (3 + 4 + 5) // 3)
print("k:", d1 + (d2 * d3))
print("l:", d1 + d2 * d3)
print("m:", d1 / d2 - d3)
print("n:", d1 / (d2 - d3))
print("o:", d1 + d2 + d3 / 3)
print("p:", (d1 + d2 + d3) / 3)
print("q:", d1 + d2 + (d3 / 3))
print("r:", 3 * (d1 + d2) * (d1 - d3))

# Giải thích cách thực hiện các lệnh:

# a: i1 + (i2 * i3)
# Nhân i2 với i3 trước (5 * -3 = -15), sau đó cộng với i1 (2 + -15 = -13)

# b: i1 * (i2 + i3)
# Cộng i2 với i3 trước (5 + -3 = 2), sau đó nhân với i1 (2 * 2 = 4)

# c: i1 / (i2 + i3)
# Cộng i2 với i3 trước (5 + -3 = 2), sau đó chia i1 cho kết quả (2 / 2 = 1.0)

# d: i1 // (i2 + i3)
# Cộng i2 với i3 trước (5 + -3 = 2), sau đó chia lấy phần nguyên (2 // 2 = 1)

# e: i1 / i2 + i3
# Chia i1 cho i2 trước (2 / 5 = 0.4), sau đó cộng với i3 (0.4 + -3 = -2.6)

# f: i1 // i2 + i3
# Chia lấy phần nguyên i1 cho i2 (2 // 5 = 0), sau đó cộng với i3 (0 + -3 = -3)

# g: 3 + 4 + 5 / 3
# Chia 5 cho 3 trước (5 / 3 ≈ 1.6667), sau đó cộng với 3 và 4 (3 + 4 + 1.6667 ≈ 8.6667)

# h: 3 + 4 + 5 // 3
# Chia lấy phần nguyên 5 cho 3 (5 // 3 = 1), sau đó cộng với 3 và 4 (3 + 4 + 1 = 8)

# i: (3 + 4 + 5) / 3
# Cộng 3, 4, 5 trước (3 + 4 + 5 = 12), sau đó chia cho 3 (12 / 3 = 4.0)

# j: (3 + 4 + 5) // 3
# Cộng 3, 4, 5 trước (3 + 4 + 5 = 12), sau đó chia lấy phần nguyên cho 3 (12 // 3 = 4)

# k: d1 + (d2 * d3)
# Nhân d2 với d3 trước (5.0 * -0.5 = -2.5), sau đó cộng với d1 (2.0 + -2.5 = -0.5)

# l: d1 + d2 * d3
# Nhân d2 với d3 trước (5.0 * -0.5 = -2.5), sau đó cộng với d1 (2.0 + -2.5 = -0.5)

# m: d1 / d2 - d3
# Chia d1 cho d2 trước (2.0 / 5.0 = 0.4), sau đó trừ d3 (0.4 - -0.5 = 0.9)

# n: d1 / (d2 - d3)
# Trừ d3 khỏi d2 trước (5.0 - -0.5 = 5.5), sau đó chia d1 cho kết quả (2.0 / 5.5 ≈ 0.3636)

# o: d1 + d2 + d3 / 3
# Chia d3 cho 3 trước (-0.5 / 3 ≈ -0.1667), sau đó cộng với d1 và d2 (2.0 + 5.0 + -0.1667 ≈ 6.8333)

# p: (d1 + d2 + d3) / 3
# Cộng d1, d2, d3 trước (2.0 + 5.0 + -0.5 = 6.5), sau đó chia cho 3 (6.5 / 3 ≈ 2.1667)

# q: d1 + d2 + (d3 / 3)
# Chia d3 cho 3 trước (-0.5 / 3 ≈ -0.1667), sau đó cộng với d1 và d2 (2.0 + 5.0 + -0.1667 ≈ 6.8333)

# r: 3 * (d1 + d2) * (d1 - d3)
# Cộng d1 với d2 trước (2.0 + 5.0 = 7.0), trừ d3 khỏi d1 (2.0 - -0.5 = 2.5), sau đó nhân tất cả (3 * 7.0 * 2.5 = 52.5)