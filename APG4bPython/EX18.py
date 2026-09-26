""" 
#EX18-1
N = int(input())
 
# p[i] : 組織 i の親組織 
p = [-1] + list(map(int, input().split()))
 
# 2 次元配列 children
# children[i] : 組織 i の子組織の一覧 であるような 2 次元配列
children = [[] for _ in range(N)]
for i in range(1, N):
    children[p[i]].append(i)
 
# 再帰関数 complete_time
# 入力 : 組織番号 x
# 出力 : 組織 x に子組織からの報告書が揃った時刻（報告書を親組織へ送った時刻）
def complete_time(x):
        if len(children [x]) == 0:
              return 0
        else:
            return max(complete_time(y) + 1 for y in children[x])

 
# 組織 0 の元に報告書が揃う時刻を出力
print(complete_time(0)) 
"""

#18-2
# x 番の組織が親組織に提出する報告書の枚数を返す関数
def num_report(children, x):
    if len(children[x]) == 0:
        return 1
    # 再帰ステップ
    ans = 1 # 自身の報告書
    for c in children[x]:
        ans += num_report(children, c)
    return ans
 
# これ以降の行は変更しなくてよい
N = int(input())
# p[i] : 組織 i の親組織
# 組織 0 の親組織は存在しないので -1 を入れておく
# 組織 0 に相当する部分は入力で与えられないため、リスト [-1] を作成して "+" 演算子で結合する
p = [-1] + [int(c) for c in input().split()] 
 
# children[i] = 組織 i の子組織のリスト
children = [[] for _ in range(N)]
for i in range(1, N):
    parent = p[i] # 組織 i の親組織は parent
    children[parent].append(i) # parent の子組織リストに i を追加
 
# 各組織について答えを計算し出力する
for i in range(N):
    res = num_report(children, i)
    print(res)