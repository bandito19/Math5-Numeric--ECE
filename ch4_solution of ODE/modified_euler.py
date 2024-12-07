# differential equation we wish to solve
def model(x, y):
    return x**2 + y


def modified_euler(xn: float, yn: float, h: float, X: float):
    '''
    Computes the solution of ODE at a given point using modified Euler method
    xn: intial x value
    yn: intial y value
    h: step size
    X: x point at wich the y value is required
    '''
    while xn < X:
        xn1 = xn + h
        z = yn + h * model(xn, yn)
        yn += (h / 2) * (model(xn, yn) + model(xn1, z))
        xn  = xn1
    return xn, yn


print(modified_euler(0, 1,0.1, 0.1))