S = str(input())
E_sum = 0
W_sum = 0
for i in range(len(S)):
    if S[i] == "E":
        E_sum += 1
    else:
        W_sum += 1
print("East" if E_sum > W_sum else "West")
