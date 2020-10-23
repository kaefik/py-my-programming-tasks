'''
Задача:
Пользователь вводит англ. букву, вывести следующие три по алфавиту.
Если алфавит закончился, то вывести циклично с начала алфавита, то есть если z, то a b c.
Вывод только маленьких букв. Учесть, что пользователь может ввести заглавную
'''

simbol =input('Введи букву английского алфавита: ')

if simbol.isupper():
    print('Введите строчную букву английского алфавита ')
    exit(0)

current_pos = ord(simbol)

for i in range(3):
    current_pos_i = current_pos + i + 1
    if current_pos_i > ord('z'):
        current_pos = ord('a') - 1
        current_pos_i = current_pos + 1
    print(chr(current_pos_i))

