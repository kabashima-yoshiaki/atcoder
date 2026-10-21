a = int(input())
n = int(input())

def is_pal_a(m):
    if m % a == 0:      # A進法で一の位が0なら、先頭は0にならないので回文になりえない
        return False
    lst = []
    while m:
        lst.append(m % a)
        m //= a
    return lst == lst[::-1]

ans = 0
half = 1
while True:
    s = str(half)
    odd = int(s + s[-2::-1])    # 123 → 12321(奇数桁)
    if odd > n:
        break
    if is_pal_a(odd):
        ans += odd
    even = int(s + s[::-1])     # 123 → 123321(偶数桁)
    if even <= n and is_pal_a(even):
        ans += even
    half += 1

print(ans)