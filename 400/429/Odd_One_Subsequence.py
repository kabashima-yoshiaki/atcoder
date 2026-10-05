import math
n=int(input())
a=list(map(int,input().split()))
a.sort()
ans = 0
L=dict()
for a_i in a:
    if a_i not in L:
        L[a_i] = 0
    L[a_i] += 1
 
for key,val in L.items():
    ans +=  math.comb(val,2)*(n-val)
print(ans)
