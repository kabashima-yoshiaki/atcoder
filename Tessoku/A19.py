"""
ナップザック問題（容量の制限で価値の合計の最大を出す）：DP
品物をi合計の重さをj、最大価値をDPとして、×を小さい値にするといい
"""
N, W = map(int, input().split())
dp = [[-10**15]*(W+1) for _ in range(N+1)]
dp[0][0] = 0
w = [None]* (N+1)
v = [None]* (N+1)

for i in range(1, N+1):
    w[i], v[i] = map(int, input().split())

for i in range(1, N+1):
    for j in range(0, W+1):
        if j < w[i]:
            dp[i][j] = dp[i-1][j]
        if j >= w[i]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]] + v[i])

print(max(dp[N]))
