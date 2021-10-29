from functools import wraps


def type_logger(func):
    @wraps(func)
    def cube_type(*args, **kwargs):
        arg_nums = (i for i in (*args, *kwargs.values()) if type(i) in [float, int])
        # Вывод возведения в третью степень получился некрасивый
        inp = [f'{func.__name__}({j}: {type(j)}) {j}^3 = {func(j)}' for j in arg_nums]
        print(*inp, sep='\n')
    return cube_type


@type_logger
def calc_cube(*args, **kwargs):
    nums = [i for i in (*args, *kwargs.values()) if type(i) in [float, int]]
    return [round(x ** 3, 3) for x in nums]


calc_cube(-8, 9.3, 78, i_n=3, f_n=8.9, s_n='6')
print(f'function: {calc_cube.__name__}')
