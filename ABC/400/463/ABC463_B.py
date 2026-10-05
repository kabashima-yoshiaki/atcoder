N, X = map(str, input().split())
N = int(N)
X = ord(X)-ord('A')
for i in range(N):
    S = str(input())
    if S[X] == 'o':
        print('Yes')
        quit()
    
print('No')