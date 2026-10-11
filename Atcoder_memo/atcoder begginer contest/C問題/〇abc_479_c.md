https://atcoder.jp/contests/abc479/tasks/abc479_c
## ナップザック(N < 30)の問題。

ナップザック問題だが、N＜30なので2^N
でも全探索で間に合う。
選ぶor選ばない系の全探索はbit全探索すればいい。
if ((i >> j) & 1):

