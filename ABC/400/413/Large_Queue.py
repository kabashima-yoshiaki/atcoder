from collections import deque
a=deque()
q=int(input())
cur = 0
diff = 0
for _ in range(q):
    query = list(map(int,input().split()))

    if query[0] == 1:
        c,x=query[1], query[2]
        a.append([c,x])

    else:
        k = query[1]
        ans = 0
        cur = 0
  
        while cur < k:
            if a[0][0] - diff <= k - cur:
                cur += a[0][0] - diff
                ans += (a[0][0]-diff)*a[0][1]
                diff = 0
                a.popleft()
            else:
                ans += (k-cur)*a[0][1]
                diff += k-cur
                print(ans) 
                break
        else:
            print(ans) 
