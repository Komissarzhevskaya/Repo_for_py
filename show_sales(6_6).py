from sys import argv

with open('bakery.csv', 'r', encoding='utf-8') as show:
    try:
        if len(argv[1:]) == 2:
            print(*(el for i, el in enumerate(show) if int(argv[1]) <= i + 1 <= int(argv[2])), sep='')
        elif len(argv[1:]) == 1:
            print(*(el for i, el in enumerate(show) if int(argv[1]) <= i + 1), sep='')
        else:
            print(show.read())
    except ValueError:
        print('You must enter a correct value!')
