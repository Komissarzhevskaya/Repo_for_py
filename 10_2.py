from abc import ABC, abstractmethod


class Clothes(ABC):
    res_exp = 0

    def __init__(self):
        pass

    @property
    @abstractmethod
    def cons(self):
        pass

    def __str__(self):
        result = Clothes.res_exp
        Clothes.res_exp = 0
        return f'{result}'

    def __add__(self, other):
        Clothes.res_exp += self.cons + other.cons
        return Clothes.res_exp


class Coat(Clothes):
    def __init__(self, size):
        super().__init__()
        self.size = size

    def size(self):
        return self.size

    @property
    def cons(self):
        return round(self.size / 6.5 + 0.5, 1)


class Suit(Clothes):
    def __init__(self, height):
        super().__init__()
        self.height = height

    def height(self):
        return self.height

    @property
    def cons(self):
        return round(2 * self.height / 100 + 0.3, 1)


try:
    us_size, us_height = input('Введите Ваш размер одежды и рост через пробел: ').split(' ')
    a = Coat(int(us_size))
    b = Suit(int(us_height))
    print(f'Для пошива пальто размера {us_size} вам потребуется {a.cons} м ткани\n'
          f'Для пошива костюма на рост {us_height} вам потребуется {b.cons} м ткани\n'
          f'Суммарный расход ткани: {a + b}')
except ValueError:
    print(f'Please enter correct values!')
