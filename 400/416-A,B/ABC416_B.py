S = list(input())
tag = 1
for i in range(len(S)):
    if S[i] == "#":
        tag = 1
        continue
    if S[i] == ".":
        if tag == 1:
            S[i] = "o"
            tag = 2
            continue
    
print("".join(S))


        

