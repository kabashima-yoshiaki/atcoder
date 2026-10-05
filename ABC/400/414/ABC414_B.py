""" N = int(input())
cl = []
for i in range(N):
    c, l = input().split()
    cl.append([c, int(l)])

S = ""
for i in range(N):
    S += cl[i][0] * cl[i][1]

if len(S) <= 100:
    print(S)
else:
    print("Too Long") """

N = int(input())
cl = []
total_len = 0
for i in range(N):
    c, l = input().split()
    l = int(l)
    total_len += l
    cl.append([c, l])

if total_len  > 100:
    print("Too Long")
else:
    S = ""
    for i in range(N):
        S += cl[i][0] * cl[i][1]
    print(S)
