n= int(input())
x = list(map(int,input().split()))
for i in range(n):
    if i == 0 or i == n-1:
        print((x[-1] - x[0]) // 2)
    else:
        migi = max(x[-1] - x[i], x[i+1] -x[0])
        hidari = max(x[i] - x[0], x[-1] - x[i-1])
        print(min(migi//2, hidari//2))