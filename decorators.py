# a decorator function that prints debug information about the wrapped function
import functools


def start_end_decorator_4(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Start')
        result = func(*args, **kwargs)
        print('End')
        return result
    return wrapper


def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {result!r}")
        return result
    return wrapper


@debug
@start_end_decorator_4
def say_hello(name):
    greeting = f'Hello {name}'
    print(greeting)
    return greeting


# now `debug` is executed first and calls `@start_end_decorator_4`, which then calls `say_hello`
say_hello(name='Alex')
