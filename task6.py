# Program to calculate profitability including per one employee
# Lets check if the firm has profit
gain = int(input('Введите, пожалуйста, размер выручки: '))
expenses = int(input('Введите, пожалуйста, размер расходов: '))
if gain > expenses:
    profitability = (gain - expenses)/gain
    print(f'Поздравляю, Вы работаете с прибылью!!! Рентабельность Вашей компании: {profitability}')
    persons_quantity = int(input('Введите численность сотрудников Вашей компании: '))
    per_person = (gain - expenses) / persons_quantity
    print(f'На каждого сотрудника Вашей компании приходится {per_person} прибыли.')
else:
    print('Надо что-то менять, Вы работаете в убыток')
