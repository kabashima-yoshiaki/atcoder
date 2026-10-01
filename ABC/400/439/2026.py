import math 

n=int(input())
x=1
y=2
ans=[0]*(n+1)
for x in range(1, math.isqrt(n)+1):
    for y in range(x+1, math.isqrt(n)+1):
        if x**2 + y**2 <= n:
            ans[x**2 + y**2] += 1
sum = 0
n_i=[]
for i in range(n+1):
    if ans[i] == 1:
        sum += 1
        n_i.append(i)
print(sum)
print(*n_i)
