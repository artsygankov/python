# Program to calculate quantity of days to reach desired result
fist_day_kilometers = int(input('Сколько километров спортсмен пробежал в первый день? '))
target_kilometers = int(input('Сколько километров нужно пробегать? '))
curr_kilometers = fist_day_kilometers
count = 0
while curr_kilometers < target_kilometers:
    curr_kilometers = curr_kilometers + curr_kilometers/10
    count = count + 1
print(f'Для того, чтобы улучшить результат с {fist_day_kilometers} км до {target_kilometers} км, спортсмену понадобится {count} дней.')
