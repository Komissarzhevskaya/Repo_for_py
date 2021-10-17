from itertools import islice

n = int(input("Please, inter the number of odd numbers: "))


# 1
def gen_odd(num):
    for i in range(1, num + 1):
        if i % 2 != 0:
            yield i


num_gen = gen_odd(n)
print(*islice(num_gen, n), type(num_gen))  # 1 3 5 7 <class 'generator'>
# 2
num_gen_2 = (i for i in range(1, n + 1) if i % 2 != 0)
print(*islice(num_gen_2, n), type(num_gen_2))  # 1 3 5 <class 'generator'>
