import functools


def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('%s %s' % (text, func.__name__))
            return func(*args, **kwargs)
        return wrapper
    return decorator


@log('execute')
def now(a):
    print(a**2)


now(6)
print(now.__name__)
