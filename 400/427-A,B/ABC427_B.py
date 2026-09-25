n = int(input())
ans = 1
for i in range(n-1):
    ans += sum(list(map(int, list(str(ans)))))
print(ans)


