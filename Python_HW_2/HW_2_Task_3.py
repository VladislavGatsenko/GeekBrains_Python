# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.


dict_var = {1: 'Зима', 2: 'Зима', 3: 'Весна', 4: 'Весна', 5: 'Весна', 6: 'Лето', 7: 'Лето', 8: 'Лето', 9: 'Осень', 10: 'Осень', 11: 'Осень', 12: 'Зима'}
list_var = ['Зима', 'Зима', 'Весна', 'Весна', 'Весна', 'Лето', 'Лето', 'Лето', 'Осень', 'Осень', 'Осень', 'Зима']

input_month = input("Введите номер месяца в году: ")

while (input_month.isdigit() != True) or (int(input_month) > 12) or (int(input_month) < 0):
    input_month = input('Пожалуйста, Введите корректный номер месяца (от 1 до 12) в году: ')
else:
    input_month = int(input_month)
    print(f"В списке  это время года называется: {list_var[input_month - 1]}")
    print(f"В словаре это время года называется: {dict_var.get(input_month)}")
