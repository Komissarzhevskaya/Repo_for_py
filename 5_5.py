from time import perf_counter
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# 1
start = perf_counter()
src_set = set()
unique_src = []
for el in src:
    src_set.update('el')
    if el not in unique_src and el not in src_set:
        unique_src.append(el)
    else:
        unique_src.remove(el)
finish = perf_counter()
print(unique_src, finish - start)  # [23, 1, 3, 10, 4, 11] 1.4500000000000624e-05
# 2
start = perf_counter()
unique_src = []
src_set = set()
a = (lambda x: (unique_src.append(x), src_set.update('el')) if x not in unique_src and x not in src_set
     else unique_src.remove(x))
for i in src:
    a(i)
finish = perf_counter()
print(unique_src, finish - start)  # [23, 1, 3, 10, 4, 11] 1.0099999999998999e-05
# 3
start = perf_counter()


def new_func(b):
    new_set = set()
    new_unique = []
    for j in b:
        new_set.update('el')
        if j not in new_unique and j not in new_set:
            new_unique.append(j)
        else:
            new_unique.remove(j)
    return new_unique


finish = perf_counter()
print(new_func(src), finish - start)  # [23, 1, 3, 10, 4, 11] 5.000000000005e-07

"""Три способа реализации вывода уникальных значений. 
Если просто поместить цикл в функцию, получаем выигрыш по времени"""