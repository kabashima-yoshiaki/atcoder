n=int(input())
a=list(map(int,input().split()))

from collections import defaultdict
di=defaultdict(int)

ans = 0
for j in range(1, n+1):
    ans += di[j-a[j-1]]
    di[j+a[j-1]] += 1
print(ans) 