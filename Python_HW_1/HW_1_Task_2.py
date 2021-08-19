# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

user_seconds = ''

while user_seconds.isnumeric() != True:
    if user_seconds.isnumeric() == True:
        break
    else:
        user_seconds = input("Введите время в секундах >>> ")
        continue

sec = int(user_seconds)
hh = sec // 3600
mm = (sec % 3600) // 60
ss = (sec % 3600) % 60

print(f"Вы ввели : {hh:02.0f}:{mm:02.0f}:{ss:02.0f}")
