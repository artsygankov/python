# Program to determine season by month's number
seasons_list = ['зима', 'весна', 'лето', 'осень']
# Simple variant
seasons_dict = {1: 'зима', 2: 'зима', 12: 'зима', 3: 'весна', 4: 'весна', 5: 'весна', 6: 'лето', 7: 'лето', 8: 'лето',
                9: 'осень', 10: 'осень', 11: 'осень'}
# Smart variant
seasons_dict_smart = {1: 'зима', 2: 'весна', 3: 'лето', 4: 'осень'}
users_input = 0
while True:
    users_input = int(input(f' Введите, пожалуста, номер месяца от 1 до 12, включительно): '))
    if users_input < 1 or users_input > 12:
        print(f' Вы ввели некорректное значение номера месяца - {users_input}!')
    else:
        break
# Resolve task by list
marker = users_input
if marker == 12:
    marker = 1
marker = marker // 3
print(f'Решение через список:')
print(f'Месяц с номером {users_input}, это {seasons_list[marker]} \n')
print(f'Решение через словарь, простой вариант:')
print(f'Месяц с номером {users_input}, это {seasons_dict.get(users_input)} \n')
print(f'Решение через словарь, умный вариант:')
print(f'Месяц с номером {users_input}, это {seasons_dict_smart.get(marker+1)} \n')