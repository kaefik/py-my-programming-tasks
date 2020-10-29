"""
задача:
Дана строка, содержащая полное имя файла (например, 'c:\WebServers\home\testsite\www\myfile.txt').
Выделите из этой строки имя файла без расширения.
"""

def cut_only_filename(s):
    result = ''
    len_s = len(s)
    for i in range(len_s):
        simbol = s[-i-1]
        if simbol == '\\':
            break
        result = simbol + result
        if simbol == '.':
            result = ''
    return result

# тестовая строка
# strs = 'c:\WebServers\home\testsite\www\myfile.txt'
# strs = 'myfile.txt'
strs = input('Введите полный путь до файла, а я выделю имя файла без расширения: ')


name = cut_only_filename(strs)

print('Имя файла без расширения: ', name)