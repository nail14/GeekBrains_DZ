##    Осуществить программу работы с органическими клетками, состоящими из ячеек. 
##    Необходимо создать класс «Клетка». В его конструкторе инициализировать параметр,
##    соответствующий количеству ячеек клетки (целое число). В классе должны быть реализованы методы перегрузки арифметических операторов: 
   ## сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__floordiv____truediv__()). Эти методы должны применяться
   ## только к клеткам и выполнять увеличение, уменьшение, умножение и округление до целого числа деления клеток соответственно.


class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __add__(self, other):
        return f'Размер клетки равен: {self.quantity + other.quantity}'

    def __sub__(self, other):
        sub = self.quantity - other.quantity
        return f'Клетка теперь равна: {sub} клеткам' if sub > 0 else 'Нет клеток'

    def __truediv__(self, other):
        return self.quantity // other.quantity

    def __mul__(self, other):
        return self.quantity * other.quantity

    def make_order(self, rows):
        result = ''
        for i in range(int(self.quantity / rows)):
            result += '*' * rows + '\n'
        result += '*' * (self.quantity % rows) + '\n'
        return result

cell = Cell(26)
cell_2 = Cell(3)
print(f'сложение:', cell + cell_2)
print(f'вычитание:', cell - cell_2)
print(f'деление:', cell / cell_2)
print(f'умножение:', cell * cell_2)
print(cell.make_order(6))
