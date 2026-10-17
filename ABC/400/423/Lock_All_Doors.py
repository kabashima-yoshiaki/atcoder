n,r=map(int,input().split())
l=list(map(int,input().split()))

l_open=[i for i in range(n) if l[i] == 0]
if not l_open:
    print(0)
    exit()
ans = 0
x=min(l_open[0], r) 
y=max(l_open[-1], r)
for i in range(x,y+1):
    ans += l[i] +1
print(ans)