##Реализовать класс Stationery (канцелярская принадлежность):
##определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
##создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
##в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
##создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    #атрибут
    title = "канцелярские принадлежности"

    #метод
    def draw(self):
        print("«Запуск отрисовки»")

class Pen(Stationery):
    def draw_1(self):
        print("Ручка пишет")

class Pencil(Stationery):
    def draw_2(self):
        print("Карандаш рисует")

class Handle(Stationery):
    def draw_3(self):
        print("Маркер помечает")

s = Stationery()
print(s.title)

p = Pen()
p.draw()
p.draw_1()

pc = Pencil()
pc.draw()
pc.draw_2()

h = Handle()
h.draw()
h.draw_3()
