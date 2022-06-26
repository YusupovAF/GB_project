'''Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения функции и
выбрасывать исключение ValueError, если что-то не так, например:
def val_checker...
    ...
@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3
>>> a = calc_cube(5)
125
>>> a = calc_cube(-5)
Traceback (most recent call last):
  ...
    raise ValueError(msg)
ValueError: wrong val -5
Примечание: сможете ли вы замаскировать работу декоратора?'''

from functools import wraps

def dummy_dec(func):
    @wraps(func)
    def wrapper(*args):
        print('dummy dec')
        result = func(*args)
        return result
    return wrapper

def val_checker(check_func):
    def inner_wrapper(func):
        def wrapper(*args):
            print(f'check args for func: {func.__name__}')
            for arg in args:
                if not check_func(arg):
                    raise ValueError(f'Wrong val {arg}')
            result = func(*args)
            return result
        return wrapper
    return inner_wrapper

@val_checker(lambda x: x > 0)
@dummy_dec
def calc_cube(x):
    return x ** 3

print(calc_cube(5))
print(calc_cube(-5))
