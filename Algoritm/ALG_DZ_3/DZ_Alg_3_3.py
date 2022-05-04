# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

u = [random.randint(0, 99) for _ in range(10)]
print(f'Массив до изменения элементов min и max:{u}')

max = u[0]
min = u[0]

for i in u:
    if i > max:
        max = i
    elif i < min:
        min = i
min_index = u.index(min)
max_index = u.index(max)
u[min_index], u[max_index] = u[max_index], u[min_index]
print(f'Массив после изменения элементов {min_index} и {max_index}: {u}')