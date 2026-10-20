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
        if na > nc:
            pair = nc
            naa =  na - pair
            if pair <= naa:
                ans += pair
            else:
                ans += naa
                pair -= naa
                ans += (pair * 2) // 3

        else:
            pair = na
            nbb = nc - pair
            if pair <= nbb:
                ans += pair
            else:
                ans += nbb
                pair -= nbb
                ans += (pair * 2) // 3

    
        print(ans)