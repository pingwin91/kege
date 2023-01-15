def f(n):
    if n < 3:
        return n
    if n % 3 == 0:
        return 2 * n - f(n // 3) - f(n - 1)
    else:
        return n + f(n - 2) + f(n // 10)

count = 0
for i in range(50, 101):
    if 50 < f(i) <= 200:
        count += 1
        print(i, f(i))
print(count)