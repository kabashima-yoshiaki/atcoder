import collections
N, K = map(int, input().split())
S = input()
count = []
for i in range(N-K+1):
    count.append(S[i:i+K])
c = collections.Counter(count)
c = c.most_common()
print(c[0][1])
for i in range(len(c)):
    if c[i][1] == c[0][1]:
        print(c[i][0], end=' ')
    else:
        exit()
