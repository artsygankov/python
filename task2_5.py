# Program to resolve rating task
my_list = [197, 7, 5, 4, 4, 2]
print(f'Текущий рейтинг натуральных чисел: \n {my_list}')
users_input = int(input('Введите, пожалуйста, новое значение для рейтинга: '))
idx = 0
right_border = len(my_list) - 1
while idx <= right_border:
    if users_input >= my_list[idx]:
        my_list.insert(idx, users_input)
        break
    elif idx == right_border:
        my_list.insert(len(my_list), users_input)
        break
    idx = idx + 1
print(f' Новый рейтинг натуральных чисел: \n {my_list}')

