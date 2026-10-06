n,k=map(int,input().split())
med = []
for _ in range(n):
    med.append(list(map(int, input().split())))
med=sorted(med, key= lambda x: x[0])
ans=[]
sum = 0
for a,b in med:
    sum += b
ans.append(sum)
for i in range(n):
    ans.append(sum - med[i][1])
    sum -= med[i][1]
is_first=False
for i,a in enumerate(ans):
    if a <= k:
        if i == 0:
            print(1)
            break
        print(med[i-1][0]+1)
        break
