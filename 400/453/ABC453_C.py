import numpy 
N = int(input())
L = list(map(int, input().split()))
current = 0.5
ans = []
for bit in range(1 << N):
    t = []
    current = 0.5
    answer = 0
    for j in range(N):
        before = current
        if ((bit >> j) & 1):
            current -= L[j]
        else:
            current += L[j]
        if (before > 0) != (current > 0):
            answer += 1
    ans.append(answer)

print(max(ans))