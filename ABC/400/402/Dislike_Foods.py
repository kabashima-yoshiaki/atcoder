n,m=map(int,input().split())
"""
ryouri[食材名]=[料理名のリスト]
"""
ryouri=[[] for _ in range(n+1)]
ryouri_cnt=[0]*m
for i in range(1, m+1):
    syokuzai=list(map(int,input().split()))
    k_i = syokuzai[0]
    ryouri_cnt[i-1] = k_i
    for j in range(1, k_i+1):
        ryouri[syokuzai[j]].append(i)

b = list(map(int,input().split()))
ans = 0
for b_i in b:

    while ryouri[b_i]:
        ryouri_cur = ryouri[b_i].pop() -1
        ryouri_cnt[ryouri_cur] -= 1
        if ryouri_cnt[ryouri_cur] == 0:
            ans += 1
    print(ans)