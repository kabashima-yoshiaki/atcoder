s=input()
t=input()
alfas=[0]*27
alfat=[0]*27
a = ord("a")
atcoder =["a","t","c","o","d","e","r"]
P=[]
for at in atcoder:
    P.append(ord(at) - a)

for i in range(len(s)):
    if s[i] == "@":
        alfas[26] += 1
    else:
        alfas[ord(s[i])-ord("a")] += 1
    if t[i] == "@":
        alfat[26] += 1
    else:
        alfat[ord(t[i])-ord("a")] += 1

for i in range(26):
    if alfas[i] == alfat[i]:
        alfas[i] = 0
        alfat[i] = 0
    else:
        if alfas[i] > alfat[i] :
            alfas[i] -= alfat[i]
            alfat[i] = 0
        else:
            alfat[i] -= alfas[i]
            alfas[i] = 0

sums = sum(alfas[:26])
sumt = sum(alfat[:26])
if sums > alfat[26] and sumt > alfas[26]:
    print("No")
else:
    for i in range(26):
        if (alfas[i] != 0 or alfat[i] != 0) and i not in P:
            print("No")
            break
    else:
        print("Yes")
