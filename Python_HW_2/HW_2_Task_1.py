# 1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

my_list = ['string', 4, 4.4, False, 4 + 4j, None, ['string', 4], {"name": "John", "age": 10}, ('string'), range(4), b"string", bytearray(4), memoryview(bytes(4))]

print(f'List: {my_list}\n')

for i in range(len(my_list)):
    print(f'Type of the {i + 1} element is {type(my_list[i])}')
