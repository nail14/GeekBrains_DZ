###Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения функции и выбрасывать исключение ValueError, если что-то не так,
from functools import wraps

def val_checker(func_filter):

    def checker(func):

        @wraps(func)
        def decorator(x):

            if func_filter(x):
                return func(x)

            raise ValueError from ValueError

        return decorator

    return checker

@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3
print(type(val_checker), val_checker)
print(type(wraps), wraps)

a = calc_cube(5)
print(type(a), a)
a = calc_cube(-5)
print(type(a), a)
