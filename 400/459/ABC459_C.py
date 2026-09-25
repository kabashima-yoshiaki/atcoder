N, Q = map(int, input().split())

mass = [0 for _ in range(N+1)]
s = [N for _ in range(Q+1+3*10**5)]
down = 0

for i in range(Q):
    a, b = map(int, input().split())

    if a == 1:
        s[mass[b]] -= 1
        mass[b] += 1
        if s[down] == 0:
            down += 1
    if a == 2:
        print(N - s[b+down-1])

#以上のものを考えるときにN-以下にするといい。また、全体に更新が必要な時は更新した回数を保存するとうまくいく。