n, k, x=map(int,input().split())
a=list(map(int,input().split()))

a.sort(reverse=True)
drink = 0
cnt = 0
for sake in a[n-k:]:
    if x  > drink:
        drink += sake
        cnt +=1
if x > drink:
    cnt = 0
print(cnt+n-k if cnt >= 1 else -1)