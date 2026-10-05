from collections import defaultdict
n, m = map(int, input().split())
memo = defaultdict(int)
cnt = defaultdict(int)
for i in range(n):
    a, b = map(int, input().split())
    memo[a] += b
    cnt[a] += 1

for j in range(1, m+1):
    print(memo[j]/cnt[j]) 
