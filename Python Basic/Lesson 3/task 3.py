from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
jokes = []


def get_jokes(n, flag=False):
    """
        Генерирует вывод списка из n элементов.
                Параметры:
                        n (int): количество элементом (генераций)
                        flag (bool): параметр отслеживания повторений в генерации
        """
    for i in range(n):
        first = choice(nouns)
        second = choice(adverbs)
        third = choice(adjectives)
        joke = f'{first} {second} {third}'
        jokes.append(joke)
        check = []
        if flag:
            check = joke.split()
            for noun in nouns:
                for fun in check:
                    if noun == fun:
                        nouns.remove(noun)
            for adverb in adverbs:
                for fun in check:
                    if adverb == fun:
                        adverbs.remove(adverb)
            for adjective in adjectives:
                for fun in check:
                    if adjective == fun:
                        adjectives.remove(adjective)
    print(jokes)
