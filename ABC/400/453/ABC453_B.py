T, X = map(int, input().split())
A = list(map(int, input().split()))

time = [0]

for i in range(1, T+1):
    if abs(A[i] - A[time[-1]]) >= X:
        time.append(i)

for j in range(len(time)):
    print(time[j], A[time[j]])