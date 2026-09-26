N = int(input())
C = list(map(int, input().split()))
t = [0] *(N+1)

for i in range(N):
    t[C[i]] += 1

print(N- max(t))