from abc import ABC, abstractmethod

class Clothes(ABC):

    def __init__(self, param):
        self.param = param

    @property
    def tissue_consumption(self):
        return f'Сумма затраченной ткани равна: {self.param / 6.5 + 0.5 + 2 * self.param + 0.3 :.2f}'
    print(tissue_consumption)

    @abstractmethod
    def abstract(self):
        return 'недописано'

class Coat(Clothes):
    def tissue_consumption(self):
        return f'Для пошива пальто нужно: {self.param / 6.5 + 0.5 :.2f} м2 ткани'


    def abstract(self):
        return 'check abstract method not implemented!'

class Costume(Clothes):
    def tissue_consumption(self):
        return f'Для пошива костюма нужно: {2 * self.param + 0.3 :.2f} м2 ткани'

    def abstract(self):
        pass

coat = Coat(40)
costume = Costume(5)
print(coat.tissue_consumption())
print(costume.tissue_consumption())
print(coat.abstract())
