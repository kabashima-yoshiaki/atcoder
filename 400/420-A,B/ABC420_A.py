X, Y = map(int, input().split())

A = X + Y
if A > 12:
    print(A - 12)
    exit()
else:
    print(A)
