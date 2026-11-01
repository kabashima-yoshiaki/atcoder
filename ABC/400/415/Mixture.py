t=int(input())
for _ in range(t):
    n=int(input())
    s=input()

    full = (1 << n) -1
    dp = [False]* (full + 1)
    dp[0] = True

    for mask in range(1, full + 1):
        if s[mask -1 ] == "1":
            continue
        for k in range(n):
            if (mask >> k) & 1 and dp[mask ^ (1 << k)]:
                dp[mask] = True
                break
    print("Yes" if dp[full] else "No")
    
