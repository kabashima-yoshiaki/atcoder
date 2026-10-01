t=int(input())
for _ in range(t):
    n,w=map(int,input().split())
    c=list(map(int,input().split()))
    A = [0]*2*w
    for i in range(n):
        A[i%(2*w)] += c[i]
    for j in range(2*w):
        if j == 0:
            cur = sum(A[:w])
            ans = cur
        else:
            cur = cur - A[j-1] + A[(j+w-1)%(2*w)]
        ans = min(cur, ans)
    print(ans)

    
        