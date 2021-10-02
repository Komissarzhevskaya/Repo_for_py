start_list = [i**3 for i in range(1, 1001, 2)]  # Заполняем список кубами нечётных чисел от 1 до 1000
final_sum = 0  # Вводим начальное значение искомой суммы
for i, j in enumerate(start_list):  # Перебираем индексы элементов и сами элементы
    sum_of_digits = 0  # Сумма цифр элемента списка
    while j != 0:  # путём нахождения остатка от деления на 10 элементов исходного списка рассчитываем сумму цифр
        sum_of_digits += j % 10
        j = j // 10
    if sum_of_digits % 7 == 0:
        final_sum += start_list[i]
print(f'Sum of sequence elements from 1 to 1000, the sum of digits of which is divided by 7: {final_sum}')

final_sum = 0
for i, j in enumerate(start_list):
    sum_of_digits = 0
    some_el = j + 17  # Увеличиваем элементы списка на 17
    while some_el != 0:
        sum_of_digits += some_el % 10
        some_el = some_el // 10
    if sum_of_digits % 7 == 0:
        final_sum += start_list[i] + 17
print(f'Sum of sequence elements from 1 to 1000 (after increasing each element by 17),'
      f' the sum of digits of which is divided by 7: {final_sum}')
