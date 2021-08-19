def my_function(x, y):
    try:
        z = x / y
        return z
    except ZeroDivisionError:
        return "y не является 0"
    except ValueError:
        return "Введите только номер"


print(my_function(int(input("Введите x = ")), int(input("Введите y = "))))
