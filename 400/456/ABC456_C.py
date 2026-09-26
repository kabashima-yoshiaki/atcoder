S = input()
memo = []
cnt = 0
for i in range(len(S)-1):
    if S[i] == S[i+1]:
        memo.append(S[cnt:i+1])
        cnt = i+1
memo.append(S[cnt:])
ans = 0
for s in memo:
    n = len(s)
    ans += n*(n+1)//2
ans %= 998244353
print(ans)
