N = int(input())

P = [0] * (N + 1)

for _ in range(N):
    X, Y = map(int, input().split())
    P[X] = Y

ans = 0
mn = N + 1

for x in range(1, N + 1):
    if P[x] < mn:
        ans += 1
        mn = P[x]

print(ans)