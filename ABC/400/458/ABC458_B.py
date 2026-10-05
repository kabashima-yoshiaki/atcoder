H, W = map(int, input().split())
G = [[0]*W for _ in range(H)]
for i in range(H):
    for j in range(W):
        if i-1 >= 0:
           G[i][j] += 1
        if i+1 < H:
           G[i][j] += 1
        if j+1 < W:
           G[i][j] += 1
        if j-1 >= 0:
           G[i][j] += 1
for g in G:
   print(" ".join(map(str, g)))