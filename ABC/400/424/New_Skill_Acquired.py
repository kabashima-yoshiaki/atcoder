
import sys
sys.setrecursionlimit(10**6)

from collections import deque


n=int(input())
G=[[]for _ in range(n)]
learned=[False]*n
que=deque()

for i in range(n):
    a,b=map(int,input().split())
    if a == 0 and b == 0:
        learned[i] = True
        que.append(i)
    else:
        G[a-1].append(i)
        G[b-1].append(i)

while que:
    v=que.popleft()
    for nv in G[v]:
        if not learned[nv]:
            learned[nv] = True
            que.append(nv)

print(sum(learned))