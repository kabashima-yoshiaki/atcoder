N = int(input())
A = list(map(int, input().split()))
ans = 0
current = 0

for a in A:
    while current < N and A[current] * 2 <= a:
        current += 1
    ans += current
    
print(ans)