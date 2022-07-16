# Program to create generator with yield

def fact(n):
    for idx in range(1, n+1):
        yield idx


users_input = int(input('Введите, пожалуйста, запрашиваемый факториал: '))
factorial_result = 1
for idx1 in fact(users_input):
    factorial_result *= idx1
print(factorial_result)



