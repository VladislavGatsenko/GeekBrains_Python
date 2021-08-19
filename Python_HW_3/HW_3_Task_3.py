def my_func():
    x = float(input("Введите число x: "))
    y = float(input("Введите число y: "))
    z = float(input("Введите число z: "))
    return x + y + z - min(x, y, z)


print("Сумма двух максимальных чисел = ", my_func())
