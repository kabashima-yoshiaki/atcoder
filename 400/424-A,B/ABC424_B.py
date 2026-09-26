from collections import defaultdict
n, m, k = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(k)]

a = defaultdict(int)
b = []
for i in range(k):
    person = ab[i][0]
    a[person] += 1
    if a[person] == m:
        b.append(person)

print(*b)