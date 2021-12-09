start_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for i, s in enumerate(start_list):
    if s.isdigit():
        start_list[i] = f'"{int(s):02d}"'
    elif s[1:].isdigit():
        start_list[i] = f'"{s[0]}{int(s[1:]):02d}"'
    print(start_list[i], end='')
print('\n', start_list)
