A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))
A3 = list(map(int, input().split()))
cnt = 0
for a1 in A1:
    for a2 in A2:
        for a3 in A3:
            mass = [a1, a2, a3]
            mass.sort()
            if mass == [4, 5, 6]:
                cnt += 1
print(cnt/ 216)