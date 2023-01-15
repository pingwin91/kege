for i in range(100):
    bin_num = bin(i)[2:]
    if bin_num[-1] == '0':
        bin_num += '01'
    else:
        bin_num = '1' + bin_num + '10'
    if int(bin_num, 2) > 214:
        print(i)
        break