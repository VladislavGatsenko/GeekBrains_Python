def my_func(*args):
    result = 0
    flag = False
    for itm in args:
        try:
            result += float(itm) if itm else 0
        except ValueError:
            if itm == 'q':
                flag = not flag
                break
    return result, flag


user_input_sum = 0
while True:
    user_input = input('Введите числа через пробел\n').split(' ')
    result_sum, exit_flag = my_func(*user_input)
    user_input_sum += result_sum
    print(f'{user_input_sum}')

    if exit_flag:
        print('Выход')
        break
