#Nが小さいのでbit全探索する。計算量はO(n*2**n*)
n,w=map(int,input().split())
ab = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(2**n):
    value = 0
    weight = 0
    for j in range(n):
        if ((i >> j) & 1):
            value += ab[j][0]
            weight += ab[j][1]
    if weight <= w:
        ans = max(ans, value)
print(ans)