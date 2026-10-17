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
        nc -= nc
        if na > nb:
            pair = nb
            naa =  na - pair

        else:
            pair = na
            nbb = nb - pair
        
        

        print(ans)