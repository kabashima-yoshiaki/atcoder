#=====================
#境界を進めるだけの場合
#=====================
def shakutori_A(A, N, condition):
    """
    パターンA: 外側のループが進むにつれて、条件を満たす境界(current)が
    広がる一方(狭くならない)ときに使う。

    パラメータ
    ----------
    A : list        ソート済みの配列(または条件判定に使うリスト)
    N : int         配列の長さ
    condition : function(current, i, a) -> bool
        「current番目の要素が条件を満たすか」を判定する関数
        i: 外側ループのインデックス, a: 外側ループの現在の値

    Returns
    -------
    ans : int       各iについてcurrentを足し合わせた合計
    """
    current = 0
    ans = 0
    for i, a in enumerate(A):
        while current < N and condition(current, i, a):
            current += 1
        ans += current
    return ans

def shakutori_B(A, N, is_ng, count_func=None):
    """
    パターンB: 左右2つのポインタ(left, right)で区間[left, right]を管理し、
    条件がNGになったら左を縮める。「合計がK以下の最長区間」などに使う。

    Parameters
    ----------
    A : list        配列
    N : int         配列の長さ
    is_ng : function(state) -> bool
        現在のstate(合計など)が条件NGかどうかを判定する関数
    count_func : function(left, right, state) -> int, optional
        各rightごとに答えに加算する値を計算する関数
        省略時は「区間の個数(right-left+1)」を数える

    Returns
    -------
    ans : int
    """
    left = 0
    total = 0  # 区間の合計(必要に応じて別の値に変えてもOK)
    ans = 0

    for right in range(N):
        total += A[right]  # 右端を1つ伸ばす

        while left <= right and is_ng(total):
            total -= A[left]  # 左端を縮める
            left += 1

        if count_func:
            ans += count_func(left, right, total)
        else:
            ans += (right - left + 1)

    return ans
