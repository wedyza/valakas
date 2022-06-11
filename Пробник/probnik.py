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
for x in range(1000):
    n = bin(x)[2:]
    n += "10" if x % 2 == 0 else "01"
    n = int(n,2)
    if n > 516:
        print(x)
        break
"""

#6
"""
for i in range(10000):
    s = i
    n = 8
    while s < 156:
        if (s+n) % 3 == 0:
            s += 6
        n += 11
    if n == 140:
        print(i)
"""
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

