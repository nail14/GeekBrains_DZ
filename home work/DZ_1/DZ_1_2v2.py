def list_of_numbers(numbers):
    result = 0

    while numbers != 0:
        result += numbers % 10
        numbers //= 10

    return result
count_sum = [i ** 3 for i in range(1, 1001, 2)] #

result_7 = sum(filter(lambda num: list_of_numbers(num) % 7 == 0, count_sum ))
print(result_7)

result_17 = sum(filter(lambda num: list_of_numbers(num + 17) % 7 == 0, count_sum ))
print(result_17)