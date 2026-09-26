X, Y = map(int, input().split())
print('Yes' if (X % 16 == 0) and(Y % 9 == 0) else 'No')
