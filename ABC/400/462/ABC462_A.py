S = str(input())
for i in range(len(S)):
    if not S[i].islower():
        print(S[i], end='')
        
