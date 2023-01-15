f = open('26.txt')

value, n = map(int, f.readline().split())

files = []
for i in f:
    files.append(int(i))

files.sort(reverse=True)

cur_value = 0
count = 0
min_file = value
for i in range(len(files)):
    if cur_value + files[i] <= value:
        cur_value += files[i]
        count += 1
        min_file = files[i]

print(count, min_file)