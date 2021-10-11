user_num = input("Please, enter a number in English from 0 to 20 inclusive: ")
translate = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
             'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}


def num_translate(num):
    try:
        if num[0].isupper():
            return translate[num.lower()].title()
        return translate[num]
    except KeyError:  # В случае неправильного ввода не будет ошибки
        return 'You have entered an incorrect value!'


print(num_translate(user_num))
