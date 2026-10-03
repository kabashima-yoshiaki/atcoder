n,m=map(int,input().split())
a = [0]*n
while m >= 1:
    for i in range(n):
        if m >= 1:
            a[i] += 1
            m -= 1
for i in range(n):
    print(a[i])