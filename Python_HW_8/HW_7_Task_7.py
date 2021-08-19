# Задание #7
# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив
# сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class ComplexNumber:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return ComplexNumber(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return ComplexNumber(self.x * other.x - self.y * other.y, (self.x * other.y + other.y * self.y))

    def __str__(self):
        return f'({self.x} + i{self.y})'


print(ComplexNumber(1, 2) * ComplexNumber(3, 4))
print(ComplexNumber(1, 2) + ComplexNumber(3, 4))
