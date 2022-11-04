from cfunc import f
from func import nf
import cmath
from scipy import integrate
def self_Simpson(a, b, e):
    h, n = b-a, 1
    s1 = h * ( f(a) + 4*f((a+b)/2) + f(b) ) / 6
    s = 2*( f(a+h/4) + f(a+3*h/4) ) - f(a+h/2)
    s2 = (3*s1 + h*s)/6
    while(abs(s2-s1)>=e):
        h, s1, n, s = h/2, s2, 2*n, 0
        for k in range(0,n):
            s += 2*( f(a+h/4+k*h) + f(a+3*h/4+k*h) ) - f(a+h/2+k*h)
        s2 = (3*s1 + h*s)/6
    print('self-Simpson: ',s2)
    print('iteration times: ', int(cmath.log(n,2).real)+1)

def complex_Trapezoid(a, b, n):
    h = (b-a)/n
    t = (h * (f(a)+f(b)))/2
    for k in range(1,n):
        t += h*f(a+k*h)
    return t

def Richardson(a, b, n):
    s = ( 4*complex_Trapezoid(a, b, 2*n) - complex_Trapezoid(a, b, n) ) / 3
    c = ( 64*complex_Trapezoid(a, b, 4*n) - 20*complex_Trapezoid(a, b, 2*n) + complex_Trapezoid(a, b, n) ) / 45
    print('simpson-Richardson: ',s)
    print('complex-simpson-Richardson: ',c)

def innerMethod(a, b):
    I = integrate.quad(nf, 0, 3)
    print('inner-method: ',I)
