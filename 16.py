"""
def f(n):
    if n <= 1:
        return 1
    elif n > 1 and n % 2 == 1:
        return 5*n + f(n-1) + f(2)
    else:
        return 3*f(n-1)

print(f(23))


def f(n):
    if n <= 1:
        return 2
    elif n > 1 and n % 2 == 1:
        return 1 + f(n-1) * f(n-2) - f(n-1) - f(n-2)
    else:
        return 2*f(n-1)


print(f(12))
"""
"""
def f(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n > 2 and n % 2 == 0:
        return int((7*n + f(n-3))/9)
    elif n > 2 and n % 2 == 1:
        return int((5*n + f(n-1) + f(n-2))/7)


print(f(50))
"""

"""
def f(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2 and n % 2 == 0:
        return int((n*f(n-1))/2)
    elif n > 2 and n % 2 == 1:
        return int((n*(f(n-1)+f(n-2)))/3)

print(f(13))
"""
"""
def f(n):
    if n == 1:
        return 1
    elif n > 1 and n % 2 == 1:
        return n + f(n-2)
    elif n % 2 == 0:
        return n * f(n-1)


print(f(60))
        """
def f(n):
    if n == 0:
        return 0
    elif n % 2 == 1:
        return f(n-1) + 1
    elif n > 0 and n % 2 == 0:
        return f(n/2)

c = 0
for x in range(1,10**9):
    if f(x) == 3:
        c += 1
print(c)








