n=int(input())
s=input()
from collections import deque

b=deque()
sort_s = [s[0]]
ans=0
for i in range(1,2*n):
    if sort_s[-1] != s[i]:
        ans+=len(b)
        sort_s.append(s[i])
        if len(b) > 0:
            sort_s.append(b.popleft())
    else:
        b.append(s[i])

j = 1
while s[j] == s[0]:
    j += 1

# s[j] を先頭まで持ってくる → s[0]〜s[j-1] の j 文字を飛び越えるので j 回
ans1 = j
b = deque(s[:j])            # 飛び越えた文字(すべて s[0] と同じ文字)は待機列へ
sort_s = [s[j]]
sort_s.append(b.popleft())  # 2文字目は待機列から1つ出す

for i in range(j + 1, 2 * n):
    if sort_s[-1] != s[i]:
        ans1 += len(b)
        sort_s.append(s[i])
        if len(b) > 0:
            sort_s.append(b.popleft())
    else:
        b.append(s[i])

print(min(ans, ans1))