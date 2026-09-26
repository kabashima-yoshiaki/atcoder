from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))

a_dict = defaultdict(int)
memo = list(j for j in range(1, n+1))

for i in range(n):
    if a[i] != -1:
        a_dict[a[i]] += 1
        idx = memo.index(a[i])
        memo[i], memo[idx] = memo[idx], memo[i]
        if a_dict[a[i]] > 1:
            print('No')
            exit()
print('Yes')
print(*memo)

