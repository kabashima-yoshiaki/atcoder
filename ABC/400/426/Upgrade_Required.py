n,q=map(int,input().split())
pc=[1]*(n+1)
pc[0]=0
for _ in range(q):
    x,y=map(int,input().split())
    cnt = 0
    while pc[x] != 0:
        cnt += pc[x]
        pc[x] = 0
        x-=1
    pc[y] += cnt
    print(cnt)
