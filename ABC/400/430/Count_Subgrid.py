n,m=map(int,input().split())
s = [input() for _ in range(n)]
grid = []
for i in range(n-m+1):
    for j in range(n-m+1):
        g = [[0]*m for _ in range(m)]
        for x in range(m):
            for y in range(m):
                g[x][y] = s[i+x][j+y]
        grid.append(g)
seen = []
kind = 0
for grid_i in grid:
    if grid_i not in seen:
        seen.append(grid_i)
        kind += 1
print(kind)