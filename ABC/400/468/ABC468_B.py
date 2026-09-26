M, D = map(int, input().split())
S = input()
guard = [False]*M
cnt = 0
for x in range(M):
    for i in range(M):
        if S[i] == 'G' and abs(x - i) <= D:
            cnt += 1
            break
print(M-cnt)