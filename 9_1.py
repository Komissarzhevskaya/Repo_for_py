from time import sleep


class TrafficLight:
    # первый элемент - цвет светофора, второй - продолжительность (в сек), третий - код цвета вывода
    __colors = [['Красный', 7, '31'], ['Желтый', 2, '33'], ['Зеленый', 7, '32'], ['Желтый', 2, '33']]

    def running(self):
        while True:
            for i in self.__colors:
                print(f"\033[{i[2]}m{i[0]}", end='')
                sleep(i[1])
                print('\r', end='')  # каждый последующий элемент затирает предыдущий


a = TrafficLight()
a.running()
