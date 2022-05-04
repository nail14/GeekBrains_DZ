
# DZ_Alg_5_1
# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# (т.е. 4 числа) для каждого предприятия. Программа должна определить среднюю прибыль
# (за год для всех предприятий) и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.


from collections import namedtuple

Enterprises = namedtuple('Enterprises', 'name quart_1 quart_2 quart_3 quart_4 year')

Count_enteprise = int(input('введите кол-во предприятий: '))
enterp = [0 for a in range(Count_enteprise)]

total_profit = 0

for i in range(Count_enteprise):
    
    name = input(f'Введите название {i+1} предприятия: ')
    quarts = [float(k) for k in input('Введите через пробел прибыль за каждый квартал: ').split()]
    year = 0
    for quart in quarts:
        year += quart
    total_profit += year
    enterp[i] = Enterprises(name, *quarts, year)

if Count_enteprise == 1:
    
    print(f'Предприятие: {enterp[0].name} с годовой прибылью: {enterp[0].year}')
else:
    
    average_profit = total_profit / Count_enteprise
    less = []
    more = []

    for i in range(Count_enteprise):
        
        if enterp[i].year < average_profit:
            less.append(enterp[i])
            
        elif enterp[i].year > average_profit:
            more.append(enterp[i])

    print(f'\nСредняя годовая прибыль по всем предприятиям: {average_profit: .2f}')
    print(f'\nПредприятия, чья прибыль меньше: {average_profit: .2f}')
    
    for t in less:
        print(f'Предприятие {t.name} с прибылью {t.year: .2f}')
    print(f'\nПредприятия, чья прибыль больше: {average_profit: .2f}:')
    
    for t in more:
        print(f'Предприятие {t.name} с прибылью {t.year: .2f}')
