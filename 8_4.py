from functools import wraps


def val_checker(lambda_f):
    def _val_checker(calc_f):
        @wraps(calc_f)
        def wrapper(arg):
            if lambda_f(arg):  # True - x > 0, False - x <= 0
                print(f'{arg}^3 = {calc_f(arg)}')
            else:
                raise ValueError

        return wrapper
    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


for i in range(-1, 3):
    try:
        calc_cube(i)
    except ValueError as e:
        print(f"{type(e).__name__}: wrong val {i}")
# Если аргумент функции вводит пользователь - перехватываем исключение TypeError
