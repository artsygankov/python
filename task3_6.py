# Program to make all first letters capital
# Похоже, что это и 7-го номера решение:)
def convert_to_capital(arg1):
    return arg1.title()

# Main flow
users_string=input('Введите, пожалуйста, строку: ')
print(f'\n Исходная строка:          {users_string}')
print(f' Конвертированная строка:  {convert_to_capital(users_string)}')
