n,q=map(int,input().split())
k=list(map(int,input().split()))
card = [i for i in range(1,n+1)] 
cur=[True]*(n+1)
cur[0] = None
for i in range(q):
    card1 = card[:k[i]]
    card1.reverse()
    card2 = card[k[i]:]
    card = card1 + card2

    for c in card1:
        cur[c] = not cur[c]


for i in range(n):
    if cur[card[i]]:
        print(card[i])
    else:
        print(-card[i])