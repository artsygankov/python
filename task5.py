# Program to decide if firm has profit
gain = int(input('Введите, пожалуйста, размер выручки: '))
expenses = int(input('Введите, пожалуйста, размер расходов: '))
if gain > expenses:
    print('Поздравляю, Вы работаете с прибылью!!!')
else:
    print('Надо что-то менять, Вы работаете в убыток')
