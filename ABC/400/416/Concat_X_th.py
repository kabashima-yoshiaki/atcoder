import itertools

n,k,x=map(int,input().split())
s = [input() for i in range(n)]

f = [i for i in range(n)]
f_s = []
p = list(itertools.product(range(n), repeat=k))

for p_i in p:
    s_i = ""
    for i in range(k):
        s_i += s[p_i[i]]
    f_s.append(s_i)

f_s.sort()
print(f_s[x-1])