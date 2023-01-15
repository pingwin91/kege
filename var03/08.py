def f():
    chars = 'EKOP'
    count = 0
    for _1 in chars:
        for _2 in chars:
            for _3 in chars:
                for _4 in chars:
                    for _5 in chars:
                        for _6 in chars:
                            word = _1 + _2 + _3 + _4 + _5 + _6
                            count += 1
                            if _1 == 'O' and 'EE' not in word:
                                return count


print(f())