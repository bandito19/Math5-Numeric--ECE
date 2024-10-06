import matplotlib.pyplot as plt
import numpy as np

n = int(input("How many points do you have: "))

# x values
x = []
print("Enter X values")
for i in range(n):
    v = float(input(f"X{i}: "))
    x.append(v)
# y values
y = []
print("Enter Y values")
for i in range(n):
    v = float(input(f"Y{i}: "))
    y.append(v)

sum_x = sum(x)
sum_y = sum(y)

# x^2
sq_x = []
for i in x:
    sq_x.append(i * i)

# x * y 
xy = []
for i in range(n):
    xy.append(x[i] * y[i])

# slope 
a = (n * sum(xy) - (sum_x * sum_y)) / (n * sum(sq_x) - (sum_x * sum_x))
# intercept
b = ((sum(sq_x) * sum_y) - (sum_x * sum(xy))) / (n * sum(sq_x) - (sum_x * sum_x))
# equation
print(f"y = {round(a,4)}x + {round(b,4)}")

# plot 
x_l = np.linspace(-1, 4, 400)
y_l = a * x_l + b

plt.scatter(x, y, s=15, label='Points', color='red')
plt.plot(x_l, y_l , label=f'y = {round(a,4)}x + {round(b,4)}')
plt.xlabel('X_values')
plt.ylabel('Y_values')
plt.title('Scatter Plot of X and Y values')
plt.legend()
plt.show()
