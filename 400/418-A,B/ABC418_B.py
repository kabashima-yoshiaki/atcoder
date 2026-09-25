S = input()
max_t = 0

for i in range(len(S)-2):
    for j in range(i + 2,len(S)):
        x = S.count("t", i, j+1)
        if j-i-1 == 0:
            continue
        else:
            max_t = max(max_t, (x-2)/(j-i-1))
            
print(max_t)
