
import sys
sys.setrecursionlimit(10**6)

from collections import deque


n=int(input())
learned = [False]*n
G=[[]for _ in range(n)]
queue = deque()
for i in range(n):
    a,b=map(int,input().split())
    if a == 0 and b == 0:
        learned[i] = True
        queue.append(i)
    else:
        G[a-1].append(i)
        G[b-1].append(i)


while queue:
    v = queue.popleft()
    for nv in G[v]:
        if not learned[nv]:
            learned[nv] = True
            queue.append(nv)
print(sum(learned))