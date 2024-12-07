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


A = np.array([[5, -1, 3], [1, 5, -2], [2, -4, 10]])
b = np.array([-2, 10, 6])
x0 = np.zeros_like(b)
solution = jacobi(A, b, x0,9)
print(solution)

