from json import dumps
from itertools import zip_longest
from sys import argv

# 5
try:
    users, hobby, us_hob = argv[1:]
except ValueError:
    users, hobby, us_hob = 'users.csv', 'hobby.csv', 'users_hobby.txt'
# 3
with open('hobby.csv', 'r', encoding='utf-8') as h:
    with open('users.csv', 'r', encoding='utf-8') as u:
        len_u, len_h = len([*u]), len([*h])
        u.seek(0)
        h.seek(0)
        if len_u >= len_h:
            with open('users_hobbies.json', 'w', encoding='utf-8') as j:
                new_dict = {}
                while len_h:
                    name = u.readline().strip().replace(',', ' ')
                    new_dict[name] = h.readline().strip()
                    len_h -= 1
                    len_u -= 1
                for i in range(len_u):
                    name = u.readline().strip().replace(',', ' ')
                    new_dict[name] = None
                j.write(dumps(new_dict, ensure_ascii=False, indent=1, sort_keys=True))
        else:
            exit(1)
# 4
with open(users, 'r', encoding='utf-8') as h:
    with open(hobby, 'r', encoding='utf-8') as u:
        len_u, len_h = len([*u]), len([*h])
        u.seek(0)
        h.seek(0)
        user_hobby = zip_longest(u, h, fillvalue=None)
        if len_u < len_h:
            exit(1)

        with open(us_hob, 'w', encoding='utf-8') as t:
            for i in user_hobby:
                t.write(f'{str(i[0]).strip().replace(",", " ")}: {i[1]}')
