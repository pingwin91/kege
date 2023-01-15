for _1 in range(10):
    for _2 in range(10):
        for _3 in range(10):
            num = int('3261' + f'{_1}' + f'{_2}' + '64' + f'{_3}')
            if num % 163 == 0:
                print(num, num // 163)