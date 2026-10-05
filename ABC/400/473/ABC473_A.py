N = int(input())
A = list(map(int, input().split()))
t = N // 2
ans = 0
for i in range(t, N):
    ans += A[i]
print(ans)