""" 
Lが単調増加になっているからHが単調減少になれば、その時刻の最大値がわかる
L1 < L2かつ、H1 < H2だったらL1, H1は消しても、L1の時の最大値はH2だから大丈夫

"""

from bisect import bisect_right
N = int(input())

stack = []
for _ in range(N):
    h, l = map(int, input().split())
    
    while stack and stack[-1][0] <= h:
        stack.pop()
    stack.append((h,l))


Q = int(input())
T = list(map(int, input().split()))
H = [h for h, l in stack]
L =[l for h, l in stack]
for t in T:
    idx = bisect_right(L, t)
    print(H[idx])



""" 
import bisect
N = int(input())
HL = []
H = []
L = []

for i in range(N):
    HL= (list(map(int, input().split())))
    H.append(HL[0])
    L.append(HL[1])

Q =int(input())
ans = [None]*Q
T = sorted(enumerate(list(map(int, input().split()))), key = lambda x: x[1])
for i in range(Q):
    index = bisect.bisect(L, T[i][1])
    H_tmp = H[index:]
    for j in range(len(H_tmp)):
        H_tmp[j] *= -1

    heapq.heapify(H_tmp)
    ans[] = heapq.heappop(H_tmp) * -1

for i in range(Q):
    print(ans[i]) 
"""