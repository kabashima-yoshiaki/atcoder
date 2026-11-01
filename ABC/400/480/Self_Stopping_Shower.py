n,k,t=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
#https://qiita.com/kkdd/items/6488757de0cc0cbb50cd
def merger(intervals):
    intervals.sort(key=lambda interval: interval[0])
    merged = [intervals[0]]
    for w in intervals:
        if w[0] > merged[-1][1]:
            merged.append(w)
        elif w[1] > merged[-1][1]:
            merged[-1][1] = w[1]
    return merged

a_distance = []
for a_i in a:
    a_distance.append([a_i, a_i+k])

merged_a_distance = merger(a_distance)

ans = 0
cur = 0

for i in range(len(merged_a_distance)):

    if cur < merged_a_distance[i][0] < t and i != (len(merged_a_distance) -1):
        ans += (merged_a_distance[i][0] - cur) // k
        if (merged_a_distance[i][0] - cur) % k != 0:
            ans += 1
        cur = merged_a_distance[i][1]

    elif merged_a_distance[i][0] >= t and i == 0:
        ans += t // k
        if t % k != 0:
            ans += 1
        break


    elif i == (len(merged_a_distance) -1) and merged_a_distance[i][1] < t:
        ans += (t - merged_a_distance[i][1]) // k
        ans += (merged_a_distance[i][0] - cur) // k
        if (t - merged_a_distance[i][1]) % k != 0 :
            ans += 1
        if (merged_a_distance[i][0] - cur) % k != 0 :
            ans += 1

    elif i == (len(merged_a_distance) -1) and merged_a_distance[i][1] >= t:
        ans += (merged_a_distance[i][0] - cur) // k
        if (merged_a_distance[i][0] - cur) % k != 0 :
            ans += 1
        

    elif merged_a_distance[i][0] >= t and i > 0:
        ans += ((t - merged_a_distance[i-1][1]) // k)
        if (t - merged_a_distance[i-1][1]) % k != 0:
            ans += 1
        break
        


print(ans)
