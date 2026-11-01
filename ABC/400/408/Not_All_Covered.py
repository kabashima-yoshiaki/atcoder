n,m=map(int,input().split())
zyouheki=[0]*(n+1)
for i in range(m):
    l,r=map(int,input().split())
    l-=1
    zyouheki[l]+=1
    zyouheki[r]-=1
ans=zyouheki[0]
for j in range(1, n):
    zyouheki[j] += zyouheki[j-1]
    if zyouheki[j] == 0 or ans == 0:
        print(0)
        break
    else:
        ans = min(ans, zyouheki[j])
else:
    print(ans)
