n,d=map(int,input().split())
x=list(map(int,input().split()))
ans = []
for i in range(n):
    is_true = True
    for j in range(n):
        if i != j and abs(x[i] - x[j]) < d:
            is_true = False
    if is_true:
        ans.append(i+1)
ans.sort()
print(len(ans))
print(*ans)