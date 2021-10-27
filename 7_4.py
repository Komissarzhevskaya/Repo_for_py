import os
import django
from collections import defaultdict


def stat_dirs(parent=django.__path__[0]):
    root_dir = parent
    django_files = defaultdict(int)
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            obj_size = os.stat(os.path.join(root, file)).st_size
            max_size = 10 ** len(str(obj_size))
            django_files[max_size] += 1
    print(django_files)


stat_dirs()
