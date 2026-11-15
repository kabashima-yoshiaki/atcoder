n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# aの後ろの方にある要素を、change_idx の位置へ「前に」移動して b になるか
def can_change(a, b, n):
    flag = True    # True: ズレていない状態 / False: ズレた区間の中
    done = False   # ズレた区間を1回処理し終えたか
    for i in range(n):
        if flag:
            if a[i] != b[i]:
                if done:          # 修正③: 2回目のズレはNG
                    return False
                flag = False
                change_idx = i
        # 修正①: ズレを見つけた i 自身からチェックする（elseにしない）
        if not flag:
            if i < n - 1 and a[i] == b[i + 1]:
                continue          # 1つ右にずれている → 区間が続く
            # 修正②: 末尾 i = n-1 もここで判定される
            if a[i] == b[change_idx]:
                flag = True       # ここが移動した要素 → 区間終わり
                done = True
            else:
                return False
    return True

if a == b:
    print("Yes")
    exit()

print("Yes" if (can_change(a, b, n) or can_change(b, a, n)) else "No")