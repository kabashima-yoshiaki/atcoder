N, Q = map(int, input().split())
P = list(map(int, input().split()))
P_inv = [0]*(N)
for i in range(1, N+1):
    P_inv[P[i-1]-1] = i
inv = False
for _ in range(Q):
    data = list(map(int, input().split()))
    
    if data[0] == 1:
        x = data[1]
        y = data[2]
        if inv:
            cur, other = P_inv, P
        else:
            cur, other = P, P_inv
        a = cur[x-1]
        b = cur[y-1]
        cur[x-1] , cur[y-1] = b, a
        other[a-1], other[b-1] = y, x
        
    elif data[0] == 2:
        inv = not inv

if inv:
    print(" ".join(map(str, P_inv)))
else:
    print(" ".join(map(str, P)))