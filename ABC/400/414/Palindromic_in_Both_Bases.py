A = int(input())
N = int(input())

# 10進数からA進数に変換する関数
def dec_to_n(num:int, base:int) -> str:
    s = ''
    while num > 0:
        s += str(num % base)
        num //= base
    return s[::-1]

# 問題の条件を満たすか判定する
def is_ok(kaibun:int, base:int) -> bool:
    # N以下の条件
    if kaibun > N:
        return False

    # A進数に変換する
    kaibun_a_str = dec_to_n(kaibun, base)

    # 変換後も回分なら、答えに加算する
    return kaibun_a_str == kaibun_a_str[::-1]        

answer = 0
for i in range(1, 10**6):
    # 回文を生成する
    # i=12 なら、1221 と 121 を作る
    str_i = str(i)
    kaibun_a = int(str_i + str_i[::-1])
    kaibun_b = int(str_i[:-1] + str_i[::-1])

    # 条件を満たすなら、答えを追加
    if is_ok(kaibun_a, A):
        answer += kaibun_a
    if is_ok(kaibun_b, A):
        answer += kaibun_b

print(answer)