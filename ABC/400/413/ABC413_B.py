N = int(input())
A = [str(input()) for _ in range(N)]

import itertools

#順列の数を計算
result = list(itertools.permutations(A, 2))
#重複を見る
concat_set = set(a + b for a, b in result)
print(len(concat_set))


