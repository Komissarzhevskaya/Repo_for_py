import os


# Создает родительскую папку и подпапки. Если какие-то подпапки уже существуют - создает те, которых нет
def create_dirs(parent, *args):
    dir_dict = {}
    for child in args:
        if parent in dir_dict:
            dir_dict[parent].append({child: []})
        dir_dict.setdefault(parent, [{child: []}])
    for k, v in dir_dict.items():
        for i in v:
            for j in i:
                dir_path = os.path.join(k, j)
                if not os.path.exists(dir_path):
                    os.makedirs(dir_path)


if __name__ == '__main__':
    create_dirs('my_project', 'adminapp', 'authapp', 'mainapp', 'setting')
