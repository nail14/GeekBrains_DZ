set_num_2 = (input('Введите валюту в формате: '))
set_num = (int(set_num_2))
print(set_num)
print(set_num_2)
def nums_generator(set_num):
    for num in range(1, set_num + 1, 2):
        yield num + 2
num_gen = nums_generator(set_num)
print(sum(num_gen))
print(f'>>> next(odd_to_{set_num})')
print('...StopIteration...')
