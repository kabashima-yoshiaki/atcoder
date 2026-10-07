import sys
input = sys.stdin.readline
n, q = map(int, input().split())
a = list(map(int, input().split()))
b = a + a
for i in range(2 * n - 1, 0, -1):
    b[i - 1] += b[i]
rui_c = 0
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        c = query[1]
        rui_c += c
        rui_c %= n
    else:
        l, r = query[1] - 1, query[2]
        print(b[l + rui_c] - b[r + rui_c])


