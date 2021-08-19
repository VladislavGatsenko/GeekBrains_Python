# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию input().


lengthList = input('Введите количество элементов в списке: ')
userList = []
swappedUserList = []

while not lengthList.isdigit():
    lengthList = input('Пожалуйста, введите целое положительное число: ')
else:
    lengthList = int(lengthList)
    for i in range(lengthList):
        userList.append(input(f'Введите {i + 1} элемент из списка: '))
        if i % 2 == 0:
            swappedUserList.insert((i + 1), userList[i])
        else:
            swappedUserList.insert((i - 1), userList[i])

print(f'\nОригинальный список: {userList}')
print(f'Модифицированный список: {swappedUserList}')
