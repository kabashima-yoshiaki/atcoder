a, b, c, d = map(int, input().split())

if c >= a:
    if d >= b:
        print('No')
        exit()
    else:
        print('Yes')
        exit()
print('No')