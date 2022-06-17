"""
def f(n):
    mind = float('inf')
    maxd = 0
    for i in range(2,n-1):
        if n % i == 0:
            mind = min(mind, i)
            maxd = max(maxd, i)
    return maxd - mind


for i in range(850000,851001):
    z = f(i)
    if z > 0 and z % 7 == 0:
        print(i, z)

def f(n):
    s = 0
    for i in range(2,n-1):
        if n % i == 0:
            if isPrime(i):
                s += i
    return s

def isPrime(n):
    for i in range(2,int(n**0.5)):
        if n % i == 0:
            return False
    return True

for n in range(550001, 550501):
    z = f(n)
    if z % 10 == 1:
        print(n, z)


def m(n):
    arr = []
    for i in range(2,int(n**0.5)):
        if n % i == 0:
            arr.append(i)
            if len(arr) == 5:
                p = 1
                for j in arr:
                    p *= j
                return p
    return 0

for n in range(500000001,500000050):
    sm = m(n)
    if sm > 0 and sm < n:
        print(sm)


def m(n):
    s = 0
    c = 0
    for i in range(n//2,2,-1):
        if n % i == 0:
            c += 1
            s += i
            if c == 2:
                return s
    return 0

for i in range(11000001, 11000500):
    s = m(i)
    if s > 0 and s < 10000:
        print(s)


# вот эта херня для определения всех делителей числа(доработана)

def m(n):
    divs = []
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            divs.append(i)
            if i != n // i:
                divs.append(n // i)
    divs = sorted(divs)
    if len(divs) >= 5:
        return divs[-5]
    return 0
c = 0
for n in range(300000001,300000050):
    z = m(n)
    if z > 0:
        print(z)
        c += 1
        if c == 5:
            break

def m(k):
    arr = []
    for i in range(2,int(k**0.5)+1):
        if k % i == 0:
            if i % 2 == 0:
                arr.append(i)
            if i != k // i and (k // i) % 2 == 0:
                arr.append(k//i)
    return len(arr)%2 == 1
s = 900000000
for j in range(1,25):
    if m(s+j):
        print(j)
"""

def n(k):
    p = True
    for d1 in range(2,int(k**0.5)+1):
        if k % d1 == 0:
            for d2 in range(2, int(k**0.5)+1):
                if k % d2 == 0:
                    p = False
    return p

c = 500000000
for k in range(250):
    if n(c+k):
        print(k)



























