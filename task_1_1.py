time_in_s = abs(int(input('Please, inter the time in seconds: ')))  # Получаем на вход число пользователя по модулю
# Вводим постоянные переменные времени
time_in_m = time_in_s // 60
time_in_h = time_in_s // 3600
time_in_d = time_in_s // 86400

# В зависимости от введённых пользователем данных осуществляем вывод
if time_in_s < 60:
    print(f'{time_in_s} s')  # В секундах
if 60 <= time_in_s < 3600:
    sec = time_in_s % 60
    print(f'{time_in_m} m {sec} s')  # В минутах и секундах
if 3600 <= time_in_s < 86400:
    sec = time_in_s % 3600 % 60
    min = time_in_s % 3600 // 60
    print(f'{time_in_h} h {min} m {sec} s')  # В часах, минутах и секундах
if time_in_s >= 86400:
    sec = time_in_s % 86400 % 3600 % 60
    min = time_in_s % 86400 % 3600 // 60
    hours = time_in_s % 86400 // 3600
    print(f'{time_in_d} d {hours} h {min} m {sec} s')  # В днях, часах, минутах и секундах
