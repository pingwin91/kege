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
answer_mass = []
max_val = 0
for i in range(n):
    if max_val + files[i] <= value:
        max_val += files[i]
    else:
        max_val -= files[i - 1]
        break
    answer_mass.append(files[i])

# Реверсируем оба массива
answer_mass.reverse()
files.reverse()

# Подбираем наибольший файл на последнюю вакансию в архив
index = 0
count = 0
while True:
    if max_val + files[index] <= value:
        max_val += files[index]
        answer_mass.append(files[index])
        i = 0
        index += 1
        while max_val < value:
            if max_val - answer_mass[i] + files[index] <= value:
                max_val = max_val - answer_mass[i] + files[index]
                answer_mass[i] = files[index]
                i += 1
            index += 1
        break
    else:
        index += 1
        count += 1

print(max_val, count)