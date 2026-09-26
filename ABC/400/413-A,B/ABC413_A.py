N, M = map(int, input().split())
A = list(map(int, input().split()))
sum = A[0]
for i in range(1, N):
    sum += int(A[i])

if sum <= M:
    print("Yes")
else:
    print("No")