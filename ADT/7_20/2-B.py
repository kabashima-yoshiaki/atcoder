import copy
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

def kaiten(P, N):
    ans = copy.deepcopy(P)
    memo = copy.deepcopy(P)
    for i in range(N):
        for j in range(N):
            ans[i][j] = memo[N-j-1][i]
    return ans

def check(P, N):
    flag = True
    for i in range(N):
        for j in range(N):
            if P[i][j] == 1 and B[i][j] != 1:
                flag = False
                break
        if not flag:
            break
    return flag

A1 = kaiten(A, N)
A2 = kaiten(A1, N)
A3 = kaiten(A2, N)    
if check(A, N) or check(A1, N) or check(A2, N) or check(A3, N):
    print("Yes")
else:
    print("No")