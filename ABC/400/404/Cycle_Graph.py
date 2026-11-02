n,m=map(int,input().split())
G=[[] for _ in range(n)]
for _ in range(m):
    a,b=map(int,input().split())
    a-=1
    b-=1
    G[a].append(b)
    G[b].append(a)

seen = [False]*(n)
stack = [0]
seen[0] = True

while stack:
    v = stack.pop()
    for nv in G[v]:
        if not seen[nv]:
            seen[nv] = True
            stack.append(nv)

if not all(seen):
    print("No")
    exit()

if all(len(i) == 2 for i in G):
    print("Yes")
else:
    print("No")
