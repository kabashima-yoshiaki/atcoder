#==================================
#【DPの考え方】
#1:どのような配列を持つか      
#2:配列の遷移
#配列のどこが求めるべき答えになるのか
#==================================
H, W = map(int, input().split())
C = [list(input()) for _ in range(H)]
dp = [[0] * (W+1) for _ in range(H+1)]

for i in range(H):
    for j in range(W):
        if i == 0 and j == 0:
            dp[0][0] = 1
        else:
            dp[i][j] = 0
            if i >= 1 and C[i-1][j] == '.':
                dp[i][j] += dp[i-1][j]
            if j >= 1 and C[i][j-1] == '.':
                dp[i][j] += dp[i][j-1]

print(dp[H][W])
