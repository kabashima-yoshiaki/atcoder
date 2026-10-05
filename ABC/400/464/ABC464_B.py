H , W = map(int, input().split())
grid = [list(input()) for _ in range(H)]
ans_1 = 0
ans_2 = 0
ans_3 = 0
ans_4 = 0

for i in range(H):
    white = 0
    for j in range(W):
        if grid[i][j] == ".":
            white += 1
    if white == W:
        ans_1 += 1
    else:
        break

for i in reversed(range(H)):
    white = 0
    for j in range(W):
        if grid[i][j] == ".":
            white += 1
    if white == W:
        ans_2 += 1
    else:
        break

for i in range(W):
    white = 0
    for j in range(H):
        if grid[j][i] == ".":
            white += 1
    if white == H:
        ans_3 += 1
    else:
        break

for i in reversed(range(W)):
    white = 0
    for j in range(H):
        if grid[j][i] == ".":
            white += 1
    if white == H:
        ans_4 += 1
    else:
        break

for i in range(ans_1, H-ans_2):
    for j in range(ans_3, W-ans_4):
        print(grid[i][j], end = '')
    print('')
