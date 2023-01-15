p = [i for i in range(43, 50)]
q = [i for i in range(44, 54)]

a1 = [i for i in range(0, 43)]
a2 = [i for i in range(0, 44)]
a3 = [i for i in range(43, 50)]
a4 = [i for i in range(43, 54)]
a5 = [i for i in range(44, 50)]
a6 = [i for i in range(44, 54)]
a7 = [i for i in range(54, 100)]

for a in (a1, a2, a3, a4, a5, a6, a7):
    for x in range(1, 100):
        if ((x in a) <= (x in p)) or (x in q) == False:
            break
    else:
        print(a)
