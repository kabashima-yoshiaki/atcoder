n,m=map(int,input().split())
mass = set()
cnt = 0
block = [[0,0], [0,1], [1,0], [1,1]]
for i in range(m):
    r,c=map(int,input().split())
    for b in block:
        if (r+b[0],c+b[1]) in mass:
            break
    else:
        cnt += 1
        for b in block:
            mass.add((r+b[0],c+b[1]))

print(cnt)