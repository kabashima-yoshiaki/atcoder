n = int(input())
a = list(map(int, input().split()))
for i in range(n+1):
    cnt = 0
    x = i
    for j in range(n):
        if a[j] >= x:
            cnt += 1
    if cnt >= x:
        ans = x 

print(ans)
