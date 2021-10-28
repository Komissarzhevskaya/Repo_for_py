import os
import django
from collections import defaultdict
import json


def stat_dirs(parent=django.__path__[0]):
    root_dir = parent
    django_files = defaultdict(int)
    result_dict = defaultdict(tuple)
    ext_dict = defaultdict(list)
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            ext = file.rsplit('.', maxsplit=1)[-1].lower()
            obj_size = os.stat(os.path.join(root, file)).st_size
            max_size = 10 ** len(str(obj_size))
            ext_dict.setdefault(max_size, [ext])
            if ext not in ext_dict[max_size]:
                ext_dict[max_size].append(ext)
            django_files[max_size] += 1
    for k, v in django_files.items():
        for i, j in ext_dict.items():
            if k == i:
                result_dict.setdefault(k, (v, j))
    return result_dict


func_dict = stat_dirs()
sort_dict = {i: func_dict[i] for i in sorted(func_dict.keys())}
file_name = os.path.basename(os.getcwd()) + '_summary.json'

with open(file_name, 'w', encoding='utf-8') as f:
    json.dump(sort_dict, f, indent=3)
