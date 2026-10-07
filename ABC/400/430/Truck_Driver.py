n,a,b=map(int,input().split())
s=input()
count_a=[0]
count_b=[0]
for i in range(n):
    if s[i] == "a":
        count_a.append(count_a[i]+1)
        count_b.append(count_b[i])
    else:
        count_a.append(count_a[i])
        count_b.append(count_b[i]+1)

ra = 0
rb = 0
ans = 0
for l in range(n):                   
    while ra <= n and count_a[ra] - count_a[l] < a:   
        ra += 1
    while rb <= n and count_b[rb] - count_b[l] < b: 
        rb += 1
    ans += max(0, rb - ra)        
print(ans)