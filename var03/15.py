def delit(x, y):
    return x % y == 0


for a in range(301, 10000):
    for x in range(1, 10000):
        f = ((not delit(x, a)) <= (delit(x, 27) <= (not delit(x, 89)))) and (a > 300)
        if f == 0:
            break
    else:
        print(a)
        break