N, K =map(int, input().split())
A = list(map(int, input().split()))
S = []
A.sort()
t = A[0]
b = A[0]
for i in range(1, len(A)):
    if b == A[i]:
        t += A[i]
    else:
        S.append(t)
        b = A[i]
        t = A[i]
S.append(t)
S.sort(reverse = True)


print(sum(S[K:]))


