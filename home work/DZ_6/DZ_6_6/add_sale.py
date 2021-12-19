import sys

if __name__ == '__main__':
    sale = sys.argv[1]
    with open('bakery.csv', 'a') as f:
        f.write(sale + '\n')
        exit()

# from itertools import zip_longest, islice
# def test_fun():
#     print('Вы поключились к списку счетов, "add_sale"')
#
#
#
# with open('bakery.csv', 'r', encoding='utf-8') as bakery:
#
#     bakery_1=(bakery.read().strip(str(1)).split('\n'))
#     bakery_2 = bakery_1[0:]
#     # print(bakery_2)
#
# if __name__ == '__main__':
#     print('Конец операции')