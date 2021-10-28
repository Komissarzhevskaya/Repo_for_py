import os
import shutil

for root in os.walk('my_project'):
    if 'templates' in root[0]:
        dir_path = root[0]
        try:
            shutil.copytree(root[0], root[0].replace('\\authapp', '', 1).replace('\\mainapp', '', 1))
        except FileExistsError:
            continue
