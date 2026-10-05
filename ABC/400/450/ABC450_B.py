N = int(input())
C = []

for i in range(N-1):
    row = input().split()
    
    padded = [0]*i + row
    
    C.append(padded)

for i in range(N-2):
    for j in range(i+2, N):
        print(i, j)
        k = i+1
        while k < j:
            if C[i][j] < C[i][k] + C[k][j]:
                print("Yes")
                exit()
            k += 1
print("No")  