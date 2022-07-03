# Program to create structure and some analytics
count_list = 0
count_tuple = 0
count_dict = 0
my_structure = [({})]
while True:
    users_input = input(f'Введите значение элемента списка, для завершения введите STOP или stop, и нажмите Enter: ')
    if users_input == 's' or users_input == 'S':
        break
    my_structure[count_list].