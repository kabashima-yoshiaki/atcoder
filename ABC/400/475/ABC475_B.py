N = int(input())
A = list(map(int, input().split()))

hundred_sum = 0
ten_sum = 0
one_sum = 0

for a in A:
    paid = (a // 1000)
    if a != paid*1000:
        paid += 1
    money_back = str(paid*1000 - a)
    money_back_number = money_back.zfill(3)

    hundred_sum += int(money_back_number[0])
    ten_sum += int(money_back_number[1])
    one_sum += int(money_back_number[2])
print(one_sum, ten_sum, hundred_sum)
    