A = list(map(int, input().split()))
B = list(map(int, input().split()))
def solution(A, B):
    out_degree = [0]* (len(A)+1)
    for a in A:
        out_degree[a] += 1
    return out_degree.count(0)

print(solution(A, B))