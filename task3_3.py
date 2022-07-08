# Program with function to calculate sum of two biggest from three args of function
def sum_2_max_numbers(arg1, arg2, arg3):
    count_list = 0
    count_outside_loop = 1
    quantity_of_max_numbers = 2
    max1 = arg1
    max2 = arg2
    numbers_list = [arg1, arg2, arg3]
    max1 = max(numbers_list)
    numbers_list.remove(max1)
    max2 = max(numbers_list)
    return max1 + max2


# Main flow
usr_input = input(f'Введите, пожалуйста, через пробел, три числа: ')
arg1, arg2, arg3 = usr_input.split()
arg1 = int(arg1)
arg2 = int(arg2)
arg3 = int(arg3)
print(f' Сумма двух максимальных из введеных чисел, равна {sum_2_max_numbers(arg1, arg2, arg3)}')
