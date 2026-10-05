""" N = int(input())
M = list(map(int, input().split()))
E = list(map(int, input().split()))

for i in range(N):
    print(M[i] + E[i])
"""

#EX10
N = int(input())
M = list(map(int, input().split()))

average = 0
for x in M:
    average += x

average //= N

for x in M:
    if x - average < 0:
        print((x - average) * (-1))
    else:
        print(x - average)

