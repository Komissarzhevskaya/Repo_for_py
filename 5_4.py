from time import perf_counter
from sys import getsizeof
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# 1
a = perf_counter()


def sort_list(nums):  # Попробовала для себя вариант записи функции через исключение
    for i in range(len(nums)):
        try:
            if nums[i] < nums[i + 1]:
                yield nums[i + 1]
        except IndexError:
            return


b = perf_counter()
print(f'{[*sort_list(src)]}, size gen = {getsizeof(sort_list(src))}, size list = {getsizeof([*sort_list(src)])},'
      f' time = {b - a}')  # [12, 44, 4, 10, 78, 123], size gen = 112, size list = 120, time = 3.999999999976245e-07
# 2
c = perf_counter()
new_list = (src[i] for i in range(len(src)) if src[i - 1] < src[i] and i != 0)  # 1-ый элемент не с чем сравнивать
d = perf_counter()
print(f'{[*new_list]}, size gen = {getsizeof(new_list)}, size list = {getsizeof([*new_list])},'
      f' time = {d - c}')  # [12, 44, 4, 10, 78, 123], size gen = 112, size list = 56, time = 1.000000000001e-06

"""В случае записи генератора в функции, получаем выигрыш по времени. Однако проигрываем
 в размере итогового списка"""
