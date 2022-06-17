"""
for s in range(1000):
    x = s
    a = 0
    b = 0
    while x > 0:
        a += 1
        b += 9 - x % 10
        x //= 10
    if a == 2 and b == 8:
        print(s)
        break

for s in range(1000):
    x = s
    q = 15
    l = 0
    while x >= q:
        l += 1
        x -= q
    m = x
    if m < l:
        m = l
        l = x
    if l == 3 and m == 7:
        print(s)

for s in range(1000):
    x = s
    q = 2
    l = 0
    while x >= 5:
        l += 1
        x //= q
    m = x
    if m < l:
        m = l
        l = x
    if l == 3 and m == 4:
        print(s)

for z in range(1000):
    x = z
    p = 0
    s = 6 * (x - x % 22)
    i = 1
    while p < s:
        s -= 2 * i
        p += i
        i += 1
    if s == 82 and p == 91:
        print(z)

for z in range(10000):
    x = z
    l = 1
    m = 0
    while x > 0:
        m += 1
        if x % 8 > 3:
            l *= x % 8
        x //= 8
    if l == 120 and m == 4:
        print(z)

for z in range(10000):
    x = z
    l = 0
    m = 0
    while x > 0:
        m += 1
        if x % 2 == 1:
            l += 1
        x //= 2
    if m == 7 and l == 4:
        print(z)

for z in range(100,100001):
    x = z
    l = x
    m = 77
    if l % 2 == 0:
        m = 32
    while l != m:
        if l > m:
            l -= m
        else:
            m -= l
    if m == 16:
        print(z)
        break

for z in range(5,100000):
    x = z
    a = 7*x + 27
    b = 7*x - 33
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    if a == 10:
        print(z)
        break



for z in range(1,100000):
    a = 0
    b = 0
    x = z
    while x > 0:
        a += 1
        if x % 2 == 0:
            b += x % 100
        x //= 10
    if a == 4 and b == 160:
        print(z)

c = 0
for z in range(1,1000000):
    x = z
    a = 0
    b = 0
    while x > 0:
        a += 1
        d = x % 10
        if d % 3 == 0:
            b += d
        x //= 10
    if a == 9 and b == 75:
        c += 1
print(c)
"""

for z in range(1,100000):
    x = z
    a = 1
    b = 0
    while x > 0:
        d = x % 10
        a *= d
        if d >5:
            b += d
        x //= 10
    if a == 8820:
        print(b)


























