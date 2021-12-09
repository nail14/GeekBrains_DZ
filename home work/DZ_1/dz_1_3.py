number = 1
while number <= 100:
    if number > 1 and number <= 4 or number >=22 and number <= 24 or number >=32 and number <= 34 or number >=42 and number <= 44 or number >=52 and number <= 54 or number >=62 and number <= 64 or number >=72 and number <= 74 or number >=82 and number <= 84 or number >=92 and number <= 94:
        print ( number, 'Процента' )
    elif number == 1 or number == 21 or number == 31 or number == 41 or number == 51 or number == 61 or number == 71 or number == 81 or number == 91:
        print( number,'Процент')
    elif number >= 5 and number <= 20 or number >=25 and number <= 30 or number >= 35 and number <= 40 or number >= 45 and number <= 50 or number >= 55 and number <= 60 or number >= 65 and number <= 70 or number >= 75 and number <= 80 or number >= 85 and number <= 90 or number >= 95 and number <= 100:
        print(number,'Процентов')
    number += 1