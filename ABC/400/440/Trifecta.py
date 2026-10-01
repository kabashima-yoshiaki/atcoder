n=int(input())
t=list(map(int,input().split()))
s=[[t[i-1], i] for i in range(1,n+1)]
s.sort()
print(s[0][1], s[1][1], s[2][1])

print(3%4)