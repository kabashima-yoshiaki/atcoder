n, m = map(int,input().split())
s = [input() for _ in range(n)]
for i, s_i in enumerate(s):
    if s_i == "x"*m:
        print("Faucet", i+1)
        exit()
ans = [True]*(m)
for i in range(n):
    for j in range(m):
        if s[i][j] == "x":
            ans[j] = ans[j] and True
        else:
            ans[j] = False

for i in range(m):
    if ans[i]:
        print("Drain", i+1)