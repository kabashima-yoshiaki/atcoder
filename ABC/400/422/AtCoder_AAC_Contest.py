t=int(input())
for _ in range(t):
    na, nb, nc = map(int,input().split())
    min_testcase = min(na, nb, nc)
    if min_testcase == na:
        print(na) 
    elif min_testcase == nc:
        print(nc)
    else:
        ans = nb
        na -= nb
        nc -= nb
        while na > 1 or nc > 1:
            if na > nc:
                na -= 2
                nc -= 1
            else:
                nc -= 2
                na -= 1
            ans += 1
            
        print(ans)