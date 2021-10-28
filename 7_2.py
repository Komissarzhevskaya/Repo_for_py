import os
import yaml
"""Сначала сделала через чтение отступов (решение мне не понравилось). Посмотрела разбор задания и разобрала для себя"""


def tree_dirs(dir_dict, directory=''):
    for key, val in dir_dict.items():
        dir_path = os.path.join(directory, key)
        os.makedirs(dir_path, exist_ok=True)
        if isinstance(val, dict):
            tree_dirs(val, dir_path)
        else:
            for i in val:
                if isinstance(i, str):
                    with open(os.path.join(dir_path, i), 'w'):
                        pass
                else:
                    tree_dirs(i, dir_path)


with open('config.yaml', 'r') as f:
    yaml_dict = yaml.safe_load(f)
    tree_dirs(yaml_dict)
