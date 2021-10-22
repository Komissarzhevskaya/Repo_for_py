from sys import argv

with open('bakery.csv', 'a+', encoding='utf-8') as add:
    try:
        float(argv[1].replace(",", "."))
        add.write(f'{argv[1]}\n')
    except ValueError:
        print('You must enter a numeric value!')
