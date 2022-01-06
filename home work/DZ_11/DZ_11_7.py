class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'Сумма чисел равна : {self.a + other.a} , {self.b + other.b} '

    def __mul__(self, other):
        return f'Произведение равно: {self.a * other.a + (self.b * other.b)} , {self.b * other.a} '

c_1 = ComplexNumber(1, 5)
c_2 = ComplexNumber(4, 3)
print(c_1 + c_2)
print(c_1 * c_2)
c_1 = ComplexNumber(8, 5)
c_2 = ComplexNumber(2, 10)
print(c_1 + c_2)
print(c_1 * c_2)