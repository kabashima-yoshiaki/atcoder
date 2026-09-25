a, b = map(int, input().split())

def Fib_Return(x, y, n):
    if n == 1:
        return x
    elif n == 2:
        return y
    else:
        return int(str(Fib_Return(x, y, n-1) + Fib_Return(x, y, n-2))[::-1])
    
print(Fib_Return(a, b, 10))