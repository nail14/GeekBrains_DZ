
# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный
# и отсортированный массивы. Сортировка должна быть реализована в виде функции.
# По возможности доработайте алгоритм (сделайте его умнее).

# O(n**2)

# def bubble_sort(spisok):
#     swapped = False
#     for i in range(len(spisok) - 1, 0, -1):
#         for j in range(i):
#             if spisok[j] > spisok[j + 1]:
#                 spisok[j], spisok[j + 1] = spisok[j + 1], spisok[j]
#                 swapped = True
#         if swapped:
#             swapped = False
#         else:
#             break
#     return spisok
# # ------------------------------------------
# c = 0
# for i in range(1, 10):
#     if A[i - 1] >= A[i]:
#         t = A[i]
#         A[i] = A[i - 1]
#         A[i - 1] = t
#     else:
#         c = c + 1
# # ------------------------------------------
# if __name__ == '__main__':
#     s = [5,4,3,21,12,3]
#     print(*bubble_sort(s))

from random import randint
from timeit import timeit

MAX_SIZE = 100
NUMBER_EXECUTIONS = 10_000


def bubble_sort(array):
    for i in range(len(array) - 1, 0, -1):
        flag = True
        for n in range(i):
            if array[n] > array[n+1]:
                array[n], array[n+1] = array[n+1], array[n]
                flag = False

        if flag == True:
            break
    return array


def bubble_sort_no_smart(array):
    for i in range(len(array) - 1, 0, -1):
        for n in range(i):
            if array[n] > array[n+1]:
                array[n], array[n+1] = array[n+1], array[n]

    return array


numbers = [randint(-100, 100) for _ in range(MAX_SIZE)]
print(numbers)
print(bubble_sort(numbers))

time_smart = timeit(f'bubble_sort({numbers})',
              setup='from __main__ import bubble_sort',
              number=NUMBER_EXECUTIONS)
time = timeit(f'bubble_sort_no_smart({numbers})',
              setup='from __main__ import bubble_sort_no_smart',
              number=NUMBER_EXECUTIONS)
print(time_smart)
print(time)
