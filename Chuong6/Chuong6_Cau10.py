
def nhap_matrix(m, n, name):
    print(f"Nhập ma trận {name}:")
    matrix = []
    for i in range(m):
        row = []
        for j in range(n):
            x = float(input(f"{name}[{i}][{j}]: "))
            row.append(x)
        matrix.append(row)
    return matrix

def cong_matrix(A, B):
    m, n = len(A), len(A[0])
    result = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(A[i][j] + B[i][j])
        result.append(row)
    return result

def hoan_vi_matrix(M):
    m, n = len(M), len(M[0])
    transposed = []
    for j in range(n):
        row = []
        for i in range(m):
            row.append(M[i][j])
        transposed.append(row)
    return transposed

def in_matrix(M, name):
    print(f"Ma trận {name}:")
    for row in M:
        print(row)

def main():
    m = int(input("Nhập số dòng: "))
    n = int(input("Nhập số cột: "))
    A = nhap_matrix(m, n, "A")
    B = nhap_matrix(m, n, "B")
    C = cong_matrix(A, B)
    print("\nKết quả cộng 2 ma trận:")
    in_matrix(C, "A+B")
    print("\nMa trận hoán vị của A:")
    in_matrix(hoan_vi_matrix(A), "A^T")
    print("\nMa trận hoán vị của B:")
    in_matrix(hoan_vi_matrix(B), "B^T")

main()