s=input()
cnt = 0
for s_i in s:
    if s_i == 'o':
        cnt += 1
if cnt % 2 == 1:
    print('odd')
else:
    print('even')