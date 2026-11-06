"""
=========
BFSでの解法
=========
 from collections import deque
n, m = map(int, input().split())
G = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(lambda x: int(x) - 1, input().split())
    G[u].append(v)
    G[v].append(u)

visited = [False] * n
c = 0  # 連結成分の数
for s in range(n):
    if visited[s]:
        continue
    c += 1               # 新しい連結成分を見つけた
    visited[s] = True
    q = deque([s])
    while q:
        cur = q.popleft()
        for nv in G[cur]:
            if not visited[nv]:
                visited[nv] = True
                q.append(nv)

print(m - (n - c))
 """
#========
#union-findを用いた回答
#========