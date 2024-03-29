# Задание #3
#
# Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо
# создать класс Клетка. В его конструкторе инициализировать параметр,
# соответствующий количеству ячеек клетки (целое число). В классе должны быть реализованы методы
# перегрузки арифметических операторов: сложение ( __add__() ), вычитание ( __sub__()) ,
# умножение ( __mul__()) , деление ( __truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и
# целочисленное (с округлением до целого) деление клеток, соответственно.

# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться
# сумме ячеек исходных двух клеток.

# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность
# количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.

# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как
# произведение количества ячеек этих двух клеток.

# Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как
# целочисленное деление количества ячеек этих двух клеток.

# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и
# количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида * ****\n*****\n*****. .., где количество ячеек между \ n
# равно переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний
# ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод
# make_order() вернет строку: *****\n*****\n** .
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод
# make_order() вернет строку: *****\n*****\n***** .


class NumberCell:
    def __init__(self, number_x: int):
        self.number_x = number_x

    def __add__(self, other):
        return f"Сложение, размер клетки равен >>> {self.number_x + other.number_x}"

    def __sub__(self, other):
        return f"Вычитание, размер клетки равен >>> {self.number_x - other.number_x}" \
            if self.number_x - other.number_x > 0 else "Клетка исчезла"

    def __mul__(self, other):
        return f"Умножение, размер клетки равен >>> {self.number_x * other.number_x}"

    def __truediv__(self, other):
        return f"Деление, размер клетки равен >>> {self.number_x // other.number_x}"

    def make_order(self, cell_row):
        row_cell = ''
        for i in range(int(self.number_x / cell_row)):
            row_cell += '*' * cell_row + '\n'
        row_cell += '*' * (self.number_x % cell_row)
        return row_cell


cell_base = NumberCell(21)
cell_change = NumberCell(3)

print(cell_base + cell_change)
print(cell_base - cell_change)
print(cell_base * cell_change)
print(cell_base / cell_change)

print(f"Метод make_order() позволяет организовать ячейки по рядам:")
print(cell_base.make_order(5))
