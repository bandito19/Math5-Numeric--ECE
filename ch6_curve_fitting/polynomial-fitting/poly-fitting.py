import numpy as np
import matplotlib.pyplot as plt

# Degree of polynomial
N = int(input("What is the degree of the polynomial: "))

# Data points of experiment
x_points = input("Input X_values seperated by a space: ")
y_points = input("Input Y_values seperated by a space: ")

xs = x_points.split()
ys = y_points.split()

x = np.array([float(i) for i in xs])
y = np.array([float(i) for i in ys])

# Vandermonde Matrix of x data points
A = np.vander(x, N + 1)

# Unkown coefficients 
coeff, resid, rank, s = np.linalg.lstsq(A, y)

# polynomial form
polynomial = np.poly1d(coeff)

# plotting the results
plt.scatter(x,y, color='green', label='Date points')
x_line = np.linspace(min(x), max(x), 100)
plt.plot(x_line, polynomial(x_line), color='red', label=f'y = {polynomial}')
plt.legend()
plt.show()