# Program to convert single number n to n+nn+nnn
user_number = input('Введите, пожалуйста, произвольное число: ')
single_n = int(user_number)
double_n = int(user_number + user_number)
triple_n = int(user_number + user_number + user_number)
sum_n = single_n + double_n + triple_n
print (f'Результат: {single_n}+{double_n}+{triple_n}={sum_n}')
