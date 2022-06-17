f = open('01.txt')
arr = []
x = f.readline()
while x != "":
    arr.append(int(x))
    x = f.readline()

c = 0
m = 0

for i in range(len(x) - 1):
    if int(arr[i] ** 0.5) == arr[i]**0.5 or int(arr[i+1]**0.5) == arr[i+1]**0.5:
        c += 1
        m = max(m, arr[i] + arr[i+1])
print(c, m)






"""
f = open('06.txt')
x = f.readline()
arr = []
while x != "":
    arr.append(int(x))
    x = f.readline()

c = 0
m = float('inf')

for i in range(len(arr)-1):
    absum = abs(arr[i])+abs(arr[i+1])
    if absum >= 50 and absum <= 200:
        s = min(arr[i],arr[i+1])
        m = min(s,m)
        c += 1

print(c, m)

f = open('07.txt')
x = f.readline()
arr = []
while x != "":
    arr.append(int(x))
    x = f.readline()

mins = float('inf')
maxn = 0
c = 0

for i in range(len(arr)-1):
    sq = arr[i]**2 + arr[i+1]**2
    if sq % 2 == 1 and sq > 90:
        c += 1
        s = arr[i] + arr[i+1]
        if mins >= s:
            mins = s
            n = max(arr[i], arr[i+1])
            maxn = n
print(c, maxn)

f = open('08.txt')
x = f.readline()
arr = []
while x != "":
    arr.append(int(x))
    x = f.readline()

mins = float('inf')
c = 0

for i in range(len(arr)-2):
    if arr[i] < 0 or arr[i+1] < 0 or arr[i+2] < 0:
        c += 1
        s = arr[i] + arr[i+1] + arr[i+2]
        mins = min(mins, s)
print(c, mins)

f = open('09.txt')
x = f.readline()
arr = []
while x != "":
    arr.append(int(x))
    x = f.readline()

c = 0
maxs = 0

for i in range(len(arr)-1):
    s = arr[i] + arr[i+1]
    if (arr[i] % 5 == 0 or arr[i+1] % 5 == 0) and s % 7 == 0:
        c += 1
        maxs = max(maxs, s)
print(c, maxs)

f = open('10.txt')
arr1 = []
arr = []
c = 0
for i in range(5541):
    c += 1
    x = int(f.readline())
    arr.append(x)
    if c % 2 == 1:
        arr1.append(x)
    
c = 0
m = sum(arr1)/len(arr1)
maxs = 0
for i in range(5540):
    if (arr[i] % 5 == 0 or arr[i+1] % 5 == 0) and (arr[i]< m or arr[i] < m):
        maxs = max(maxs, arr[i]+arr[i+1])
        c += 1
print(c, maxs)
"""

    
