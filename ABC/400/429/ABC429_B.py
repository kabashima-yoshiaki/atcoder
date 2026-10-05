n, m = map(int, input().split())
a = list(map(int, input().split()))

for i in range(n):
    b = a.copy()
    del b[i]
    if sum(b) == m:
        print('Yes')
        exit()
    else:
        continue 

print('No')
    