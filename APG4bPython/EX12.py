N = int(input())
T = list(map(int, input().split()))

min_sec = min(T)
# print(T.index(min_sec)+1)
for i, v in enumerate(T):
    if v == min_sec:
        print(i + 1)
        break