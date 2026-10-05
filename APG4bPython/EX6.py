A, op, B = input().split()
A = int(A)
B = int(B)

if op == "+":
    print(A + B)
elif op == "-":
    print(A - B)
elif op == "*":
    print(A * B)
elif op == "/":
    if B == 0:
        print("error")
    else:
        print(int(A / B))
elif op == "?":
    print("error")
elif op == "=":
    print("error")
elif op == "!":   
    print("error") 
