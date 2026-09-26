N = int(input())
L = list(map(int, input().split()))
current = 0.5
ans = 0
T = []
for bit in range(1 << N):
    t = []
    for j in range(N):
        if ((bit >> j) & 1):
            t.append(True)
        else:
            t.append(False)
    T.append(t)
ans = []
for T1 in T:
    current = 0.5
    answer = 0
    for T2 in T1:
        if T2:
            before = current
            current += T2
            if before * current < 0:
                answer += 1
        else:
            before = current
            current -= T2
            if before * current < 0:
                answer += 1
    ans.append(answer)
print(max(ans))