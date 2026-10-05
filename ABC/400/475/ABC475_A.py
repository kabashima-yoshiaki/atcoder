s = input()
for i in range(len(s)):
    if i != len(s)-1:
        print(s[i]+"o", end = "")
    else:
        print(s[i])