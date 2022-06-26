# Program to find max digit in a whole positive number
user_number = int(input('Введите произвольное целое положительное число: '))
result = user_number
max_digit = 0
while result > 1:
    digit = result % 10
    if digit > max_digit:
        max_digit = digit
    result = round((result - digit)/10)
print(f' Максимальная цифра числа {user_number} - это {max_digit}')
