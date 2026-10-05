N = int(input())
G = []
for i in range(N):
    L_A = list(map(int, input().split()))
    L_A.pop(0)
    G.append(L_A)
X, Y = map(int, input().split())
print(G[X-1][Y-1])