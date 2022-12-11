# Задание # 3
# Создайте собственный класс-исключение, который должен проверять содержимое списка на
# наличие только чисел. Проверить работу исключения на реальном примере. Необходимо
# запрашивать у пользователя данные и заполнять список только числами. Класс-исключение
# должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока
# пользователь сам не остановит работу скрипта, введя, например, команду “stop”. При этом
# скрипт завершается, сформированный список с числами выводится на экран.

class NotNumException(Exception):
    def __str__(self):
        print("Введено не число!")


class CheckListNumbers:
    result_list: list = []
    user_input: str

    def __init__(self, user_input):
        self.user_input = user_input

    def check(self):
        if self.user_input.isdigit():
            print(f"Элемент {self.user_input} добавлен в список")
            self.result_list.append(self.user_input)
        elif self.user_input == '':
            print(self.result_list)
            exit()
        else:
            raise NotNumException()


while True:
    next_value = CheckListNumbers(input("Введите число или enter для остановки >>> "))
    try:
        next_value.check()
    except NotNumException:
        print("Введено не число!")
