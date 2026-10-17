import bisect
n,q=map(int,input().split())
a=list(map(int,input().split()))

a.sort()
sum_a = []
sum_a.append(0)
for a_i in a:
    sum_a.append(sum_a[-1] + a_i)
max_a = max(a)
for i in range(q):
    b = int(input())
    if b > max_a:
        print(-1)
        continue
    else:
        idx = bisect.bisect_left(a, b)
        print(sum_a[idx] + (len(a) - idx)*(b-1) + 1)


        