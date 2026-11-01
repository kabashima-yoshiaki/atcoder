h,w,n=map(int,input().split())
row=[set() for _ in range(h+1)]
column=[set() for _ in range(w+1)]
for _ in range(n):
    x,y=map(int,input().split())
    row[x].add(y)
    column[y].add(x)

q=int(input())
ans=[]

for i in range(q):
    t, v = map(int,input().split())
    if t == 1:
        x = v
        ans.append(len(row[x]))
        for y in row[x]:
            column[y].discard(x)
        row[x].clear()
    else:
        y = v
        ans.append(len(column[y]))
        for x in column[y]:
            row[x].discard(y)
        column[y].clear()
for i in range(q):
    print(ans[i])