n,q=map(int,input().split())
groups = [[] for _ in range(q+1)]

for _ in range(q):
    l,r,x=map(int,input().split())
    groups[x].append((l,r))

diff = [0]*(n+2) #nは1からn+1まで(いもす法ではr+1に書き込むため)


for x in range(1,q+1):
    groups[x].sort()
    done = 0
    for l,r in groups[x]:
        start = max(l,done+1)
        if start <= r:
            diff[start] += 1
            diff[r+1] -= 1
            done = r

ans = []
cnt = 0
for i in range(1,n+1):
    cnt += diff[i]
    ans.append(cnt)
print(*ans)