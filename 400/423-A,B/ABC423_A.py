x, c = map(int, input().split())
t = 0
i = 1
while True:
    if 1000 * i + ((1000 * i * c) / 1000) <= x:
        i += 1
        continue
    elif i == 1:
        print(0)
        exit()
    elif i > 1:
        print(1000 * (i-1))
        exit()

