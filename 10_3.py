class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        return f'Результат операции {self.quantity * "*"}'

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        return Cell(self.quantity - other.quantity) if (self.quantity - other.quantity) > 0 \
            else print('Упс! Разность количества ячеек отрицательна')

    def __mul__(self, other):
        return Cell(int(self.quantity * other.quantity))

    def __truediv__(self, other):
        return Cell(round(self.quantity // other.quantity))

    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.quantity / cells_in_row)):
            row += f'{"*" * cells_in_row}\n'
        row += f'{"*" * (self.quantity % cells_in_row)}'
        return f'Организация {self.quantity} ячеек\n{row}'


cells_1 = Cell(33)
cells_2 = Cell(9)
print(f'Сложение. {cells_1 + cells_2}')
print(f'Вычитание. {cells_1 - cells_2}')
print(f'Деление. {cells_1 / cells_2}')
print(cells_2.make_order(5))
print(cells_1.make_order(10))
