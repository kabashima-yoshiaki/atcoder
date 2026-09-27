q=int(input())
s=input()
t=input()
kouho = []
import bisect
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





