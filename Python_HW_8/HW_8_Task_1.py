# Задание # 1
# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
# строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с
# декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к
# типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
# реальных данных.

class Date:
    date: str

    def __init__(self, date: str = 'dd-mm-yyyy'):
        self.date = date

    @classmethod
    def date_get(cls, date):
        try:
            return [int(el) for el in date.split('-')]
        except ValueError:
            print("Wrong date")
            exit()

    @staticmethod
    def date_validate(date: list):
        day, month, year = date
        if 0 < day < 32 and 0 < month < 13:
            return f'Date {day:02d}:{month:02d}:{year:0004d} is correct'
        else:
            return f'Date {day:02d}:{month:02d}:{year:0004d} incorrect'


user_date = input('Type date in format dd-mm-yyyy\n>>> ')
val_date = Date.date_get(user_date)
print(Date.date_validate(val_date))

# date_example = "22-01-1980"
# date_wrong = "44-55-66"
# print(Date.date_validate(Date.date_get(date_example)))
# print(Date.date_validate(Date.date_get(date_wrong)))
