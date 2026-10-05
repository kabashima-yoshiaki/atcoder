N = int(input())
S = [[] for _ in range(N+1)] 
for i in range(1, N+1):
    A = list(map(int, input().split()))
    K = A[0]
    for j in range(1, K+1):
        S[A[j]].append(i) 
for i in range(1, N+1):
    if len(S[i]) == 0:
        print(0)
    else:
        S1 = len(S[i])
        S2 = S[i]
        S2 = [str(a) for a in S2]
        S2 = ' '.join(S2)
        print(S1, end = ' ')
        print(S2)

