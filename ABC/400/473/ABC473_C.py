N, K = map(int, input().split())
A = list(map(int, input().split()))

C = [0]*(K)
for a in A:
    C[a-1] += 1
C.sort(reverse = True)
memo1 = C[0]
memo2 = C[0] - 1
ans = 0
for c in C:
    if c == memo1 or c == memo2:
        ans += 1
print(ans)