import sys
h,w=map(int,input().split())
grid=[]
for _ in range(h):
    grid.append(input())
dx = [0,1,0,-1]
dy = [1,0,-1,0]


for i in range(h):
    for j in range(w):
        if grid[i][j] == ".":
            cnt = 0
            for x, y in zip(dx, dy):
                if 0 <= i+y <= h-1 and 0 <= j+x <= w-1:
                    if grid[i+y][j+x] == "#":
                        cnt += 1
            if cnt >= 2:
                print(i+1,j+1)
                sys.exit()
            