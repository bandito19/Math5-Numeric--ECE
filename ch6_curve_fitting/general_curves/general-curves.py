import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
x = [1, 1.5, 2, 2.5, 3]
y = [3, 5.69, 9.57, 14.7, 21.09]
x_range = np.linspace(0.5, 3.7, 100)

def model(x, a, b):
    return a * np.exp(b * x) + 1

popt, pcov = curve_fit(model, x, y)

print(f"a: {popt[0]:.5f}\nb: {popt[1]:.5f}")

plt.scatter(x, y)
plt.plot(x_range, model(x_range, popt[0], popt[1]), color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.show()