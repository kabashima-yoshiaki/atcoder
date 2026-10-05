N = int(input())
S = input()
DP = [0]*(N+1)

#DP[1]を数える
for i in range(N):
    if S[i] == 'o':
        DP[1] += 1
    elif S[i] == 'x':
        DP[1] += 1
        break

for j in range(2, N+1):
    DP[j] = DP[j-1]
    if DP[j] == N:
        continue
    DP[j] += 1
    if DP[j] < N and S[DP[j]-1] == 'o':
        DP[j] += 1
        while DP[j] < N and S[DP[j]-1] == 'o' :
            DP[j] += 1

for i in range(1, N+1):
    print(DP[i])


    
