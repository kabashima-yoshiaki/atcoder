n,q=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
ans = 0
for a_i, b_i in zip(a,b):
    ans += min(a_i,b_i)

for i in range(q):
    c,x,v=input().split()
    x,v=int(x),int(v)
    ans -= min(a[x-1], b[x-1])
    if c == "A":
        a[x-1] = v
        ans += min(a[x-1], b[x-1])
    else:
        b[x-1] = v
        ans += min(a[x-1], b[x-1])

    print(ans)