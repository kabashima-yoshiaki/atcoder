import itertools
n,v=map(int,input().split())
w=list(map(int,input().split()))
idx=[i for i in range(1,n+1)]
ans = 0
for idx in itertools.permutations(idx,3):
    kakaku = idx[0] + idx[1] + idx[2]
    if kakaku <= v:
        ans = max(ans, (w[idx[0]-1]+w[idx[1]-1]+w[idx[2]-1]))
print(ans)