# Strings: ordered, immutable, text representation
from timeit import default_timer as timer
my_string = '     hello '
my_string = my_string.strip()
print(my_string.upper())
print(my_string.find('lo'))
print(my_string.replace('hello', 'helo'))

my_string = 'how,are,you,doing'
my_list = my_string.split(',')
new_string = ' '.join(my_list)
print(new_string)

# good or bad?
my_list = ['a'] * 100000

# bad
start = timer()
my_string = ''
for i in my_list:
    my_string += i
stop = timer()
print(stop - start)

# good
start = timer()
my_string = ''.join(my_list)
stop = timer()
print(stop - start)

# formatting: %, .format(), f-Strings
var = 3.45645
var2 = 6
my_string = "the variable is %.2f" % var
print(my_string)
my_string = "the variables are {:.2f} and {}".format(var, var2)
print(my_string)
my_string = f"the variable are {var*2:.2f} and {var2}"
print(my_string)
