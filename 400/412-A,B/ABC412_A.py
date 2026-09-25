n = int(input())
ans = 0
for i in range(n):
    ab = list(map(int, input().split()))
    if ab[0] < ab[1]:
        ans += 1
print(ans)

