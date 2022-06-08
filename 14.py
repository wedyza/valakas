#1
"""
expr = 5**2022 - 2*5**1010 + 25**850 + 2500
c = 0
while expr > 0:
    if expr % 5 == 4:
        c += 1
    expr //= 5
print(c)
"""

#2
"""
expr = 2*3**2022 + 5 * 3**1800 + 4*3**1000 + 3**1001 + 3
c = 0
while expr > 0:
    if expr % 9 == 0:
        c += 1
    expr //= 9
print(c)
"""

#3
"""
expr = 81**17 + 3**24 - 45
c = 0
while expr > 0:
    if expr % 9 == 8:
        c += 1
    expr //= 9
print(c)
"""

#4
"""
e = 343**6 - 7**10 + 47
c= 0
while e > 0:
    if e % 7 == 6:
        c += 1
    e //= 7
print(c)
"""

#5
#"""
e = 216**5 + 6**3 - 1
for x in range(1000):
    new = e - x
    c = 0
    while new > 0:
        if new % 6 == 5:
            c += 1
        new //= 6
    if c == 12:
        print(x)
        break

"""
задание легкое - пояснений, я думаю, не нужно...




