""" 
#自分で考えた解法
n=int(input())
a=list(map(int,input().split()))
from collections import deque
que=deque()
l=[0]*(n+1)

for i in range(n):
    que.append(a[i])

    if len(que) > 1:
        if que[-2] == a[i]:
            l[a[i]] += 1
            if l[a[i]] >= 4:
                cnt = 0
                for j in range(1,4):
                    if que[-j] == que[-j-1]:
                        cnt += 1
                if cnt == 3:
                    que.pop()
                    que.pop()
                    que.pop()
                    que.pop()
                    l[a[i]] -= 4
                    
        else:
            l[a[i]] += 1
    else:
        l[a[i]] += 1

print(len(que)) 
"""
"""
模範解答：ただスタックでi=1~nで毎回判定するだけ
"""
from collections import deque
n=int(input())
que=deque()
for v in list(map(int,input().split())):
    que.append(v)
    if len(que) > 3 and (que[-1] == que[-2] == que[-3] == que[-4]):
        que.pop()
        que.pop()
        que.pop()
        que.pop()
print(len(que))