# Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы
def thesaurus(*names):
    diction = {}
    for name in names:
        key = name[0].capitalize()
        if key not in diction:
            diction[key] = []
        diction[key].append(name)
    return diction
print(thesaurus("иван".title(), "МаРия".title(), "Петр", "ИльЯ".title())) #вывод