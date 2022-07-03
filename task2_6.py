# Program to create structure and some analytics
count_dict = 0
goods_dict = {}
goods_tuple = ()
goods_list = []
analytics_dict = {}
while True:
    good_name = input(' Введите, пожалуйста, наименование товара: ')
    good_price = input(' Введите, пожалуйста, цену товара: ')
    good_quantity = input(' Введите, пожалуйста, количество этого товара: ')
    good_measure = input(' Введите, пожалуйста, единицу измерения товара: ')
    goods_dict = {'Наименовние': good_name, 'Цена': good_price, 'Количество': good_quantity,
                  'Единица измерения': good_measure}
    goods_tuple = (count_dict + 1, goods_dict)
    goods_list.append(goods_tuple)
    users_input = input(
        'Для продолжения ввода нажмите Enter, для завершения, введите STOP или stop и нажмите Enter: ')
    if users_input == 'stop' or users_input == 'STOP':
        break
    count_dict = +1
print(goods_list)
