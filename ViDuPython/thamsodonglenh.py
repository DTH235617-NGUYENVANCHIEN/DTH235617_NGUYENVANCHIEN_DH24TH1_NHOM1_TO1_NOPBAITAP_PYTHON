import sys

# Bỏ qua sys.argv[0] vì đó là tên chương trình
args = sys.argv[1:]

# Ghép tất cả tham số thành một chuỗi
chuoi = " ".join(args)

print("Chuỗi nhập từ tham số dòng lệnh là:")
print(chuoi)
print(args)