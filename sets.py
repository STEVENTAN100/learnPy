# Sets: unordered, mutable, no duplicates

# set calculate
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(evens)
print(u)

i = odds.intersection(primes)
print(i)

diff = odds.difference(primes)
print(diff)

diff = odds.symmetric_difference(primes)
print(diff)

# update, intersection_update, difference_update and so on

print(odds.issubset(primes))
print(odds.isdisjoint(evens))

a = frozenset([1, 2, 3, 4])
print(a)
