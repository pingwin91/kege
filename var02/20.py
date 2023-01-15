def f(start, finish, n):
    if start >= finish:
        return n == 3
    if n % 2 == 0:
        return f(start + 2, finish, n + 1) or f(start * 3, finish, n + 1)
    else:
        return f(start + 2, finish, n + 1) and f(start * 3, finish, n + 1)

for i in range(16, 100):
    if f(10, i, 0):
        print(i)

# 37 96