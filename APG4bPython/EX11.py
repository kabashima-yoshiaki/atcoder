S = input()

count = 0
count_minus = 0
 
for i in range(len(S)):
    if S[i] == "+":
        count += 1

for i in range(len(S)):
    if S[i] == "-":
        count_minus += 1
print(1 + count - count_minus)