import heapq
def main():
    n,m,s,t=map(int,input().split())   
    to_list = [[] for _ in range(n)]    
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b= map(int, input().split())
        a -= 1
        b -= 1
        to_list[a].append(b)

    for v in range(n):
        if not to_list[v]:
            continue
        mn = min(to_list[v])
        for w in to_list[v]:
            graph[v].append((w, 0 ) if w == mn else (w, 1))


    # 頂点 k からダイクストラ法で各頂点までの最短路長を求める
    def dist_from(k: int):
        pque = []
        dist = [10 ** 9] * n
        dist[k] = 0
        heapq.heappush(pque, (0, k))
        while len(pque) > 0:
            now_cost, now = heapq.heappop(pque)
            if now_cost > dist[now]:
                continue
            for to, cost in graph[now]:
                if now_cost + cost < dist[to]:
                    dist[to] = now_cost + cost
                    heapq.heappush(pque, (now_cost + cost, to))
        return dist
    from_first = dist_from(s-1)  # 頂点 1 からの最短路長
    INF =10 ** 9
    ans = from_first[t - 1]
    print(ans if ans < INF else -1)

if __name__ == "__main__":
    main()

      