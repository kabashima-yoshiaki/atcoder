https://atcoder.jp/contests/abc415/tasks/abc415_c
- 状態iを決める際に、一つ前の状態が安全かつ今回入れても安全なら安全になる
	- 状態をbitDPで持つことで状態iのとき、一個前に入れた瓶の状態dp[mask ^ (1 << k)]を0<=k<nでTrueの時dp[mask]=True
	- dp[-1]がTrueなら”Yes”
## 発想
- 問題文がビット
- 全体の長さ$2^n-1$ で、テストケースすべての場合でo($2^n$)でnが18程度➔bit全探索orbitDP
- 順番ではなく状態で決まる➔BitDP
