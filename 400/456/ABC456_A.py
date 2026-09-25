import sys
X = int(input())
A = [1, 2, 3, 4, 5, 6]
for a in A:
    for b in A:
        for c in A:
            if X == a + b + c:
                print("Yes")
                sys.exit()
else:
    print("No")