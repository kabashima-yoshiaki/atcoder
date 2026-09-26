N, K = map(int, input().split())

DP = [[0] for _ in range(N)]
for i in range(1, N+1):
    T = []
    cnt = 0
    while cnt <= K:
        T.append(cnt)
        cnt += i
    DP[i-1] = T
print(DP)