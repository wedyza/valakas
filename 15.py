"""def f(a):
    for x in range(1,1000):
        if not((x % a != 0) <= ((x%18==0) <= (x%81 != 0))):
            return False
    return True

for a in range(1000,1,-1):
    if f(a):
        print(a)
        break
"""

"""
в этом задании есьть несколько видов.
"""
"""
def f(a):
    for x in range(1,1000):
        for y in range(1,1000):
            if not ((x >= a) or (y >= a) or (x*y <= 200)):
                return False
    return True

for a in range(1000,1,-1):
    if f(a):
        print(a)
        break
"""
"""
def f(a):
    for x in range(1,1000):
        for y in range(1,1000):
            if not((3*x + y < a) or (x < y) or (16 <= x)):
                return False
    return True

for a in range(1,1000):
    if f(a):
        print(a)
        break
"""
"""
def f(a):
    for x in range(1,1000):
        for y in range(1,1000):
            if not((y + 5*x <= 34) <= ((y - x > 4) or (y <= a))):
                return False
    return True

for a in range(-1000,1000):
    if f(a):
        print(a)
        break
"""
# & -поразрядная конъюкция
"""
def f(a):
    for x in range(1,1000):
        if not( (x & 46 != 0) <= ((x & 42 == 0) <= (x & a!= 0))):
            return False
    return True

for a in range(1,1000):
    if f(a):
        print(a)
        break
"""

"""
def f(a):
    for x in range(1,1000):
        if not((a < 50) and ((x % a != 0) <= ((x%10==0)<=(x%18!=0)))):
            return False
    return True


for a in range(1000,1,-1):
    if f(a):
        print(a)
        break
"""
"""
def f(a):
    for x in range(1,1000):
        if not((a % 40 == 0) and ((780 % x == 0) <= ((a % x != 0) <= (180 % x != 0)))):
            return False
    return True




for a in range(1, 1000):
    if f(a):
        print(a)
        break
"""

def f(a):
    for x in range(1000):
        if not( (x & 49 == 0) <= ((x & 28 != 0) <= (x&a != 0))):
            return False
    return True

for a in range(1000):
    if f(a):
        print(a)
        break





