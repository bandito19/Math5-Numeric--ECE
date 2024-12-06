# The equation we wish to find root for
def model(x):
    return x**3 - 8*x +5

# Straight line joining (a,f(a)) and (b, f(b))
def line_model(a, b, f_a, f_b, x ):
    return f_a + (((f_b - f_a) / (b - a)) * (x - a))



def root(a: float, b: float):
    '''
    a: the lower limit of interval
    b: the upper limit of interval
    '''
    f_a = model(a)
    f_b = model(b)
    f_x_1 = 0
    root = 0

    
    while True:
        f_a = model(a)
        f_b = model(b)
        
        # new estimated root 
        xn = (a * f_b - b * f_a) / (f_b - f_a)
        f_xn = model(xn)
        
        if abs(f_xn - f_x_1) > 10**-5:
            if (f_xn * f_a) < 0:
                b = xn
            elif (f_xn * f_a) > 0:
                a = xn
            else:
                root = xn
                break
        else:
            root = xn
            break
        f_x_1 = f_xn


    return f"Root = {root}"

    
print(root(0, 1))

