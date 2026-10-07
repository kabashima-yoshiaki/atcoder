"""
最長部分列問題：DPを最長部分列数にして、右下に行く回数を数える
"""
S = str(input())
T = str(input())
N = len(S)
M = len(T)
dp = [[None]*(M+1) for _ in range(N+1)]
dp[0][0] = 0
for i in range(N+1):
    for j in range(M+1):
        if i == 0 or j == 0:
            dp[i][j] = 0
        else:
            if S[i-1] == T[j-1]:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1] + 1)
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[N][M])

