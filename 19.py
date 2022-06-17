# +1 +2 *2
"""def(x, p, h1, h2, h3):
    if x >= 29 or p > 4:
        return p == 4 or p == 2
    if p <= 2:
        if p % 2 == 1:
            return f(x+1,p+1,[1) or f(x+2,p+1,) or f(x*2,p+1,)
        else:
            return f(x+1,p+1,) and f(x+2,p+1,) and f(x*2,p+1,)
    else:
        if p % 2 == 1:
            if h1 == 1:
                return f(x+2,p+1,0,1,0) or f(x*2,p+1,0,0,1)
            elif h2 == 1:
                return f(x+1,p+1,1,0,0) or f(x*2,p+1,0,0,1)
            elif h3 == 1:
        else:
            return f(x+1,p+1,1,0,0) and f(x+2,p+1,0,1,0) and f(x*2,p+1,0,0,1)
#+6 x**2/y**2
def f(x,y,p):
    if x + y >= 200 or p > 5:
        return p == 5
    if p % 2 == 0:
        return f(x+6,y,p+1) or f(x**2,y,p+1) or f(x,y+6,p+1) or f(x,y**2,p+1)
    else:
        return f(x+6,y,p+1) and f(x**2,y,p+1) and f(x,y+6,p+1) and f(x,y**2,p+1)

for i in range(1,195):
    if f(3,i,1):
        print(i)

def f(x,y,p):
    if x + y >= 144 or p > 4:
        return p == 4
    if p % 2 == 1:
        return f(x+1,y,p+1) or f(x*2,y,p+1) or f(x,y+1,p+1) or f(x,y*2,p+1)
    else:
        return f(x+1,y,p+1) and f(x*2,y,p+1) and f(x,y+1,p+1) and f(x,y*2,p+1)

for s in range(1,143):
    if f(1,s,1):
        print(s)
       

def f(x, p):
    if x >= 100 or p > 5:
        return p == 5
    if p % 2 == 0:
        return f(x+4,p+1) or f(x*2, p+1)
    else:
        return f(x+4,p+1) and f(x*2, p+1)


for s in range(1,97):
    if f(s,1):
        print(s)
        

# +1 +2 *2
def f(x,p,h1,h2,h3):
    if x >= 50 or p > 5:
        return p == 3
    if p % 2 == 0:
        if h1 == 1:
            return f(x+2,p+1,0,1,0) or f(x*2,p+1,0,0,1)
        elif h2 == 1:
            return f(x+1,p+1,1,0,0) or f(x*2,p+1,0,0,1)
        elif h3 == 1:
            return f(x+2,p+1,0,1,0) or f(x+1,p+1,1,0,0)
        else:
            return f(x+1,p+1,1,0,0) or f(x+2,p+1,0,1,0) or f(x*2,p+1,0,0,1)
    else:
        if h1 == 1:
            return f(x+2,p+1,0,1,0) and f(x*2,p+1,0,0,1)
        elif h2 == 1:
            return f(x+1,p+1,1,0,0) and f(x*2,p+1,0,0,1)
        elif h3 == 1:
            return f(x+2,p+1,0,1,0) and f(x+1,p+1,1,0,0)
        else:
            return f(x+1,p+1,1,0,0) and f(x+2,p+1,0,1,0) and f(x*2,p+1,0,0,1)


for s in range(1,50):
    if f(s,1,0,0,0):
        print(s)
"""

def f(x,p):
    if x >= 26 or p > 6:
        return p == 6 
    if x % 2 == 1:
        if p % 2 == 1:
            return f(x+1,p+1) or f(x+2,p+1)
        else:
            return f(x+1,p+1) and f(x+2,p+1)
    else:
        if p % 2 == 1:
            return f(x+1,p+1) or f(x+2,p+1) or f(x*2,p+1)
        else:
            return f(x+1,p+1) and f(x+2,p+1) and f(x*2,p+1)

for s in range(1,26):
    if f(s,1):
        print(s)


























