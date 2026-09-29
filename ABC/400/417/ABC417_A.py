N, A, B = map(int, input().split())
S = list(input())
s = S[A:N-B]
print("".join(s))