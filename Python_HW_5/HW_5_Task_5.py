# Задание # 5
# Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint

with open('HW_5_Task_5_DATA.txt', 'w', encoding='utf-8') as put:
    for num in range(20):
        put.write(str(randint(0, 1000)) + ' ')
with open('HW_5_Task_5_DATA.txt', 'r', encoding='utf-8') as put:
    print(sum(int(i) for i in put.readline().split()))
