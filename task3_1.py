# Program with function - division of two numbers
# Define function to convert arguments and to calculate division
def division(divident, divisor):
        return divident / divisor
# Main module
while True:
    usr_input = input(
        'Введите, пожалуйста, через пробел делимое и делитель (введите S или s для выхода из программы): ')
    if usr_input == 'S' or usr_input == 's':
        break
    user_divident, user_divisor = usr_input.split();
    user_divident = int(user_divident)
    user_divisor = int(user_divisor)
    if user_divisor == 0:
        print(f'Внимание! Делитель не может быть равен нулю!')
    else:
        print(f'Ответ: {user_divident} : {user_divisor} = {division(user_divident, user_divisor)}');

