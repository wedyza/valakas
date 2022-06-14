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
"""
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
