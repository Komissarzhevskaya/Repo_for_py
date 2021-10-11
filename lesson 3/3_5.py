from random import choice, sample

user_num = int(input("Please, inter the number of jokes: "))
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(num, limit=True):
    """
    This function generates a list of random jokes from 3 word lists

    :param num: number of jokes
    :param limit: restriction on repetition of words in jokes
    :return: list of random jokes
    """
    jokes = []
    #  создаем переменные, содержащие перемешанные элементы исходных списков с длинами наименьшего исходного списка
    n_mix, adv_mix, adj_mix = sample(nouns, len(nouns)), sample(adverbs, len(nouns)), sample(adjectives, len(nouns))
    min_len = min(n_mix, adv_mix, adj_mix)  # длина наименьшего списка
    if limit:  # Если есть ограничение на повторы, генерируем шутки до тех пор, пока их количество не будет равно
        # заданному пользователем числу шуток или длине наименьшего списка
        while min_len and num:
            jokes.append(f'{n_mix.pop()} {adv_mix.pop()} {adj_mix.pop()}')
            num -= 1
        return jokes
    for i in range(num):  # выбираем рандомное слово из каждого списка, комбинируем в шутку и вносим в список с шутками
        jokes.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')
    return jokes


print(get_jokes(user_num))
