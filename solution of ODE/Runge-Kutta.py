# differential equation we wish to solve
def model(x, y):
    return 3*x + y**2   


def RK2(xn: float, yn: float, h: float):
    '''
    Computes the Runge-Kutta approximation of order 2
    xn: intial x value
    yn: intial y value
    h: step size
    '''
    k = h * model(xn, yn)
    yn += h * model(xn + h/2, yn + k/2)
    xn += xn + h
    return xn, yn


def RK4(xn: float, yn: float, h: float):
    '''
    Computes the Runge-Kutta approximation of order 4
    xn: intial x value
    yn: intial y value
    h: step size
    '''
    k1 = h * model(xn, yn)
    k2 = h * model(xn + h/2, yn + k1/2)
    k3 = h * model(xn + h/2, yn + k2/2)
    k4 = h * model(xn + h, yn + k3)

    yn += 1/6 * (k1 + 2*k2 + 2*k3 + k4)
    xn += h

    return xn, yn


print(RK2(0, 0, 0.2))

print(RK4(0, 1, 0.1))