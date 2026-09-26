n = int(input())
a = list(map(int, input().split()))

c = list(set(a))
print(len(c))
print(*(sorted(c)))