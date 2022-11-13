# Tuple: ordered, immutable, allows duplicate elements

# unpack
my_tuple = 0, 1, 2, 3, 4

i1, *i2, i3 = my_tuple

print(i1)
print(i3)
print(i2)

# Since tuple is immutable, Python can make some internal optimizations
# the following is the difference between list and tuple
import sys
my_list = [0, 1, 2, "hello", True]
my_tuple = 0, 1, 2, "hello", True
print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(my_tuple), "bytes")

# iteration comparison
import timeit
print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000))
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000))
