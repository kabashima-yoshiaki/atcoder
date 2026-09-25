n = int(input())
l = list(map(int, input().split()))
ans = n
for i in range(n):
    if l[i] == 0:
        ans -= 1
        continue
    else:
        ans -= 1
        break
for j in range(n-1, -1, -1):
    if j == i:
        break
    elif l[j] == 0:
        ans -= 1
    else:
        break

print(ans)