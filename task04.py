"""
Задача:
1) Написать алгоритм генерации пароля.
2) Дополнить программу возможностью определить, сгенерирован ли данный пароль вашим алгоритмом.

Дополнительная информация:
1) Модуль random на примерах — Изучение методов генерации случайных данных
   https://python-scripts.com/random#generator-random-string
"""

# алгоритм будет генерировать пароль указанный пользователем длины
# и будет поочередно большая затем маленькая буква выбирающаяся случайным порядком

import random

# генерация пароля
def generate_password(abc_pass, len_pass):
    password = ''
    flag_upper = True
    for i in range(len_pass):
        simbol = random.choice(abc_pass)
        if simbol.isalpha():
            if flag_upper:
                simbol = simbol.upper()
            flag_upper = not flag_upper

        password += simbol
    return password

# проверка соответствует ли правилу генерации моих паролей
def is_my_password(pswrd):
    flag_upper = True # первая буква должна быть заглавной
    for sim in pswrd:
        if sim.isalpha():
            if flag_upper:
                if not sim.isupper():
                    return False
            else:
                if sim.isupper():
                    return False
            flag_upper = not flag_upper
    return True


abc = 'abcdefghijklmnopqrstuvwxyz'
number = '0123456789'
spec_simbol = '~`!@$%^&*(){}<>'

abc_pass = abc + number + spec_simbol

while True:
    len_password = input('Введите длину пароля (число): ')
    if len_password.isdigit():
        break
    else:
        print('введенное строка не число.')

my_pass = generate_password(abc_pass, int(len_password))

print('Сгенирированный пароль: ', my_pass)

# соответствует моему алгоритму
check_password = 'WsE}t68Kg@(U'
fl = is_my_password(check_password)

print(f"Ответ на вопрос соответствует ли пароль {check_password} моему алгоритму: ", fl)

# НЕ соответствует моему алгоритму
check_password2 = 'WsE}T68Kg@(U'
fl2 = is_my_password(check_password2)
print(f"Ответ на вопрос соответствует ли пароль {check_password2} моему алгоритму: ", fl2)