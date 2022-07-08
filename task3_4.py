# Program to rise in a power
def raise_in_power_simple(basis, power):
    return basis ** power


def raise_in_power_loop(basis, power):
    count = 1
    power_level = abs(power)
    result = 1
    while count <= power_level:
        result = result * (1 / basis)
        count = count + 1
    return result


# Main flow
users_input = input('Введите, пожалуйста, через пробел, вещественное положительное число и целое отрицательное чило:  ')
basis, power = users_input.split()
basis = float(basis)
power = int(power)
print(basis, power * power)
print(f'Вывод: {basis} в степени {power}, равно: 1). простое решение: {raise_in_power_simple(basis, power)}, 2). с циклами {raise_in_power_loop(basis,power)}')
