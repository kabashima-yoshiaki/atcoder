n=int(input())
parts = [tuple(map(int,input().split())) for _ in range(n)]
S = sum(w for w,h,b in parts)
cap = S // 2
base = sum(b for w,h,b in parts)

dp = [[0]*(cap+1) for _ in range(n+1)]
for i in range(1,n+1):
    w,h,b=parts[i-1]
    gain = h-b
    for j in range(cap+1):
        dp[i][j] = dp[i-1][j]
        if j >= w and gain > 0:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + gain)
print(base + dp[n][cap])