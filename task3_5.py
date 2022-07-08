# Program to sum many numbers
def sum_numbers(args):
    count_list = 0
    funct_sum = 0
    while count_list < len(args):
        funct_sum += float(args[count_list])
        count_list += 1
    return funct_sum


# Main flow
stop_marker = ''
numbers_list = []
while True:
    if stop_marker == 's':
        break
    users_input = input(
        ' Введите числа через пробел, для суммы нажмите ENTER, для суммы и выхода из программы, введите s : ')
    numbers_list = users_input.split()
    count = 0
    while count < len(numbers_list):
        if numbers_list[count] == 's':
            stop_marker = 's'
            numbers_list.remove('s')
        count += 1
    else:
        print(sum_numbers(numbers_list))
