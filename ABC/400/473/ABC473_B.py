N = int(input())
A = list(map(int, input().split()))
A.sort()
cnt = 0
while len(A) > cnt+1:
    if A[cnt] == A[cnt+1]:
        A.pop(cnt)
        A.pop(cnt)
    else:
        cnt += 1
print(sum(A))
        