# differential equation we wish to solve
def model(x, y):
    return x**2 + y


def euler(xn: float, yn: float, h: float, X: float):
    '''
    Computes the solution of ODE at a given point using Euler method
    xn: intial x value
    yn: intial y value
    h: step size
    X: x point at wich the y value is required
    '''
    while xn < X:
        yn += h * (model(xn, yn))
        xn += h
    return xn, yn



print(euler(0, 1, 0.02, 0.06))