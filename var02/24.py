f = open('24.txt')

string = f.readline()
string = string.replace('XYZ', 'XY YZ')
string = string.split()

print(len(max(string, key=len)))

# 305