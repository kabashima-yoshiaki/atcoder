q=int(input())
query = (input().split() for _ in range(q))
l=0
r=0
a=[]
is_r_over = False
r_over_idx = -1
for que in query:
    if que[0] == "1":
        if que[1] == "(":
            l += 1
            a.append("(")
        else:
            r+=1
            a.append(")")
            if not is_r_over and l < r :
                is_r_over = True
                r_over_idx = len(a)-1

    else:
        p = a.pop()
        if p == "(":
            l -= 1
        else:
            r -= 1
        if is_r_over and len(a) <= r_over_idx:
            is_r_over = False
            r_over_idx = -1


    if l == r and not is_r_over:
        print("Yes")
    else:
        print("No")


