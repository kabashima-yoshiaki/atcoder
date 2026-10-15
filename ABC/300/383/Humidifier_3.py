import sys
sys.setrecursionlimit(10**6)
from collections import deque
h,w,d=map(int,input().split())
grid=[list(input()) for _ in range(h)]
visited = [[-1]*w for _ in range(h)]

dirs = [(-1,0),(1,0),(0,-1),(0,1)]
queue = deque()
for i in range(h):
    for j in range(w):
        if grid[i][j] == "H":
            visited[i][j] = 0
            queue.append([i,j])

while queue:
    x,y = queue.popleft()
    
    for dx, dy in dirs:
        nx, ny = x+dx, y+dy
        if 0 <= nx < h and 0 <= ny < w and visited[nx][ny] == -1 and (grid[nx][ny] == "."  or grid[nx][ny] == "H"):
            visited[nx][ny] = visited[x][y] + 1
            queue.append((nx, ny))
cnt = 0
for i in range(h):
    for j in range(w):
        if visited[i][j] != -1 and visited[i][j] <= d:
            cnt += 1
print(cnt)