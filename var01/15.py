for A in range(1, 100):
    flag = True
    for x in range(135):
        for y in range(135):
            logic = ((2 * y + 3 * x) != 135) or (x > A) or (y > A)
            if logic == False:
                flag = False
    if flag:
        print(A)
