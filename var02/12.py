for i in range(101, 110):
    string = '3' * i
    while '111' in string or '333' in string:
        if '111' in string:
            string = string.replace('111', '3')
        else:
            string = string.replace('333', '1')
    print(f'{i}: {string}')

# 107