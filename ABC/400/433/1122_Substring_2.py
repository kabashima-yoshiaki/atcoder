s=input()
kouho=[]
for i in range(len(s)-1):
    if int(s[i])+1 == int(s[i+1]):
        kouho.append(i)
if len(kouho) == 0:
    print(0)
else:
    cnt = 0
    for x in kouho:
        cnt +=1
        l = x-1
        r = x+2
        while l >= 0 and r < len(s) :
            if s[x] == s[l] and s[x+1] == s[r]:
                cnt += 1
                l-=1
                r+=1
            else:
                break
    print(cnt)

        
        
