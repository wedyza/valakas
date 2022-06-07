#1
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                expr = (x == ( y <= z )) and ((not w) <= (x == y))
                if expr == 1:
                    print(x, y, z, w)
