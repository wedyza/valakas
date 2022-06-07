#1
"""
for i in range(100,1000):
    n1 = i // 100
    n2 = i//10 -n1*10
    n3 = i % 10
    s1 = str(n1*n1 + n2*n2)
    s2 = str(n2*n2 + n3*n3)
    if s1+s2 == "9752":
        print(i)
        break
"""

#2
"""
for n in range(1000):
    n -= n%4
    n = bin(n)[2:]
    n += str(n.count("1")%2)
    n += str(n.count("1")%2)
    r = int(n,2)
    if r > 56:
        print(r)
"""
#3
"""
for n in range(1000):
    n -= n%8
    n += n%2
    n = bin(n)[2:]
    n += str(n.count("1")%2)
    n += str(n.count("1")%2)
    r = int(n,2)
    if r > 90:
        print(r)
"""
#4
"""
for n in range(1000):
    n = bin(n)[2:]
    n = n.replace("0","00")
    n = n.replace("1","11")
    r = int(n,2)
    if r > 32:
        print(r)
        break
"""
#5
"""
for n in range(1000):
    r = bin(n)[2:]
    if n % 4 == 0:
        r += "00"
    elif n % 4 == 1:
        r += "01"
    elif n % 4 == 2:
        r += "10"
    else:
        r += "11"
    r = int(r,2)
    if r < 100:
        print(r)
"""
#dat ist end.





    
