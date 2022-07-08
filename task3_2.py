# Program to call function with personal data
def out_finction(name, last_name, birth_year, city, email, phone):
    result_string = name + ' ' + last_name + ' ' + birth_year + ' ' + city + ' ' + email + ' ' + phone
    return result_string
usr_string = input(
    'Введите, пожалуйста, через пробел имя, фамилию, год рождения, город проживания, email и телефон пользователя: ')
usr_name, usr_last_name, usr_birth_year, usr_city, usr_email, usr_phone = usr_string.split()
print(
    f'Выводим персональные данные одной строкой: {out_finction(name=usr_name, last_name=usr_last_name, birth_year=usr_birth_year, city=usr_city, email=usr_email, phone=usr_phone)}')
