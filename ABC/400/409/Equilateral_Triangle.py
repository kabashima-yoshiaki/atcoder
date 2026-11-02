n,l=map(int,input().split())
d=list(map(int,input().split()))
pos=[0]
cnt=[0]*l
cnt[0] += 1
for d_i in d:
    pos.append((pos[-1]+d_i)%l)
    cnt[pos[-1]] += 1

ans = 0    

if l % 3 != 0:
    print(0)
    exit()
else:
    for i in range(l//3):
        ans += cnt[i] * cnt[i + l // 3] * cnt[i + 2 * l // 3]
print(ans)
