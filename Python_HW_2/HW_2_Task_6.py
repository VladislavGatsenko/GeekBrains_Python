# 6. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например название, а значение — список значений-характеристик, например список названий товаров.

#Первая часть: формирование структуры данных «Товары»
src_list = ["название", "цена", "кол-во", "ед"]
in_list = []
result_list = []
index = 1
in_str = " "
while in_str:
    in_str = input("Введите через запятую : (название, цену, количество, единицу измерения) вашего товара \n(или enter для завершения)\n>>> ")
    if in_str == "":
        print("Ввод завершен")
        break
    in_list = in_str.split(",")

    tmp_list = []
    for el in in_list:
        tmp_list.append(el.strip(" "))
    if len(src_list) != len(tmp_list):
        print("Вы ошиблись, попробуйте еще раз")
    else:
        new_set = {src_list[0]: tmp_list[0], src_list[1]: tmp_list[1],
                   src_list[2]: tmp_list[2], src_list[3]: tmp_list[3]}
        new_tuple = (index, new_set)
        index += 1
        result_list.append(new_tuple)
        print(new_tuple)

print("Вы ввели данные по товарам :")
for i in range(len(result_list)):
    print(f"{result_list[i]}")

#Вторая часть: аналитика о товарах
analitic_set = {}
tmp_list = []
for i in range(len(src_list)):
    for j in range(len(result_list)):
        tmp_list.append(result_list[j][1][src_list[i]])
    analitic_set[src_list[i]] = tmp_list
    tmp_list = []
print("Мы проанализировали информацию :")
for i in analitic_set.items():
    print(f"{i}")
