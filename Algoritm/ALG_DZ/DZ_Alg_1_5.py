
# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

letter1, letter2 = [
  x.upper() for x in input('Введите две буквы в диапазоне (A - Z): ').split()
]
az_list = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

index_letter1 = az_list.index(letter1) + 1
index_letter2 = az_list.index(letter2) + 1

if index_letter1 < index_letter2:
    step = 1
else:
    step = -1

print(f'Буква {letter1}, место в алфавите: {index_letter1}')
print(f'Буква {letter2}, место в алфавите: {index_letter2}')

print(f'Между ними находятся буквы \
{az_list[az_list.index(letter1) + step:az_list.index(letter2):step]} \
({abs(index_letter1 - index_letter2) - 1})')
