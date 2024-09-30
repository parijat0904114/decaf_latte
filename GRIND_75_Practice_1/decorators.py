import time


def cache_decorator(func):
    cache = {}

    def wrapper(a, b):
        start = time.time()
        if (a, b) in cache:
            print('yes in cache')
            end = time.time()
            print((end - start)*10**6)
            return cache[(a, b)]
        print('computing')
        result = func(a, b)
        cache[(a, b)] = result
        end = time.time()
        print((end - start)*10**6)
        return result
    return wrapper


@cache_decorator
def add(a: 'int', b: 'int') -> int:
    return a + b


print(add(1, 5))
print(add(1, 5))
