# generators are memory efficient, especially processing big numbers
import sys


def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums


def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1


print(sys.getsizeof(firstn(1000)))
print(sys.getsizeof(firstn_generator(1000)))


def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a+b


fib = fibonacci(30)
for i in fib:
    print(i)

# [] stands for lists, () stands for generator
mygenerator = (i for i in range(10) if i % 2 == 0)
for i in mygenerator:
    print(i)
