n=int(input())
s=input()
abc = set()
for i in range(n):
    abc.add(s[i])
    if len(abc) == 3:
        left = i
        break
abc = set()
for i in reversed(range(n)):
    abc.add(s[i])
    if len(abc) == 3:
        right = i
        break
ans = 0
cnt = {"A":0, "B":0,"C":0}
kinds = 0
e = left

for i in range(left + 1 , right):
    while kinds < 3 and e+1 < right:
        e += 1
        cnt[s[e]] += 1
        if cnt[s[e]] == 1:
            kinds += 1

    if kinds < 3:
        break

    ans += right - e
    cnt[s[i]] -= 1
    if cnt[s[i]] == 0:
        kinds -= 1
        
print(ans)


