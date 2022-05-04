class CustomException (Exception):
    def __init__(self, segm):
        self.segm = segm

def func():
    try:
        num_1 = int(input('Введите делимое: '))
        num_2 = int(input('Введите делитель: '))
        if num_2 == 0:
            raise CustomException("Делить на ноль нельзя!")
        else:
            res = num_1 / num_2
            return res
    except ValueError:
        return "Неверный операнд"
    except CustomException as err:
        return err

print("Проверка операции деления")
print(func())