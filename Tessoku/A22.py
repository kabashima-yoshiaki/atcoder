"""
一手先を更新するDP
"""
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [0]*(N+1)

for i in range(N-1):

    dp[A[i]] = max((dp[i+1] + 100), dp[A[i]])
    dp[B[i]] = max((dp[i+1] + 150), dp[B[i]])

print(dp[N])
