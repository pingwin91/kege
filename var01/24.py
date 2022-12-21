# 83
string = open('24.txt').readline()

max_len = 0
cur_len = 0
for i in string:
    if i in 'GWP':
        max_len = max(max_len, cur_len)
        cur_len = 0
    else:
        cur_len += 1
print(max_len)