# 7094 220
f = open('26.txt')

# Читаем первую строку с максимальным объемом и количеством файлов
# Читаем данные в массив и сортируем его
value, n = map(int, f.readline().split())
files = []
for i in f:
    files.append(int(i))
files.sort()

# Находим максимальный обхем файлов, которые точно попадут в архив
# удаляем последний поместившийся элемент, чтобы подобрать на последнюю вакансию файл наибольшего объема
max_val = 0
for i in range(n):
    x = files[i]
    if max_val + files[i] <= value:
        max_val += files[i]
    else:
        max_val -= files[i - 1]
        break

# Подбираем наибольший файл на последнюю вакансию в архив
index = n - 1
count = 0
while True:
    x = files[index]
    if max_val + files[index] <= value:
        max_val += files[index]
        break
    else:
        index -= 1
        count += 1

print(max_val, count)