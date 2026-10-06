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

