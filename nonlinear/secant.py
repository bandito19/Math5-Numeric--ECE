# The equation we wish to find root for
def model(x):
    return x**3 - 8*x +5


def root(a: float, b:float):
    '''
    a: the lower limit of interval
    b: the upper limit of interval
    '''
    x0 = a
    x1 = b
    while True:
        # new estimated root
        xn = ((x0 * model(x1)) - (x1 * model(x0))) / (model(x1) - model(x0))

        if abs(xn - x1) < 10**-5:
            return xn
        
        # updating bounds of interval
        x0, x1 = x1, xn

print(root(0, 1))

