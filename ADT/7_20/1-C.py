N = int(input())
A = list(map(int, input().split()))
ans = 0
# a / 2 より大きい最初の要素（なければ最後の次）を表す値 j
j = 0
for a in A:
    # 越えるまで進める
    while j < N and A[j] * 2 <= a:
        j += 1
    ans += j
print(ans)