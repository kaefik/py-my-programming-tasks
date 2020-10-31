"""
Задача:
Удалите в строке все 'abc', за которыми следует цифра.
"""


def del_abc_number(strs):
    new_str = ''
    strs_len = len(strs)
    i = 0
    while i < strs_len:
        if i + 3 <= strs_len:
            s_abc = strs[i:i + 3]
            if s_abc == 'abc':
                if (i + 4 <= strs_len) and (strs[i + 4].isdigit()):
                    i += 3
                else:
                    new_str = new_str + strs[i]
                    i += 1
            else:
                new_str = new_str + strs[i]
                i += 1
        else:
            new_str = new_str + strs[i]
            i += 1
    return new_str


if __name__ == '__main__':
    s = input('Введите любую строку: ')
    r = del_abc_number(s)
    print('Новая строка в которой удалены все "abc", за которыми следует цифра: ', r)
