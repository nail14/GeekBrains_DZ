#Дан список, содержащий искажённые данные с должностями и именами сотрудников:
#['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
# Известно, что имя сотрудника всегда в конце строки. Сформировать из этих имён и вывести на экран фразы вида:
# 'Привет, Игорь!' Подумать, как получить имена сотрудников из элементов списка,
# как привести их к корректному виду. Можно ли при этом не создавать новый список?

my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
hello, sim_1 = 'Привет','!'
greeting = hello + str(my_list) + sim_1
print(greeting)
suffixes = [item.split()[-1] for item in my_list]
# print (suffixes.title())
mystr = 'Привет!'
underline = '-' * len(mystr) * len(my_list)
num= enumerate(my_list)
for i, v in num:
           
    print(mystr[-1])
  
    print(mystr[:-1], f',{v}'.lower().title(), mystr[-1], (f'\n {underline}'))
 
for i in range(len(my_list)):
    Name_list = my_list[i].split(" ")
    n_indexes = len(Name_list) - 1
    temporary_name = Name_list[n_indexes].title()
    name = temporary_name.lower().title()
    my_list.append(name)

for Names in my_list.copy():
    print(mystr[:-1], Names, mystr[-1], (f'\n {underline}'))
    my_list.remove(Names)

