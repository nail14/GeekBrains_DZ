given_number = int(input('Укажите время задержки в секундах: '))
if given_number > 1 and given_number <= 59:
    print(given_number, 'сек')
elif given_number >= 60 and given_number <= 3599:
    print(given_number // 60, 'мин', given_number % 60, 'сек')
elif given_number >= 3600 and given_number <= 86399:
    print(given_number // 3600, 'час', ((given_number % 3600 ) // 60), 'мин', given_number % 60, 'сек')
elif given_number >= 86400 and given_number <= 31536000:
    print(given_number // (24 * 3600), 'дней', ((given_number % 86400)// 3600), 'час', ((given_number % 3600 ) // 60), 'мин', given_number % 60, 'сек')
elif given_number >= 31536001 :
    print('больше года...я сломался')
print('Отсчёт начат')
print('3')
print('2')
print('1')



