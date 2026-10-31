import sys
s = [input() for _ in range(5)]
cnt_tate=0
cnt=yoko=0
ans = 5
for i in range(5):
    cnt_yoko=0
    for j in range(5):
        if s[i][j] == 'o':
            cnt_yoko += 1
    if cnt_yoko == 5:
        print(0)
        sys.exit()
    else:
        ans = min(ans, 5-cnt_yoko)

for k in range(5):
    cnt_tate=0
    for l  in range(5):
        if s[l][k] == 'o':
            cnt_tate += 1
    if cnt_tate == 5:
        print(0)
        sys.exit()
    else:
        ans = min(ans, 5-cnt_tate)

for t in range(2):
    cnt_naname = 0
    for x in range(5):
        if s[x][x] == 'o':
            cnt_naname += 1
    if cnt_naname == 5:
        print(0)
        sys.exit()
    else:
        ans = min(ans, 5-cnt_naname)

print(ans)
    