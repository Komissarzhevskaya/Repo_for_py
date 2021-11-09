import re


class Data:
    def __init__(self, data):
        self.data = data
        self.dict_data = {}

    @classmethod
    def data_int(cls, data):
        return [*map(int, data.split('-'))]

    @staticmethod
    def check_data(data):
        check = re.compile(r'(?<!\d)(?:0?[1-9]|[12][0-9]|3[01])-(?:0?[1-9]|1[0-2])-(?:19[0-9][0-9]|20[01][0-9])(?!\d)')
        if check.match(data):
            return f'Date is correct'
        raise AssertionError


user_date = input('Введите дату в формате ДД-ММ-ГГГГ: ')
try:
    print(Data.check_data(user_date))
    print(Data.data_int(user_date))
except (ValueError, AssertionError):
    print(f'Wrong date "{user_date}"')
