n,m,q=map(int,input().split())

all_ok=[False]*(n)
ok=[set() for _ in range(n)]

for i in range(q):
    query=list(map(int,input().split()))

    if query[0] == 1:
        ok[query[1]-1].add(query[2])
    elif query[0] == 2:
        all_ok[query[1]-1] = True
    else:
        if all_ok[query[1]-1]:
            print("Yes")
        else:
            if query[2] in ok[query[1] -1]:
                print("Yes")
            else:
                print("No")

