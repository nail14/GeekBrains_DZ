class Car:
    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f' {self.name} едет.'

    def stop(self):
        return f'\n {self.name} остановился.'

    def turn(self, direction):
        return f'\n {self.name} повернул на {direction}'

    def show_speed(self):
        return f'\n Ваша скорость {self.speed}'

    def colorcar(self):
        return f' цвет {self.color}'

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'\n Ваша скорость выше допустимой! Ваша скорость {self.speed}'
        else:
            return f'Ваша скорость {self.name} в норме'

class SportCar(Car):
    def show_speed(self):
        if self.speed > 120:
            return f'\n Ваша скорость выше допустимой! Ваша скорость {self.speed}'
        else:
            return f'Ваша скорость {self.name} в норме'

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\n Ваша скорость выше допустимой! Ваша скорость {self.speed}'
        else:
            return f'Ваша скорость {self.name} в норме'

class PoliceCar(Car):
    def show_speed(self):
        if self.speed > 100:
            return f'\n Ваша скорость выше допустимой! Ваша скорость {self.speed}'
        else:
            return f'Ваша скорость {self.name} в норме'

town = TownCar('Volvo', 61, 'серый', False)
print('1:\n' + town.go(), town.colorcar(), town.show_speed(), town.turn('лево'), town.turn('право'), town.stop())

sport = SportCar('Ferrari', 150, 'красный', False)
print('2:\n' + sport.go(), sport.colorcar(), sport.show_speed(), sport.turn('лево'), sport.stop())

work = WorkCar('Камаз', 41, 'синий', False)
print('3:\n' + work.go(), work.colorcar(), work.show_speed(), work.turn('лево'), work.stop())

police = PoliceCar('Chevrolet', 120, 'белый', True)
print('4:\n' + police.go(), police.colorcar(), police.show_speed(), police.turn('право'), police.stop())
