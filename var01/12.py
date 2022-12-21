string = '1' + '0' * 33

while '1' in string or '100' in string:
    if '100' in string:
        string = string.replace('100', '0001', 1)
    else:
        string = string.replace('1', '00', 1)
print(string.count('0'))