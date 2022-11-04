from numeric_Integral import *
import cmath
a, b, e, n = 0, 3, 1e-11, 2**20
self_Simpson(a,b,e)
t = complex_Trapezoid(a,b,n)
print('complex Trapezoid: ',t)
Richardson(a,b,n)
Romberg(a,b,e)
innerMethod(a,b)
