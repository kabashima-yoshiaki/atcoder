n,q=map(int,input().split())
a = [i for i in range(1, n+1)]
cur = 0
for i in range(q):
    query = list(map(int,input().split()))
    if query[0] == 1:
        a[(cur + query[1]-1)%(n)] = query[2] 
    elif query[0] == 2:
        print(( a[(cur + query[1]-1)%n]))
    else:
        cur = (cur + query[1])%n


