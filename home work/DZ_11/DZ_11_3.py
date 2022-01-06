class MyError(Exception):
    def __init__(self):
        pass
class TypeCheck:
    def __init__(self):
        self.my_list = []
    def check_value(self):
        global user_var
        while True:
            try:
                try:
                    user_var = int(input('Введите числа: '))
                    ex = input(f'Добавляем "{user_var}" в список. \n Хотите продолжить? y/n: ').lower()
                    self.my_list.append(user_var)
                    if ex == 'n' or ex != 'y':
                        print(self.my_list)
                        break
                except ValueError:
                    raise MyError
            except MyError:
                ex = input(f"Неверный операнд! \n Хотите продолжить? y/n: ").lower()
                if ex == 'n' or ex != 'y':
                    print(self.my_list)
                    break
                else:
                    self.check_value()

a = TypeCheck()
a.check_value()