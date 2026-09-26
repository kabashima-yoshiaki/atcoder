n, m = map(int, input().split())
s = []
for i in range(n):
    s.append(input())      

p = [0]*n 

count_zero = 0
count_one = 0
for j in range(m):
    v = [s[i][j] for i in range(n)]
    count_zero = v.count('0')
    count_one = v.count('1')
    if count_zero == 0 or count_one == 0:
        p = [x + 1 for x in p]
    elif count_zero < count_one:
        for i in range(n):
            if s[i][j] == '0':
                p[i] +=1
    elif count_zero > count_one:
        for i in range(n):
            if s[i][j] == '1':
                p[i] +=1

ans = [i+1 for i, x in enumerate(p) if x == max(p)]
print(*ans)