# Program to work with command prompt parameters
from sys import argv
script_name, worked_hours, pay_per_hour, bonus = argv
print(f'Сотрудник отработал:')
print(f'{worked_hours} час(а)ов, его ставка составляет: {pay_per_hour} тугрик(а)ов в час, премия: {bonus} тугрик(а)ов')
print(f'Итого, работник заработал: {(float(worked_hours) * float(pay_per_hour)) + float(bonus)} тугрик(а)ов')
