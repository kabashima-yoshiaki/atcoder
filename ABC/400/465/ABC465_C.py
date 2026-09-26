N = int(input())
S = input()
L = [i for i in range(1, N+1)]

for i in range(N):

    if S[i] == 'o':
        L_i = L[i::-1] + L[i+1::]
        L = L_i
print(' '.join(map(str, L)))