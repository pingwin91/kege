string = '>' + '2' * 15 + '3' * 20 + '5' * 25

summa = 0
while '>2' in string or '>3' in string or '>5' in string:
    if '>2' in string:
        string = string.replace('>2', '333>')
        summa += 9
    if '>3' in string:
        string = string.replace('>3', '23>')
        summa += 5
    if '>5' in string:
        string = string.replace('>5', '35>')
        summa += 8
print(summa)