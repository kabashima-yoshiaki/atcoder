n,q=map(int,input().split())    
a=list(map(int,input().split()))
mass=[0 for _ in range(n+2)]
mass[0] = -1
mass[-1] = -1
def check(li,idx):
    if li[idx-1] != -1 and li[idx+1] != -1:
        return li[idx-1]+li[idx+1]
    elif li[idx-1] == -1 and li[idx+1] != -1 :
        return li[idx+1]
    elif li[idx+1] == -1 and li[idx-1] != -1:
        return li[idx-1]
    else:
        return 0
cnt = 0
for a_i in a:

    if mass[a_i] == 0:
        mass[a_i] = 1
        if check(mass, a_i) == 2:
            cnt -= 1
        elif check(mass, a_i) == 0:
            cnt += 1
    else:
        mass[a_i] = 0
        if check(mass, a_i) == 2:
            cnt += 1
        elif check(mass, a_i) == 0:
            cnt -= 1
    print(cnt)
