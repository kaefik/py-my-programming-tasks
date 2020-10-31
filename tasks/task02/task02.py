"""
Задача:
Дана строка. Показать третий, шестой, девятый и так далее символы.
"""


def string_3_6(strs):
    result = ''
    s_len = range(3, len(strs), 3)

    for i in s_len:
        result += strs[i - 1]

    if len(strs) % 3 == 0:
        result += strs[-1]
    return result


if __name__ == '__main__':
    str1 = input('Введите любую строку: ')

    r = string_3_6(str1)

    print('Результат: ', r)
