n = int(input())
a = list(map(int, input().split()))
k = int(input())

ans = 0

for i in range(n):
    if k <= a[i]:
        ans += 1
print(ans)

