import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 1.5, 2, 2.5, 3])
y = np.array([1.41, 1.96, 2.88, 4.16, 5.8])
N = 2

A = np.vander(x, N + 1)
# print(A)

coff, resid, rank, s = np.linalg.lstsq(A, y)

polynomial = np.poly1d(coff)

plt.scatter(x,y, color='green', label='Date points')
x_line = np.linspace(min(x), max(x), 100)
plt.plot(x_line, polynomial(x_line), color='red', label=f'y = {polynomial}')
plt.legend()
plt.show()