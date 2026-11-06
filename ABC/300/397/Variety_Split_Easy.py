n=int(input())
a=list(map(int,input().split()))

right=[0]*(n+1)
kind=0
ans = 0
for a_i in a:
    right[a_i] += 1
for s in right:
    if s > 0:
        kind += 1
left=[0]*(n+1)
kind_l = 0
kind_r = kind
for i in range(n):
    if right[a[i]] == 1:
        kind_r -= 1
        if left[a[i]] == 0:
            kind_l += 1
    elif right[a[i]] > 1:
        if left[a[i]] == 0:
            kind_l += 1
    left[a[i]] += 1
    right[a[i]] -=1
    ans = max(ans, kind_l+kind_r)
print(ans)