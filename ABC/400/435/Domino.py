n=int(input())
domino = list(map(int,input().split()))
max_d = 1
for i in range(1, n+1):
    if i <= max_d:
        max_d = max(i + domino[i-1] - 1, max_d)
print(max_d if max_d < n else n)