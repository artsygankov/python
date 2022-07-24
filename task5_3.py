# Program to work with employee's salary
file_name = 'users_text_file.txt'
accounting_dict = {}
usr_sum = 0
count = 0
with open(file_name, 'r') as opened_file:
    part1 = part2 = ' '
    for line in opened_file:
        part1, part2 = line.split()
        accounting_dict[part1] = int(part2)
print(f'Список сотрудников с зарплатой больше 20000: ')
for line in accounting_dict:
    if accounting_dict[line] > 20000:
        count += 1
        usr_sum += accounting_dict[line]
        print(line, accounting_dict[line])
print(f'Среднее арифметическое окладов больше 20000 равно: {usr_sum/count}')
