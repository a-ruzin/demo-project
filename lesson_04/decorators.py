import sys


def dec(f):
    def x(*args, **kwargs):
        print('func is called', args, kwargs)
        f(*args, **kwargs)
    return x


def trace(file=sys.stdout):
    def inner_dec(f):
        def x(*args, **kwargs):
            print('func is called', args, kwargs, file=file)
            f(*args, **kwargs)
        return x
    return inner_dec


@trace()
def our_func(a=1, b=2, c=3, k='value'):
    return 1

our_func(3, k='another')
