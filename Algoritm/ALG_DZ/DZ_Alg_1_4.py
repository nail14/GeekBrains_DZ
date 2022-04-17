# 4. Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
# --------------------------------------------------------------

from os import urandom as r_random


def random(list):
    random = int(int.from_bytes(r_random(7), 'big')) >> 100
    maxsize = len(list)
    i = random % maxsize
    return list[i]


def frange(start, stop, jump):
    while start < stop:
        yield start
        start += jump


print('Введите диапазон. Диапазон целых чисел \
Или диапазон вещественных чисел \
Или диапазон символов \
 ')

type_range, raw_start, raw_end, raw_jump = [
    x for x in input('Введите диапазон: ').split()
]

if type_range == 'int':
    start = int(raw_start)
    stop = int(raw_end)
    jump = int(raw_jump)
    list_int = [x for x in range(start, stop + 1, jump)]
    print(list_int)
    print(
        f'Случайное целое число из диапазона {start} - {stop}: \
    {random(list_int)}'
    )

elif type_range == 'float':
    start = float(raw_start)
    stop = float(raw_end)
    jump = float(raw_jump)
    list_float = [x for x in frange(start, stop + jump, jump)]
    print(list_float)
    print(
        f'Случайное вещественное число из диапазона {start} - {stop}: \
    {random(list_float)}'
        )

elif type_range == 'str':
    start = raw_start
    stop = raw_end
    jump = int(raw_jump)
    list_abc = [chr(i) for i in range(ord(start), ord(stop) + 1, jump)]
    print(list_abc)
    print(f'Случайный символ из из диапазона {start} - {stop}: \
    {random(list_abc)}')

else:
    print('Неправильно задан диапазон')

