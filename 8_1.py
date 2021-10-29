import re


def email_parse(email_address):
    re_mail = re.match(r'(?P<username>\w+)@(?P<domain>\w+\.\w+)', email_address, re.I)
    if not re_mail:
        raise ValueError(email_address)
    return print(re_mail.groupdict())


try:
    email_parse(input("Please, enter your email address: "))
except ValueError as e:
    print(f'wrong email: {e}')
