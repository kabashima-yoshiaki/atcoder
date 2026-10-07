n,r=map(int,input().split())
l=list(map(int,input().split()))

for i in range(n):
    if l[i] == 0:
        break
    elif i <= r-1:
        l[i] = -1

for j in reversed(range(n)):
    if l[j] == 0:
        break
    elif j >= r:
        l[j] = -1
ans =0
for a in l:
    if a == 0:
        ans += 1
    elif a == 1:
        ans += 2
    else:
        continue

print(ans)
