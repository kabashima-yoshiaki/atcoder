s=input()
t=input()
is_true = True
for i in range(1, len(s)):
    if s[i].isupper():
        if s[i-1] in t:
            is_true = True
            continue
        else:
            is_true = False
            break

print("Yes" if is_true else "No")