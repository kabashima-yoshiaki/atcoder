S = list(input())
R = []
cnt = 0
N = S.count("#")
for i in range(len(S)):
    if S[i] == "#":
         R.append(i+1)

for j in range(0, N, 2):
     print(R[j], R[j+1], sep=",")
        