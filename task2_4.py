# Program to split string by words with numeration
users_string = input(f'Введите, пожалуйста, строку слов, разделенных пробелами: ')
users_list = users_string.split(' ')
count = 1
for idx in users_list:
    print(f'{count} {idx:{10}}')
    count = count + 1
