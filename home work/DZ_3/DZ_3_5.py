from random import randrange, choice
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
random_idx_1 = randrange(len(nouns))
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
random_idx_2 = randrange(len(adverbs))
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
random_idx_3 = randrange(len(adjectives))
jokes= nouns[random_idx_1], adverbs[random_idx_2], adverbs[random_idx_3]
print(jokes) #вывод
