from cfunc import f
from func import nf
import cmath
from scipy import integrate
def self_Simpson(a, b, e):
    h, n = b-a, 1
    s1 = h * ( f(a) + 4*f((a+b)/2) + f(b) ) / 6
    s = 2*( f(a+h/4) + f(a+3*h/4) ) - f(a+h/2)
    s2 = (3*s1 + h*s)/6
    while abs(s2-s1)>=e:
        h, s1, n, s = h/2, s2, 2*n, 0
        for k in range(n):
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

def Romberg(a, b, e):
    h, k, n = b-a, 1, 1 
    t1 = (h * (nf(a)+nf(b)))/2
    s = nf(a+h/2)
    t2 = (t1+h*s)/2
    s2 = (4*t2-t1)/3
    c1, c2 = e, 0
    while abs(c2-c1)>=e:
        c1, k, h, t1, s1, n, s = c2, k+1, h/2, t2, s2, 2*n, 0
        for i in range(n):
            s += nf(a+(2*i+1)*h/2)
        t2 = (t1+h*s)/2
        s2 = (4*t2-t1)/3
        c2 = (16*s2-s1)/15
    print('Romberg: ',c2)
    print('iteration times: ', k)

def innerMethod(a, b):
    I = integrate.quad(nf, a, b)
    print('inner-method: ',I)
