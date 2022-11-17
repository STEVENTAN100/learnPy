from numeric_Integral import *
import cmath
import cProfile
a, b, e, n = 0, 4, 1e-11, 2**20

with cProfile.Profile() as pr:
    s, err, nodes = adapt_Simpson(a, b, e)
    print('adapt-Simpson: ', s, err)
pr.print_stats()

with cProfile.Profile() as pr:
    self_Simpson(a, b, e)
pr.print_stats()

with cProfile.Profile() as pr:
    t = complex_Trapezoid(a, b, n)
    print('complex Trapezoid: ', t)
pr.print_stats()

with cProfile.Profile() as pr:
    Richardson(a, b, n)
pr.print_stats()

with cProfile.Profile() as pr:
    Romberg(a, b, e)
pr.print_stats()

with cProfile.Profile() as pr:
    innerMethod(a, b)
pr.print_stats()
