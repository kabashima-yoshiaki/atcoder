import math
n=int(input())
r_i=[]
c_i=[]

for _ in range(n):
    r,c=map(int,input().split())
    r_i.append(r)
    c_i.append(c)

r_distance = max(r_i)-min(r_i)
c_distance = max(c_i)-min(c_i)
print((math.ceil(max(r_distance, c_distance)/2)))