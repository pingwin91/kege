x = 49 ** 7 + 7 ** 21 - 7
num_7 = ''
while x > 0:
    num_7 = str(x % 7) + num_7
    x //= 7
print(num_7.count('6'))