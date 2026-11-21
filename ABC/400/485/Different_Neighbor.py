n=int(input())
c=list(map(int,input().split()))
migi = [0]*(n)
hidari = [0]*(n)

cnt = 1
for i in range(n-1):
    if c[i] == c[i+1]:
        cnt += 1
    else:
        cur = i
        for j in range(1, cnt+1):
            migi[cur] = j
            cur -= 1
        cnt = 1
c = c[::-1]
cnt = 1
for i in range(n-1):
    if c[i] == c[i+1]:
        cnt += 1
    else:

        cur = i
        for j in range(1, cnt+1):
            hidari[cur] = j
            cur -= 1
        cnt = 1
hidari=hidari[::-1]
ans = []
for i in range(n):
    if hidari[i] != 0 and migi[i] != 0:
        ans.append(min(hidari[i], migi[i]))
    elif hidari[i] == 0:
        ans.append(migi[i])
    elif migi[i] == 0:
        ans.append(hidari[i])
print(*ans)