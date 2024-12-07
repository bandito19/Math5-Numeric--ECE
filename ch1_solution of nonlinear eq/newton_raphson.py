# The equation we wish to find root for
def model(x):
    return x**3 - 8*x +5

def driv(x: float):
     '''
     Computes derivative of a function at given `x` point
     '''
     h = 1e-5
     return (model(x + h) - model(x- h)) / (2 * h)


def root(xn):
    h = (model(xn) / driv(xn)) 
    while abs(h) >= 1e-5:
        h = (model(xn) / driv(xn)) 
        xn = xn - h
        
    return xn

print(f"Root = {root(0):5f}")
        
        
