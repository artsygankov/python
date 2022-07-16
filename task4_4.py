# Program to generate list with nonrepitable elements with original order
start_list = [1, 4, 1, 4, 754, 74, 4, 7, 69, 5, 45, 9, 0, 544, 7, 9, 54, 3, 7, 9, 4, 6, 5]
result_list = [member for member in start_list if start_list.count(member) == 1]
print(f'[ Для исходного списка: {start_list} \n Список не повторяющихся элементов с сохранением плоркда следования: '
      f'{result_list}')
