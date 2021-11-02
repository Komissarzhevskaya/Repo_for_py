class Road:

    def __init__(self, length, wight):
        self._length = length
        self._wight = wight

    def calculation(self, weight=25, thick=5):
        res = self._length * self._wight * weight * thick // 1000
        return print(f'Для покрытия участка дороги {self._length}x{self._wight}x{thick} необходимо {res} т. асфальта')


try:
    x, y = input('Введите длину и ширину дороги через пробел: ').split(' ')
    a = Road(int(x), int(y))
    a.calculation()
except ValueError:
    print('Введите корректное целое значение!')
