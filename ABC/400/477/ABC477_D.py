n, q = map(int, input().split())
qry = [(2, "a")]
tile = [0] * n
for i in range(q):
    t, x = input().split()
    if t == "1":
        x = int(x) - 1
        tile[x] ^= 1
        qry.append((1, x))
    else:
        qry.append((2, x))
s = set(i for i in range(n) if tile[i] == 0)
ans = [""] * n
for t, x in reversed(qry):
    if t == 1:
        if tile[x] == 0 and ans[x] == "":
            s.remove(x)
        if tile[x] and ans[x] == "":
            s.add(x)
        tile[x] ^= 1
    else:
        for i in s:
            ans[i] = x
        s.clear()
print("".join(ans))