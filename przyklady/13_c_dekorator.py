import time



def zmierz_czas(func):

    def wrapper(*args, **kwargs):
        t = time.time()
        r = func(*args, **kwargs)
        print(f"wykonanie funkcji {func.__name__} zajęło: ",  time.time() - t)
        return r

    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__

    return wrapper

@zmierz_czas
def foo(n):
    suma = 0
    for i in range(n):
        x = i ** 5
        suma += x
    return suma

@zmierz_czas
def bar(n):
    """docstring funkcji bar"""
    suma = 0
    for i in range(n):
        x = i ** 1
        suma += x ** 0.5
    return suma


# t = time.time()
# foo()
# print(time.time() - t)
#
#
# t = time.time()
# bar()
# print(time.time() - t)
# bar = zmierz_czas(bar)
bar(10000)

help(bar)