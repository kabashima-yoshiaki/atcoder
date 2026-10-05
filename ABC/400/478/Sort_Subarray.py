""" n,k=map(int,input().split())
a=list(map(int,input().split()))
b=sorted(a)
same=[0]*n
for i in range(n):
    if a[i] == b[i]:
        same[i] = 1
    if i > 0:
        same[i] += same[i-1]
for x in range(n-k):
    if x == 0:
        if same[n-1] - same[x+k-1] == len(same[x+k:]):
            print("Yes")
            break
    else:
        if same[x] == x and same[n-1] - same[x+k-1] == len(same[x+k:]):
            print("Yes")
            break
else:
    print("No") """

n,k=map(int,input().split())
a=list(map(int,input().split()))
b=sorted(a)

for i in range(n):
    if a[i] != b[i]:
        min_i = i
        break
for j in range(n-1, 0, -1):
    if a[j] != b[j]:
        max_i = j
        break

print("Yes" if a == b or max_i-min_i < k else "No")