"""
def f(x,p):
    if x >= 50 or p > 5:
        return p == 5 
    if p % 2 == 0:
        return f(x+3, p+1) or f(x*3, p+1)
    else:
        return f(x+3, p+1) and f(x*3, p+1)

for s in range(1,49):
    if f(s,1):
        print(s)

s П В П В
1 2 3 4 5
(в тетради есть)
код для решения задач с 1 кучей
в 19 надо обращать внимания на то, какой ход был сделан Петей.
Если этот ход неудачный, то его можно не рассматривать, а если наоборот - удачный,
то надо рассмотреть эти ходы.
(Рассматривать - как выше)
(Не рассматривать - return f(x+y, p+1) or f...
"""

def f(x,p):
    if x >= 50 or p > 5:
        return p == 5
    if p % 2 == 0:
        return f(x+3, p+1) or f(x*3, p+1)
    else:
        return f(x+3, p+1) and f(x*3, p+1)
    
for s in range(1,48):
    if f(s,1):
        print(s)
