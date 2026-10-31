from collections import defaultdict

n,m=map(int,input().split())
s=[input() for _ in range(n)]
t=[input() for _ in range(m)]
cnt=defaultdict(int)

for t_i in t:
    if t_i in s:
        cnt[t_i] += 1
    else:
        candidate = []
        for s_i in s:
            if len(s_i) == len(t_i):
                count = 0
                for i in range(len(s_i)):
                    if s_i[i] == t_i[i]:
                        count += 1
                if count == len(s_i) -1:
                    candidate.append(s_i)
        if len(candidate) == 1:
            cnt[candidate[0]] += 1
for s_i in s:
    print(cnt[s_i])
