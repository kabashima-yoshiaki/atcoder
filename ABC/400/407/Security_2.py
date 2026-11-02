s=input()
cnt = 0
for i in range(len(s)):
    if i == 0:
        cnt += int(s[i]) + 1
    else:
        if int(s[i]) == int(s[i-1]):
            cnt += 1
        elif int(s[i]) > int(s[i-1]):
            cnt += 10 + 1
        else:
            cnt += 1
print(cnt)