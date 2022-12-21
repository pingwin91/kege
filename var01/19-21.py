# 19 -> 12
def f(s, n):
    if s > 99 or n > 2:
        return n == 2
    return any([f(s * 2, n + 1), f(s * 3, n + 1)])

for s in range(1, 50):
    if f(s, 0):
        print(s)
        break


# 20 -> 6 16
def f(s, n):
    if s > 99 or n > 3:
        return n == 3
    if n % 2 == 0:
        return any([f(s * 2, n + 1), f(s * 3, n + 1)])
    return all([f(s * 2, n + 1), f(s * 3, n + 1)])

answer = []
for s in range(1, 50):
    if f(s, 0):
        answer.append(s)
print(answer[0], answer[-1])


# 21 -> 3
def f(s, n):
    if s > 99 or n > 4:
        return n == 2 or n == 4
    if n % 2 == 1:
        return any([f(s * 2, n + 1), f(s * 3, n + 1)])
    return all([f(s * 2, n + 1), f(s * 3, n + 1)])


for s in range(1, 50):
    if f(s, 0):
        print(s)
        break