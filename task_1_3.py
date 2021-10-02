for numb in range(1, 101):
    if numb % 10 == 1 and numb != 11:
        print(f'{numb} процент')
    if 1 < numb % 10 <= 4 and numb not in range(12, 15):
        print(f'{numb} процента')
    if numb % 10 > 4 or numb % 10 == 0 or numb in range(11, 15):
        print(f'{numb} процентов')
