n, s = map(int, input().split())
t = list(map(int, input().split()))

time = 0

if t[0] >= (s + 0.5):
    print('No')
    exit()
for i in range(1, n):
    if t[i] - t[i-1] < (s + 0.5):
        continue
    else:
        print('No')
        exit()

print('Yes')

        