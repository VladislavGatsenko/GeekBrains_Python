# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл
# не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

from itertools import count, cycle
from random import randint

def my_count_func(start_number, stop_number):
    for el in count(start_number):
        if el > stop_number:
            break
        else:
            print(el)


def my_cycle_func(my_list, iteration):
    i = 0
    iter = cycle(my_list)
    print(my_list)
    while i < iteration:
        print(next(iter))
        i += 1

my_list = []
for i in range(10):
    my_list.append(randint(1, 50))

my_count_func(start_number=int(input("Введите начальное число:\n>>>")), stop_number=int(input("Введите конечное число:\n>>>")))
my_cycle_func(my_list, iteration=int(input("Введите итератор:\n>>>")))
