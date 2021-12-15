from itertools import zip_longest, islice


with open('hobby.csv', 'r', encoding='utf-8') as hobby:

    hobby_1=(hobby.readline().strip(str(1)).split(','))
    hobby_2 = hobby_1[0:]
    # print(hobby_2)
with open('users.csv', 'r', encoding='utf-8') as users:


    users_1 = (users.read().strip(str()).split('\n'))
    users_2 = users_1[0:]
    # print(users_2)
gen_mix = ((users_2,':', hobby_2) for users_2, hobby_2 in zip_longest(users_2, hobby_2, fillvalue=None))

output_1 = (*islice(gen_mix, len(hobby_2)),)  ##не смог реализовать пернос строки sep='\n'тут не работатет, как тогда????


# print(*islice(gen_mix, len(hobby_2)), sep='\n')
print(output_1)
with open('write_data.txt', 'w', encoding='utf-8') as mix:
    mix.writelines(str(output_1))
