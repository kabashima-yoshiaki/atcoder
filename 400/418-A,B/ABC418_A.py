""" 
N = int(input())
S = input()

s = []
if N > 2:
    for i in range(N - 1, N - 4, -1):
        s.insert(0, S[i])
else:
    print("No")
    exit()

s = "".join(s)
if s == "tea":
    print("Yes")
else:
    print("No")
 """


N = int(input())
S = input()

is_tea = S.endswith("tea")
print("Yes" if is_tea else "No")
