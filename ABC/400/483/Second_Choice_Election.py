n,m=map(int,input().split())
one=[0]*(n+1)
two=[[]for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    two[a].append(b)
    one[a]+=1
one.sort()

print(two)
