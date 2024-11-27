import numpy as np


def gauss_seidel(A, b, x0, n_iterations):
    n = len(b)
    x = x0.astype(float)
    for _ in range(n_iterations):
        for i in range(n):
            
            s1 = sum(A[i][j] * x[j] for j in range(i))
            s2 = sum(A[i][j] * x[j] for j in range(i+1, n))
            x[i] = (b[i] - s1 - s2) / A[i][i]
    return x


A = np.array([[5, -1, 3], [1, 5, -2], [2, -4, 10]])
b = np.array([-2, 10, 6])
x0 = np.zeros_like(b)

solution = gauss_seidel(A, b, x0, 9)
print(solution)