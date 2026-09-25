N = int(input())
A = list(map(int, input().split()))
X = int(input())

cnt = 0

for i in range(N):
    if A[i] == X:
        cnt += 1 
        
if cnt >= 1:
    print("Yes")
else:
    print("No")


""" if X in A:
    print("Yes")
else:
    print("No") """

