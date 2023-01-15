symbols = 'ABCDX'

count = 0
for _1 in symbols:
    for _2 in symbols:
        for _3 in symbols:
            for _4 in symbols:
                word = _1 + _2 + _3 + _4
                if word.count('X') == 1:
                    count += 1
print(count)

# 256, но вручную считать гораздо проще