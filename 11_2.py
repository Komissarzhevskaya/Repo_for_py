class ZeroDivision(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    numb = [*map(int, input('Введите делимое и делитель (натуральные) через пробел: ').split())]
    if numb[1] == 0:
        raise ZeroDivision('На ноль делить нельзя!')
    print(f'{numb[0]} / {numb[1]} = {round(numb[0] / numb[1], 2)}')
except ValueError:
    print('Вы ввели некорректные значения!')
except ZeroDivision as err:
    print(err)
