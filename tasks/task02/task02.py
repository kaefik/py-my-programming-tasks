"""
Задача:
Дана строка. Показать третий, шестой, девятый и так далее символы.
"""

str = input('Введите любую строку: ')

s_len = range(3, len(str), 3)

for i in s_len:
    print(str[i - 1])

if len(str) % 3 == 0:
    print(str[-1])
