new_list = ['Анна', 'Сергей', 'Владимир', 'Геннадий', 'Олег', 'Аркадий', 'Вячеслав']
new_list_adv = ["Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"]
new_dict = {}
new_dict_adv = {}


def thesaurus(names):
    for el in names:
        if el[0] in new_dict:  # Если ключ (первая буква имени) есть в словаре, добавляем к имеющемуся значению новое
            new_dict[el[0]].append(el)
        new_dict.setdefault(el[0], [el])  # Если ключа нет, то добавляем его и соответствующее значение
    return new_dict


def thesaurus_adv(celebrity):
    for el in celebrity:
        name, surname = el.split(' ')  # добавляем переменные, содержаещие имя и фамилию отдельно
        if surname[0] in new_dict_adv:
            if name[0] in new_dict_adv[surname[0]]:  # Если в словаре есть ключ-фамилия и ключ-имя,
                # добаляем к имеющимся новую пару "имя фамилия"
                new_dict_adv[surname[0]][name[0]].append(el)
            else:  # Если нет ключа-имени, то создаем его и добавляем соответствующую пару "имя фамилия"
                new_dict_adv[surname[0]].update({name[0]: [el]})
        new_dict_adv.setdefault(surname[0], {name[0]: [el]})  # Если нет ключа-фамилии - добавляем его и ключ-имя
    return new_dict_adv


print(thesaurus(new_list))
print(thesaurus_adv(new_list_adv))
