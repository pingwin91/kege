for num in range(135790, 163229):
    summ = 0
    count = 0
    for eq in range(2, num // 2 + 1):
        if num % eq == 0:
            summ += eq
            count += 1
    if summ > 460000:
        print(count, summ)

# 142 473759
# 118 462767
# 126 464999
# 118 461969
# 118 477071