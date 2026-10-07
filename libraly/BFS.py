# =====================
# BFS（幅優先探索）
# =====================
from collections import deque
def bfs(G, s):
    """
    スタートからの最短距離（辺の本数）を求める。
    G：隣接リスト
    s:グラフの開始位置
    """
    dist = [-1] * len(G)
    dist[s] = 0
    q = deque([s])
    while q:
        v = q.popleft()
        for nv in G[v]:
            if dist[nv] == -1:
                dist[nv] = dist[v] + 1
                q.append(nv)
    return dist

N = 6
edges = [(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)]

G = [[] for _ in range(N)]
for a, b in edges:
    a -= 1; b -= 1          # 1 始まり → 0 始まり
    G[a].append(b)
    G[b].append(a)          # 無向グラフなので両方向

dist = bfs(G, 0)            # 頂点 1（index 0）から BFS
print(dist)                 # [0, 1, 1, 2, 3, -1]