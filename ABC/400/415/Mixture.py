import math
t=int(input())
idx=1
out=[]
for i in range(t):
    idx+=2
    n = int(input())
    s=input()
    DP = [0]*(2**n+1)
    DP[0] = 1
    for mask in range(1, 2**n+1):
        if s[mask -1] == "1":
            continue
        m = mask
        while m:
            low = m & -m
            if DP[mask ^ low]:
                DP[mask] = 1
                break
        m ^= low
    out.append("Yes" if dp[2**n+1] else "No")
print("\n".join(out))