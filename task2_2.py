# Program to change list elements by places
start_list = []
# Creating list without requesting the length of the list
while True:
    users_input = input(f'Введите значение элемента списка, для завершения введите S или s, и нажмите Enter: ')
    if users_input == 's' or users_input == 'S':
        break
    start_list.append(users_input)
# Calculating the "right border" of the list
right_border = len(start_list)
if right_border % 2 != 0:
    right_border = right_border - 1
# Printing non modified list
print(f' Это первоначальный список \n {start_list}')
# Loop to change elements of the list by places
count = 0
while count < right_border:
    start_list[count], start_list[count + 1] = start_list[count + 1], start_list[count]
    count = count + 2
print(f' Это измененный список \n {start_list}')
