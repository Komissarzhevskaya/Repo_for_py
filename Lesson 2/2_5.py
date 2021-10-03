# A
prices = [57.8, 46.51, 97, 23, 100.67, 34.5, 56, 12.9, 139.9, 89, 21, 115.98, 39, 145.6, 856.43]
for i, el in enumerate(prices):
    prices[i] = round(el % 1 * 100)  # приводим число копеек к целоцисленному значению
    # Дополняем число копеек нулем до двух разрядов и записываем ответ (в руб. и коп.) в строку через запятую
    print(f'А: {int(el)} руб {prices[i]:02d} коп', end=', ')
# B
prices = [57.8, 46.51, 97, 23, 100.67, 34.5, 56, 12.9, 139.9, 89, 21, 115.98, 39, 145.6, 856.43]
print(f'\nB: Initial prices : {prices} ; id {id(prices)}')
prices.sort()
print(f'   Sorted prices : {prices} ; id {id(prices)}')
# C
prices = [57.8, 46.51, 97, 23, 100.67, 34.5, 56, 12.9, 139.9, 89, 21, 115.98, 39, 145.6, 856.43]
new_list_prices = sorted(prices)[::-1]
print(f'C: Reversed sorting: {new_list_prices}')
# D
prices = [57.8, 46.51, 97, 23, 100.67, 34.5, 56, 12.9, 139.9, 89, 21, 115.98, 39, 145.6, 856.43]
print(f'D: Five highest prices: {sorted(prices)[:-6:-1]}')
