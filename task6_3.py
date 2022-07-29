# Program to create basic class
class Worker:
    def __init__(self, name, surname, position, income, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f' Полное имя: {self.name} {self.surname}'

    def get_full_profit(self):
        return f'Доход с учетом премии: {sum(self._income.values())}'


wrkr = Position('Ким', 'Космолетов', 'Капитан "Синей Чайки"', 7500000, 1500000, 5000000)
print(wrkr.get_full_name())
print(wrkr.get_full_profit())
