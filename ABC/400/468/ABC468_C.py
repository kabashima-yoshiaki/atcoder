N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
import math
cnt = 0
R = [i for i in range(N, 0, -1)]

def order (S):
    res = 0
    while S:
        res += sum(s < S[0] for s in S) * math.factorial(len(S) - 1)
        S = S[1:]
    return res+1

ans = order(Q) - order(P) 
if ans <= 0:
    print(0)
else:
    print(ans-1)
