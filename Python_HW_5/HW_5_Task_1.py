# Задание # 1
# Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

import os

file_path = os.path.join(os.path.dirname(__file__), 'HW_5_Task_1_DATA.txt')

with open(file_path, 'w+', encoding='UTF-8') as file_obj:
    while True:
        input_data = input('Введите данные для файла:\n>>>')
        if not input_data:
            break
        file_obj.write(f'{input_data}\n')
