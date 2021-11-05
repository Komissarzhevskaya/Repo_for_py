class Matrix:
    def __init__(self, m_1):
        self.m_1 = m_1

    def __str__(self):
        return '\n'.join([''.join(['%d\t' % el for el in line]) for line in self.m_1])

    def __add__(self, other):
        sum_m = [[self.m_1[i][j] + other.m_1[i][j] for j in range(len(self.m_1[0]))] for i in range(len(self.m_1))]
        return Matrix(sum_m)


matr_1 = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
matr_2 = [[9, 8, 7], [9, 8, 7], [9, 8, 7]]
print(f'Matrix 1: \n{Matrix(matr_1)}')
print(f'Matrix 2: \n{Matrix(matr_2)}')
print(f'Result: \n{Matrix(matr_1) + Matrix(matr_2)}')

"""try:
    lines, col = input('Введите число строк и столбцов матрицы через пробел: ').split(' ')
    user_matr_1 = [[*map(int, input('Введите элементы строки через пробел: ').split(' ')[:int(col)])]
                   for i in range(int(lines))]
    print(f'Matrix 1: \n{Matrix(user_matr_1)}')
    user_matr_2 = [[*map(int, input('Введите аналогично строки второй матрицы: ').split(' ')[:int(col)])]
                   for i in range(int(lines))]
    print(f'Matrix 2: \n{Matrix(user_matr_2)}')
    print(f'Result: \n{Matrix(user_matr_1) + Matrix(user_matr_2)}')
except ValueError as e:
    print(f'{type(e).__name__}: Please enter correct values!')"""
