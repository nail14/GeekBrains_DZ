##  import random
from time import sleep
class TrafficLight:
    # атрибуты класса
    #color = [random.randint ("Красный ", "Желтый ○", "Зеленый ☻") for i in range(0:)]   #(1, 2, 3)    #("Красный ", "Желтый ○", "Зеленый ☻")

    ##color = random.choice(["Красный ", "Желтый ○", "Зеленый ☻"])
    __color = ["Красный ", "Желтый ○", "Зеленый ☻"]
    # __a_red = "Красный "
    # __a_yellow = "Желтый ○"
    # __a_green = "Зеленый ☻"
    # метод
    def running(self):
        i = 0
        while i != 3:
            print(TrafficLight.__color[i])
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(1)
            i += 1

t = TrafficLight()
t.running()
# print(t.__color)
        #print(color())
print(f"Заводим автомобиль♣♥☻☺♦•◘○♠5♣0☺")
