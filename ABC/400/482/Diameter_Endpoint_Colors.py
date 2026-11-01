import sys
sys.setrecursionlimit(10**6)

n=int(input())
G=[[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int,input().split())
    a -= 1; b -= 1   
    G[a].append(b)
    G[b].append(a)


from collections import deque
def bfs(s):
    dist = [None]*n
    que = deque([s])
    dist[s] = 0
    while que:
        v = que.popleft()
        d = dist[v]
        for w, c in G[v]:
            if dist[w] is not None:
                continue
            dist[w] = d + c
            que.append(w)
    d = max(dist)
    return dist.index(d), d

u, _ = bfs(0)
v, d = bfs(u)

print(d)

c=list(map(int,input().split()))