n,k=map(int,input().split())
a=list(map(int,input().split()))
b=sorted(a)
same=[0]*n
for i in range(n):
    if a[i] == b[i]:
        same[i] = 1
    if i > 0:
        same[i] += same[i-1]
for x in range(n-k):
    if x == 0:
        if same[n-1] - same[x+k-1] == len(same[x+k:]):
            print("Yes")
            break
    else:
        if same[x] == x and same[n-1] - same[x+k-1] == len(same[x+k:]):
            print("Yes")
            break
else:
    print("No")
    