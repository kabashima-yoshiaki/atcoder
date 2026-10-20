d=int(input())
import math
x_max= math.isqrt(d)
ans = float("inf")
for i in range(x_max):
    C = i ** 2 - d
    if C > 0:
        y = 0
        ans = min(ans, C)
    else:
        y = -C
        ans = min()
