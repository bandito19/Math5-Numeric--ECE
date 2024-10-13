# least-square-fitting-of-polynomials

In polynomial fitting, the goal is to find a polynomial of degree 𝑚
that best fits a set of data points(x<sub>i</sub>, y<sub>i</sub>) in a least-squares sense.
To do this, we set up a system of equations where the polynomial:
```math
\ p(x) = c_0 + c_1 x + c_2 x^2 + \cdots + c_m x^m \
```
This equation can be written in matrix form as:
```math
A⋅c=y
```
Where:
- $A$ is the Vandermonde matrix, constructed from the *x* values.
- $c$ = $[cm, c_{m-1},…,c_1,c_0]^T$
- $y$ are the *y* data points
Now the system is a set of linear equations that can be solved
to find coefficients $c$ that that minimize the sum of squared errors between the predicted values 
$𝑝(𝑥_𝑖)$  and the observed values $𝑦_𝑖$.

