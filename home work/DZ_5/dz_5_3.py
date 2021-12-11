from itertools import zip_longest

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена','Анастасия', 'Петр',]
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

gen_mix = zip_longest(tutors, klasses[:len(tutors)])
print(list(gen_mix ))
