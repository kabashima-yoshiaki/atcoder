s = list(input())
a = int(((len(s) + 1) / 2) - 1)
s[a] = ''
s = ''.join(s)
print(s)