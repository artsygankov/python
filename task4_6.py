# Program with iterator
from itertools import count, cycle

start_number = int(input(f'Введите, пожалуйста, начальное число: '))
print(f'Вывод результатов первого подзадания: ')
for idx in count(start_number):
    if idx > 15:
        break
    else:
        print(idx)
print(f'Вывод результатов второго подзадания: ')
some_list = ['Предварительное', 'Промежуточное', 'Главное', 'Прошел контакт подъема', 'Есть отделение!']
count_user = 0
for idx in cycle(some_list):
    print(f'{count_user} {idx}')
    count_user += 1
    if count_user > 15:
        break
