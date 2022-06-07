"""word = "АМОТ"
c = 0
for n1 in word:
    for n2 in word:
        for n3 in word:
            for n4 in word:
                c += 1
                if n1 == "О":
                    print(c)
                    

c = 0
word = "АНДРЕЙ"
for n1 in word:
    for n2 in word:
        for n3 in word:
            for n4 in word:
                for n5 in word:
                    for n6 in word:
                        new = n1+n2+n3+n4+n5+n6
                        if new.count("А")>=1 and new.count("Й") <= 1:
                            c += 1
print(c)
"""
word = "ВАЛЕРИЯ"
#в этом задании необходимо располагать алфавиты в алфавитном порядке важная функция
# - sorted(word).
print(sorted(word)) 
