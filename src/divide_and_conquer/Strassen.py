# 矩阵乘法的strassen算法

# 矩阵乘法计算方式
def square_matrix_multiply(matrix_a, matrix_b):
    n = len(matrix_a)
    matrix_c = [[0 for __ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                matrix_c[i][j] += matrix_a[i][k] * matrix_b[k][j]
    return matrix_c


import numpy as np

def strassen(A, B):
    n = A.shape[0]
    if n != A.shape[1] or n != B.shape[0] or n != B.shape[1]:
        raise ValueError("Matrix dimensions must agree")

    if n == 1:
        return A * B

    # Split matrices into 4 sub-matrices
    A11 = A[:n//2, :n//2]
    A12 = A[:n//2, n//2:]
    A21 = A[n//2:, :n//2]
    A22 = A[n//2:, n//2:]

    B11 = B[:n//2, :n//2]
    B12 = B[:n//2, n//2:]
    B21 = B[n//2:, :n//2]
    B22 = B[n//2:, n//2:]

    # Recursively compute 7 sub-products
    P1 = strassen(A11, B12 - B22)
    P2 = strassen(A11 + A12, B22)
    P3 = strassen(A21 + A22, B11)
    P4 = strassen(A22, B21 - B11)
    P5 = strassen(A11 + A22, B11 + B22)
    P6 = strassen(A12 - A22, B21 + B22)
    P7 = strassen(A11 - A21, B11 + B12)

    # Compute the 4 sub-matrices C1, C2, C3, and C4
    C11 = P5 + P4 - P2 + P6
    C12 = P1 + P2
    C21 = P3 + P4
    C22 = P1 + P5 - P3 - P7

    # Combine the 4 sub-matrices to form the final C
    C = np.zeros((n, n))
    C[:n//2, :n//2] = C11
    C[:n//2, n//2:] = C12
    C[n//2:, :n//2] = C21
    C[n//2:, n//2:] = C22

    return C