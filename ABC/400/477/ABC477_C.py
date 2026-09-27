q=int(input())
s=input()
t=input()
idx = [0]
for i in range(len(s)):
    if i < len(s)-len(t)+1:
        if s[i:i+len(t)] == t:
            idx.append(1)
        else:
            idx.append(0)
    else:
        idx.append(0)
for i in range(1, len(idx)):
    idx[i] = idx[i-1] + idx[i]

for _ in range(q):
    l, r = map(int,input().split())
    if r-l+1 < len(t):
        print("No")
    else:
        if (idx[r-len(t)+1] - idx[l-1]) >= 1:
            print("Yes")
        else:
            print("No")

""" 
import bisect
kouho = []
for i in range(len(s)-len(t)+1):
    if s[i:i+len(t)] == t:
        kouho.append(i+1)
for _ in range(q):
    l, r = map(int,input().split())
    if r - l < len(t)-1 or bisect.bisect_left(kouho, l) >= len(kouho):
        print("No")
        continue
    else:
        if kouho[bisect.bisect_left(kouho, l)] + len(t) -1 <= r:
            print("Yes")
        else:
            print("No")
"""





