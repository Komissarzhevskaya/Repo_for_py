class ComplexNumber:
    def __init__(self, param_1, param_2):
        self.param_1 = int(param_1)
        self.param_2 = int(param_2)

    def __str__(self):
        if self.param_2 == 0:
            return '{}'.format(self.param_1)
        elif self.param_2 < 0:
            return '{}{}i'.format(self.param_1, self.param_2)
        elif self.param_1 == 0:
            return '{}i'.format(self.param_2)
        return '{}+{}i'.format(self.param_1, self.param_2)

    def __add__(self, other):
        return ComplexNumber(self.param_1 + other.param_1, self.param_2 + other.param_2)

    def __mul__(self, other):
        x_1, x_2, y_1, y_2 = self.param_1, other.param_1, self.param_2, other.param_2
        return ComplexNumber(x_1 * x_2 - y_1 * y_2, x_1 * y_2 + y_1 * x_2)


try:
    x, y = input('Введите действительную и мнимую часть первого комплексного числа через пробел: ').split()
    k, z = input('Введите действительную и мнимую часть второго комплексного числа через пробел: ').split()
    compl = ComplexNumber(x, y)
    compl_2 = ComplexNumber(k, z)
    print(f'({compl})+({compl_2}) = {compl + compl_2}')
    print(f'({compl})*({compl_2}) = {compl * compl_2}')
except ValueError:
    print('Введите корректные значения!')
