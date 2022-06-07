def f(x,y,p):
    if x + y >= 118 or p > 5:
        return p == 3 
    if p % 2 != 1:
        return f(x+2,y,p+1) or f(x,y+2,p+1) or f(x*2,y,p+1) or f(x,y*2,p+1)
    else:
        return f(x+2,y,p+1) and f(x,y+2,p+1) and f(x*2,y,p+1) and f(x,y*2,p+1)

for s in range(1,114):
    if f(3,s,1):
        print(s)
        
"""
короче, все то же самое, как и с одной кучей, но только с 2 :)
надо учитывать все случаи, смотреть на текст задания внимательно,
может быть какая-то ловушка.
"""
