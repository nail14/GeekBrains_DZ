from itertools import zip_longest

with open('users.csv', 'r', encoding='utf-8') as name, \
        open('hobby.csv', 'r', encoding='utf-8') as hobby:
    names = name.read().splitlines()
    hobbys = hobby.readline().strip(str(1)).split(',')

users_hobbys_gen = ((names, hobbys) for names, hobbys in zip_longest(names, hobbys, fillvalue=None))

with open('users_hobby.txt', 'a', encoding='utf-8') as f:
    for users_hobby in users_hobbys_gen:
        f.write(f'{users_hobby[0]}: {users_hobby[1]}\n')