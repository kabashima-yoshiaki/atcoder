n,q=map(int,input().split())
s = [set() for _ in range(n)]

for _ in range(q):
    l,r,x=map(int,input().split())
    for i in range(l-1,r):
        s[i].add(x)

