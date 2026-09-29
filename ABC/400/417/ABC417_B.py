N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for i in range(M):
    if B[i] in A:
        A.remove(B[i])
A = [str(a) for a in A]
print(" ".join(A))

