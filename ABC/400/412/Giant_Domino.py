from bisect import bisect_right

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    mid = sorted(a[1:-1])          # 最初と最後以外をソート
    now, end = a[0], a[-1]
    count = 2                      # 最初と最後のドミノ
    while mid and now * 2 < end:
        ind = bisect_right(mid, now * 2) - 1   # 2*now 以下で最大のものの位置
        if ind < 0 or mid[ind] <= now:         # 倒せるものがない or 大きくならない
            break
        count += 1
        now = mid[ind]

    print(count if now * 2 >= end else -1)