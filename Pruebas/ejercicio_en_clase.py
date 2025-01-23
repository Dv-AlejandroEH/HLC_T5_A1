abc = [1,1,1,1,1,1,1,1,1,1,1,1,2]

for i in range(len(abc)-2):
    if 1 in abc:
        abc.remove(1)
print(abc)
