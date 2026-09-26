w, b = map(int, input().split())
n = 1
while n * b <= w * 1000:
    n += 1
print(n)