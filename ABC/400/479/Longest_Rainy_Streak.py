n=int(input())
s=input()
cur = False
ans = [0]
cnt = 0
for i in range(n):
    if s[i] == "S":
        ans.append(cnt)
        cnt = 0
    else:
        cnt += 1
ans.append(cnt)
print(max(ans))