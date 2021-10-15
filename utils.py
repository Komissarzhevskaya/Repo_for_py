from requests import get, utils
from decimal import Decimal
from bs4 import BeautifulSoup  # Для себя немного поигралась с парсером (Scrapy показался сложноватым)
from datetime import datetime


def currency_rates(valute):
    valute = valute.upper()
    response = get("http://www.cbr.ru/scripts/XML_daily.asp")
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings).split('</Valute>')
    # Извлекаем данные с помощью BS, а после все аттрибуты в виде пар ключ-значение(dict) и ищем значение ключа Date
    date_unpack = BeautifulSoup(response.content, 'xml').find('ValCurs').attrs.get('Date').split('.')
    for i in content:
        if valute in i:
            date = list(map(int, date_unpack))
            nominal = i[i.find("<Value>") + 7:i.find("</Value>")].replace(",", ".")
            return f'{valute}: {Decimal(nominal)} rub, Date: {datetime(day=date[0], month=date[1],year=date[2])}'


if __name__ == '__main__':
    print(currency_rates('HUF'))
    print(currency_rates('uSd'))
    print(currency_rates('доллары'))
