N, L, R = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
for i in range(N):
    if XY[i][0] <= L and XY[i][1] >= R:
        cnt += 1
print(cnt)
