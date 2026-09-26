data = [int(c) for c in input().split()]
for idx in range(len(data)-1):
    if data[idx] == data[idx + 1]:
        print("YES")
        break
else:
    print("NO")
    