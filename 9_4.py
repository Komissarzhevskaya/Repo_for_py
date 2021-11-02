from random import choice


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return print(f'The {self.color} {self.name} is starting')

    def stop(self):
        return print(f'The {self.color} {self.name} is stopping')

    def turn(self):
        turn = ['south', 'north', 'east', 'west', 'northeast', 'northwest', 'southeast', 'southwest']
        return print(f'The {self.color} {self.name}  is turning {choice(turn)}')

    def show_speed(self):
        print(f'The {self.color} {self.name} is moving at a speed {str(self.speed)} km/h')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return print(f'{self.speed} km/h! You were speeding!')
        else:
            super().show_speed()


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=True)


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return print(f'{self.speed} km/h! You were speeding!')
        else:
            super().show_speed()


class PoliceCar(Car):
    pass


Toyota = Car(80, 'Red', 'Toyota')
Lada = TownCar(70, 'Blue', 'Lada')
Ferrari = PoliceCar(100, 'Black', 'Ferrari')
Nissan = WorkCar(40, 'White', 'Nissan')

Toyota.turn()
Lada.go()
Lada.show_speed()
Ferrari.show_speed()
Nissan.show_speed()
