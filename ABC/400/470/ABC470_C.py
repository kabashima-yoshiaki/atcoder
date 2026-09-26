input = __import__("sys").stdin.readline
N, Q = map(int, input().split())
query = [list(map(int, input().split())) for _ in range(Q)]

A = [0]*(N+1)
ans = 0
dec = []
for q in query:
    if q[0] == 1:
        if A[q[1]] == 0:
            dec.append(q[1])
        ans = ans ^ A[q[1]] ^ (A[q[1]]+1)
        A[q[1]] += 1

    else:

        for d in dec:
            ans = ans ^ A[d] ^ (A[d]-1)
            A[d] -= 1

        newdec = []
        for d in dec:
            if A[d] != 0:
                newdec.append(d)
        dec = newdec

    print(ans)
 
