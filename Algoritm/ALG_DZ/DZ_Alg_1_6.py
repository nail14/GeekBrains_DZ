# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

abc_number = int(input('Введите номер буквы в алфавите: '))

abc_list = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
if abc_number <= len(abc_list):
    print(f'Буква в алфавите {abc_number}: {abc_list[abc_number - 1]}')
else:
    print(f'В алфавите меньше букв ({len(abc_list)})')

