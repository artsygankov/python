# Program to calculate seconds to minutes and hours
time_seconds_entered = int(input('Введите время в секундах, для конвертации в формат чч:мм:сс '))
time_hours = time_seconds_entered // 3600
time_minutes = (time_seconds_entered % 3600) // 60
time_seconds = (time_seconds_entered % 3600) % 60
print(f'Вывод: {time_seconds_entered} секунд, это {time_hours}:{time_minutes}:{time_seconds}')
