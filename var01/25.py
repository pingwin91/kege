'''
126789 3251
1296789 33251
12216789 313251
12606789 323251
12996789 333251
'''

mask = '12*6789'

if 126789 % 39 == 0:
    print(126789, 126789 // 39)
if 12006789 % 39 == 0:
    print(126789, 126789 // 39)
for i in range(100):
    number = int(mask.replace('*', str(i)))
    if number % 39 == 0:
        print(number, number // 39)