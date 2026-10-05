n,m=map(int,input().split())
s=list(input())
t=list(input())
q=int(input())

for _ in range(q):
    t_lang = False
    s_lang = False
    w=input()
    for w_i in w:
        if w_i in s:
            continue
        else:
            s_lang = False
            break
    else:
        s_lang = True
        
    for w_i in w:
        if w_i in t:
            continue
        else:
            t_lang = False
            break
    else:
        t_lang = True

    if t_lang and s_lang:
        print("Unknown")
    elif s_lang and not t_lang:
        print("Takahashi")
    else:
        print("Aoki")
