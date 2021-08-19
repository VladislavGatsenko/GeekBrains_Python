def my_func(x, y):
    if y == 0:
        return 1
    y = abs(y)
    return x * my_func(x, y - 1)  # x^y=x*(x^(y-1)) рекурсивный процесс


while True:
    try:
        x = float(input("Введите действительное положительное число x: "))
        if x < 0:
            raise Exception()
        y = int(input("Введите целое отрицательное число y: "))
        if y > 0:
            raise Exception()
        print(1 / my_func(x, y))
        break
    except Exception as e:
        print('Неверный формат')
