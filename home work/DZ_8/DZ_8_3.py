# Написать декоратор для логирования типов позиционных аргументов функции, например:
# def type_logger...
def type_logger(verbosity=0):
   def _logger(func):
       def wrapper(*args):
           result = func(*args)
           msg = f'\tcall {func.__name__}'
           if verbosity == 0:
               msg = f'{msg}({", ".join(map(str, args))})'
           if verbosity > 1:
               msg = f'{msg} -> {result}'
           return msg

       return wrapper

   return _logger

@type_logger(verbosity=2)

def calc_cube(x):
   return x ** 3
a = calc_cube(5)

print(type(a), a)
print(type(type_logger), type_logger)
