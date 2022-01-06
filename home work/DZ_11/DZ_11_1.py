from datetime import datetime, date, time


class Data:
    def __init__(self, data):
        self.data = data.split('-')

    @classmethod
    def form(cls, data):
        try:
            day, month, year = [int(i) for i in data.split('-')]
            return f"{type(day), day}\n{type(month), month}\n{type(year), year}"
        except ValueError:
            return 'Указана неправильная дата!'

    @staticmethod
    def exam(data):
        try:
            day, month, year = data.split('-')
            date(int(year), int(month), int(day))
            return 'Верный ввод даты!'
        except ValueError:
            return 'Указан некорректный формат даты!'


print(Data.exam('06-01-2021'))
print(Data.form('06-01'))
