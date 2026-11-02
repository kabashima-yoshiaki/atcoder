import bisect
h,w,n,q=map(int,input().split())
row=[]
column=[]
for _ in range(n):
    r, c=map(int,input().split())
    row.append(r)
    column.append(c)
row.sort()
column.sort()

for _ in range(q):
    query=list(map(int,input().split()))
    if query[0] == 1:
        print(bisect.bisect_right(row, query[2])-bisect.bisect_left(row, query[1]))
    else:
        print(bisect.bisect_right(column, query[2])-bisect.bisect_left(column, query[1]))



