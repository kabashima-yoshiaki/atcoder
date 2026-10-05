N = int(input())

X = 10000
Y = 10000
for i in range(N):
    A, B, S = input().split()
    A = int(A)
    B = int(B)
    Y -= A
    if S == 'keep':
        X -= B
    else:
        X -= A
print(Y-X)