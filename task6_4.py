# Program to create class Car

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        return f'Текущая скорость автомобиля {self.name}: {self.speed}'

    def go(self):
        return f'Автомобиль {self.name} поехал'

    def stop(self):
        return f'Автомобиль {self.name} остановился'

    def turn(self):
        return f'Автомобиль {self.name} повернул'


class Citycar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Запрошенная скорость движения автомобиля {self.name} - {self.speed}, НО сокрость в городе ограничена 60 км/ч')
            self.speed = 57
        return f'Текущая скорость автомобиля {self.name}: {self.speed} км/ч'


class Policecar(Car):
    def siren(self):
        return f'Включен проблесковый маячок и сирена! Всем уступить дорогу!'

class Workcar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Запрошенная скорость движения автомобиля {self.name} - {self.speed}, НО сокрость на крьере '
                  f'ограничена 40 км/ч')
            self.speed = 40
        return f'Текущая скорость автомобиля {self.name}: {self.speed} км/ч'

CityCar = Citycar(100, 'Красный', "Pontiac", False)
PoliceCar = Policecar(210, 'Белый', 'Nissan SkyLine', True)
WorkCar=Workcar(30,'Оранжевый','БЕЛАЗ', False)
WorkCar=Workcar(50,'Оранжевый','БЕЛАЗ', False)
print(CityCar.go())
print(CityCar.show_speed())
print(PoliceCar.show_speed())
print(WorkCar.show_speed())
print(WorkCar.turn())
