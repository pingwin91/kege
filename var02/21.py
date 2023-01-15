def f(start, finish, n):
    if start >= finish:
        return n == 2 or n == 4
    if n % 2 == 1:
        return f(start + 2, finish, n + 1) or f(start * 3, finish, n + 1)
    else:
        return f(start + 2, finish, n + 1) and f(start * 3, finish, n + 1)

for i in range(6, 100):
    if f(5, i, 0):
        print(i)

# 6 (не работает)