# The equation we wish to find root for
def model(x):
    return x**3 - 8*x +5


def root(a: float, b:float):
    '''
    a: the lower limit of interval
    b: the upper limit of interval
    '''

    f_a = model(a)
    f_b = model(b)
    f_x_1 = 0
    while True:
        # new estimatetd root
        xn = (a + b) / 2
        f_xn = model(xn)
        
        if abs(f_xn - f_x_1) > 10**-5:
            if (f_a * f_xn) < 0:
                b = xn
            elif (f_b * f_xn) < 0:
                a = xn
            else:
                root == xn
                break

        else:
            root = xn
            break
        
    return f"Root = {root:.5f}"

print(root(0,1))
