# Program to create class Stationary
class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f' Начато рисование при помощи {self.title}'


class Pencil(Stationary):
    def draw(self):
        return f'Рисование карандашом начато'


class Pen(Stationary):
    def draw(self):
        return f'Рисование ручкой начато'


class Handle(Stationary):
    def draw(self):
        return f'Рисование маркером начато'


PenciL = Pencil('Карандаш')
print(PenciL.draw())
PeN = Pen('Ручка')
print(PeN.draw())
HandlE = Handle('Маркер')
print(HandlE.draw())
