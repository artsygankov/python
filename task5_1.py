# Porgram to write user's text into text file
from random import random


def write_to_file(user_text):
    with open(file_name, 'a') as file_usr:
        file_usr.writelines(user_text)


# Maim program flow
file_name ='users_text_file.txt'
try:
    f = open(file_name, 'x')
    f.close()
except FileExistsError:
    usr_request = input(
        'Такой файл уже существует! Для перезаписи введите Y, для создания файла с произвольным имененм, '
        'нажмите ENTER: ')
    if usr_request == 'Y' or usr_request == 'y':
        f = open('users_text_file.txt', 'w')
        f.close()
    else:
        file_name = 'users_text_file_' + str(round(random() * 1000)) + '.txt'
        f = open(file_name, 'w')
        f.close()
# Ask lines from user
while True:
    usr_input = input('Введите строчки для созранения в файл, для завершения ввода, введите пустую строку: ')
    if usr_input == '':
        break
    result_string = usr_input + '\n'
    write_to_file(result_string)
