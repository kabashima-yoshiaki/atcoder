N = int(input())
S = input()

if S[0] != 'o':
    print(S)
else:
    for i in range(N-1):
        if S[i] == 'o' and S[i+1] != 'o':
            print(S[i+1:])
            exit()
    print('')
