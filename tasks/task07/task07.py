"""
Задача:
Дано натуральное число. Получить строку, в которой тройки цифр этого числа разделены пробелом,
начиная с правого конца. Например, число 1234567 преобразуется в 1 234 567
"""


def add_space_to_number(number):
    result = ''
    s = str(number)
    s_len = len(s)
    ii = 0
    for i in range(s_len):
        if ii == 3:
            result += ' '
            ii = 1
        else:
            ii += 1
        result += s[-i - 1]

    result = result[::-1]
    return result


if __name__ == '__main__':
    pass
