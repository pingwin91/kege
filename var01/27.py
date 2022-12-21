f = open('27-A.txt')

n = int(f.readline())
for i in range(2):
    x = int(f.readline())
    if x % 2 == 0:
        min_0 = x
    else:
        min_1 = x
count_0 = 1
count_1 = 1
count = 0
for i in f:
    x = int(f.readline())
    if x % 2 == 0 and x > min_1:
        count += count_1
        count_0 += 1
    if x % 2 == 1 and x > min_0:
        count += count_0
        count_1 += 1
    if x % 2 == 0:
        count_0 += 1
        min_0 = min(min_0, x)
    else:
        count_1 += 1
        min_1 = min(min_1, x)
print(count)