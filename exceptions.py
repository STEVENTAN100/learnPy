# Errors and Exceptions
x = 5
if x < 0:
    raise Exception('x should be positive')
assert (x >= 0), 'x is not positive'

try:
    a = 5/1
    b = a+'10'
# except Exception as e:
#     print(e)
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print('everyting is fine')
finally:
    print('cleaning up...')

# customized exceptions


class ValueTooHighError(Exception):
    pass


class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value


def test_value(x):
    if x > 100:
        raise ValueTooHighError('value is too high')
    if x < 5:
        raise ValueTooSmallError('value is too small', x)


try:
    test_value(2)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)
