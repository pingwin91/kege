f = open('27b.txt')
n = int(f.readline())

deltas = []
min_value = 0
max_value = 0
for i in f:
    i = list(map(int, i.split()))
    i_min, i_max = min(i), max(i)
    min_value += i_min
    max_value += i_max
    deltas.append(i_max - i_min)
deltas.sort()

if max_value % 7 == min_value % 7:
    print(max_value)
else:
    cur_max_val = max_value
    delta = max_value % 7 - min_value % 7
    for i in deltas:
        if (delta > 0 and i % 7 == delta) or (delta < 0 and i % 7 == 7 + delta):
            max_value -= i
            print(max_value)
            break
        else:
            if i % 7 != 0:
                cur_max_val -= i
            if cur_max_val % 7 == min_value % 7:
                print(cur_max_val)
                break
