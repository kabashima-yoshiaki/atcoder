#==================================
#【ビット演算】
# k番目のビットを見る:(x >> k) & 1
# k番目を1にする:(x | (1 << k)) 
# k番目を0にする:x & ~ (1 << k)
# k番目を反転する:x^(1<<k)          
#
#
#==================================
N, M = map(int, input().split())
A = [None]*M
for i in range(M):
    A[i] = list(map(int, input().split()))

dp = [[10**9]*(2**N) for _ in range(M+1)] 
dp[0][0] = 0
for i in range(1, M+1):
    for j in range(0, 2**N):
        already = [None]*N
        for k in range(N):
            if(j >> k) & 1 == 1:
                already[k] = 1
            else:
                already[k] = 0
            
        v = 0
        for k in range(0, N):
            if already[k] == 1 or A[i-1][k] == 1:
                v += ( 2 ** k)

        dp[i][j] = min(dp[i][j], dp[i-1][j])
        dp[i][v] = min(dp[i][v], dp[i-1][j]+1)

if dp[M][2**N -1] == 1000000000:
    print("-1")
else:
    print(dp[M][2**N -1])
