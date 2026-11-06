from collections import defaultdict
n=int(input())
a=list(map(int,input().split()))
count_a = defaultdict(int)

for a_i in a:
    count_a[a_i] += 1
ans_max = -1
ans = -1
for i in range(n):
    if count_a[a[i]] == 1:
        if ans_max < a[i]:
            ans = i+1
            ans_max = a[i]
print(ans)    