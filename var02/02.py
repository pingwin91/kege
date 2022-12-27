for x in range(2):
    for y in range(2):
        for z in range(2):
            f = ((not x) and y and z) or ((not x) and (not y) and z) or ((not x) and (not y) and (not z))
            if f == 1:
                print(x, y, z)

# zxy