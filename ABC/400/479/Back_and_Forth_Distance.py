n,q=map(int,input().split())
l=list(map(int,input().split()))
r=list(map(int,input().split()))
query=[list(map(int,input().split())) for _ in range(q)]

one=0
for s,t in query:
    if s - t < 0:
        one = r[s-1]
    else:
        one = l[t-1]


    print(one)
