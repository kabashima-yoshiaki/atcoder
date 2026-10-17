from collections import deque
n,m,k=map(int,input().split())

h=list(map(int,input().split()))
b=list(map(int,input().split()))
h.sort(reverse=True)
h = deque(h)
b.sort(reverse=True)
b = deque(b)
cnt = 0
for _ in range(m):
    if len(h) > 0 and len(b) > 0:
        if h[-1] > b[-1]:
            b.pop()
        else:
            h.pop()
            b.pop()
            cnt += 1

if cnt >= k:
    print("Yes")
else:
    print("No")