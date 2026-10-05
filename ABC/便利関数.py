#=======================
# グリッド関係
#=======================

#グリッドの基本入力
H,W = map(int(input().split()))
grid = [input() for _ in range(H)]

# グリッドの回転
def rotate(a):
    return ["".join(r) for r in zip(*a[::-1])]
