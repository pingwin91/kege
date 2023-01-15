f = open('26.txt')
n = int(f.readline())
# индекс массива - строка, в ней расположен массив значений ячеек со стенами
rows = [[] for i in range(10001)]
# формируем матрицу ячеек со стенками
for i in f:
    row, col = map(int, i.split())
    rows[row].append(col)
# перебираем матрицу стенок в поисках ответа
for i in range(len(rows)):
    break_point = False
    rows[i].sort()
    for j in range(len(rows[i]) - 1):
        if rows[i][j + 1] - rows[i][j] == 15:
            print(i, rows[i][j] + 1)
            break_point = True
            break
    if break_point:
        break