"""
EX15-1
A = list(map(int, input().split()))
B = list(map(int, input().split()))
answer = False

for i in range(len(A)):
    for j in range(len(B)):
        A[i] == B[j]
        answer = True

if answer:
    print("YES")
else:
    print("NO")
"""

#EX15-2
N, S = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = 0

for i in range(N):
    for j in range(N):
        if S == A[i] + B[j]:
            result += 1

print(result)
