n,k=map(int,input().split())
a=[1]
cur=0
a_i = 0
for i in range(1, n+1):

    if 1 <= i and i < k:
        a.append(1)
    elif i == k:
        a_i = sum(a)
        a.append(a_i)
    else:
        a_i -= a[cur] % (10 ** 9) 
        a_i += a[-1] % (10 ** 9)
        a.append(a_i)
        cur += 1

print(a[-1]%(10**9))
