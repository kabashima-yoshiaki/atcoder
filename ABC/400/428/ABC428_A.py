S, A, B, X = map(int, input().split())
sum = 0
while X > 0:
    if X > A:
        X -= A
        sum += S * A
        X -= B
    elif 0 < X < A:
        sum += S * X
        break
        
print(sum)