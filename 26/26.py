"""
f = open('02.txt')
matrix = [['0' for i in range(10000)] for x in range(10000)]
n = int(f.readline())

for i in range(n):
    string = f.readline().split()
    x = int(string[0])-1
    y = int(string[1])-1
    matrix[x][y] = '1'

maxs = 0
number = 0

for i in range(10000):
    current = ''.join(matrix[i])
    count = 0
    for j in range(1,10000-i+1):
        switch = '10'*j
        if switch in current:
            count = j
        else:
            break
    if maxs < count:
        maxs = count
        number = i + 1
print(maxs, number)

f = open('03.txt')
matrix = [['' for i in range(10000)] for x in range(10000)]
n = int(f.readline())

for i in range(n):
    string = f.readline().split()
    x = int(string[0])-1
    y = int(string[1])-1
    if (y+1)%2 == 1:
        matrix[x][y] = '1'

pos = 0
maxs = 0

for i in range(10000):
    current = ''.join(matrix[i])
    switch = len(current)
    if maxs < switch:
        maxs = switch
        pos = i + 1
print(maxs, pos)
"""
f = open('04.txt')
matrix = [['0' for i in range(10000)] for x in range(10000)]
n = int(f.readline())

for i in range(n):
    string = f.readline().split()
    x = int(string[0])-1
    y = int(string[1])-1
    matrix[x][y] = '1'

maxs = 0
maxx = 0
thes = ''

def find(s, l):
    for i in range(10000):
        if s[i:i+l] == '1'*l:
            return i


ras = 0

for i in range(10000):
    current = ''.join(matrix[i])
    count = 0
    for j in range(1, 10000-i+1):
        switch = '1'*j
        if switch in current:
            count = j
        else:
            break
    if maxs < count:
        maxs = count
        maxx = i
        thes = current
        n1 = abs(find(thes, maxs))
        m1 = abs(10000-maxx)
        ras = min(n1,m1)
    elif maxs == count:
        n1 = abs(10000-find(thes, maxs))
        n2 = abs(10000-find(current, maxs))
        m1 = abs(10000-maxx)
        m2 = abs(10000-i)
        min1 = min(n1,m1)
        min2 = min(n2,m2)
        if min2 > min1:
            maxx = i
            thes = current
            ras = min2
print(maxx+1, ras)

