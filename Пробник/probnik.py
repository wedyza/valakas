#2
"""
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                expr = not( x <= z ) or (y == w) or y
                if expr == 0:
                    print(x, y, z, w)
"""
#5
"""
x = int(input())
n = bin(x)[2:]
if x % 2 == 1:
    n = "1" + n
n += "10" if x % 2 == 0 else "01"
print(int(n,2))
"""
#6

for i in range(10000):
    s = i // 5
    n = 8
    while s < 156:
        if (s+n) % 3 == 0:
            s += 6
        n += 11
    if n == 140:
        print(i)

#8
"""
word = "ЕКЛОСТ"
c = 0
for s1 in word:
    for s2 in word:
        for s3 in word:
            for s4 in word:
                for s5 in word:
                    new = s1 + s2 + s3 + s4 + s5
                    c += 1
                    if new[0] == "С" and "ОО" in new:
                        print(c)
                        exit()
"""
#9
"""
st = "0" + "2"*10 + "3"*25 + "1"*16 + "0"
while not("00" in st):
    st = st.replace("01","210")
    st = st.replace("02", "3101")
    st = st.replace("03", "2012")
print(st.count("1"), st.count("2"), st.count("3"))
"""
#14
"""
s = 64**12 - 8**14 + 127
c7 = 0
c1 = 0
while s > 0:
    if s % 8 == 7:
        c7 += 1
    elif s % 8 == 1:
        c1 += 1
    s //= 8
print(c1,c7)
"""
#16
"""
def f(n):
    if n == 0:
        return 1
    elif n > 0 and n % 2 == 1:
        return 1 + f(n-1)
    else:
        return f(n/2)
"""
#17
"""
f = open("17-282.txt")
arr = []
arr13 = []
for i in range(10000):
    arr.append(int(f.readline()))
    if arr[i] % 13 == 0:
        arr13.append(arr[i])
c=0
eq = float('inf')
max13 = max(arr13)
for i in range(9999):
    if arr[i] % max13 == 0 or arr[i+1] % max13 == 0:
        c += 1
        eq = min(eq, arr[i]+arr[i+1])
print(c, eq)
"""
#19-21
"""
def f(x, p):
    if x >= 50:
        if x <= 70:
            return p == 5 or p == 3
        else:
            return p - 1 == 3
    if p % 2 == 0:
        return f(x+1,p+1) or f(x*2,p+1)
    else:
        return f(x+1,p+1) and f(x*2,p+1)

for s in range(1,50):
    if f(s, 1):
        print(s)
"""
#22
"""
for i in range(100000000,1,-1):
    x = i
    a = 1
    b = 0
    while x > 0:
        d = x % 9
        a *= d
        b += d
        x //= 9
    if a == 10 and b == 13:
        print(i)
        break
"""
#23
"""
def f(n,k,flag):
    if n == 12 or n == 20:
        return 0
    if n == k:
        return 1
    elif n > k:
        return 0
    else:
        if flag == 0:
            return f(n+1,k,0)+f(n+2,k,0)+f(n*3,k,1)
        else:
            return f(n+1,k,0)+f(n+2,k,0)
print(f(2,15,0)*f(15,30,0)*f(30,38,0))
print(f(2,5,0), f(15,30,0))
"""
#24
"""
f = open("24-1.txt")
x = f.readline()
x = x.replace("A","1")
x = x.replace("B", "1")
x = x.replace("X", "1")

x = x.split("1")


maxlen = 0


for i in range(len(x)-4):
    current = len(x[i] + x[i+1] + x[i+2] + x[i+3] + x[i+4])
    maxlen = max(maxlen, current)

print(maxlen)
"""
#25
"""
for n1 in range(10):
    for n2 in range(10):
        mask = "12345" + str(n1) +"6" + str(n2) + "8"
        num = int(mask)
        if num % 17 == 0:
            print(num, num // 17)
"""
#27

f = open("27-98b.txt")
string = f.readline().split()
n = int(string[0])
k = int(string[1])
arr = []
for i in range(n):
    arr.append(int(f.readline()))

need = list(range(k))[1::]
maxlen = float('inf')
for h in range(n):
    for c in range(h+1,n):
        flag = 0
        srez = arr[h:c+1]
        if len(srez) >= maxlen:
            break
        for i in range(len(need)):
            if not(need[i] in srez):
                flag = 1
                break
        if flag == 0:
            maxlen = min(maxlen, len(srez))
print(maxlen)




