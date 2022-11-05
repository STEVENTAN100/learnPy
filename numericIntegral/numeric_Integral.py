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

def Simpson(a, b, n):
    if n%2==1:
        n += 1
    h, s = (b-a)/n, f(a)+f(b)
    
    for i in range(1,n,2):
        x = a+h*i
        s += 4*f(x)
    for i in range(2,n-1,2):
        x = a+h*i
        s += 2*f(x)
    s *= h/3
    return s

def recursive_Simpson(a,b,s,e):
    c = (a+b)/2
    sl, sr = Simpson(a,c,1), Simpson(c,b,1)
    sn = sl+sr
    err = abs(sn-s)/15
    if err<e:
        s = sn
        nodes = [a,c,b]
        return s, err, nodes
    else:
        sl, err1, nodes1 = recursive_Simpson(a,c,sl,e/2)
        sr, err2, nodes2 = recursive_Simpson(c,b,sr,e/2)
        s, err = sl+sr, err1+err2
        nodes = nodes1[0:-1]
        nodes.extend(nodes2)
    return sl+sr, err, nodes

def adapt_Simpson(a, b, e):
    s = Simpson(a,b,1)
    s, err, nodes = recursive_Simpson(a,b,s,e)
    return s, err, nodes

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
    t1 = (h * (f(a)+f(b)))/2
    s = f(a+h/2)
    t2 = (t1+h*s)/2
    s2 = (4*t2-t1)/3
    c1, c2 = e, 0
    while abs(c2-c1)>=e:
        c1, k, h, t1, s1, n, s = c2, k+1, h/2, t2, s2, 2*n, 0
        for i in range(n):
            s += f(a+(2*i+1)*h/2)
        t2 = (t1+h*s)/2
        s2 = (4*t2-t1)/3
        c2 = (16*s2-s1)/15
    print('Romberg: ',c2)
    print('iteration times: ', k)

def innerMethod(a, b):
    I = integrate.quad(nf, a, b)
    print('inner-method: ',I)
