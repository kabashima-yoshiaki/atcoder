c=int(input())

for _ in range(c):
    n,h= map(int,input().split())
    target = []
    T=0
    L=h
    R=h
    ok=True
    for _ in range(n):
        t,l,r= map(int,input().split())
        L-=t-T
        R+=t-T
        T = t
        L=max(L,l)
        R=min(R,r)
        if L > R:
            ok = False
    if ok:
        print("Yes")
    else:
        print("No")



