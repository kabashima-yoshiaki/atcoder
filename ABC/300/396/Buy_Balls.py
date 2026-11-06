n,m=map(int,input().split())
b=list(map(int,input().split()))
w=list(map(int,input().split()))
b.sort(reverse=True)
w.sort(reverse=True)
sum_b =[0]
for i in range(n):
    sum_b.append(sum_b[-1]+b[i])

w_suffix_max=[0]
for j in range(m):
    w_suffix_max.append(max(w_suffix_max[-1], w_suffix_max[-1]+w[j]))
ans = 0
for i in range(n+1):
    if i < m:
        ans = max(sum_b[i]+w_suffix_max[i], ans)
    else:
        ans = max(sum_b[i]+w_suffix_max[-1], ans)
print(ans)