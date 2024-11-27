import numpy as np


def jacobi(A, b, x0, n_iterations):
    n = len(b)
    x = x0.astype(float)

    for _ in range(n_iterations):
        new_x = np.zeros_like(x, dtype=float)
        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if i != j)
            new_x[i] = (b[i] - s) / A[i][i]
        x = new_x
    return x


A = np.array([[5, 1, -2, 1], [1, 10, -1, 2], [1, -2, 8, -1], [1, -1, 1, 4]])
b = np.array([5, 15, 20, 25])
x0 = np.zeros_like(b)
solution = jacobi(A, b, x0, 11)
print(solution)

