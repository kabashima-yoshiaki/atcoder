ans = 0

def dfs(i, pos, count):
    global ans
    
    if i == N:
        ans = max(ans, count)
        return
    
    # 正方向
    next1 = pos + L[i]
    add1 = 1 if min(pos, next1) < 0 < max(pos, next1) else 0
    dfs(i+1, next1, count + add1)
    
    # 負方向
    next2 = pos - L[i]
    add2 = 1 if min(pos, next2) < 0 < max(pos, next2) else 0
    dfs(i+1, next2, count + add2)


N = int(input())
L = list(map(int, input().split()))

dfs(0, 0.5, 0)
print(ans)