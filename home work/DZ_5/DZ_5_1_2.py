##Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield

###### 5_1

import sys

set_num = (input('Введите число для генерации нечётных чисел: '))
num_gen = (num for num in range(1, int(set_num) + 1, 2))
print((num_gen), sys.getsizeof(num_gen),  list(num_gen)) 


###### 5_2
set_num_2 = int(input('Введите число для генерации нечётных чисел (V2): '))
def nums_generator(set_num_2):
    for i in range(1, int(set_num_2) + 1 % 2 != 0, 2):
        # one#set_num
        yield i*1
num_gen_2= nums_generator(set_num_2 *1)
print (type(set_num_2), sys.getsizeof(num_gen), *num_gen)
