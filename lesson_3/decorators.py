# if there is multiple decorators with one func-how do i call an appropriate func vs the decorator


# def decorated_func():

# decorated_func()

from argparse import ArgumentTypeError
import time

def decorator(func):
    def wrapper(decorated_func):  # (*args, **kwargs)
        print("calling decorated f-n")
        res = func()  # (*args, **kwargs)
        res += 100

    return func


def decorator2(func):
    def wrapper(*args, **kwargs):
        print("calling decorated f-n")
        func(*args, **kwargs)
        res = 100
        return res

    return wrapper


def decorator3(func):
    def wrapper(*args, **kwargs):
        print("calling decorated f-n")
        res = func(*args, **kwargs)
        res += 100
        return res

    return wrapper


def decorator4(arg_type):
    def inner_deco(func):
        def wrapper(*args, **kwargs):
            if not all([isinstance(arg,arg_type) for arg in args]):
                raise TypeError("All arguments must be of type int")
                #raise AgrumentTypeError
            print("calling decorated f-n")
            res = func(*args, **kwargs)
            res += 100
            return res

        return wrapper



def decorator_time_score(arg_type):
    def inner_deco(func):
        def wrapper(*args, **kwargs):
            if not all([isinstance(arg,arg_type) for arg in args]):
                raise TypeError("All arguments must be of type int")
                #raise AgrumentTypeError
            start_time = time.time()
            res = func(*args, **kwargs)
            execute_time = time.time() - start_time
            print(f"Execute time for {func.__name__}: {execute_time}")
            res = func(*args, **kwargs)
            res += 100
            return res
        return wrapper
    return inner_deco



# @decorator2
# def decorated_func():
#     return 10


# @decorator3
# def decorated_func(a, b):
#     return a + b
#
# @decorator4(arg_type=int)
# def decorated_func(a, b):
#     return a + b


@decorator_time_score(arg_type=int)
def decorated_func(a, b):
    return a + b


print(decorated_func(10, 20))

