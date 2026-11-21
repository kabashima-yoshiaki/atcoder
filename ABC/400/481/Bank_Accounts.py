from collections import defaultdict

q =int(input())
query=[input() for _ in range(q)]

kouza=defaultdict(int)
ID = 1

for que in query:
    if que  in kouza:
        print(kouza[que])
    else:
        print(ID)
        kouza[que] = ID
        ID += 1
