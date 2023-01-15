def f(x, n):
    if x > 135:
        return n == 2
    return any([f(x + 1, n + 1), f(x * 4 - 3, n + 1)])


for s in range(5, 136):
    if f(s, 0):
        print(s)
        break

