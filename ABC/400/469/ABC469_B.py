N = int(input())
S = input()
ans = 0

if N == 1:
    if S[0] == 'x':
        ans += 1
    print(ans)

else:
    for i in range(N):
        if i == 0:
            if S[i] == 'x' and S[i+1] == 'x':
                ans += 1
        elif 0 < i < N-1 :
            if S[i] == 'x' and S[i-1] == 'x' and S[i+1] == 'x':
                ans += 1
        elif i == N-1:
            if S[i] == 'x' and S[i-1] == 'x':
                ans += 1
    print(ans)

