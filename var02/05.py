for i in range(100):
    bin_num = bin(i)[2:]
    bin_num += bin_num[-1]
    if bin_num.count('1') % 2 == 0:
        bin_num += '00'
    else:
        bin_num += '10'
    if int(bin_num, 2) > 97:
        print(i)
        break

# 13