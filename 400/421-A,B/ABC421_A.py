n = int(input())
s = [input() for _ in range(n)]
x, y = map(str, input().split())
x = int(x)

print('Yes' if s[x-1] == y else 'No')