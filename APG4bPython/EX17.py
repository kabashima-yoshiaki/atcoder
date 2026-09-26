N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]

R = [["-" for _ in range(N)] for _ in range(N)]
for i in range(M):
    R[AB[i][0] - 1][AB[i][1] - 1] = "o"
    R[AB[i][1] - 1][AB[i][0] - 1] = "x"
for i in range(N):
    print(*R[i])
