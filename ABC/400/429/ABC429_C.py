""" from collections import Counter
n = int(input())
a = list(map(int, input().split()))
ans = 0

for i in range(n-2):
    counter = Counter(a[i+1:])
    keys = list(counter.keys())
    print(counter)
    for j in range(len(keys)):    
        if a[i] != keys[j] and counter[keys[j]] > 1:
            print(counter[keys[j]])
            ans += counter[keys[j]] - 1
            print('ans:', ans)
        elif a[i] == keys[j] and counter[keys[j]] == 1 :
            ans += 1
print(ans)
import itertools
n = int(input())
a = list(map(int, input().split()))
ans = 0
memo = list(itertools.combinations(a, 3))
for i in range(len(memo)):
    setmemo = set(memo[i])
    if len(setmemo) == 2:
        ans += 1
print(ans)  """

from collections import Counter
n = int(input())
a = list(map(int, input().split()))
ans = 0
counter = Counter(a)
print(counter)
