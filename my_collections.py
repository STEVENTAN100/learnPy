# collections: Counter, namedtuple, OrderedDict, defaultdict, deque
from collections import Counter, namedtuple, OrderedDict, defaultdict, deque
a = "aaaaabbbbccc"
my_counter = Counter(a)
print(my_counter)
print(my_counter.most_common(2)[0][0])
print(list(my_counter.elements()))

# like creating a class
Point = namedtuple('Point', 'x,y')
pt = Point(1, -4)
print(pt)

# python3.7 or more wouldn't need OrderedDict

d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print(d['c'])

d = deque()

d.append(1)
d.append(2)

d.appendleft(3)
print(d)

d.popleft()
print(d)

d.extendleft([4, 5, 6])
print(d)

d.rotate(1)
print(d)
