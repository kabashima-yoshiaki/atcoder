from collections import defaultdict
s = input()

s_dict = defaultdict(int)
for x in s:
    s_dict[x] += 1

for key, value  in s_dict.items():
    if value == 1:
        print(key)
        exit()

