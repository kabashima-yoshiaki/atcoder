n = int(input())
memo = n
ans = []
while len(ans) < 10:
    memo, memo1 = divmod(memo, 2)
    ans.insert(0, memo1)
ans = map(str, ans)
ans1 = "".join(ans)
print(ans1)