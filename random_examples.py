import numpy as np
import random
import secrets

a = np.random.rand(3, 4)
print(a)

b = np.random.randint(0, 10, (3, 4))
print(b)

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr)
np.random.shuffle(arr)
print(arr)
