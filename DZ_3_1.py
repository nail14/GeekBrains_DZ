# Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
# Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить информацию, необходимую для перевода: какой тип данных выбрать, в теле функции или снаружи.
num_translate = input('Введите число для перевода: ')
eng_num = {'0':'zero', '1':'one', '2':'two','3':  'three', '4':'four','5':  'five','6': 'six', '7': 'seven', '8':'eight', '9':'nine', '10':'ten', }
ru_num = {'0':'ноль','1': 'один','2': 'два', '3': 'три','4': 'четыре','5':  'пять','6': 'шесть', '7': 'семь', '8':'восемь','9': 'девять','10':'десять'}
#num_1 = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'}

output = "" #вывод
for i in num_translate:
    output += eng_num.get(i, "None").title()+' - '+ ru_num.get(i, "None").title() + ", "
num_translate = eng_num, ru_num

print(output)