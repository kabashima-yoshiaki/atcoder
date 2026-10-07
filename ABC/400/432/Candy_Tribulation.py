n,x,y=map(int,input().split())
a=list(map(int,input().split()))

left = x*max(a)
right = y*min(a)

if left > right:
    print(-1)
else:
    amari = a[0]*x % (y-x)
    for a_i in a:
        if amari == a_i*x % (y-x):
            continue
        else:
            print(-1)
            break
    else:
        w = right
        ans = 0
        for a_i in a:
            ans += (w - x * a_i) / (y-x)

        print(int(ans))