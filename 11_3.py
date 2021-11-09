class IsNumber(Exception):
    @classmethod
    def check(cls, param):
        try:
            if param.isdigit() or float(param.replace(',', '.')):
                pass
            else:
                return False
        except ValueError:
            raise IsNumber('Это не число, но окей...')


numb_list = []
while True:
    try:
        x = input("Введите число. Если хватит, то так и скажите!: ")
        if x == 'хватит':
            break
        if IsNumber.check(x) is False:
            raise IsNumber('Это не число, но окей...')
        numb_list.append(x)
    except IsNumber as err:
        print(err)
print(numb_list)
