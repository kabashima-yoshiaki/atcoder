N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
answer = 0
answer_memo = []
for j in range(2):
    A0 = A
    A0[0] = j
    for i in range(N-2):

        sum_1 = A0[i] + A0[i+1] + B[i]
        sum_2 = A0[i+1] + A0[i+2] + B[i+1]
        if sum_1 % 2 == 0:
            continue
        elif sum_1 % 2 == 1:
            answer += 1
            if sum_2 % 2 == 1:
                A0[i+1] += 1
    if A0[N-2] + A0[N-1] + B[N-2] % 2 == 1:
        answer += 1
    answer_memo.append(answer)
    
print(min(answer_memo))


""" N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
answer = 0
for i in range(N-2):
    if (A[i] + A[i+1]) % M != B[i]:
        answer += 1
        if (A[i+1] + A[i+2] % M != B[i+1]):
            A[i+1] += 1
        else:
            A[i] += 1
if (A[N-2] + A[N-1]) % M != B[N-2]:
    answer += 1
print(A)
print(answer)
         """