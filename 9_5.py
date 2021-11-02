class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return print(f'Запуск отрисовки. {self.title}')


class Pen(Stationery):
    def draw(self):
        return print(f'\033[32m{self.title} зеленым карандашом')


class Pencil(Stationery):
    def draw(self):
        return print(f'\033[3m\033[34m{self.title} синей ручкой')


class Handle(Stationery):
    def draw(self):
        return print(f'\033[1m\033[33m{self.title} желтым маркером')


new_list = [Stationery, Pen, Pencil, Handle]
for i in new_list:
    i('Пишем текст').draw()
