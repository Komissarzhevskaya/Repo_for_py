tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Станислав', 'Игорь', 'Елена']
classes = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def pairs(list1, list2, no_item=None):
    combo_list = list1.copy()
    try:
        for i in range(len(list1)):
            yield list1[i], list2[i]
            combo_list.remove(list1[i])
    except IndexError:
        for j in combo_list:
            yield j, no_item


result = pairs(tutors, classes)
print(*result, type(result))
