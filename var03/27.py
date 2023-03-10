import time

start = time.time()  # время начала выполнения программы (т.к. работает дольше минуты)
f = open('27-B.txt')
n = int(f.readline())  # читаем количество повторов

'''
программа работает по принципу динамического программирования: 
мы с каждым следующим числом наполняем суммы и количество элементов, т.е.
на первой позиции в матрице находится сумма всех чисел и их количество
на второй позиции - сумма всех чисел, кроме первого и их количество
на третьей - сумма всех чисел, кроме первого и второго и их количество

Каждое новое приходящее число наполняет уже имеющиеся суммы и в конце формирует новую сумму для последующих подсчетов
'''
summs = []  # создаем матрицу сумм
max_sum = 0  # константа для поиска максимальной суммы
max_len = 0  # константа для поиска длины максимальной суммы
for i in range(n):
    num = int(f.readline())  # берем новое число из файла
    for j in range(i):  # цикл для прогона всех на данный момент существующих сумм
        summs[j][0] += 1  # увеличиваем длину текущей суммы
        summs[j][1] += num  # увеличиваем текующую сумму
        if summs[j][1] > max_sum and summs[j][1] % 107 == 0:  # если нашли наибольшую подходящую сумму
            max_sum = summs[j][1]
            max_len = summs[j][0]
    summs.append([1, num])  # конце число формирует новую сумму длиной 1, состоящую только из самого числа
    print(round(i / n * 100, 2))  # т.к. работает долго, то для контроля следим за процентом выполнения задания

print('answer =', max_len)
print('time script: ', round(time.time() - start))  # выводим время работы скрипта (у меня 326 секунд)