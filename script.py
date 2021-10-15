import sys
from utils import currency_rates
# Считается ли вызов функции с print ошибкой?)
print(currency_rates('usd'))
print(currency_rates('BGN'))
print(currency_rates('Бла-бла'))
# Во избежание ошибок при запуске не через терминал создаем исключение
try:
    print(currency_rates(sys.argv[1]))  # Первый элемент списка - имя скрипта, поэтому берем второй элемент)
    print(sys.argv[0])
except IndexError:
    sys.exit()
