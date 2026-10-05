N, M = map(int, input().split())
K = [[]for _ in range(M+1)]

for i in range(N):
    c, s = map(int, input().split())
    K[c].append(s)
for i in range(1, M+1):
    if len(K[i]) == 0:
        print(-1, end = ' ')
    else:
        print(max(K[i]), end = ' ')

