q=int(input())
s=input()
t=input()

kouho=[]
for i in range(len(s)-len(t)+1):
    if s[i:i+len(t)] == t:
        kouho.append([i,i+len(t)-1])

for _ in range(q):
    l,r=map(int, input().split())
    l -= 1
    r -= 1
    for i, j in kouho:
        if l <= i and r >= j:
            print("Yes")
            break
    else:
        print("No")