def sum_scores(scores):
    scores_sum = 0
    for i in range(len(scores)):
        scores_sum += scores[i]
    return scores_sum

def output(sum_a, sum_b, sum_c):
    print(sum_a * sum_b * sum_c)

def input_list(N):
    l = list(map(int, input().split()))
    return l

N = int(input())
A = input_list(N)
B = input_list(N)
C = input_list(N)
 
# それぞれの合計点を計算
sum_A = sum_scores(A)
sum_B = sum_scores(B)
sum_C = sum_scores(C)
 
# プレゼントの予算を出力
output(sum_A, sum_B, sum_C)