import sys
N = int(input())
L = 1
R = 2
X = 0
M = []*N
while R <= N :
    print(f'? {L} {R}')
    ans = input()
    if ans == "Yes":
        R += 1
    else:
        X += R - L - 1
        L += 1
        if L == R:
            R += 1
while L < N:
    X += R - L - 1
    L += 1

print(f'! {X}')
sys.exit()


